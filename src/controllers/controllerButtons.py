from events import Events
from PySide2 import QtWidgets

class Controller():
    """
    Controlador para los botones de la GUI
    """

    def __init__(self, mainWidget):
        """
        Inicializa la clase Controller

        parameter:

            mainWidget: QtWidget de la GUI
        """

        self.window = mainWidget.window
        self.event = Events(mainWidget)
        self.connectButtons()
        self.clicCapture = False
        mainWidget.show()

    def configAqcquisition(self):
        """
        Configuración de adquisición. Extrae los parametros de la GUI y los setea
        en el programa. 
        """

        delay = float(self.window.lineEditDelay.text())
        NoImages = int(self.window.lineEditNoImages.text())
        frameRate = float(self.window.lineEditframeRate.text())
        pathImages = self.saveDialog()
        if pathImages != '':
            self.event.setConfigAutoAcq(delay, NoImages, frameRate, pathImages)

    def connectButtons(self):
        """
        Connecta cada botón con su respectivo evento
        """

        self.window.pushButtonInit.clicked.connect(
            self.showRgbImage)
        self.window.pushButtonStop.clicked.connect(
            self.offCamera)
        self.window.pushButtonCapture.clicked.connect(
            self.captureImage)
        self.window.pushButtonSave.clicked.connect(
            self.saveImage)
        self.window.pushButtonPlay.clicked.connect(
            self.saveImages)

    def showRgbImage(self):
        """
        Muestra la imagen adquirida en la GUI
        """

        self.cleanWorkspace()
        self.event.setFrameRate(float(self.window.lineEditframeRate.text()))
        image = self.event.turnOnCamera()
        self.window.layoutShowImage.addWidget(image)

    def offCamera(self):
        """
        Detiene el stream
        """

        self.cleanWorkspace()
        self.event.turnOffCamera()

    def captureImage(self):
        """
        captura la imagen actual y la muestra en la GUI
        """

        self.cleanWorkspace()
        image = self.event.captureImage()
        self.window.layoutShowImage.addWidget(image)
        self.clicCapture = True

    def saveImage(self):
        """
        Guarda la imagen en la ruta escogida por el usuario
        """

        if self.clicCapture:
            nameImage = self.saveDialog()
            if nameImage != '':
                self.event.saveImage(nameImage)
            else:
                print('se debe seleccionar una ruta')

    def saveImages(self):
        """
        Guarda n imagenes en a ruta escogida por el usuario
        """

        images = self.event.turnOffCamera()
        self.cleanWorkspace()
        self.configAqcquisition()
        image = self.event.turnOnCamera()
        self.window.layoutShowImage.addWidget(image)

    def saveDialog(self):
        """
        Abre el cuadro de dialogo para seleccionar la ruta de almacenamiento
        y el nombre de la imagen
        """

        relativePath = '../data'
        nameImage = QtWidgets.QFileDialog.getSaveFileName(
            self.window, 'Save as', relativePath)
        nameImage = "%s.png" % nameImage[0]
        return nameImage

    def cleanWorkspace(self):
        """
        Limpia la imagen del espacio de trabajo
        """

        for index in reversed(range(self.window.layoutShowImage.count())):
            layoutItem = self.window.layoutShowImage.itemAt(index)
            widgetToRemove = layoutItem.widget()
            print("found widget: " + str(widgetToRemove))
            widgetToRemove.setParent(None)
            self.window.layoutShowImage.removeWidget(widgetToRemove)