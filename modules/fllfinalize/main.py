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

    # copy sddm-*.conf --> sddm.conf
    source = glob.glob(os.path.join(root_mount_point, "etc/sddm-*.conf"))
    target = os.path.join(root_mount_point, "etc/sddm.conf")
    shutil.copy( source[0], target)


    # regenerate default snakeoil with new hostname
    return_code = target_env_call(["make-ssl-cert", "generate-default-snakeoil", "--force-overwrite"])

    # don't allow everyone to use sudo.
    source = os.path.join(root_mount_point, "usr/share/base-files/profile")
    target = os.path.join(root_mount_point, "etc/profile")
    shutil.copy( source, target)

    # also fix sudoers
    # rm -f "${TARGET_MNT_POINT}/etc/sudoers.d/15_${FLL_DISTRO_NAME}"
    os.remove( os.path.join( root_mount_point, "/etc/sudoers.d/10-installer" ))
    os.remove( os.path.join( root_mount_point, "/etc/sudoers.d/10_siduction" ))
    # chroot_it deluser "${USER_NAME}" sudo
    # not implemented yet !TODO!

