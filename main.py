import numpy as np
import cv2
import time
import extra_systems.mainLineWindow
from arayuz.arayuz import Ui_MainWindow, MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

print("Physik")

class Physik():
    def __init__(self):
        
        self.ScreenWidth = 1024
        self.ScreenHeight = 712
        self.screenlineWidth_aralik = 100 #genişlik aralık değişkeni
        self.screenlineHeight_aralik = 100 #yükseklik aralık değişkeni
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        Ui_MainWindow.setupUi(self,MainWindow)
        self.CreateMainScreen()
        while 1:
            self.TaleopPeriodic()    
        super().__init__()
    def copy_img(self):
        self.copied_image = self.mainWindow.copy()
    def clear_img(self):
        self.mainWindow = self.copied_image.copy()

    def CreateMainScreen(self):
        Ui_MainWindow.retranslateUi(self,MainWindow)
        self.mainWindow = np.zeros((self.ScreenHeight,self.ScreenWidth,3),np.uint8)
        self.copy_img()
        extra_systems.mainLineWindow.createLines(self.mainWindow,self.ScreenWidth,self.ScreenHeight,self.screenlineWidth_aralik,self.screenlineHeight_aralik,self.font)

        
    
    def TaleopPeriodic(self):
        self.clear_img()
        self.copy_img()

        self.screenlineHeight_aralik = int(Ui_MainWindow.get_slider_xValue(self,MainWindow))
        self.screenlineWidth_aralik = int(Ui_MainWindow.get_slider_yValue(self,MainWindow))

        if self.screenlineHeight_aralik > 0:
            pass
        else:
            self.screenlineHeight_aralik = 1
        if self.screenlineWidth_aralik > 0:
            pass
        else:
            self.screenlineWidth_aralik = 1

        if Ui_MainWindow.get_checkbox_Value(self,MainWindow):
            extra_systems.mainLineWindow.createLines(self.mainWindow,self.ScreenWidth,self.ScreenHeight,self.screenlineWidth_aralik,self.screenlineHeight_aralik,self.font)
        
        cv2.imshow("mainWindow",self.mainWindow)
        cv2.waitKey(1)
        if Ui_MainWindow.get_quitbutton_Value(self,MainWindow):
            exit()

Physik()
