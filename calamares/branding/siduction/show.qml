/* === This file is part of Calamares - <http://github.com/calamares> ===
 *
 *   Copyright 2015, Teo Mrnjavac <teo@kde.org>
 *
 *   Calamares is free software: you can redistribute it and/or modify
 *   it under the terms of the GNU General Public License as published by
 *   the Free Software Foundation, ei[\chm-
 *   (at your option) any later version.
 *
 *   Calamares is distributed in the hope that it will be useful,
 *   but WITHOUT ANY WARRANTY; without even the implied warranty of
 *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 *   GNU General Public License for more details.
 *
 *   You should have received a copy of the GNU General Public License
 *   along with Calamares. If not, see <http://www.gnu.org/licenses/>.
 */

import QtQuick 2.0;
import calamares.slideshow 1.0;

Presentation
{
    id: presentation

    Image {
        id: image1
        source: "slide1.png"
        width: 467; height: 280
        fillMode: Image.PreserveAspectFit
        anchors.horizontalCenter: parent.horizontalCenter
    }
    Text {
        anchors.horizontalCenter: image1.horizontalCenter
        anchors.top: image1.bottom
        text: "<b>Welcome to siduction 2021.2.0 \"Farewell\".</b><br/>"+
              "The rest of the installation is automated and typically takes a few minutes to complete. <br/><br/>"+
              "WARNING: After the installation finishes, your system will not be DFSG-compliant (Debian Free Software Guide).<br/>"+
              "We ship non-free firmware that enables you to set up wifi and other hardware with non-free needs.<br/>"+
              "If you want your system to be DFSG-compliant, you need to run the script <b>'remove-nonfree'</b><br/>"+
              "after you reboot into the installed system."
        wrapMode: Text.WordWrap
        width: 700
        horizontalAlignment: Text.Center
   }
}

