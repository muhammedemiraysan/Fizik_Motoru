import cv2
import numpy as np

def createLines(mainWindow,ScreenWidth,ScreenHeight,screenlineWidth_aralik,screenlineHeight_aralik,font):
    
    for i in range(0,int(ScreenWidth/(screenlineWidth_aralik/2))):
        cv2.line(mainWindow, (i*screenlineWidth_aralik,30),(i*screenlineWidth_aralik,50),(255,0,0),1)
    
        cv2.putText(mainWindow,str(i*screenlineWidth_aralik),(i*screenlineWidth_aralik,10), font, 0.2,(255,0,0),1,cv2.LINE_AA)
    
    for i in range(0,int(ScreenHeight/(screenlineHeight_aralik/2))):
        cv2.line(mainWindow, (30,i*screenlineHeight_aralik),(50,i*screenlineHeight_aralik),(0,255,0),1)
    
        cv2.putText(mainWindow,str(i*screenlineHeight_aralik),(10,i*screenlineHeight_aralik), font, 0.2,(0,255,0),1,cv2.LINE_AA)
