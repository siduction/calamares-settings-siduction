/* === This file is part of Calamares - <https://calamares.io> ===
 *
 *   SPDX-FileCopyrightText: 2022 Anke Boersma <demm@kaosx.us>
 *   SPDX-License-Identifier: GPL-3.0-or-later
 * 
 *   Calamares is Free Software: see the License-Identifier above.
 *
 */

import io.calamares.core 1.0
import io.calamares.ui 1.0

import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.3


Item {
	width: parent.width
	height: parent.height

	Rectangle {
		anchors.fill: parent
		color: "#f2f2f2"

		Text {
			text: qsTr("Select additional software sources")
			font.bold: true
			font.pointSize: 14
			anchors.horizontalCenter: parent.horizontalCenter
			anchors.top: parent.top
			anchors.topMargin: 30
			wrapMode: Text.WordWrap
		}

		Column {
			id: column
			anchors.centerIn: parent
			spacing: 5

			Rectangle {

				//id: rectangle
				width: 850
				height: 180
				color: "#ffffff"
				radius: 10
				border.width: 0

				Text {
					width: 650
					height: 160
					anchors.centerIn: parent
					text: qsTr("<b>Debian</b> - The sources only contain <b>main</b> and <b>non-free-firmware</b> (the default)<br/><br/>Debian comes with dfsg software only, since Debian 12, they added <b>non-free-firmware</b>.<br/>With this choice, you will stay the debian way, but you cannot install non-free drivers (like nvidia)<br/>or proprietary software.")
					font.pointSize: 10
					anchors.verticalCenterOffset: 10
					anchors.horizontalCenterOffset: 90
					wrapMode: Text.WordWrap
				}

				Image {
					id: image2
					x: 40
					y: 30
					height: 100
					fillMode: Image.PreserveAspectFit
					source: "images/debian.png"
				}
			}

			Rectangle {
				width: 850
				height: 180
				radius: 10
				border.width: 0

				Text {
					width: 650
					height: 190
					anchors.centerIn: parent
					text: qsTr("<b>non-free</b> - This option allows you to install proprietary drivers or software.<br/><br/>This means that you deviate from the debian dfsg guidelines.<br/>It adds <b>contrib</b> and <b>non-free</b> to your software sources.")
					font.pointSize: 10
					anchors.verticalCenterOffset: 20
					anchors.horizontalCenterOffset: 90
					wrapMode: Text.WordWrap
				}

				CheckBox {
					id: control
					text: qsTr("I also want to use <b>non-free</b>.")
					checked: false
					x: 190
					y: 120

					indicator: Rectangle {
						implicitWidth: 30
						implicitHeight: 30
						x: control.leftPadding
						y: parent.height / 2 - height / 2
						radius: 15
						border.width: 2
						// border.color: "#31363b"  // schlecht bei dunklem Hintergrund
						// border.color: "#9e919a"  // geht bei dunklem Hintergrund
						// border.color: "#727272"  // (grau) gut bei dunklem + hellem Hintergrund
						border.color: "#00aaff"  // (blauton) gut bei dunklem + hellem Hintergrund

						Rectangle {
							width: 20
							height: 20
							x: 5
							y: 5
							radius: 10
							color: "#009900"
							visible: control.checked
						}
					}

					contentItem: Text {
						text: control.text
						verticalAlignment: Text.AlignVCenter
						leftPadding: control.indicator.width + 15
					}

					checkState: allChildrenChecked ? Qt.Checked : Qt.Unchecked

					onCheckedChanged: {
						if (checkState === Qt.Checked) {
							config.packageChoice = "non-free"
							print("non-free used")
						} else {
							print("non-free not used")
							config.packageChoice = "debian"
						}
					}
				}


				Image {
					id: image
					x: 40
					y: 30
					height: 100
					fillMode: Image.PreserveAspectFit
					source: "images/non-free.png"
				}
			}
		}
	}

	// Setze config.packageChoice auf den Standardwert
	Component.onCompleted: {
		config.packageChoice = "debian"
	}
}
