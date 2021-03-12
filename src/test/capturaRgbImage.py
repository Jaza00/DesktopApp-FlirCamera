from src.acquisition.acquisition import  Acquisition
import cv2


cam = Acquisition()
frame = cam.getRgbImage()
print(frame.shape)
cv2.imshow("frame", frame) 
cv2.waitKey(0)
cv2.destroyAllWindows()