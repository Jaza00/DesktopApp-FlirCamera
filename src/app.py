""" 
File: app.py
Creation date: 12-mar-2021
author: Jaimen Aza
email: jaza@intecol.com.co
"""

from PySide2 import QtWidgets
import sys
import os

"""
Add directories to path
"""
dirs = ['views', 'controllers', 'acquisition']
for nameDir in dirs:
    path = os.path.join(sys.path[0], nameDir)
    sys.path.append(path)

from mainGUI import FlirCameraWidget
from controllerButtons import Controller

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    flirCameraWidget = FlirCameraWidget()
    controller = Controller(flirCameraWidget)
    app.exec_()