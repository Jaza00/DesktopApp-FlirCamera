from PySide2 import QtCore, QtUiTools, QtWidgets, QtGui
from views.acqGUI import Ui_MainWindow
from views.style import Styles
import cv2
import sys
import os

class FlirCameraWidget(QtWidgets.QMainWindow):
    """
    Main QTWidget para la adquisicion de la cámara FLIR
    """    

    def __init__(self, *args, **kwargs):
        """
        Inicializa la clase FlirCameraWidget
        """

        super(FlirCameraWidget, self).__init__(*args, **kwargs)
        #self.loadForm()
        self.window = Ui_MainWindow()
        self.window.setupUi(self)

        self.initUI()
        Styles(self)

    def initUI(self):
        """
        Setea los valores iniciales de la GUI
        """
        
        self.setWindowTitle("Intecol Flir camera")
        self.setGeometry(300, 100, 1012, 622)

    def loadForm(self):
        """
        Carga el archivo .ui de la GUI
        """

        formUI = os.path.join(sys.path[0], 'views/acquisition.ui')
        file = QtCore.QFile(formUI)
        file.open(QtCore.QFile.ReadOnly)
        loader = QtUiTools.QUiLoader()
        self.window = loader.load(file)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.window)
        self.setLayout(layout)