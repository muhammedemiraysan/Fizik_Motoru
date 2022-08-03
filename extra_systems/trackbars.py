import cv2
import numpy
class Trackbars():
    def __init__(self):
        super().__init__()
    def create_trackbars(self):
        def nothing():
            pass
        self.img = numpy.zeros((300, 512, 3), numpy.uint8)
        cv2.namedWindow('trackbarWindow')
        cv2.createTrackbar('R', 'trackbarWindow', 0, 255, nothing)

    def get_trackbar_pos(self):
        cv2.imshow('trackbarWindow', self.img)
        if cv2.waitKey(1) == 27:
            exit()        
        print(cv2.getTrackbarPos('R', 'trackbarWindow'))