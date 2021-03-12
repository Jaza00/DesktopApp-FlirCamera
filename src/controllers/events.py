from src.acquisition.acquisition import  Acquisition
from PySide2 import QtGui, QtWidgets, QtCore
import numpy as np
import cv2
import time

class Events():
    def __init__(self, window):
        self.window = window
        self.scalaImage = 80
        self.clicPlay = False
        self.clicCapture = False
        self.acquisitionImages = False
        self.countNoImageAcq = 0
        self.dimensionsCamera = np.array([960, 600])*(self.scalaImage/100)
        self.camera = Acquisition()

    def setFrameRate(self, valueFrameRate):
        self.frameRate = valueFrameRate

    def setConfigAutoAcq(self, delay, NoImages, valueFrameRate, pathImages):
        self.delay = delay
        self.NoImagesAcq = NoImages
        self.frameRate = valueFrameRate
        self.pathImages = pathImages
        time.sleep(self.delay)
        self.acquisitionImages = True

    def turnOnCamera(self):
        print('start stream')
        self.initCamera()
        self.initCounter()  
        return self.viewCamera

    def turnOffCamera(self):
        if (self.clicPlay or self.clicCapture):
            print('stop stream')
            self.timerCamera.stop()
        self.countNoImageAcq = 0
        self.clicCapture = False
        self.clicPlay = False

    def initCamera(self):
        self.timerCamera = QtCore.QTimer()
        print("frame rate:", (1/self.frameRate)*1000)
        self.timerCamera.setInterval((1/self.frameRate)*1000)
        self.timerCamera.timeout.connect(self.getFrame)            
        self.timerCamera.start()
        self.viewCamera = QtWidgets.QGraphicsView()
        scene = QtWidgets.QGraphicsScene()
        self.imagePixmap = QtGui.QPixmap(*self.dimensionsCamera)
        self.imagePixmapItem = scene.addPixmap(self.imagePixmap)
        self.viewCamera.setScene(scene)
        self.clicPlay = True

    def getFrame(self):
        frame = self.camera.getRgbImage()
        if self.acquisitionImages:
            if self.countNoImageAcq < self.NoImagesAcq:
                nameImage = "%s%i%s" % (self.pathImages, self.countNoImageAcq, '.png')
                cv2.imwrite(nameImage, frame)
                self.countNoImageAcq += 1
        frame = self.imageResize(frame, self.scalaImage)
        image = QtGui.QImage(frame, *self.dimensionsCamera,QtGui.QImage.Format_RGB888).rgbSwapped()
        self.imagePixmap = QtGui.QPixmap.fromImage(image)
        self.imagePixmapItem.setPixmap(self.imagePixmap)

    def initCounter(self):
        if self.acquisitionImages:
            self.timerCounter = QtCore.QTimer()
            self.timerCounter.setInterval(20)
            self.timerCounter.timeout.connect(self.setValueProgressBar)
            self.timerCounter.start()

    def setValueProgressBar(self):
        if self.acquisitionImages:
            value = (self.countNoImageAcq/self.NoImagesAcq)*100
            self.window.progressBarAcq.setValue(value)
            self.window.labelImagesCapt.setText(str(self.countNoImageAcq))

    def imageResize(self, pathImage, scalePercent):
        if (isinstance(pathImage, str)):
            image = cv2.imread(pathImage, cv2.IMREAD_UNCHANGED)
        else:
            image = pathImage
        width = int(image.shape[1] * scalePercent / 100)
        height = int(image.shape[0] * scalePercent / 100)
        dim = (width, height)
        resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
        return resized

    def captureImage(self):
        frameImage = []
        if (self.clicPlay or self.clicCapture):
            self.timerCamera.stop()
        self.clicCapture = False
        self.clicPlay = False
        frameImage = self.camera.captureRgbImage()
        self.imageToQtWidget(frameImage)
        self.clicCapture = True
        return self.viewCamera

    def saveImage(self, pathImage):
        self.camera.saveRgbImage(pathImage)

    def imageToQtWidget(self, frame):
        frame = self.imageResize(frame, self.scalaImage)
        image = QtGui.QImage(frame, *self.dimensionsCamera, QtGui.QImage.Format_RGB888).rgbSwapped()
        imagePixmap = QtGui.QPixmap.fromImage(image)
        imageScene = QtWidgets.QGraphicsScene()
        framePixmap = QtGui.QPixmap(*self.dimensionsCamera)
        imagePixmapItem = imageScene.addPixmap(framePixmap)
        imagePixmapItem.setPixmap(imagePixmap)
        self.viewCamera = QtWidgets.QGraphicsView()
        self.viewCamera.setScene(imageScene)