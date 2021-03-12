from PySide2 import QtCore, QtUiTools, QtWidgets, QtGui
from style import Styles
import cv2
import sys
import os

class FlirCameraWidget(QtWidgets.QWidget):
    """
    Main QTWidget for intrinsic acquisition
    """    

    def __init__(self, *args, **kwargs):
        super(FlirCameraWidget, self).__init__(*args, **kwargs)
        self.loadForm()
        self.initUI()
        Styles(self)

    def initUI(self):
        self.setWindowIcon(QtGui.QIcon('views/icons/cameraIcon.png'))
        self.setWindowTitle("Intecol Flir camera")
        self.setGeometry(300, 100, 1012, 622)

    def loadForm(self):
        formUI = os.path.join(sys.path[0], 'views/acquisition.ui')
        file = QtCore.QFile(formUI)
        file.open(QtCore.QFile.ReadOnly)
        loader = QtUiTools.QUiLoader()
        self.window = loader.load(file)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.window)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    acquisitionIntrinsicCalibration = FlirCameraWidget()
    acquisitionIntrinsicCalibration.show()
    app.exec_()