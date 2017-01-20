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
import platform

def run():
    """ Remove some fll leftovers - thats what the fll-installer would do.

    :return:
    """

    # copy sddm-*.conf --> sddm.conf
    return_code = target_env_call(["cp -a /etc/sddm-*.conf sddm.conf"])
    if return_code != 0:
        return "Failed to copy /etc/sddm-*.conf to sddm.conf on the target", "The exit code was {}".format(return_code)

    # regenerate default snakeoil with new hostname
    return_code = target_env_call(["make-ssl-cert generate-default-snakeoil --force-overwrite"])
    if return_code != 0:
        return "Failed to regenerate snakeoil certificate  on the target", "The exit code was {}".format(return_code)

