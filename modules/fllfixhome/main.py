#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#   Copyright 2017, Alf Gaida <agaida@siduction.org>
#
#   This Module is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This Module is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this module. If not, see <http://www.gnu.org/licenses/>.

import libcalamares
import os
import subprocess

def run():
    """ Remove some fll leftovers - thats what the fll-installer would do.

    :return:
    """

    # set root_mount_point
    user = libcalamares.globalstorage.value("username")
    instHome ='/home/%s' % (user)
    # home of user on live media
    # local LIVEHOME="/home/${DEFAULT_USER}" --> /home/siducer
    liveHome = '/home/siducer'

    # move livehome --> insthome
    #        if [ -d "${TARGET_MNT_POINT}${LIVEHOME}" ] && \
    #           [ ! -d "${TARGET_MNT_POINT}${INSTHOME}" ]; then
    #            mv "${TARGET_MNT_POINT}${LIVEHOME}" "${TARGET_MNT_POINT}${INSTHOME}"
    libcalamares.utils.target_env_call(['/bin/mv', '%s' % (liveHome), '%s' % (instHome)])
    libcalamares.utils.target_env_call(['chown', '-R', '%s:' % (user), '%s' % (instHome)])

    # fix /home/user paths in various config files
    #       find "${TARGET_MNT_POINT}${INSTHOME}" \
    #          -type f \
    #          -exec sed -i "s|${LIVEHOME}|${INSTHOME}|g" {} \;

    # purge unwanted files
    # ${TARGET_MNT_POINT}${INSTHOME}/Desktop/${FLL_DISTRO_NAME}.desktop
    unwanted = os.path.join( instHome, 'Destktop/sidu-installer.desktop' )
    libcalamares.utils.target_env_call(['/bin/rm', '-f', '%s'  % (unwanted)])

    # ${TARGET_MNT_POINT}${INSTHOME}/Desktop/install-gui.desktop
    unwanted = os.path.join( instHome, 'Destktop/sidu-manual.desktop' )
    libcalamares.utils.target_env_call(['/bin/rm', '-f', '%s'  % (unwanted)])

    # ${TARGET_MNT_POINT}${INSTHOME}/.config/autostart/${FLL_DISTRO_NAME}.desktop
    # OUTDATED - RELEASE-NOTES???
    unwanted = os.path.join( instHome, '.config/autostart/siduction.desktop' )
    libcalamares.utils.target_env_call(['/bin/rm', '-f', '%s'  % (unwanted)])

    # ${TARGET_MNT_POINT}${INSTHOME}/.hushlogin
    unwanted = os.path.join( instHome, '.hushlogin' )
    libcalamares.utils.target_env_call(['/bin/rm', '-f', '%s'  % (unwanted)])

    # ${TARGET_MNT_POINT}${INSTHOME}/.config/chromium/SingletonLock
    unwanted = os.path.join( instHome, '.config/chromium/SingletonLock' )
    libcalamares.utils.target_env_call(['/bin/rm', '-f', '%s'  % (unwanted)])

    # ${TARGET_MNT_POINT}${INSTHOME}/.config/chromium/Local State
    unwanted = os.path.join( instHome, '.config/chromium/Local State' )
    libcalamares.utils.target_env_call(['/bin/rm', '-f', '%s'  % (unwanted)])

    # ${TARGET_MNT_POINT}${INSTHOME}/.config/chromium/First Run
    unwanted = os.path.join( instHome, '.config/chromium/First Run' )
    libcalamares.utils.target_env_call(['/bin/rm', '-f', '%s'  % (unwanted)])

    # ${TARGET_MNT_POINT}/root/.hushlogin
    unwanted = '/root/.hushlogin'
    libcalamares.utils.target_env_call(['/bin/rm', '-f', '%s'  % (unwanted)])

    # purge content of some dirs
    #        for dir in "${TARGET_MNT_POINT}${INSTHOME}/.cache"; do
    #            [ -d "$dir" ] && rm -Rf ${dir}/*
    #        done

    # revert sudo workarounds
    # don't test for now grep -s -q sudo "$file" && rm -f "$file"
    # ${TARGET_MNT_POINT}${INSTHOME}/.config/kdesurc
    unwanted = os.path.join( instHome, '.config/kdesurc' )
    libcalamares.utils.target_env_call(['/bin/rm', '-f', '%s'  % (unwanted)])

    # ${TARGET_MNT_POINT}${INSTHOME}/.kde/share/config/kdesurc
    unwanted = os.path.join( instHome, '.kde/share/config/kdesurc' )
    libcalamares.utils.target_env_call(['/bin/rm', '-f', '%s'  % (unwanted)])

    # ${TARGET_MNT_POINT}${INSTHOME}/.kde/share/apps/konsole/sumc.desktop
    unwanted = os.path.join( instHome, '.kde/share/apps/konsole/sumc.desktop' )
    libcalamares.utils.target_env_call(['/bin/rm', '-f', '%s'  % (unwanted)])

    # ${TARGET_MNT_POINT}${INSTHOME}/.kde/share/apps/konsole/su.desktop
    unwanted = os.path.join( instHome, '.kde/share/apps/konsole/su.desktop' )
    libcalamares.utils.target_env_call(['/bin/rm', '-f', '%s'  % (unwanted)])

    # ${TARGET_MNT_POINT}${INSTHOME}/.gconf/apps/gksu/%gconf.xml
    unwanted = os.path.join( instHome, '.gconf/apps/gksu/%gconf.xml' )
    libcalamares.utils.target_env_call(['/bin/rm', '-f', '%s'  % (unwanted)])

    # ${TARGET_MNT_POINT}${INSTHOME}/.su-to-rootrc
    unwanted = os.path.join( instHome, '.su-to-rootrc' )
    libcalamares.utils.target_env_call(['/bin/rm', '-f', '%s'  % (unwanted)])

    # revert gksu sudo mode hack
    # sudo -u "${FLL_LIVE_USER}" gconftool-2 -s -t bool /apps/gksu/sudo-mode false
    # sudo -u "${FLL_LIVE_USER}" gconftool-2 -s -t bool /apps/gksu/display-no-pass-info true

    # remove installer from fluxbox menu
    # if grep -s -q Installer "${TARGET_MNT_POINT}${INSTHOME}"/.fluxbox/fll-flux-*; then
    #    sed -i '/Installer/d' "${TARGET_MNT_POINT}${INSTHOME}"/.fluxbox/fll-flux-*
    # fi

    # make sudo alias's vanish
    # if grep -s -q sudo "${TARGET_MNT_POINT}${INSTHOME}/.bashrc"; then
    #    sed -i 's|\(.*sudo.*\)||' "${TARGET_MNT_POINT}${INSTHOME}/.bashrc"
    # fi

    # enable automount-open for gnome, mate and cinnamon in install mode
    # if [ -d /usr/share/siduction-settings-${FLL_FLAVOUR}-${FLL_DISTRO_CODENAME_SAFE} ]; then
    #   case "$FLL_FLAVOUR" in
    #                        gnome)
    #                                cat > "${TARGET_MNT_POINT}/usr/share/siduction-settings-${FLL_FLAVOUR}-${FLL_DISTRO_CODENAME_SAFE}/automount-open" <<EOF

                                   # if [ ! -d /usr/share/fll-installer ]; then
                                 #    gsettings set org.gnome.desktop.media-handling automount true
                                 #    gsettings set org.gnome.desktop.media-handling automount-open true
                                 #    rm ${INSTHOME}/.config/autostart/automount-open.desktop

                              # EOF
    #                        ;;
    #                        cinnamon)
    #                                cat > "${TARGET_MNT_POINT}/usr/share/siduction-settings-${FLL_FLAVOUR}-${FLL_DISTRO_CODENAME_SAFE}/automount-open" <<EOF
                                 # #!/bin/sh
                                    # if [ ! -d /usr/share/fll-installer ]; then
                                             #     gsettings set org.cinnamon.desktop.media-handling automount true
                                            #     gsettings set org.cinnamon.desktop.media-handling automount-open true
                                           #     rm ${INSTHOME}/.config/autostart/automount-open.desktop
                                     # fi
                                               # EOF
    #                                 ;;
    #                         mate)
    #                                 cat > "${TARGET_MNT_POINT}/usr/share/siduction-settings-${FLL_FLAVOUR}-${FLL_DISTRO_CODENAME_SAFE}/automount-open" <<EOF
                             # #!/bin/sh
                               # if [ ! -d /usr/share/fll-installer ]; then
                               #     gsettings set org.mate.media-handling automount true
                               #     gsettings set org.mate.media-handling automount-open true
                                 #     rm ${INSTHOME}/.config/autostart/automount-open.desktop
                               # fi
                                # EOF
                             #                                 ;;
                               #         esac

    # We don't check existence, -p handles that
    # mkdir -p ${TARGET_MNT_POINT}${INSTHOME}/.config/autostart

    # fix permisions for automount-open automount-open.desktop and /.config/autostart
    # chown ${USER_NAME} ${INSTHOME}/.config/autostart

    # chgrp ${USER_NAME} ${INSTHOME}/.config/autostart

    # chmod +x ${TARGET_MNT_POINT}/usr/share/siduction-settings-${FLL_FLAVOUR}-${FLL_DISTRO_CODENAME_SAFE}/automount-open

    # ln -sf /usr/share/siduction-settings-${FLL_FLAVOUR}-${FLL_DISTRO_CODENAME_SAFE}/automount-open.desktop ${INSTHOME}/.config/autostart/automount-open.desktop

    # chown ${USER_NAME} /usr/share/siduction-settings-${FLL_FLAVOUR}-${FLL_DISTRO_CODENAME_SAFE}/automount-open

    # chown ${USER_NAME} /usr/share/siduction-settings-${FLL_FLAVOUR}-${FLL_DISTRO_CODENAME_SAFE}/automount-open.desktop
