#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# === This file is part of Calamares - <http://github.com/calamares> ===
#
#   Copyright 2014-2024, Anke Boersma <demm@kaosx.us>
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

import os
import re
import libcalamares

def run():
    """ Configure Software Sources """
    install_path = libcalamares.globalstorage.value("rootMountPoint")
    sources = libcalamares.globalstorage.value("packagechooser_sources")

    if sources == 'debian':
        print('debian defaults selected')

    elif sources == 'non-free':
        print('non-free selected')
        sources_dir = os.path.join(install_path, "etc/apt/sources.list.d/")
        replacement_text = "main contrib non-free non-free-firmware"
        pattern = re.compile(r'\bmain non-free-firmware\b')

        if os.path.exists(sources_dir):
            for filename in os.listdir(sources_dir):
                if filename.endswith(".list"):
                    file_path = os.path.join(sources_dir, filename)

                    with open(file_path, 'r') as file:
                        content = file.read()

                    # Add the replacement text if it's not already there
                    if replacement_text not in content:
                        new_content = pattern.sub(replacement_text, content)

                        with open(file_path, 'w') as file:
                            file.write(new_content)
                        print(f"Updated {filename}")
                    else:
                        print(f"No changes in {filename}")
        else:
            print(f"{sources_dir} does not exist.")

    print('configure software sources done')
    return None
