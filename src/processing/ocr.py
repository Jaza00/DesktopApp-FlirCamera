from acquisition.acquisition import  Acquisition
from skimage.morphology import skeletonize
from matplotlib import pyplot as plt
from pytesseract import Output
import numpy as np
import pytesseract
import cv2

class Ocr():
    def __init__(self):
        pass

    def esqueletizar(self, image):
        """ 
        esqueletizar: reduce el grosor de la linea original
        parameters: imágen de perfilación láser
        return: nueva imagen 
        """
        # suavizamos un poco la imágen con un filtro gaussiano y kernel de (3,3)
        GBlur = cv2.GaussianBlur(image, (3, 3), 0)
        # generamos matriz de ceros para guardar la imagen resultante
        skel = np.zeros(GBlur.shape, np.uint8)
        size = np.size(image)
        # binarizamos la imágen con límites de 15 y 255
        ret, img = cv2.threshold(GBlur, 33, 255, 0)
        # empezamos el proceso de esqueletización
        element = cv2.getStructuringElement(cv2.MORPH_CROSS, (2, 2))
        element2 = cv2.getStructuringElement(cv2.MORPH_CROSS, (4, 4))
        done = False
        while(not done):
            eroded = cv2.erode(img, element)
            temp = cv2.dilate(eroded, element2)
            temp = cv2.subtract(img, temp)
            skel = cv2.bitwise_or(skel, temp)
            img = eroded.copy()
            zeros = size - cv2.countNonZero(img)
            if zeros == size:
                done = True
        return skel

    def getGrayscale(self, image):
        """ 
        get grayscale image
        """
        return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    def removeNoise(self, image,n):
        """
        noise removal
        """
        return cv2.medianBlur(image,n)
    
    def thresholding(self, image,threshold):
        """
        thresholding
        """
        return cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    def dilate(self, image,n):
        """
        dilation
        """
        kernel = np.ones((n,n),np.uint8)
        return cv2.dilate(image, kernel, iterations = 1)
        
    def erode(self, image,n):
        """
        erosion
        """
        kernel = np.ones((n,n),np.uint8)
        return cv2.erode(image, kernel, iterations = 1)

    def opening(self, image,n):
        """
        opening - erosion followed by dilation
        """
        kernel = np.ones((n,n),np.uint8)
        return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

    def canny(self, image,val1,val2):
        """
        canny edge detection
        """
        return cv2.Canny(image, val1, val2)

    def deskew(self, image):
        """ 
        skew correction
        """
        coords = np.column_stack(np.where(image > 0))
        angle = cv2.minAreaRect(coords)[-1]
        if angle < -45:
            angle = -(90 + angle)
        else:
            angle = -angle
        (h, w) = image.shape[:2]
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
        return rotated

    def matchTemplate(self, image, template):
        """
        template matching
        """
        return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)

    pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\Tesseract-OCR\\Tesseract.exe'


    def preprocessing (self, img, method):
        gray = self.getGrayscale(img)
        if method == 'gray':
            final_image = gray
        elif method == 'thresh':
            final_image = self.thresholding(gray,50)
        elif method == 'opening':
            final_image = self.opening(gray,5)
        elif method == 'canny':
            final_image = self.canny(gray,100,200)
        elif method == 'dilate':
            final_image = self.dilate(gray,5)
        elif method == 'erode':
            final_image = self.erode(gray,5)
        elif method == 'skew':
            final_image = self.deskew(gray)
        return final_image

    def OCRWords(self, image, gray) : 
        font = cv2.FONT_HERSHEY_SIMPLEX
        bottomLeftCornerOfText = (10,90)
        fontScale = 0.5
        fontColor = (0,0,255)
        lineType  = 2
        d = pytesseract.image_to_data(gray, output_type=Output.DICT)
        im2 = image.copy() 
        n_boxes = len(d['text'])
        for i in range(n_boxes):
            # condition to only pick boxes with a confidence > 60%
            if int(d['conf'][i]) > 60:
                (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
                im2 = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv2.putText(im2,d['text'][i],(x, y),font,fontScale,fontColor,lineType)
            
        return im2 , d

    def OCRCharacter(self, image, gray): 
        font = cv2.FONT_HERSHEY_SIMPLEX
        bottomLeftCornerOfText = (10,90)
        fontScale = 0.5
        fontColor = (0,0,255)
        lineType  = 2
        h, w, c = image.shape
        boxes = pytesseract.image_to_boxes(gray) 
        im2 = image.copy()
        for b in boxes.splitlines():
            b = b.split(' ')
            im2 = cv2.rectangle(im2, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)
            cv2.putText(im2,b[0],(int(b[1]), h - int(b[2])+20),font,fontScale,fontColor,lineType)

        return im2 , b

    def OCR(self, image, method):
        gray = self.preprocessing(image,'gray')
        if method == 'character':
            return self.OCRCharacter(image,gray)
        elif method == 'word':
            return self.OCRWords(image,gray)
         
