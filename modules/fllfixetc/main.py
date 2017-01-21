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
import contextlib
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
    target_env_call(["make-ssl-cert", "generate-default-snakeoil", "--force-overwrite"])

    # don't allow everyone to use sudo.
    source = os.path.join(root_mount_point, "usr/share/base-files/profile")
    target = os.path.join(root_mount_point, "etc/profile")
    shutil.copy( source, target)

    # also fix sudoers
    unwanted = os.path.join( root_mount_point, "etc/sudoers.d/10-installer" )
    if os.path.isfile( unwanted ):
        with contextlib.suppress(FileNotFoundError):
            os.remove( unwanted )
    unwanted = os.path.join( root_mount_point, "etc/sudoers.d/15_siduction" )
    if os.path.isfile( unwanted ):
        with contextlib.suppress(FileNotFoundError):
            os.remove( unwanted )

    # not implemented yet !TODO!

    # "normalize" gettys

   # sysvinit
#   if [ -r "${TARGET_MNT_POINT}/usr/share/sysvinit/inittab" ]; then
#           cp -f   "${TARGET_MNT_POINT}/usr/share/sysvinit/inittab" \
#                "${TARGET_MNT_POINT}/etc/inittab"
#           sed -i  -e 's/^\([2-6]\):23:respawn/\1:2345:respawn/' \
#                -e 's/id:[0-6]:initdefault:/id:5:initdefault:/' \
#                    "${TARGET_MNT_POINT}/etc/inittab"
#   fi

#    # systemd
#        if [ -r "${TARGET_MNT_POINT}/etc/systemd/system/getty@.service" ]; then
#                rm -f   "${TARGET_MNT_POINT}/etc/systemd/system/getty@.service" \
#                        "${TARGET_MNT_POINT}/etc/systemd/system/autovt@.service"
#
#                ln -fs  /lib/systemd/system/autovt@.service \
#                        "${TARGET_MNT_POINT}/etc/systemd/system/getty.target.wants/getty@tty1.service"
#        fi

    # normalize /etc/pam.d/login
#    if [ -f "${TARGET_MNT_POINT}/etc/pam.d/login" ]; then
#                sed -i '/^#.*pam_lastlog\.so/s/^#[ \t]\+//' "${TARGET_MNT_POINT}/etc/pam.d/login"
#        fi

    # remove confusing live traces from blkid.tab
#    rm -f "${TARGET_MNT_POINT}/etc/blkid.tab*"

    # Save ALSA sound volume
#    if [ -e /proc/asound/modules ] && [ -x /usr/sbin/alsactl ]; then
#            /usr/sbin/alsactl store
#            if [ -f /var/lib/alsa/asound.state ]; then
#                    cp /var/lib/alsa/asound.state \
#                            "${TARGET_MNT_POINT}/var/lib/alsa"
#            fi
#    fi

    # revert GDM3 autologin
#    if [ -f "${TARGET_MNT_POINT}/etc/gdm3/daemon.conf" ]; then
#            # we want the gdm-theme (set by desktop-defaults in live mode) on hd-install,
#            # only remove autologin for gdm
#            sed -i  -e "/^AutomaticLogin\=.*/d" \
#                   -e "/^AutomaticLoginEnable\=.*/d" \
#                   -e "/^TimedLogin\=.*/d" \
#                   -e "/^TimedLoginDelay\=.*/d" \
#                   -e "/^TimedLoginEnable\=.*/d" \
#                           "${TARGET_MNT_POINT}/etc/gdm3/daemon.conf"
#    fi

    # revert lightdm autologin
#    if [ -f "${TARGET_MNT_POINT}/etc/lightdm/lightdm.conf.d/80_fll-live-initscripts.conf" ]; then
#            rm -f "${TARGET_MNT_POINT}/etc/lightdm/lightdm.conf.d/80_fll-live-initscripts.conf"
#            rmdir --ignore-fail-on-non-empty \
#                   "${TARGET_MNT_POINT}/etc/lightdm/lightdm.conf.d" || :
#   fi

    # revert lxdm autologin
#    if [ -f "${TARGET_MNT_POINT}/etc/lxdm/live.conf" ] && \
#       [ -f "${TARGET_MNT_POINT}/etc/lxdm/lxdm.conf" ]; then
#            rm -f "${TARGET_MNT_POINT}/etc/lxdm/live.conf"
#            ln -fs lxdm.conf "${TARGET_MNT_POINT}/etc/lxdm/default.conf"
#    fi

     # revert SDDM autologin
     # partly implemented
#     rm -f   "${TARGET_MNT_POINT}/etc/sddm.conf" \
#             "${TARGET_MNT_POINT}/var/lib/sddm/state.conf"

     #
     # revert slim autologin
     #
#     if [ -f "${TARGET_MNT_POINT}/etc/slim.conf" ]; then
#             sed -i  -e "/^default_user.*/d" \
#                     -e "/^auto_login.*/d" \
#                     -e "s/^\#FLL\#//" \
#                             "${TARGET_MNT_POINT}/etc/slim.conf"
#     fi
