from src.controllers.events import Events
from PySide2 import QtWidgets

class Controller():
    def __init__(self, mainWidget):
        self.window = mainWidget.window
        self.event = Events(self.window)
        self.connectButtons()
        self.clicCapture = False
        mainWidget.show()

    def configAdqcquisition(self):
        delay = int(self.window.lineEditDelay.text())
        NoImages = int(self.window.lineEditNoImages.text())
        frameRate = int(self.window.lineEditframeRate.text())
        pathImages = self.saveDialog()
        if pathImages != '':
            self.event.setConfigAutoAcq(delay, NoImages, frameRate, pathImages)

    def connectButtons(self):
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
        self.cleanWorkspace()
        self.event.setFrameRate(int(self.window.lineEditframeRate.text()))
        image = self.event.turnOnCamera()
        self.window.layoutShowImage.addWidget(image)

    def offCamera(self):
        self.cleanWorkspace()
        self.event.turnOffCamera()

    def captureImage(self):
        self.cleanWorkspace()
        image = self.event.captureImage()
        self.window.layoutShowImage.addWidget(image)
        self.clicCapture = True

    def saveImage(self):
        if self.clicCapture:
            nameImage = self.saveDialog()
            if nameImage != '':
                self.event.saveImage(nameImage)
            else:
                print('se debe seleccionar una ruta')

    def saveImages(self):
        images = self.event.turnOffCamera()
        self.cleanWorkspace()
        self.configAdqcquisition()
        image = self.event.turnOnCamera()
        self.window.layoutShowImage.addWidget(image)

    def saveDialog(self):
        relativePath = '../data'
        nameImage = QtWidgets.QFileDialog.getSaveFileName(
            self.window, 'Save as', relativePath)
        nameImage = "%s.png" % nameImage[0]
        return nameImage

    def cleanWorkspace(self):
        #self.window.progressBarAcq.setValue(0)
        #self.window.labelImagesCapt.setText('0')
        for index in reversed(range(self.window.layoutShowImage.count())):
            layoutItem = self.window.layoutShowImage.itemAt(index)
            widgetToRemove = layoutItem.widget()
            print("found widget: " + str(widgetToRemove))
            widgetToRemove.setParent(None)
            self.window.layoutShowImage.removeWidget(widgetToRemove)