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
    """ Configure Software Sources for DEB822 (.sources) """
    print(' Configure Software Sources ')
    install_path = libcalamares.globalstorage.value("rootMountPoint")
    sources = libcalamares.globalstorage.value("packagechooser_sources")

    if sources == 'debian':
        print('debian defaults selected')

    elif sources == 'non-free':
        print('non-free selected')
        sources_dir = os.path.join(install_path, "etc/apt/sources.list.d/")
        
        # Regex sucht nach einer Zeile, die mit 'Components:' beginnt.
        # Es fängt den Rest der Zeile ein, um zu prüfen, was schon da ist.
        components_pattern = re.compile(r'^(Components:\s*)(.*)$', re.MULTILINE)

        if os.path.exists(sources_dir):
            for filename in os.listdir(sources_dir):
                # Jetzt filtern wir gezielt nach .sources Dateien
                if filename.endswith(".sources"):
                    file_path = os.path.join(sources_dir, filename)

                    with open(file_path, 'r') as file:
                        content = file.read()

                    # Wir suchen nach der Components-Zeile
                    match = components_pattern.search(content)
                    
                    if match:
                        prefix = match.group(1)  # Das ist "Components: "
                        current_components = match.group(2)  # z.B. "main non-free-firmware"
                        
                        # Wir wandeln die aktuellen Komponenten in eine Liste um
                        comp_list = current_components.split()
                        
                        # Die gewünschten neuen Komponenten
                        targets = ["contrib", "non-free"]
                        
                        # Prüfen, ob noch etwas hinzugefügt werden muss
                        needed = [t for t in targets if t not in comp_list]
                        
                        if needed:
                            # Wir fügen die fehlenden Komponenten hinzu. 
                            # Falls 'non-free-firmware' am Ende steht, fügen wir contrib/non-free idealerweise davor ein,
                            # oder einfach ans Ende der Liste. Für APT ist die Reihenfolge egal.
                            for t in targets:
                                if t not in comp_list:
                                    # Fügt es vor 'non-free-firmware' ein, falls vorhanden, sonst ans Ende
                                    if "non-free-firmware" in comp_list:
                                        idx = comp_list.index("non-free-firmware")
                                        comp_list.insert(idx, t)
                                    else:
                                        comp_list.append(t)
                            
                            # Die neue Zeile zusammenbauen
                            new_components_line = prefix + " ".join(comp_list)
                            
                            # Den alten Block durch den neuen ersetzen
                            new_content = components_pattern.sub(new_components_line, content)
                            
                            with open(file_path, 'w') as file:
                                file.write(new_content)
                            print(f"Updated {filename} to non-free components")
                        else:
                            print(f"No changes needed in {filename} (already contains contrib/non-free)")
                    else:
                        print(f"Could not find 'Components:' line in {filename}")
        else:
            print(f"{sources_dir} does not exist.")

    print('configure software sources done')
    return None
