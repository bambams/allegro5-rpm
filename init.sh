#!/usr/bin/env bash

root=${1:-$HOME/src/allegro/rpm}
rpm_tree=$HOME/rpm
src_path="$rpm_tree/SOURCES/allegro-5.0.0.tar.gz"
src_sha1=7a6c7bf63d65b0e76ec6daf7e09e293fdfc8c137
src_url=http://downloads.sourceforge.net/project/alleg/allegro/5.0.0/allegro-5.0.0.tar.gz

if [ "`echo $root | grep '^/'`" != "$root" -o $? != 0 ]; then
    echo "Your project root path '$root' doesn't appear to be " 1>&2
    echo "absolute. I quit." 1>&2
    exit 1
fi

if [ "`pwd`" != "$root" ]; then
    echo "This script is designed to be used from the root of the " 1>&2
    echo "project. You can override that path by passing an " 1>&2
    echo "argument to the script." 1>&2
    exit 1
fi

if [ ! -d .git ]; then
    echo "Ummm, I don't see .git here. This script isn't very smart so"
    echo "I'd recommend that you use it as it was intended."
    read -p "Try anyway? (Y/n) " answer
    if [ "$answer" != 'y' -a "$answer" != 'Y' ]; then
        echo "Aborting..." 2>&1
        exit 1
    fi
fi

if [ -d "$rpm_tree" ]; then
    echo "It seems rpm tree '$rpm_tree' already exists..."
    read -p "Would you like me to setup tree anyway? (Y/n) " answer
    if [ "$answer" != 'y' -a "$answer" != 'Y' ]; then
        skip_setuptree=1
    fi
fi

if [ ! "$skip_setuptree" == 1 ]; then
    echo "Setting up rpm tree..." 2>&1
    /usr/bin/rpmdev-setuptree
fi

echo "Creating .spec symlinks in '$rpm_tree/SPECS'..." 2>&1
for f in $root/*.spec; do
    /bin/ln -fs "$f" "$rpm_tree/SPECS/"
done

if [ -f "$src_path" ]; then
    echo "Source tarball exists... Checking SHA1..." 2>&1
    if [ `/usr/bin/sha1sum "$src_path" | sed -r 's/^([^ ]*).*/\1/'` == "$src_sha1" ]; then
        echo "SHA1 matches..." 2>&1
        skip_src=1
    else
        echo "SHA1 doesn't match..." 2>&1
    fi
fi

if [ ! "$skip_src" == 1 ]; then
    echo "Fetching source tarball..." 2>&1
    /usr/bin/wget -O "$src_path" "$src_url"
fi
