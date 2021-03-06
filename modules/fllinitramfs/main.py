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
    """ Generate an initramfs image. We can happily assume that there is no
        initrd on the live system - the old fll behaviour - and we build it only
        for the running kernel

    :return:
    """
    return_code = target_env_call(["update-initramfs", "-k", platform.release(), "-c"])

    if return_code != 0:
        return "Failed to run update-initramfs on the target", "The exit code was {}".format(return_code)

    return_code = target_env_call(["update-grub"])
    if return_code != 0:
        return "Failed to run update-grub on the target", "The exit code was {}".format(return_code)


