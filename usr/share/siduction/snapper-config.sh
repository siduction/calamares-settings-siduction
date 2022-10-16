#!/bin/bash
if  [ $(mount | grep -m1 btrfs | awk '{print $5}' ]; then
    umount @@ROOT@@.snapshots
    rm -r @@ROOT@@.snapshots
    snapper --no-dbus create-config -f btrfs @@ROOT@@
    snapper --no-dbus -c root set-config 'TIMELINE_CREATE=no'
    snapper --no-dbus -c root set-config 'ALLOW_GROUPS=users'
    snapper --no-dbus -c root set-config 'SYNC_ACL=yes'
    snapper --no-dbus -c home create-config -f btrfs @@ROOT@@home
    snapper --no-dbus -c home set-config 'TIMELINE_CREATE=yes'
    snapper --no-dbus -c home set-config 'ALLOW_GROUPS=users'
    snapper --no-dbus -c home set-config 'SYNC_ACL=yes'
    systemctl disable snapper-boot.timer
    umount @@ROOT@@.snapshots
    btrfs sub del @@ROOT@@.snapshots/
    mkdir @@ROOT@@.snapshots
    sed -i 's|GRUB_BTRFS_DISABLE=|#GRUB_BTRFS_DISABLE=|g' @@ROOT@@etc/default/grub-btrfs/config
else
    apt-get -y purge grub-btrfs snapper snapper-gui
fi
rm -f /usr/local/bin/snapper-config.sh
