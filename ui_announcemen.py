# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_announcemen.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_Announcemen(object):
    def setupUi(self, Announcemen):
        Announcemen.setObjectName("Announcemen")
        Announcemen.resize(547, 190)
        Announcemen.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(Announcemen)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_announcemen = QtWidgets.QFrame(Announcemen)
        self.frame_announcemen.setStyleSheet("\n"
"\n"
"background-color: rgb(240, 240, 240);")
        self.frame_announcemen.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_announcemen.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_announcemen.setObjectName("frame_announcemen")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_announcemen)
        self.verticalLayout_2.setContentsMargins(-1, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_title_announcemen = QtWidgets.QFrame(self.frame_announcemen)
        self.frame_title_announcemen.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_title_announcemen.setStyleSheet("background-color: rgb(204, 111, 101);")
        self.frame_title_announcemen.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_title_announcemen.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_title_announcemen.setObjectName("frame_title_announcemen")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_title_announcemen)
        self.verticalLayout_3.setContentsMargins(15, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.title_announcemen = QtWidgets.QLabel(self.frame_title_announcemen)
        self.title_announcemen.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.title_announcemen.setObjectName("title_announcemen")
        self.verticalLayout_3.addWidget(self.title_announcemen)
        self.verticalLayout_2.addWidget(self.frame_title_announcemen)
        self.frame_text = QtWidgets.QFrame(self.frame_announcemen)
        self.frame_text.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.frame_text.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_text.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_text.setObjectName("frame_text")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_text)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.frame_text)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.verticalLayout_2.addWidget(self.frame_text)
        self.verticalLayout.addWidget(self.frame_announcemen)
        self.retranslateUi(Announcemen)
        QtCore.QMetaObject.connectSlotsByName(Announcemen)

    def retranslateUi(self, Announcemen):
        _translate = QtCore.QCoreApplication.translate
        Announcemen.setWindowTitle(_translate("Announcemen", "Form"))
        self.title_announcemen.setText(_translate("Announcemen", "Thông báo"))
