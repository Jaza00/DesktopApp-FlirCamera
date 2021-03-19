from processing.ocr import Ocr
import cv2

def testOCR():
    ocr = Ocr()

    img = cv2.imread("sample2.jpg") 

    
    result,dictionary = ocr.OCR(gray, 'word')

    cv2.imshow("frame", result)

    cv2.waitKey(0)  
    cv2.destroyAllWindows()