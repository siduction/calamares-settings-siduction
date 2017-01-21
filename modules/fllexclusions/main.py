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

from libcalamares.utils import target_env_call
import glob
import libcalamares
import os
import shutil

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

    # /home/*/.DCOPserver_*

    # /home/*/.local/share/akonadi*

    # /home/*/.gvfs*

    # /home/*/.kde/cache-*

    # /home/*/.kde/socket-*

    # /home/*/.kde/tmp-*

    # /home/*/.*uthority

    # /home/*/Desktop/sidu-installer.desktop

    # /home/*/.kaxtv*

    # /lib/init/rw/*

    # /var/cache/gdm/*
 
