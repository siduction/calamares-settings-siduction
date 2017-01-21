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


#        local INSTHOME="/home/${USER_NAME}"
#        # home of user on live media
#        local LIVEHOME="/home/${DEFAULT_USER}"
#
#        if [ "${USER_NAME}" != "${DEFAULT_USER}" ];     then
#                if [ -d "${TARGET_MNT_POINT}${LIVEHOME}" ] && \
#                        [ ! -d "${TARGET_MNT_POINT}${INSTHOME}" ]; then
#                        mv "${TARGET_MNT_POINT}${LIVEHOME}" "${TARGET_MNT_POINT}${INSTHOME}"
#
#                        # fix /home/user paths in various config files
#                        find "${TARGET_MNT_POINT}${INSTHOME}" \
#                                -type f \
#                                -exec sed -i "s|${LIVEHOME}|${INSTHOME}|g" {} \;
#                fi
#        fi

        # purge unwanted files
#        for file in     "${TARGET_MNT_POINT}${INSTHOME}/Desktop/${FLL_DISTRO_NAME}.desktop" \
#                        "${TARGET_MNT_POINT}${INSTHOME}/Desktop/install-gui.desktop" \
#                        "${TARGET_MNT_POINT}${INSTHOME}/.config/autostart/${FLL_DISTRO_NAME}.desktop" \
#                        "${TARGET_MNT_POINT}${INSTHOME}/.hushlogin" \
#                        "${TARGET_MNT_POINT}${INSTHOME}/.config/chromium/SingletonLock" \
#                        "${TARGET_MNT_POINT}${INSTHOME}/.config/chromium/Local State" \
#                        "${TARGET_MNT_POINT}${INSTHOME}/.config/chromium/First Run" \
#                        "${TARGET_MNT_POINT}/root/.hushlogin"; do
#                rm -f "${file}"
#        done

        # purge content of some dirs
#        for dir in "${TARGET_MNT_POINT}${INSTHOME}/.cache"; do
#            [ -d "$dir" ] && rm -Rf ${dir}/*
#        done

        # revert sudo workarounds
#        for file in     "${TARGET_MNT_POINT}${INSTHOME}/.config/kdesurc" \
#                        "${TARGET_MNT_POINT}${INSTHOME}/.kde/share/config/kdesurc" \
#                        "${TARGET_MNT_POINT}${INSTHOME}/.kde/share/apps/konsole/sumc.desktop" \
#                        "${TARGET_MNT_POINT}${INSTHOME}/.kde/share/apps/konsole/su.desktop" \
#                        "${TARGET_MNT_POINT}${INSTHOME}/.gconf/apps/gksu/%gconf.xml" \
#                        "${TARGET_MNT_POINT}${INSTHOME}/.su-to-rootrc"; do
#                grep -s -q sudo "$file" && rm -f "$file"
#        done


        # revert gksu sudo mode hack
#        logit "revert gksu sudo mode hack"
#        chroot "${TARGET_MNT_POINT}" \
#                sudo -u "${FLL_LIVE_USER}" gconftool-2 -s -t bool /apps/gksu/sudo-mode false
#        chroot "${TARGET_MNT_POINT}" \
#                sudo -u "${FLL_LIVE_USER}" gconftool-2 -s -t bool /apps/gksu/display-no-pass-info true

    # remove installer from fluxbox menu
#        if grep -s -q Installer "${TARGET_MNT_POINT}${INSTHOME}"/.fluxbox/fll-flux-*; then
#                sed -i '/Installer/d' "${TARGET_MNT_POINT}${INSTHOME}"/.fluxbox/fll-flux-*
#        fi

    # make sudo alias's vanish
#        if grep -s -q sudo "${TARGET_MNT_POINT}${INSTHOME}/.bashrc"; then
#                sed -i 's|\(.*sudo.*\)||' "${TARGET_MNT_POINT}${INSTHOME}/.bashrc"
#        fi

    # enable automount-open for gnome, mate and cinnamon in install mode
#        if [ -d /usr/share/siduction-settings-${FLL_FLAVOUR}-${FLL_DISTRO_CODENAME_SAFE} ]; then
#                case "$FLL_FLAVOUR" in
#                        gnome)
#                                cat > "${TARGET_MNT_POINT}/usr/share/siduction-settings-${FLL_FLAVOUR}-${FLL_DISTRO_CODENAME_SAFE}/automount-open" <<EOF

# #!/bin/sh
# if [ ! -d /usr/share/fll-installer ]; then
#    gsettings set org.gnome.desktop.media-handling automount true
#    gsettings set org.gnome.desktop.media-handling automount-open true
#    rm ${INSTHOME}/.config/autostart/automount-open.desktop
# fi
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

#         # We don't check existence, -p handles that
#         mkdir -p ${TARGET_MNT_POINT}${INSTHOME}/.config/autostart

    # fix permisions for automount-open automount-open.desktop and /.config/autostart
#        chroot "${TARGET_MNT_POINT}" \
#        chown ${USER_NAME} ${INSTHOME}/.config/autostart
#        chroot "${TARGET_MNT_POINT}" \
#        chgrp ${USER_NAME} ${INSTHOME}/.config/autostart
#        chmod +x ${TARGET_MNT_POINT}/usr/share/siduction-settings-${FLL_FLAVOUR}-${FLL_DISTRO_CODENAME_SAFE}/automount-open
#        chroot "${TARGET_MNT_POINT}" \
#        ln -sf /usr/share/siduction-settings-${FLL_FLAVOUR}-${FLL_DISTRO_CODENAME_SAFE}/automount-open.desktop ${INSTHOME}/.config/autostart/automount-open.desktop
#        chroot "${TARGET_MNT_POINT}" \
#        chown ${USER_NAME} /usr/share/siduction-settings-${FLL_FLAVOUR}-${FLL_DISTRO_CODENAME_SAFE}/automount-open
#        chroot "${TARGET_MNT_POINT}" \
#        chown ${USER_NAME} /usr/share/siduction-settings-${FLL_FLAVOUR}-${FLL_DISTRO_CODENAME_SAFE}/automount-open.desktop
#        fi
#}
