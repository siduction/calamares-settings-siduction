#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#   Copyright 2017, Alf Gaida <agaida@siduction.org>
#
#   This module is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This module is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this module. If not, see <http://www.gnu.org/licenses/>.

import glob
import libcalamares
import os
import subprocess

def run():
    """ Remove some fll leftovers - thats what the fll-installer would do.

    :return:
    """

    # regenerate default snakeoil with new hostname
    libcalamares.utils.target_env_call(
        ['make-ssl-cert', 'generate-default-snakeoil', '--force-overwrite'])

    # don't allow everyone to use sudo.
    source = '/usr/share/base-files/profile'
    target = '/etc/profile'
    libcalamares.utils.target_env_call(
        ['/bin/cp', '-f', '%s' % source, '%s' % target])

    # also fix sudoers
    unwanted = '/etc/sudoers.d/10-installer'
    libcalamares.utils.target_env_call(['/bin/rm', '-f', '%s' % unwanted])

    unwanted = '/etc/sudoers.d/15_siduction'
    libcalamares.utils.target_env_call(['/bin/rm', '-f', '%s' % unwanted])

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
    #     rm -f   "${TARGET_MNT_POINT}/etc/sddm.conf" \
    #             "${TARGET_MNT_POINT}/var/lib/sddm/state.conf"
    unwanted = '/etc/sddm.conf'
    libcalamares.utils.target_env_call([ '/bin/rm', '-f', unwanted ])
    unwanted = '/var/lib/sddm/state.conf'
    libcalamares.utils.target_env_call([ '/bin/rm', '-f', unwanted ])
    # copy sddm-*.conf --> sddm.conf
    source = glob.glob('/etc/sddm-*.conf')
    target = '/etc/sddm.conf'
    libcalamares.utils.target_env_call(
        ['/bin/cp', '-f', '%s' % source[0], "%s" % target])

     #
     # revert slim autologin
     #
#     if [ -f "${TARGET_MNT_POINT}/etc/slim.conf" ]; then
#             sed -i  -e "/^default_user.*/d" \
#                     -e "/^auto_login.*/d" \
#                     -e "s/^\#FLL\#//" \
#                             "${TARGET_MNT_POINT}/etc/slim.conf"
#     fi
