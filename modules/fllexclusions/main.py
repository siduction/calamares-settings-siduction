#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# === This file is part of Calamares - <http://github.com/calamares> ===
#
#   Copyright 2014, Philip Müller <philm@manjaro.org>
#
#   Calamares is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   Calamares is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with Calamares. If not, see <http://www.gnu.org/licenses/>.

import glob
import libcalamares
import os

def run():
    """ Remove some fll leftovers - thats what the fll-installer would do.

    :return:
    """

    # set root_mount_point
    root_mount_point = libcalamares.globalstorage.value("rootMountPoint")

    # via tmpfs - in mounts
    # valid - /disks/*      -- done in mount.conf
    # valid - /media/*      -- done in mount.conf
    # valid - /mnt/*        -- done in mount.conf
    # valid - /run/*        -- done in mount.conf
    # valid - /run/.*       -- done in mount.conf
    # valid - /sys/*        -- done in mount.conf
    # valid - /tmp/*        -- done in mount.conf
    # valid - /var/tmp/*    -- done in mount.conf

    # /etc/network/run/*
    path = os.path.join( root_mount_point, "etc/network/run/*")
    for f in glob.glob(path):
        os.remove(f)

    # /home/*/.DCOPserver_*
    path = os.path.join( root_mount_point, "home/*/.DCOPserver_*")
    for f in glob.glob(path):
        os.remove(f)

    # /home/*/.local/share/akonadi*
    path = os.path.join( root_mount_point, "home/*/.local/share/akonadi*")
    for f in glob.glob(path):
        os.remove(f)

    # /home/*/.gvfs*
    path = os.path.join( root_mount_point, "home/*/.gvfs*")
    for f in glob.glob(path):
        os.remove(f)

    # /home/*/.kde/cache-*
    path = os.path.join( root_mount_point, "home/*/.kde/cache-*")
    for f in glob.glob(path):
        os.remove(f)

    # /home/*/.kde/socket-*
    path = os.path.join( root_mount_point, "home/*/.kde/socket-*")
    for f in glob.glob(path):
        os.remove(f)

    # /home/*/.kde/tmp-*
    path = os.path.join( root_mount_point, "home/*/.kde/tmp-*")
    for f in glob.glob(path):
        os.remove(f)

    # /home/*/.*uthority
    path = os.path.join( root_mount_point, "home/*/.*uthority")
    for f in glob.glob(path):
        os.remove(f)

    # /home/*/Desktop/sidu-installer.desktop
    path = os.path.join( root_mount_point, "home/*/Desktop/sidu-installer.desktop")
    for f in glob.glob(path):
        os.remove(f)

    # /home/*/.kaxtv*
    path = os.path.join( root_mount_point, "home/*/.kaxtv*")
    for f in glob.glob(path):
        os.remove(f)

    # /lib/init/rw/*
    path = os.path.join( root_mount_point, "lib/init/rw/*")
    for f in glob.glob(path):
        os.remove(f)

    # /var/cache/gdm/*
    path = os.path.join( root_mount_point, "var/cache/gdm/*")
    for f in glob.glob(path):
        os.remove(f)
