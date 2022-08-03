import cv2
import numpy
class Trackbars():
    def __init__(self):
        
        self.trackbar_R = 0
        
        super().__init__()

    def create_trackbars(self):
        
        def nothing(*args):
            pass
        
        self.img = numpy.zeros((300, 512, 3), numpy.uint8)
        
        cv2.namedWindow('trackbarWindow')

        cv2.createTrackbar('Width', 'trackbarWindow', 0, 100, nothing)
        cv2.createTrackbar('Height', 'trackbarWindow', 0, 100, nothing)
        cv2.createTrackbar('lines', 'trackbarWindow', 0, 1, nothing)

        cv2.setTrackbarPos('Width', 'trackbarWindow', 20)
        cv2.setTrackbarPos('Height', 'trackbarWindow', 20)
        cv2.setTrackbarPos('lines', 'trackbarWindow', 1)
    def trackbar_screen(self):
        cv2.imshow('trackbarWindow', self.img)
        if cv2.waitKey(1) == 27:
            exit()        
