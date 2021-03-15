from simple_pyspin import Camera
import cv2

class Acquisition():
    """
    Clase para la adquisición de imágenes de la cámara
    """

    def __init__(self):
        pass

    def initCamera(self):
        """ 
        Detecta e inicializa la cámara
        """

        self.cam = Camera()
        self.cam.PixelFormat = "RGB8"
        print(self.cam.PixelFormat)
        self.cam.init()  

    def getRgbImage(self):
        """
        Obtiene la imagen rgb de la cámara

        return:

            rgbImage: imagen de cv2
        """

        self.cam.start()
        frame = self.cam.get_array()
        self.cam.stop()
        self.rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGRA2RGB)
        #self.rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        return self.rgbImage

    def captureRgbImage(self):
        """
        captura la imagen rgb

        return:

            rgbImageCaptured: imagen de cv2
        """

        self.rgbImageCaptured = self.rgbImage
        return self.rgbImageCaptured

    def saveRgbImage(self, pathImage):         
        """
        Guarda la imagen capturada

        paramter:

                pathImage: ruta en la que se guarda la imagen
        """

        cv2.imwrite(pathImage, self.rgbImageCaptured)