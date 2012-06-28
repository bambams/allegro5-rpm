#!/usr/bin/env bash

root="${1:-$HOME/src/allegro/5-rpm}"
rpm_tree="${2:-$HOME/rpm}"
version="`./parse-version 2>/dev/null`"
tarball="allegro-${version}.tar.gz";

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

if [ -d "$rpm_tree" ]; then
    echo "It seems rpm tree '$rpm_tree' already exists..."
    read -p "Would you like me to setup tree anyway? (Y/n) " answer
    if [ "$answer" != y -a "$answer" != Y ]; then
        skip_setuptree=1
    fi
fi

if [ ! "$skip_setuptree" == 1 ]; then
    echo "Setting up rpm tree..."
    /usr/bin/rpmdev-setuptree
fi

if [ ! -d "$rpm_tree" ]; then
    echo "Failed to find '$rpm_tree' tree... Trying 'rpmbuild'..." 1>&2
    echo "In the future you can save time by specifying the rpm " 1>&2
    echo "build tree as the second argument to this script." 1>&2
    exec "$0" "$root" "`echo $rpm_tree | sed -r 's,\brpm\b,rpmbuild,'`"
fi

echo "Creating .spec symlinks in '$rpm_tree/SPECS'..."
for f in $root/*.spec; do
    /bin/ln -fs "$f" "$rpm_tree/SPECS/"
done

./fetch-src

