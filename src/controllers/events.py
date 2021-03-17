from acquisition import  Acquisition
from PySide2 import QtGui, QtWidgets, QtCore
import numpy as np
import cv2
import time

class Events():
    """
    Eventos para los botones de la GUI 
    """

    def __init__(self, mainWidget):
        """
        Inicializa la clase Eventos y las variables de control

        parameters: 

            mainWidget: QtWidget de la GUI
        """

        self.window = mainWidget.window
        self.camera = Acquisition()
        self.scalaImage = 50
        self.clicPlay = False
        self.clicCapture = False
        self.acquisitionImages = False
        self.countNoImageAcq = 0
        width, height = self.getDimensionImage()
        self.dimensionsCamera = np.array([width, height])*(self.scalaImage/100)

    def setFrameRate(self, valueFrameRate):
        """
        Setea el valor del frame rate

        parameter:

            valueFrameRate: float del numero de frames por segundo
        """

        self.frameRate = valueFrameRate

    def setConfigAutoAcq(self, delay, NoImages, valueFrameRate, pathImages):
        """
        Configura los parametros de adquisición de imágenes

        parameters:

            delay: float para esperar el tiempo de captura
            
            NoImages: int de cantidad de imágenes que se desea almacenar

            valueFrameRate: float del numero de frames por segundo

            pathImages: ruta de almacenamiento de las n imágenes
        """

        self.delay = delay
        self.NoImagesAcq = NoImages
        self.frameRate = valueFrameRate
        self.pathImages = pathImages
        time.sleep(self.delay)
        self.acquisitionImages = True

    def turnOnCamera(self):
        """
        Incializa la cámara y retorna el stream

        return:

            viewCamera: QtWidgets.QGraphicsView() donde se muestra el video
        """

        print('start stream')
        self.initCamera()
        self.initCounter()  
        return self.viewCamera

    def turnOffCamera(self):
        """
        Detiene el stream y setea las variables de control
        """

        if (self.clicPlay or self.clicCapture):
            print('stop stream')
            self.timerCamera.stop()
        self.countNoImageAcq = 0
        self.clicCapture = False
        self.clicPlay = False
        self.acquisitionImages = False

    def initCamera(self):
        """
        Inicializa el stream
        """

        #self.camera.initCamera()
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

    def getDimensionImage(self):
        """
        Retorna las dimenciones de la imagen
        """

        self.camera.initCamera()
        dim = self.camera.getRgbImage().shape
        height, width = dim[0], dim[1]
        return width, height

    def getFrame(self):
        """
        Obtiene un frame de la cámara y transforma la imagen en QtGui.QImage
        """

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
        """
        Inicializa el contador para setear el valor de la barra de progreso 
        """

        if self.acquisitionImages:
            self.timerCounter = QtCore.QTimer()
            self.timerCounter.setInterval(20)
            self.timerCounter.timeout.connect(self.setValueProgressBar)
            self.timerCounter.start()

    def setValueProgressBar(self):
        """
        Setea el valor de barra de progreso y de imágenes capturadas
        """
        
        value = (self.countNoImageAcq/self.NoImagesAcq)*100
        self.window.progressBarAcq.setValue(value)
        self.window.labelImagesCapt.setText(str(self.countNoImageAcq))

    def imageResize(self, pathImage, scalePercent):
        """
        Ajusta el tamaño original de la imagen al tamaño del espacio en la GUI   

        parameters:

            pathImages: Este parametro puede ser un string de la ruta donde se encuentra la imagen
                        o puede ser directamente una imagen.

            scalePercent: porcentaje de la imagen a la que se desea redimencionar con respecto 
                        al tamaño original  
        """

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
        """
        Captura la imagen actual del stream

        return: 
            viewCamera: widget Qt de la imagen capturada
        """

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
        """
        Guarda la imagen capturada

        parameter:

            pathImage: ruta en donde se desea almacemar la imagen
        """

        self.camera.saveRgbImage(pathImage)

    def imageToQtWidget(self, frame):
        """
        Transforma una imagen a un widget de QT

        parameter:

            frame: frame de la imagen a transformar
        """

        frame = self.imageResize(frame, self.scalaImage)
        image = QtGui.QImage(frame, *self.dimensionsCamera, QtGui.QImage.Format_RGB888).rgbSwapped()
        imagePixmap = QtGui.QPixmap.fromImage(image)
        imageScene = QtWidgets.QGraphicsScene()
        framePixmap = QtGui.QPixmap(*self.dimensionsCamera)
        imagePixmapItem = imageScene.addPixmap(framePixmap)
        imagePixmapItem.setPixmap(imagePixmap)
        self.viewCamera = QtWidgets.QGraphicsView()
        self.viewCamera.setScene(imageScene)