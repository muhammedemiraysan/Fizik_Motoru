from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(700, 10, 91, 17))
        self.checkBox.setObjectName("checkBox")
        self.cizgi_araligi_Y_slider = QtWidgets.QSlider(self.centralwidget)
        self.cizgi_araligi_Y_slider.setGeometry(QtCore.QRect(750, 30, 19, 160))
        self.cizgi_araligi_Y_slider.setMinimum(1)
        self.cizgi_araligi_Y_slider.setMaximum(100)
        self.cizgi_araligi_Y_slider.setOrientation(QtCore.Qt.Vertical)
        self.cizgi_araligi_Y_slider.setObjectName("cizgi_araligi_Y_slider")
        self.cizgi_araligi_X_slider = QtWidgets.QSlider(self.centralwidget)
        self.cizgi_araligi_X_slider.setGeometry(QtCore.QRect(670, 30, 19, 160))
        self.cizgi_araligi_X_slider.setMinimum(1)
        self.cizgi_araligi_X_slider.setMaximum(100)
        self.cizgi_araligi_X_slider.setTracking(True)
        self.cizgi_araligi_X_slider.setOrientation(QtCore.Qt.Vertical)
        self.cizgi_araligi_X_slider.setObjectName("cizgi_araligi_X_slider")
        self.cizgi_araligi_X = QtWidgets.QLabel(self.centralwidget)
        self.cizgi_araligi_X.setGeometry(QtCore.QRect(650, 179, 71, 31))
        self.cizgi_araligi_X.setObjectName("cizgi_araligi_X")
        self.cizgi_araligi_Y = QtWidgets.QLabel(self.centralwidget)
        self.cizgi_araligi_Y.setGeometry(QtCore.QRect(730, 185, 71, 21))
        self.cizgi_araligi_Y.setObjectName("cizgi_araligi_Y")
        self.Powered_By = QtWidgets.QLabel(self.centralwidget)
        self.Powered_By.setGeometry(QtCore.QRect(10, 540, 181, 16))
        self.Powered_By.setObjectName("Powered_By")
        self.slider_X_veriable = QtWidgets.QLabel(self.centralwidget)
        self.slider_X_veriable.setGeometry(QtCore.QRect(660, 100, 16, 16))
        self.slider_X_veriable.setObjectName("slider_X_veriable")
        self.slider_Y_veriable = QtWidgets.QLabel(self.centralwidget)
        self.slider_Y_veriable.setGeometry(QtCore.QRect(740, 100, 16, 16))
        self.slider_Y_veriable.setObjectName("slider_Y_veriable")
        self.quitButton = QtWidgets.QPushButton(self.centralwidget)
        self.quitButton.setGeometry(QtCore.QRect(680, 530, 101, 21))
        self.quitButton.setAutoFillBackground(False)
        self.quitButton.setCheckable(True)
        self.quitButton.setObjectName("quitButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkBox.setText(_translate("MainWindow", "Cetvel Çizgileri"))
        self.cizgi_araligi_X.setText(_translate("MainWindow", "Çizgi Aralığı X"))
        self.cizgi_araligi_Y.setText(_translate("MainWindow", "Çizgi Aralığı Y"))
        self.Powered_By.setText(_translate("MainWindow", "Powered By: Muhammed Emir AYSAN"))
        self.slider_X_veriable.setText(_translate("MainWindow", "0"))
        self.slider_Y_veriable.setText(_translate("MainWindow", "0"))
        self.quitButton.setText(_translate("MainWindow", "Uygulamayı Kapat"))

    def get_slider_xValue(self,MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.slider_X_veriable.setText(_translate("MainWindow", str(self.cizgi_araligi_X_slider.value())))
        return self.cizgi_araligi_X_slider.value()
    def get_slider_yValue(self,MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.slider_Y_veriable.setText(_translate("MainWindow", str(self.cizgi_araligi_Y_slider.value())))
        return self.cizgi_araligi_Y_slider.value()
    def get_checkbox_Value(self,MainWindow):
        return self.checkBox.isChecked()
    def get_quitbutton_Value(self,MainWindow):
        return self.quitButton.isChecked()
import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
