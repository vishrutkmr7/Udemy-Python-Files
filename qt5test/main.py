#!/usr/bin/python3

import os, sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtQuick import *
from PyQt5.Qt import *

# QML App
if __name__ == "__main__":
    app = QApplication(sys.argv)

    engine = QQmlApplicationEngine()
    engine.load(QUrl.fromLocalFile("main.qml"))
    # window = engine.rootObjects()[0]
    # window.show()

    sys.exit(app.exec_())
