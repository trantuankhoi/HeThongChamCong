import time
from os import environ
import sys
import xlsxwriter
from torch.utils.data import DataLoader
from torchvision import datasets
environ["KERAS_BACKEND"] = "plaidml.keras.backend"
import sqlite3
import cv2
import numpy as np
import self as self
import torch
from PySide2 import QtCore
from PySide2.QtCore import QTimer, QPropertyAnimation
from PySide2.QtGui import QImage, QPixmap
from PySide2.QtWidgets import QApplication, QMainWindow
from facenet_pytorch import MTCNN
from matplotlib.pyplot import gray
from ui_main import Ui_MainWindow
sys.path.insert(1, "Lib")
import model, class_user, SQLite, functions, time_keeper
from FaKeep import *
import matplotlib.pyplot as plt

GLOBAL_STATE = 1
faceDetect = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
mtcnn = MTCNN(image_size=240, margin=0, min_face_size=20)  # initializing mtcnn for face detection
resnet = model.load_resnet()
saved_data = model.load_saved_data()
time_keeper.check(time_keeper.getMonth())

class UIFunctions(QMainWindow):

    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == 1:
            GLOBAL_STATE = 0
            self.showMaximized()
        else:
            GLOBAL_STATE = 1
            self.showNormal()

    def toggleMenu(self, maxWidth, enable):
        if enable:
            width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 70

            # SET MAX WIDTH
            if width == 70:
                widthExtended = maxExtend
            else:
                widthExtended = standard
            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    def viewCam(self):
        ret, image = self.cap.read()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        id = functions.checkMatch(image, resnet, saved_data)
        print(id)
        
        time_keeper.timeKeeping(id, time_keeper.getMonth(), time_keeper.getDate())

        qImg = QImage(image.data,  640,480, 1920, QImage.Format_RGB888)
        # show image in img_label
        self.ui.image_label.setPixmap(QPixmap.fromImage(qImg))


    # start/stop timer
    def controlTimer1(self):
        # if timer is stopped
        if not self.timer.isActive():
            # create video capture
            self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
            if not self.cap.isOpened():
                print('Cam is not available')

            else:

                self.timer.start(20)
            # update control_bt text
                self.ui.control_bt.setText("Stop")
        # if timer is started
        else:
            # stop timer
            self.timer.stop()
            # release video capture
            self.cap.release()
            # update control_bt text
            self.ui.control_bt.setText("Start")

class creat(QMainWindow):
    def lay_data_nv(self):
        '''workbook = xlsxwriter.Workbook('C:/Users/Admin/Desktop/ds.xlsx')
        worksheet = workbook.add_worksheet()
        worksheet.write('A2', str(self.ui.lineEdit.text()))
        worksheet.write('B2', str(self.ui.lineEdit_2.text()))
        worksheet.write('C2', str(self.ui.lineEdit_4.text()))
        worksheet.write('D2', str(self.ui.comboBox.currentText()))
        worksheet.write('E2', str(self.ui.lineEdit_5.text()))
        worksheet.write('F2', str(self.ui.dateEdit.text()))
        worksheet.write('G2', str(self.ui.lineEdit_6.text()))
        worksheet.write('H2', str(self.ui.lineEdit_7.text()))
        worksheet.write('I2', str(self.ui.lineEdit_8.text()))
        worksheet.write('J2', str(self.ui.dateEdit_2.text()))
        worksheet.write('K2', str(self.ui.comboBox_3.currentText()))
        worksheet.write('L2', str(self.ui.comboBox_2.currentText()))
        workbook.close()'''

        SQLite.insertUser(str(self.ui.txt_ID.text()), str(self.ui.txt_Name.text()), str(self.ui.comboBox_type.currentText()), str(self.ui.comboBox_position.currentText(), str(self.ui.txt_pass.text())))

    def xem_anh(self):
        ID = self.ui.lineEdit.text()
        pixmap = QPixmap(r'Img\User_Image/'+str(ID)+ '/frame-0.jpg')
        pixmap1 = QPixmap(r'Img\User_Image/'+str(ID)+ '/frame-1.jpg')
        pixmap2 = QPixmap(r'Img\User_Image/'+str(ID)+ '/frame-2.jpg')
        pixmap3 = QPixmap(r'Img\User_Image/'+str(ID)+ '/frame-3.jpg')
        pixmap4 = QPixmap(r'Img\User_Image/'+str(ID)+ '/frame-4.jpg')
        pixmap5 = QPixmap(r'Img\User_Image/'+str(ID)+ '/frame-5.jpg')
        pixmap6 = QPixmap(r'Img\User_Image/'+str(ID)+ '/frame-6.jpg')
        pixmap7 = QPixmap(r'Img\User_Image/'+str(ID)+ '/frame-7.jpg')
        pixmap8 = QPixmap(r'Img\User_Image/'+str(ID)+ '/frame-8.jpg')
        pixmap9 = QPixmap(r'Img\User_Image/'+str(ID)+ '/frame-9.jpg')
        pixmap = pixmap.scaled(239, 239)
        self.ui.label_8.setPixmap(pixmap)
        pixmap1 = pixmap1.scaled(200, 180)
        self.ui.label_20.setPixmap(pixmap1)
        pixmap2 = pixmap2.scaled(200, 180)
        self.ui.label_21.setPixmap(pixmap2)
        pixmap3 = pixmap3.scaled(200, 180)
        self.ui.label_22.setPixmap(pixmap3)
        pixmap4 = pixmap4.scaled(200, 180)
        self.ui.label_23.setPixmap(pixmap4)
        pixmap5 = pixmap5.scaled(200, 180)
        self.ui.label_24.setPixmap(pixmap5)
        pixmap6 = pixmap6.scaled(200, 180)
        self.ui.label_25.setPixmap(pixmap6)
        pixmap7 = pixmap7.scaled(200, 180)
        self.ui.label_26.setPixmap(pixmap7)
        pixmap8 = pixmap8.scaled(200, 180)
        self.ui.label_27.setPixmap(pixmap8)
        pixmap9 = pixmap9.scaled(200, 180)
        self.ui.label_28.setPixmap(pixmap9)

    def mo_file(self):
        ID = self.ui.lineEdit.text()
        workbook = xlsxwriter.Workbook('C:/Users/Admin/Desktop/ds.xlsx')
        worksheet = workbook.add_worksheet()
        worksheet.write('A'+str(ID), str(self.ui.lineEdit.text()))
        worksheet.write('B'+str(ID), str(self.ui.lineEdit_2.text()))
        worksheet.write('C'+str(ID), str(self.ui.lineEdit_4.text()))
        worksheet.write('D'+str(ID), str(self.ui.comboBox.currentText()))
        worksheet.write('E'+str(ID), str(self.ui.lineEdit_5.text()))
        worksheet.write('F'+str(ID), str(self.ui.dateEdit.text()))
        worksheet.write('G'+str(ID), str(self.ui.lineEdit_6.text()))
        worksheet.write('H'+str(ID), str(self.ui.lineEdit_7.text()))
        worksheet.write('I'+str(ID), str(self.ui.lineEdit_8.text()))
        worksheet.write('J'+str(ID), str(self.ui.dateEdit_2.text()))
        worksheet.write('K'+str(ID), str(self.ui.comboBox_3.currentText()))
        worksheet.write('L'+str(ID), str(self.ui.comboBox_2.currentText()))
        workbook.close()
        os.startfile('C:/Users/Admin/Desktop/GUI/Data/dataset/' + str(ID))

    def viewCam2(self):
        ret, image = self.cap.read()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        faces = faceDetect.detectMultiScale(image, scaleFactor=1.3, minNeighbors=5)
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
        qImg = QImage(image,  640,480, 1920, QImage.Format_RGB888)
        self.ui.label_10.setPixmap(QPixmap.fromImage(qImg))

    def controlTimer2(self):
        ID = self.ui.txt_ID.text()
        newpath = r'Img\User_Image/' + str(ID)
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        while True:
            if not self.timer2.isActive():
                # create video capture
                self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
                self.dem = 0
                if not self.cap.isOpened():
                    print('Cam is not available')
                else:
                    self.timer2.start(20)
            else:
                ret, image = self.cap.read()
                cv2.imwrite(r'Img\\User_Image\\' + str(ID) + "\\frame-" + str(self.dem)  + ".jpg", image)
                self.dem += 1
                if self.dem == 10:
                    self.timer.stop()
                    self.cap.release()

    # start/stop timer
    def controlTimer3(self):
        # if timer is stopped
        if not self.timer.isActive():
            # create video capture
            self.count = 0
            self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
            if not self.cap.isOpened():
                print('Cam is not available')

            else:

                self.timer.start(20)
            # update control_bt text
                self.ui.control_bt.setText("Stop")
        # if timer is started
        else:
            if self.count == 10:
                # stop timer
                self.timer.stop()
                # release video capture
                self.cap.release()
                # update control_bt text
                self.ui.control_bt.setText("Start")

    def them(self):
        SQLite.insertUser(str(self.ui.txt_ID.text()), str(self.ui.txt_Name.text()), str(self.ui.comboBox_position.currentText()), str(self.ui.comboBox_type.currentText()), str(self.ui.txt_pass1.text()))
