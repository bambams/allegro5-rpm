#!/usr/bin/env bash

root=${1:-$HOME/src/allegro/rpm}
rpm_tree=${2:-$HOME/rpm}
other_rpm_tree="`echo $rpm_tree | sed -r 's,\brpm\b,rpmbuild,'`"

if [ "`echo $root | grep '^/'`" != "$root" -o $? != 0 ]; then
    echo "Your project root path '$root' doesn't appear to be " 1>&2
    echo "absolute. I quit." 1>&2
    exit 1
fi

if [ "`/bin/pwd`" != "$root" ]; then
    echo "This script is designed to be used from the root of the " 1>&2
    echo "project. You can override that path by passing an " 1>&2
    echo "argument to the script. For example:" 1>&2
    echo "  ./init.sh \`pwd\`" 1>&2
    exit 1
fi

if [ ! -d .git ]; then
    echo "Ummm, I don't see .git here. This script isn't very smart so"
    echo "I'd recommend that you use it as it was intended."
    read -p "Try anyway? (Y/n) " answer
    if [ "$answer" != y -a "$answer" != Y ]; then
        echo "Aborting..." 1>&2
        exit 1
    fi
fi

version=`grep -A 1 changelog allegro5.spec |
        tail -n 1 |
        sed -r 's,.*([0-9]+\.[0-9]+\.[0-9]+),\1,'`

major_version=`echo $version |
        sed -r 's,([0-9]+)\.[0-9]+\.[0-9]+,\1,'`

dest="castopulence.org:/var/www/rpm/allegro5/$version"

spec=allegro5.spec
srpm="allegro5-5.0.0-$major_version.fc13.src.rpm"
sha1="$root/SHA1SUM"

echo "Publishing $version to $dest..."
read -p "Continue (Y/n) " answer

if [ "$answer" != y -a "$answer" != Y ]; then
    echo "Aborting..." 1>&2
    exit 1
fi


if [ ! -d "$rpm_tree" ]; then
    if [ "$rpm_tree" != "$HOME/rpm" ]; then
        echo "Aborting..." 2>&1
        exit 1
    fi
    echo "Failed to find '$rpm_tree' tree... Trying 'rpmbuild'..." 1>&2
    if [ -d "$other_rpm_tree" ]; then
        rpm_tree="$other_rpm_tree"
    else
        echo "Failed to find '$other_rpm_tree' tree... Skipping removal." 1>&2
    fi
fi

if [ -d "$rpm_tree" ]; then
    read -p "Remove '$rpm_tree' tree? (Y/n) " answer
    if [ "$answer" == y -o "$answer" == Y ]; then
        rm -fR "$rpm_tree"
    fi
fi

./init.sh

if [ ! -d "$rpm_tree" ]; then
    echo "Can't find '$rpm_tree' tree... Aborting..." 1>&2
    exit 1
fi

/usr/bin/make &&
        (cd "$rpm_tree/SRPMS" &&
        /usr/bin/sha1sum "$srpm" 1>"$sha1") &&
        /usr/bin/sha1sum "$spec" 1>>"$sha1" &&
        /usr/bin/scp "$sha1" "$dest" &&
        /usr/bin/scp "$spec" "$dest" &&
        (cd "$rpm_tree/SRPMS" &&
        /usr/bin/scp "$srpm" "$dest")

