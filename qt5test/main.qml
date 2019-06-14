import QtQuick 2.7
import QtQuick.Window 2.2
import QtQuick.Controls 1.4
import QtGraphicalEffects 1.0

ApplicationWindow {
    id: mainWindow
    height: 160
    width: 400
    visible: true
    title: "My Window"

    Item {
        id: page
        visible: true
        width: parent.width

        Rectangle {
            id: myRectangle
            height: {
                console.log("Javascript code goes in like this")
                return 160
            }
            color: "#002424"
            width: parent.width

            Text {
                id: mainText
                text: "Some regular un-Google Text, but I don't see any JS Console?"
                height: 50
                width: parent.width
                font.pixelSize: 12
                color: "#ffffff"
                horizontalAlignment: Text.AlignHCenter
                padding: 20
            }

            Button {
                id: mainButton
                text: "Okay"
                anchors.top: mainText.bottom
                onClicked: {
                    console.log(myRectangle.color)
                    if (myRectangle.color = "#002424") {
                        myRectangle.color = "#000000"
                    } else {
                        myRectangle.color = "#002424"
                    }
                }
            }
        }
    }
}