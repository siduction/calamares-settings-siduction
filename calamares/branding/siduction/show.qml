/* === This file is part of Calamares - <http://github.com/calamares> ===
 *
 *   Copyright 2015, Teo Mrnjavac <teo@kde.org>
 *
 *   Calamares is free software: you can redistribute it and/or modify
 *   it under the terms of the GNU General Public License as published by
 *   the Free Software Foundation, either version 3 of the License, or
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

    Timer {
        interval: 20000
        running: true
        repeat: true
        onTriggered: presentation.goToNextSlide()
    }
    
    Slide {

        Image {
            id: image1
            source: "slide1.png"
            width: 467; height: 280
            fillMode: Image.PreserveAspectFit
            anchors.centerIn: parent
        }
        Text {
            anchors.horizontalCenter: background1.horizontalCenter
            anchors.top: background1.bottom
            text: "Welcome to siduction.<br/>"
            wrapMode: Text.WordWrap
            width: 600
            horizontalAlignment: Text.Center
        }
    }

    Slide {

        Image {
            id: image2
            source: "slide2.png"
            width: 467; height: 280
            fillMode: Image.PreserveAspectFit
            anchors.centerIn: parent
        }
        Text {
            anchors.horizontalCenter: background2.horizontalCenter
            anchors.top: background2.bottom
            text: "The rest of the installation is automated and typically takes a few minutes to complete.<br/><br/>"+
                  "With this little slightshow we present you some old artwork of the last ten years!<br/><br/>"+
                  "This was our first release, One Step Beyond, great artwork (maybe our best) by se7en.<br/><br/>"
            wrapMode: Text.WordWrap
            width: 600
            horizontalAlignment: Text.Center
        }
    }

    Slide {

        Image {
            id: image3
            source: "slide3.png"
            width: 467; height: 280
            fillMode: Image.PreserveAspectFit
            anchors.centerIn: parent
        }
        Text {
            anchors.horizontalCenter: background3.horizontalCenter
            anchors.top: background3.bottom
            text: "WARNING: After the installation finishes, your system will not be DFSG-compliant (Debian Free Software Guide).<br/><br/>"+
                  "This is our second release, Desperado, with the spagetti-western theme by hendrikL and the splash screen se7en<br/><br/>"
            wrapMode: Text.WordWrap
            width: 600
            horizontalAlignment: Text.Center
        }
    }

    Slide {

        Image {
            id: image4
            source: "slide4.png"
            width: 467; height: 280
            fillMode: Image.PreserveAspectFit
            anchors.centerIn: parent
        }
        Text {
           anchors.top: background4.bottom
             anchors.horizontalCenter: background4.horizontalCenter
            text: "We ship non-free firmware that enables you to set up wifi and other hardware with non-free needs.<br/><br/>"+
                  "Our fourth release, Riders On The Storm, artwork by se7en with some modifikations for our first chrismas-release by hendrikL.<br/><br/>"
            wrapMode: Text.WordWrap
            width: 600
            horizontalAlignment: Text.Center
        }
    }

    Slide {

        Image {
            id: image5
            source: "slide5.png"
            width: 467; height: 280
            fillMode: Image.PreserveAspectFit
            anchors.centerIn: parent
        }
        Text {
            anchors.horizontalCenter: background5.horizontalCenter
            anchors.top: background5.bottom
            text: "If you want your system to be DFSG-compliant, you need to run the script <b>'remove-nonfree',</b><br/>"+
                  "after you reboot into the installed system.<br/><br>"+
                  "This was our fifth release, Firestarter, artwork by hendrikL<br/><br/>"+
                  "As you found out, we used song names for our releases back in time<br/><br/>"
            wrapMode: Text.WordWrap
            width: 600
            horizontalAlignment: Text.Center
        }
    }

    Slide {

        Image {
            id: image6
            source: "slide6.png"
            width: 467; height: 280
            fillMode: Image.PreserveAspectFit
            anchors.centerIn: parent
        }
        Text {
            anchors.horizontalCenter: background6.horizontalCenter
            anchors.top: background6.bottom
            text: "Now we wish you a lot of fun with siduction, maybe you want to help us to make siduction greater than it ever was!</b><br/>"+
                  "If so, don't be shy to ask us if you can help!<br/><br/>"+
                  "This was our chrismas special, steam edition, back in 2014.<br/>"+
                  "Artwork, background by bob, which is still in use (we changed the color a bit) and as it was for chrismas the modifikations by hendrikL.<<br/><br/>"
            wrapMode: Text.WordWrap
            width: 600
            horizontalAlignment: Text.Center
        }
    }

    Slide {

        Image {
            id: image7
            source: "slide7.png"
            width: 467; height: 280
            fillMode: Image.PreserveAspectFit
            anchors.centerIn: parent
        }
        Text {
            anchors.horizontalCenter: background7.horizontalCenter
            anchors.top: background7.bottom
            text: "Don't forget to do an 'apt update; apt full-upgrade' from time to time, do not wait to long, because debian sid/unstable is rolling and rolling forward!</b><br/>"+
                  "Before you do a full-upgrade, always look in our forum if some trouble is in the air, sid/unstable can be a beast but mostly it is tame<br/>"+
                  "So, with that in mind <b>'apt moo'<b/>!<br/><br/>"
            wrapMode: Text.WordWrap
            width: 600
            horizontalAlignment: Text.Center
        }
    }
}
