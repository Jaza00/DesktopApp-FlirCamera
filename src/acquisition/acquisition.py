from simple_pyspin import Camera
import cv2

class Acquisition():
    def __init__(self):
        self.cam = Camera()
        self.cam.init()  

    def getRgbImage(self):
        self.cam.start()
        frame = self.cam.get_array()
        self.cam.stop()
        self.rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGRA2RGB)
        return self.rgbImage

    def captureRgbImage(self):
        self.rgbImageCaptured = self.rgbImage
        return self.rgbImageCaptured

    def saveRgbImage(self, pathImage):         
        """
        Save captured rgb image 
        paramters:
                pathImage: path to save image and name image
        """
        cv2.imwrite(pathImage, self.rgbImageCaptured)