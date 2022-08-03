import numpy as np
import cv2
import extra_systems.mainLineWindow
import time
print("Physik")

class Physik():
    def __init__(self):
        
        self.ScreenWidth = 1024
        self.ScreenHeight = 712
        self.screenlineWidth_aralik = 100 #genişlik aralık değişkeni
        self.screenlineHeight_aralik = 100 #yükseklik aralık değişkeni
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        
        self.CreateMainScreen()
        while 1:
            self.TaleopPeriodic()    
        super().__init__()
    def copy_img(self):
        self.copied_image = self.mainWindow.copy()
    def clear_img(self):
        self.mainWindow = self.copied_image.copy()
    def CreateMainScreen(self):
        
        self.mainWindow = np.zeros((self.ScreenHeight,self.ScreenWidth,3),np.uint8)
        self.copy_img()
        extra_systems.mainLineWindow.createLines(self.mainWindow,self.ScreenWidth,self.ScreenHeight,self.screenlineWidth_aralik,self.screenlineHeight_aralik,self.font)

        
    
    def TaleopPeriodic(self):
        cv2.imshow("mainWindow",self.mainWindow)
        if cv2.waitKey(1) == 27:
            self.clear_img()

Physik()