from simple_pyspin import Camera
import cv2


with Camera() as cam: # Initialize Camera
    # Set the area of interest (AOI) to the middle half
    cam.Width = cam.SensorWidth // 2
    cam.Height = cam.SensorHeight // 2
    cam.OffsetX = cam.SensorWidth // 4
    cam.OffsetY = cam.SensorHeight // 4

    # If this is a color camera, get the image in RGB format.
    if 'Bayer' in cam.PixelFormat:
        cam.PixelFormat = "RGB8"

    cam.init() 
    cam.start() 

    print("start video")
    while True:
        # capturar frame a frame
        frame = cam.get_array()
        cv2.imshow("frame", frame) 
        if cv2.waitKey(1) == ord('q'): #presionamos la tecla Q para cerrar la ventanas
            break
    
    cv2.destroyAllWindows()
    print("stop video")