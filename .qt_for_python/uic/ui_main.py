# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1216, 806)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Top_Bar = QFrame(self.centralwidget)
        self.Top_Bar.setObjectName(u"Top_Bar")
        self.Top_Bar.setMaximumSize(QSize(16777215, 40))
        self.Top_Bar.setStyleSheet(u"background-color: rgb(117, 12, 26);")
        self.Top_Bar.setFrameShape(QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.Top_Bar)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 40))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(151, 10, 16);")
        self.frame_toggle.setFrameShape(QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_toggle)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Btn_loggle = QPushButton(self.frame_toggle)
        self.Btn_loggle.setObjectName(u"Btn_loggle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_loggle.sizePolicy().hasHeightForWidth())
        self.Btn_loggle.setSizePolicy(sizePolicy)
        self.Btn_loggle.setStyleSheet(u"QPushButton {	\n"
"background-image: url(:/20x20/icons/20x20/cil-menu.png);\n"
"	background-position: center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(117, 12, 26);\n"
"\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.Btn_loggle)


        self.horizontalLayout.addWidget(self.frame_toggle)

        self.frame_top = QFrame(self.Top_Bar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(15, 0, 0, 0)
        self.label_9 = QLabel(self.frame_top)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_8.addWidget(self.label_9)


        self.horizontalLayout.addWidget(self.frame_top)

        self.frame = QFrame(self.Top_Bar)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMaximumSize(QSize(180, 90))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton_6 = QPushButton(self.frame)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(0, 30))
        self.pushButton_6.setStyleSheet(u"QPushButton {	\n"
"	\n"
"	background-image: url(:/16x16/icons/16x16/cil-window-minimize.png);\n"
"	background-position: top center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(151, 10, 16);\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.pushButton_6)

        self.pushButton_5 = QPushButton(self.frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(0, 30))
        self.pushButton_5.setStyleSheet(u"QPushButton {	\n"
"	\n"
"	background-image: url(:/16x16/icons/16x16/cil-window-restore.png);\n"
"	background-position:center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(151, 10, 16);\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.pushButton_5)

        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 30))
        self.pushButton_4.setStyleSheet(u"QPushButton {	\n"
"	\n"
"	background-image: url(:/16x16/icons/16x16/cil-x.png);\n"
"	background-position: center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(151, 10, 16);\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.pushButton_4)


        self.horizontalLayout.addWidget(self.frame)


        self.verticalLayout.addWidget(self.Top_Bar)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.Content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(151, 10, 16);")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menu = QFrame(self.frame_left_menu)
        self.frame_top_menu.setObjectName(u"frame_top_menu")
        self.frame_top_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_top_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_top_menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton_1 = QPushButton(self.frame_top_menu)
        self.pushButton_1.setObjectName(u"pushButton_1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_1.sizePolicy().hasHeightForWidth())
        self.pushButton_1.setSizePolicy(sizePolicy2)
        self.pushButton_1.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setFamily(u"Segoe UI")
        self.pushButton_1.setFont(font)
        self.pushButton_1.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(255, 255, 255);\n"
"	background-image: url(:/20x20/icons/20x20/cil-home.png);\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 28px solid  rgb(151, 10, 16);\n"
"	background-color:  rgb(151, 10, 16);\n"
"	text-align: left;\n"
"	padding-left: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(117, 12, 26);\n"
"	border-left: 28px solid rgb(117, 12, 26);\n"
"}\n"
"")
        self.pushButton_1.setIconSize(QSize(20, 20))

        self.verticalLayout_3.addWidget(self.pushButton_1)

        self.pushButton_7 = QPushButton(self.frame_top_menu)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(0, 50))
        self.pushButton_7.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(255, 255, 255);\n"
"	background-image: url(:/20x20/icons/20x20/cil-user.png);\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 28px solid  rgb(151, 10, 16);\n"
"	background-color:  rgb(151, 10, 16);\n"
"	text-align: left;\n"
"	padding-left: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(117, 12, 26);\n"
"	border-left: 28px solid rgb(117, 12, 26);\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.pushButton_7)

        self.pushButton_22 = QPushButton(self.frame_top_menu)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setMinimumSize(QSize(0, 50))
        self.pushButton_22.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(255, 255, 255);\n"
"	background-image: url(:/20x20/icons/20x20/cil-voice-over-record.png);\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 28px solid  rgb(151, 10, 16);\n"
"	background-color:  rgb(151, 10, 16);\n"
"	text-align: left;\n"
"	padding-left: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(117, 12, 26);\n"
"	border-left: 28px solid rgb(117, 12, 26);\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.pushButton_22)

        self.pushButton = QPushButton(self.frame_top_menu)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 50))
        self.pushButton.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-image: url(:/20x20/icons/20x20/cil-user-follow.png);\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 28px solid  rgb(151, 10, 16);\n"
"	background-color:  rgb(151, 10, 16);\n"
"	text-align: left;\n"
"	padding-left: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(117, 12, 26);\n"
"	border-left: 28px solid rgb(117, 12, 26);\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_top_menu)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 50))
        self.pushButton_2.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-image: url(:/20x20/icons/20x20/cil-settings.png);\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 28px solid  rgb(151, 10, 16);\n"
"	background-color:  rgb(151, 10, 16);\n"
"	text-align: left;\n"
"	padding-left: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(117, 12, 26);\n"
"	border-left: 28px solid rgb(117, 12, 26);\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_top_menu)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 50))
        self.pushButton_3.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-image: url(:/16x16/icons/16x16/cil-account-logout.png);\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 28px solid  rgb(151, 10, 16);\n"
"	background-color:  rgb(151, 10, 16);\n"
"	text-align: left;\n"
"	padding-left: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(117, 12, 26);\n"
"	border-left: 28px solid rgb(117, 12, 26);\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.pushButton_3)


        self.verticalLayout_2.addWidget(self.frame_top_menu, 0, Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.Pages = QStackedWidget(self.frame_pages)
        self.Pages.setObjectName(u"Pages")
        self.Pages.setMinimumSize(QSize(70, 0))
        self.Pages.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.PagesPage1_2 = QWidget()
        self.PagesPage1_2.setObjectName(u"PagesPage1_2")
        self.horizontalLayout_5 = QHBoxLayout(self.PagesPage1_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_2 = QFrame(self.PagesPage1_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setStyleSheet(u"background-color: #CBC3BE;\n"
"background-color: rgb(255, 32, 35);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(14)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, -1, 0, -1)
        self.image_label = QLabel(self.frame_2)
        self.image_label.setObjectName(u"image_label")
        self.image_label.setStyleSheet(u"background-color: #CBC3BE;\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.image_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.image_label)

        self.control_bt = QPushButton(self.frame_2)
        self.control_bt.setObjectName(u"control_bt")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.control_bt.sizePolicy().hasHeightForWidth())
        self.control_bt.setSizePolicy(sizePolicy3)
        self.control_bt.setMinimumSize(QSize(200, 35))
        self.control_bt.setMaximumSize(QSize(500, 16777215))
        self.control_bt.setSizeIncrement(QSize(0, 0))
        self.control_bt.setBaseSize(QSize(0, 0))
        self.control_bt.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(117, 12, 26);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.control_bt.setAutoRepeatInterval(100)

        self.verticalLayout_5.addWidget(self.control_bt, 0, Qt.AlignHCenter)


        self.horizontalLayout_15.addLayout(self.verticalLayout_5)


        self.horizontalLayout_5.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.PagesPage1_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: #CBC3BE;background-color: rgb(255, 32, 35);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(14)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, -1, 0, -1)
        self.image_label_2 = QLabel(self.frame_3)
        self.image_label_2.setObjectName(u"image_label_2")
        self.image_label_2.setStyleSheet(u"background-color: #CBC3BE;\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.image_label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.image_label_2)

        self.control_bt_2 = QPushButton(self.frame_3)
        self.control_bt_2.setObjectName(u"control_bt_2")
        self.control_bt_2.setMinimumSize(QSize(200, 35))
        self.control_bt_2.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(117, 12, 26);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")

        self.verticalLayout_7.addWidget(self.control_bt_2, 0, Qt.AlignHCenter)


        self.horizontalLayout_6.addLayout(self.verticalLayout_7)


        self.horizontalLayout_5.addWidget(self.frame_3)

        self.Pages.addWidget(self.PagesPage1_2)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_13 = QVBoxLayout(self.page)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.page)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_13)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_16 = QFrame(self.frame_13)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 30))
        self.frame_16.setMaximumSize(QSize(16777215, 30))
        self.frame_16.setStyleSheet(u"background-color: rgb(255, 42, 45);font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);    border-radius: 10px;")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_16)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.frame_16)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_16.addWidget(self.label_11)


        self.verticalLayout_14.addWidget(self.frame_16)

        self.frame_14 = QFrame(self.frame_13)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_14)
        self.verticalLayout_15.setSpacing(14)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.frame_14)
        self.frame_17.setObjectName(u"frame_17")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy4)
        self.frame_17.setMinimumSize(QSize(0, 100))
        self.frame_17.setMaximumSize(QSize(10000, 200))
        self.frame_17.setStyleSheet(u"")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_17)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.frame_17)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";border-radius: 10px;background-color: rgba(204, 111, 101);")

        self.verticalLayout_18.addWidget(self.label_13)

        self.frame_21 = QFrame(self.frame_17)
        self.frame_21.setObjectName(u"frame_21")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy5)
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_13.setSpacing(35)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.pushButton_19 = QPushButton(self.frame_21)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setMaximumSize(QSize(70, 35))
        self.pushButton_19.setStyleSheet(u"QPushButton {	\n"
"background-color: rgb(255, 21, 71);\n"
"	background-image: url(:/16x16/icons/16x16/cil-reload.png);\n"
"	background-position: center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(151, 10, 16);\n"
"}\n"
"")

        self.horizontalLayout_13.addWidget(self.pushButton_19)

        self.lineEdit_3 = QLineEdit(self.frame_21)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy6)
        self.lineEdit_3.setMinimumSize(QSize(100, 35))

        self.horizontalLayout_13.addWidget(self.lineEdit_3)

        self.lineEdit_12 = QLineEdit(self.frame_21)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        sizePolicy6.setHeightForWidth(self.lineEdit_12.sizePolicy().hasHeightForWidth())
        self.lineEdit_12.setSizePolicy(sizePolicy6)
        self.lineEdit_12.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_13.addWidget(self.lineEdit_12)

        self.lineEdit_13 = QLineEdit(self.frame_21)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        sizePolicy6.setHeightForWidth(self.lineEdit_13.sizePolicy().hasHeightForWidth())
        self.lineEdit_13.setSizePolicy(sizePolicy6)
        self.lineEdit_13.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_13.addWidget(self.lineEdit_13)

        self.comboBox_8 = QComboBox(self.frame_21)
        self.comboBox_8.setObjectName(u"comboBox_8")
        self.comboBox_8.setMinimumSize(QSize(0, 35))
        self.comboBox_8.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_13.addWidget(self.comboBox_8)

        self.dateTimeEdit = QDateTimeEdit(self.frame_21)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_13.addWidget(self.dateTimeEdit)

        self.dateTimeEdit_2 = QDateTimeEdit(self.frame_21)
        self.dateTimeEdit_2.setObjectName(u"dateTimeEdit_2")
        self.dateTimeEdit_2.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_13.addWidget(self.dateTimeEdit_2)

        self.pushButton_18 = QPushButton(self.frame_21)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setMinimumSize(QSize(35, 35))
        self.pushButton_18.setMaximumSize(QSize(70, 35))
        self.pushButton_18.setStyleSheet(u"QPushButton {	\n"
"background-color: rgb(255, 21, 71);\n"
"	\n"
"	background-image: url(:/16x16/icons/16x16/cil-magnifying-glass.png);\n"
"	background-position: center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(151, 10, 16);\n"
"}\n"
"")

        self.horizontalLayout_13.addWidget(self.pushButton_18)


        self.verticalLayout_18.addWidget(self.frame_21)


        self.verticalLayout_15.addWidget(self.frame_17)

        self.frame_18 = QFrame(self.frame_14)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setStyleSheet(u"background-color: rgb(229, 229, 229);")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_18)
        self.verticalLayout_17.setSpacing(5)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(5, 5, 5, 5)
        self.tableWidget = QTableWidget(self.frame_18)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem.setBackground(QColor(134, 134, 134, 0));
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem5.setBackground(QColor(0, 0, 0, 0));
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"/* VERTICAL SCROLLBAR */\n"
"\n"
"QScrollBar:vertical {\n"
"	background: rgb(180, 28, 222);\n"
"    width: 20px;\n"
"    margin:0 0 0 0;\n"
"	border-radius: 7px;\n"
" }\n"
"QScrollBar::handle:vertical {	\n"
"	min-height: 30px;\n"
"	border-radius: 7px;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	height: 15px;\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"	border: none;\n"
"	height: 15px;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-bottom-right-radius: 7px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"	background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"}\n"
"\n"
"/*-----------------*/\n"
" QScrollBar:horizontall {\n"
"	border: none;\n"
"    bac"
                        "kground: rgb(45, 45, 68);\n"
"    width: 20px;\n"
"    margin:0 0 0 0;\n"
"	border-radius: 7px;\n"
" }\n"
"QScrollBar::handle:horizontall {	\n"
"	background-color: rgb(80, 80, 122);\n"
"	min-height: 30px;\n"
"	border-radius: 7px;\n"
"}\n"
"QScrollBar::sub-line:horizontall {\n"
"	border: none;\n"
"	background-color: rgb(59, 59, 90);\n"
"	height: 15px;\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:horizontall{\n"
"	border: none;\n"
"	background-color: rgb(59, 59, 90);\n"
"	height: 15px;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-bottom-right-radius: 7px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontall, QScrollBar::down-arrow:horizontall {\n"
"	background: none;\n"
"}\n"
"QScrollBar::add-page:horizontall, QScrollBar::sub-page:horizontall {\n"
"	background: none;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
""
                        "\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(280)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setHighlightSections(True)

        self.verticalLayout_17.addWidget(self.tableWidget)


        self.verticalLayout_15.addWidget(self.frame_18)


        self.verticalLayout_14.addWidget(self.frame_14)


        self.verticalLayout_13.addWidget(self.frame_13)

        self.Pages.addWidget(self.page)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_33 = QVBoxLayout(self.page_3)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.frame_22 = QFrame(self.page_3)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_22)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame_23 = QFrame(self.frame_22)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(0, 30))
        self.frame_23.setMaximumSize(QSize(16777215, 30))
        self.frame_23.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";background-color: rgba(204, 111, 101);\n"
"color: rgb(255, 255, 255);    border-radius: 10px;")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_23)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_38 = QLabel(self.frame_23)
        self.label_38.setObjectName(u"label_38")

        self.verticalLayout_29.addWidget(self.label_38)


        self.verticalLayout_20.addWidget(self.frame_23)

        self.frame_31 = QFrame(self.frame_22)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMinimumSize(QSize(550, 50))
        self.frame_31.setMaximumSize(QSize(16777215, 30))
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_14 = QLineEdit(self.frame_31)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setMaximumSize(QSize(300, 35))
        self.lineEdit_14.setStyleSheet(u"QLineEdit{\n"
"	border: 2px solid rgb(170, 0, 0);\n"
"	border-radius: 10px;\n"
"	background-color: rgb(255, 84, 224);\n"
"}\n"
"")

        self.horizontalLayout_14.addWidget(self.lineEdit_14)

        self.pushButton_20 = QPushButton(self.frame_31)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setMinimumSize(QSize(35, 35))
        self.pushButton_20.setMaximumSize(QSize(70, 35))
        self.pushButton_20.setStyleSheet(u"QPushButton {	\n"
"background-color: rgb(255, 21, 71);\n"
"	\n"
"	background-image: url(:/16x16/icons/16x16/cil-magnifying-glass.png);\n"
"	background-position: center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(151, 10, 16);\n"
"}\n"
"")

        self.horizontalLayout_14.addWidget(self.pushButton_20)

        self.pushButton_21 = QPushButton(self.frame_31)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setMinimumSize(QSize(35, 35))
        self.pushButton_21.setMaximumSize(QSize(70, 35))
        self.pushButton_21.setStyleSheet(u"QPushButton {	\n"
"background-color: rgb(255, 21, 71);\n"
"	\n"
"	background-image: url(:/16x16/icons/16x16/cil-plus.png);\n"
"	background-position: center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(151, 10, 16);\n"
"}\n"
"")

        self.horizontalLayout_14.addWidget(self.pushButton_21)

        self.pushButton_24 = QPushButton(self.frame_31)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setMinimumSize(QSize(35, 35))
        self.pushButton_24.setMaximumSize(QSize(70, 35))
        self.pushButton_24.setStyleSheet(u"QPushButton {	\n"
"background-color: rgb(255, 21, 71);\n"
"	\n"
"	background-image: url(:/16x16/icons/16x16/cil-pencil.png);\n"
"	background-position: center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(151, 10, 16);\n"
"}\n"
"")

        self.horizontalLayout_14.addWidget(self.pushButton_24)

        self.pushButton_23 = QPushButton(self.frame_31)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setMinimumSize(QSize(35, 35))
        self.pushButton_23.setMaximumSize(QSize(70, 35))
        self.pushButton_23.setStyleSheet(u"QPushButton {	\n"
"background-color: rgb(255, 21, 71);\n"
"	background-image: url(:/16x16/icons/16x16/cil-remove.png);\n"
"	background-position: center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(151, 10, 16);\n"
"}\n"
"")

        self.horizontalLayout_14.addWidget(self.pushButton_23)


        self.verticalLayout_20.addWidget(self.frame_31, 0, Qt.AlignRight|Qt.AlignVCenter)

        self.frame_30 = QFrame(self.frame_22)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_30)
        self.verticalLayout_30.setSpacing(14)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.frame_33 = QFrame(self.frame_30)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setStyleSheet(u"background-color: rgb(229, 229, 229);")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_33)
        self.verticalLayout_32.setSpacing(5)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(5, 5, 5, 5)
        self.tableWidget_2 = QTableWidget(self.frame_33)
        if (self.tableWidget_2.columnCount() < 6):
            self.tableWidget_2.setColumnCount(6)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem6.setBackground(QColor(134, 134, 134, 0));
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem11)
        if (self.tableWidget_2.rowCount() < 100):
            self.tableWidget_2.setRowCount(100)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setStyleSheet(u"/* VERTICAL SCROLLBAR */\n"
"\n"
"QScrollBar:vertical {\n"
"	background: rgb(180, 28, 222);\n"
"    width: 20px;\n"
"    margin:0 0 0 0;\n"
"	border-radius: 7px;\n"
" }\n"
"QScrollBar::handle:vertical {	\n"
"	min-height: 30px;\n"
"	border-radius: 7px;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	height: 15px;\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"	border: none;\n"
"	height: 15px;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-bottom-right-radius: 7px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"	background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"}\n"
"\n"
"/*-----------------*/\n"
" QScrollBar:horizontall {\n"
"	border: none;\n"
"    bac"
                        "kground: rgb(45, 45, 68);\n"
"    width: 20px;\n"
"    margin:0 0 0 0;\n"
"	border-radius: 7px;\n"
" }\n"
"QScrollBar::handle:horizontall {	\n"
"	background-color: rgb(80, 80, 122);\n"
"	min-height: 30px;\n"
"	border-radius: 7px;\n"
"}\n"
"QScrollBar::sub-line:horizontall {\n"
"	border: none;\n"
"	background-color: rgb(59, 59, 90);\n"
"	height: 15px;\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:horizontall{\n"
"	border: none;\n"
"	background-color: rgb(59, 59, 90);\n"
"	height: 15px;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-bottom-right-radius: 7px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontall, QScrollBar::down-arrow:horizontall {\n"
"	background: none;\n"
"}\n"
"QScrollBar::add-page:horizontall, QScrollBar::sub-page:horizontall {\n"
"	background: none;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
""
                        "\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.tableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.setShowGrid(True)
        self.tableWidget_2.setGridStyle(Qt.SolidLine)
        self.tableWidget_2.setSortingEnabled(False)
        self.tableWidget_2.setRowCount(100)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(280)
        self.tableWidget_2.horizontalHeader().setHighlightSections(False)
        self.tableWidget_2.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setHighlightSections(True)

        self.verticalLayout_32.addWidget(self.tableWidget_2)


        self.verticalLayout_30.addWidget(self.frame_33)


        self.verticalLayout_20.addWidget(self.frame_30)


        self.verticalLayout_33.addWidget(self.frame_22)

        self.Pages.addWidget(self.page_3)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.horizontalLayout_12 = QHBoxLayout(self.page_2)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.frame_26 = QFrame(self.page_2)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_26)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frame_35 = QFrame(self.frame_26)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setMaximumSize(QSize(16777215, 35))
        self.frame_35.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";background-color: rgba(204, 111, 101);\n"
"color: rgb(255, 255, 255);    border-radius: 10px;")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_35)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.frame_35)
        self.label_12.setObjectName(u"label_12")
        sizePolicy7 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy7)
        self.label_12.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_22.addWidget(self.label_12)


        self.verticalLayout_21.addWidget(self.frame_35)

        self.frame_28 = QFrame(self.frame_26)
        self.frame_28.setObjectName(u"frame_28")
        sizePolicy5.setHeightForWidth(self.frame_28.sizePolicy().hasHeightForWidth())
        self.frame_28.setSizePolicy(sizePolicy5)
        self.frame_28.setStyleSheet(u"background-color: rgb(198, 198, 198);")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_28)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setVerticalSpacing(11)
        self.gridLayout_4.setContentsMargins(11, -1, -1, -1)
        self.frame_38 = QFrame(self.frame_28)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setMaximumSize(QSize(640, 300))
        self.frame_38.setStyleSheet(u"")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_38)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.frame_39 = QFrame(self.frame_38)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setMaximumSize(QSize(16777215, 50))
        self.frame_39.setStyleSheet(u"background-color: rgb(23, 38, 255);\n"
"color: rgb(255, 255, 255);")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_39)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_29 = QLabel(self.frame_39)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_24.addWidget(self.label_29)


        self.verticalLayout_23.addWidget(self.frame_39)

        self.frame_24 = QFrame(self.frame_38)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_24)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_31 = QLabel(self.frame_24)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_5.addWidget(self.label_31, 1, 0, 1, 1)

        self.comboBox_4 = QComboBox(self.frame_24)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.gridLayout_5.addWidget(self.comboBox_4, 0, 1, 1, 1)

        self.label_30 = QLabel(self.frame_24)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_5.addWidget(self.label_30, 0, 0, 1, 1)

        self.label_32 = QLabel(self.frame_24)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_5.addWidget(self.label_32, 2, 0, 1, 1)

        self.comboBox_5 = QComboBox(self.frame_24)
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")

        self.gridLayout_5.addWidget(self.comboBox_5, 1, 1, 1, 1)

        self.comboBox_6 = QComboBox(self.frame_24)
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.setObjectName(u"comboBox_6")

        self.gridLayout_5.addWidget(self.comboBox_6, 2, 1, 1, 1)

        self.radioButton = QRadioButton(self.frame_24)
        self.radioButton.setObjectName(u"radioButton")

        self.gridLayout_5.addWidget(self.radioButton, 3, 1, 1, 1)


        self.verticalLayout_23.addWidget(self.frame_24)


        self.gridLayout_4.addWidget(self.frame_38, 0, 0, 1, 1)

        self.frame_37 = QFrame(self.frame_28)
        self.frame_37.setObjectName(u"frame_37")
        sizePolicy4.setHeightForWidth(self.frame_37.sizePolicy().hasHeightForWidth())
        self.frame_37.setSizePolicy(sizePolicy4)
        self.frame_37.setMaximumSize(QSize(640, 16777215))
        self.frame_37.setStyleSheet(u"")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_37)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.frame_40 = QFrame(self.frame_37)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setMaximumSize(QSize(16777215, 50))
        self.frame_40.setStyleSheet(u"background-color: rgb(23, 38, 255);\n"
"color: rgb(255, 255, 255);")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_40)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_33 = QLabel(self.frame_40)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_25.addWidget(self.label_33)


        self.verticalLayout_26.addWidget(self.frame_40)

        self.frame_25 = QFrame(self.frame_37)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_25)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.lineEdit_9 = QLineEdit(self.frame_25)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.gridLayout_6.addWidget(self.lineEdit_9, 0, 1, 1, 1)

        self.lineEdit_10 = QLineEdit(self.frame_25)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.gridLayout_6.addWidget(self.lineEdit_10, 1, 1, 1, 1)

        self.label_35 = QLabel(self.frame_25)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_6.addWidget(self.label_35, 1, 0, 1, 1)

        self.label_36 = QLabel(self.frame_25)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout_6.addWidget(self.label_36, 2, 0, 1, 1)

        self.pushButton_14 = QPushButton(self.frame_25)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setMinimumSize(QSize(70, 35))
        self.pushButton_14.setStyleSheet(u"QPushButton{\n"
"	\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"	background-color: rgb(220, 220, 220);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(117, 12, 26);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")

        self.gridLayout_6.addWidget(self.pushButton_14, 1, 2, 1, 1)

        self.label_34 = QLabel(self.frame_25)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout_6.addWidget(self.label_34, 0, 0, 1, 1)

        self.lineEdit_11 = QLineEdit(self.frame_25)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.gridLayout_6.addWidget(self.lineEdit_11, 2, 1, 1, 1)

        self.pushButton_15 = QPushButton(self.frame_25)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setMinimumSize(QSize(70, 35))
        self.pushButton_15.setStyleSheet(u"QPushButton{\n"
"	\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"	background-color: rgb(220, 220, 220);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(117, 12, 26);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")

        self.gridLayout_6.addWidget(self.pushButton_15, 2, 2, 1, 1)

        self.pushButton_8 = QPushButton(self.frame_25)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(70, 35))
        self.pushButton_8.setStyleSheet(u"QPushButton{\n"
"	\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"	background-color: rgb(220, 220, 220);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(117, 12, 26);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")

        self.gridLayout_6.addWidget(self.pushButton_8, 0, 2, 1, 1)


        self.verticalLayout_26.addWidget(self.frame_25)


        self.gridLayout_4.addWidget(self.frame_37, 0, 1, 1, 1)

        self.frame_36 = QFrame(self.frame_28)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setStyleSheet(u"")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_36)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.frame_41 = QFrame(self.frame_36)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setMaximumSize(QSize(16777215, 50))
        self.frame_41.setStyleSheet(u"background-color: rgb(23, 38, 255);\n"
"color: rgb(255, 255, 255);")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_41)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_37 = QLabel(self.frame_41)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_27.addWidget(self.label_37)


        self.verticalLayout_28.addWidget(self.frame_41)

        self.frame_27 = QFrame(self.frame_36)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.comboBox_7 = QComboBox(self.frame_27)
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.setObjectName(u"comboBox_7")
        self.comboBox_7.setGeometry(QRect(70, 80, 181, 41))

        self.verticalLayout_28.addWidget(self.frame_27)


        self.gridLayout_4.addWidget(self.frame_36, 0, 2, 1, 1)

        self.frame_29 = QFrame(self.frame_28)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setStyleSheet(u"background-color: rgb(0, 170, 255);")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.frame_29, 2, 0, 1, 1)

        self.frame_15 = QFrame(self.frame_28)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy7.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy7)
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_10.setSpacing(10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.pushButton_17 = QPushButton(self.frame_15)
        self.pushButton_17.setObjectName(u"pushButton_17")
        sizePolicy3.setHeightForWidth(self.pushButton_17.sizePolicy().hasHeightForWidth())
        self.pushButton_17.setSizePolicy(sizePolicy3)
        self.pushButton_17.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_10.addWidget(self.pushButton_17)

        self.pushButton_9 = QPushButton(self.frame_15)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy3.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy3)
        self.pushButton_9.setMinimumSize(QSize(100, 0))
        self.pushButton_9.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_10.addWidget(self.pushButton_9)

        self.pushButton_16 = QPushButton(self.frame_15)
        self.pushButton_16.setObjectName(u"pushButton_16")
        sizePolicy3.setHeightForWidth(self.pushButton_16.sizePolicy().hasHeightForWidth())
        self.pushButton_16.setSizePolicy(sizePolicy3)
        self.pushButton_16.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_10.addWidget(self.pushButton_16)


        self.gridLayout_4.addWidget(self.frame_15, 2, 2, 1, 1, Qt.AlignBottom)


        self.verticalLayout_21.addWidget(self.frame_28)


        self.horizontalLayout_12.addWidget(self.frame_26)

        self.Pages.addWidget(self.page_2)
        self.PagesPage2_2 = QWidget()
        self.PagesPage2_2.setObjectName(u"PagesPage2_2")
        self.verticalLayout_8 = QVBoxLayout(self.PagesPage2_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_4 = QFrame(self.PagesPage2_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_4)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 0))
        self.frame_5.setMaximumSize(QSize(16777215, 35))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_5)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 35))
        self.label.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";background-color: rgba(204, 111, 101);\n"
"color: rgb(255, 255, 255);    border-radius: 10px;")

        self.verticalLayout_10.addWidget(self.label)


        self.verticalLayout_9.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background-color: rgb(253, 253, 253);")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_6)
        self.gridLayout.setSpacing(14)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(100, -1, 100, -1)
        self.frame_10 = QFrame(self.frame_6)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_10)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_9)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.frame_9)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"background-color: rgb(245, 245, 245);    border-radius: 10px;")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_10)


        self.horizontalLayout_9.addWidget(self.frame_9)

        self.frame_12 = QFrame(self.frame_10)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy5.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy5)
        self.frame_12.setStyleSheet(u"")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_12)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frame_20 = QFrame(self.frame_12)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMaximumSize(QSize(16777215, 120))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_11.setSpacing(14)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.pushButton_11 = QPushButton(self.frame_20)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(0, 40))
        self.pushButton_11.setMaximumSize(QSize(16777215, 40))
        self.pushButton_11.setStyleSheet(u"QPushButton{\n"
"	\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"	background-color: rgb(220, 220, 220);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(117, 12, 26);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")

        self.horizontalLayout_11.addWidget(self.pushButton_11)

        self.pushButton_13 = QPushButton(self.frame_20)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMaximumSize(QSize(150, 40))
        self.pushButton_13.setStyleSheet(u"QPushButton{\n"
"	\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"	background-color: rgb(220, 220, 220);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(117, 12, 26);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")

        self.horizontalLayout_11.addWidget(self.pushButton_13)

        self.pushButton_12 = QPushButton(self.frame_20)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMaximumSize(QSize(16777215, 40))
        self.pushButton_12.setStyleSheet(u"QPushButton{\n"
"	\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"	background-color: rgb(220, 220, 220);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(117, 12, 26);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")

        self.horizontalLayout_11.addWidget(self.pushButton_12)

        self.pushButton_10 = QPushButton(self.frame_20)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMaximumSize(QSize(150, 40))
        self.pushButton_10.setStyleSheet(u"QPushButton{\n"
"	\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"	background-color: rgb(220, 220, 220);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(117, 12, 26);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")

        self.horizontalLayout_11.addWidget(self.pushButton_10)


        self.verticalLayout_19.addWidget(self.frame_20)

        self.frame_19 = QFrame(self.frame_12)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setStyleSheet(u"")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_19)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_20 = QLabel(self.frame_19)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_3.addWidget(self.label_20, 0, 0, 1, 1)

        self.label_21 = QLabel(self.frame_19)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_3.addWidget(self.label_21, 0, 1, 1, 1)

        self.label_22 = QLabel(self.frame_19)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_3.addWidget(self.label_22, 0, 2, 1, 1)

        self.label_23 = QLabel(self.frame_19)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_3.addWidget(self.label_23, 1, 0, 1, 1)

        self.label_24 = QLabel(self.frame_19)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_3.addWidget(self.label_24, 1, 1, 1, 1)

        self.label_25 = QLabel(self.frame_19)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_3.addWidget(self.label_25, 1, 2, 1, 1)

        self.label_26 = QLabel(self.frame_19)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_3.addWidget(self.label_26, 2, 0, 1, 1)

        self.label_27 = QLabel(self.frame_19)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_3.addWidget(self.label_27, 2, 1, 1, 1)

        self.label_28 = QLabel(self.frame_19)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_3.addWidget(self.label_28, 2, 2, 1, 1)


        self.verticalLayout_19.addWidget(self.frame_19)


        self.horizontalLayout_9.addWidget(self.frame_12)


        self.gridLayout.addWidget(self.frame_10, 1, 0, 1, 1)

        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 250))
        self.frame_7.setStyleSheet(u"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_7.setSpacing(15)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(250, 250))
        self.frame_8.setMaximumSize(QSize(250, 250))
        self.frame_8.setStyleSheet(u"image: url(:/16x16/icons/depositphotos_318221368-stock-illustration-missing-picture-page-for-website.jpg);\n"
"background-position:  center;\n"
"background-repeat: no-repeat;    border-radius: 10px;\n"
"")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_8)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_8 = QLabel(self.frame_8)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_8)


        self.horizontalLayout_7.addWidget(self.frame_8)

        self.frame_11 = QFrame(self.frame_7)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMaximumSize(QSize(16777215, 250))
        self.frame_11.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgba(250, 250, 250, 250);")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_11)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.txt_ID = QLineEdit(self.frame_11)
        self.txt_ID.setObjectName(u"txt_ID")
        sizePolicy2.setHeightForWidth(self.txt_ID.sizePolicy().hasHeightForWidth())
        self.txt_ID.setSizePolicy(sizePolicy2)
        self.txt_ID.setMinimumSize(QSize(0, 0))
        self.txt_ID.setMaximumSize(QSize(250, 50))

        self.gridLayout_2.addWidget(self.txt_ID, 0, 1, 1, 1)

        self.txt_pass1 = QLineEdit(self.frame_11)
        self.txt_pass1.setObjectName(u"txt_pass1")
        self.txt_pass1.setMaximumSize(QSize(250, 50))

        self.gridLayout_2.addWidget(self.txt_pass1, 1, 1, 1, 1)

        self.label_3 = QLabel(self.frame_11)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(150, 30))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_2 = QLabel(self.frame_11)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(150, 30))
        self.label_2.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_15 = QLabel(self.frame_11)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(150, 30))
        self.label_15.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_15, 0, 2, 1, 1)

        self.txt_Name = QLineEdit(self.frame_11)
        self.txt_Name.setObjectName(u"txt_Name")
        self.txt_Name.setMaximumSize(QSize(250, 50))

        self.gridLayout_2.addWidget(self.txt_Name, 0, 3, 1, 1)

        self.label_14 = QLabel(self.frame_11)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(16777215, 30))
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_14, 2, 0, 1, 1)

        self.label_17 = QLabel(self.frame_11)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(150, 30))
        self.label_17.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_17, 1, 2, 1, 1)

        self.txt_pass2 = QLineEdit(self.frame_11)
        self.txt_pass2.setObjectName(u"txt_pass2")
        self.txt_pass2.setMaximumSize(QSize(250, 50))

        self.gridLayout_2.addWidget(self.txt_pass2, 1, 3, 1, 1)

        self.comboBox_position = QComboBox(self.frame_11)
        self.comboBox_position.addItem("")
        self.comboBox_position.addItem("")
        self.comboBox_position.setObjectName(u"comboBox_position")
        sizePolicy3.setHeightForWidth(self.comboBox_position.sizePolicy().hasHeightForWidth())
        self.comboBox_position.setSizePolicy(sizePolicy3)
        self.comboBox_position.setMaximumSize(QSize(250, 16777215))

        self.gridLayout_2.addWidget(self.comboBox_position, 2, 3, 1, 1)

        self.label_4 = QLabel(self.frame_11)
        self.label_4.setObjectName(u"label_4")
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy8)
        self.label_4.setMaximumSize(QSize(150, 500))
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_4, 2, 2, 1, 1)

        self.comboBox_type = QComboBox(self.frame_11)
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.setObjectName(u"comboBox_type")

        self.gridLayout_2.addWidget(self.comboBox_type, 2, 1, 1, 1)


        self.horizontalLayout_7.addWidget(self.frame_11)


        self.gridLayout.addWidget(self.frame_7, 0, 0, 1, 1)


        self.verticalLayout_9.addWidget(self.frame_6)


        self.verticalLayout_8.addWidget(self.frame_4)

        self.Pages.addWidget(self.PagesPage2_2)

        self.verticalLayout_4.addWidget(self.Pages)


        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Pages.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Btn_loggle.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"FaKeep", None))
        self.pushButton_6.setText("")
        self.pushButton_5.setText("")
        self.pushButton_4.setText("")
        self.pushButton_1.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Qu\u1ea3n l\u00fd nh\u00e2n vi\u00ean", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"Qu\u1ea3n l\u00fd ch\u1ea5m c\u00f4ng", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"T\u1ea1o m\u1edbi nh\u00e2n vi\u00ean", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"C\u00e0i \u0111\u1eb7t", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0110\u0103ng xu\u1ea5t", None))
        self.image_label.setText(QCoreApplication.translate("MainWindow", u"Open camera check in", None))
        self.control_bt.setText(QCoreApplication.translate("MainWindow", u"CHECK IN", None))
        self.image_label_2.setText(QCoreApplication.translate("MainWindow", u"Open camera check out", None))
        self.control_bt_2.setText(QCoreApplication.translate("MainWindow", u"CHECK OUT", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u" Qu\u1ea3n l\u00fd ch\u1ea5m c\u00f4ng", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"  B\u1ed9 l\u1ecdc", None))
        self.pushButton_19.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"M\u00e3 nh\u00e2n vi\u00ean ", None))
        self.lineEdit_12.setPlaceholderText(QCoreApplication.translate("MainWindow", u"T\u00ean nh\u00e2n vi\u00ean ", None))
        self.lineEdit_13.setPlaceholderText(QCoreApplication.translate("MainWindow", u"S\u1ed1 \u0111i\u1ec7n tho\u1ea1i", None))
        self.comboBox_8.setCurrentText("")
        self.pushButton_18.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"M\u00e3 nh\u00e2n vi\u00ean", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"T\u00ean nh\u00e2n vi\u00ean", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"S\u1ed1 \u0111i\u1ec7n tho\u1ea1i", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Ph\u00f2ng ban", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian check in", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian check out", None));
        self.label_38.setText(QCoreApplication.translate("MainWindow", u" Qu\u1ea3n l\u00fd nh\u00e2n vi\u00ean", None))
        self.pushButton_20.setText("")
        self.pushButton_21.setText("")
        self.pushButton_24.setText("")
        self.pushButton_23.setText("")
        ___qtablewidgetitem6 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"M\u00e3 nh\u00e2n vi\u00ean", None));
        ___qtablewidgetitem7 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"T\u00ean nh\u00e2n vi\u00ean", None));
        ___qtablewidgetitem8 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"S\u1ed1 \u0111i\u1ec7n tho\u1ea1i", None));
        ___qtablewidgetitem9 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Ph\u00f2ng ban", None));
        ___qtablewidgetitem10 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Gmail", None));
        ___qtablewidgetitem11 = self.tableWidget_2.horizontalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Ng\u00e0y sinh", None));
        self.label_12.setText(QCoreApplication.translate("MainWindow", u" C\u00e0i \u0111\u1eb7t", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Camera check out", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"0", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("MainWindow", u"IP", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("MainWindow", u"IP1", None))

        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Camera check in", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Camera ch\u1ee5p \u1ea3nh", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("MainWindow", u"0", None))
        self.comboBox_5.setItemText(1, QCoreApplication.translate("MainWindow", u"IP", None))
        self.comboBox_5.setItemText(2, QCoreApplication.translate("MainWindow", u"IP1", None))

        self.comboBox_6.setItemText(0, QCoreApplication.translate("MainWindow", u"0", None))
        self.comboBox_6.setItemText(1, QCoreApplication.translate("MainWindow", u"IP", None))
        self.comboBox_6.setItemText(2, QCoreApplication.translate("MainWindow", u"IP1", None))

        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"S\u1eed d\u1ee5ng 1 cam", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"T\u1ea3i d\u1eef li\u1ec7u", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Data User", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Data Admin", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Data Staff", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"M\u00e0u s\u1eafc", None))
        self.comboBox_7.setItemText(0, QCoreApplication.translate("MainWindow", u"Giao di\u1ec7n load", None))
        self.comboBox_7.setItemText(1, QCoreApplication.translate("MainWindow", u"Giao di\u1ec7n login", None))
        self.comboBox_7.setItemText(2, QCoreApplication.translate("MainWindow", u"Thanh ngang", None))
        self.comboBox_7.setItemText(3, QCoreApplication.translate("MainWindow", u"Thanh d\u1ecdc", None))
        self.comboBox_7.setItemText(4, QCoreApplication.translate("MainWindow", u"N\u1ec1n", None))

        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"  \u0110\u0103ng k\u00fd th\u00f4ng tin nh\u00e2n vi\u00ean", None))
        self.label_10.setText("")
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Ch\u1ee5p \u1ea3nh", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Xem", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"M\u1edf file \u1ea3nh", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Th\u00eam", None))
        self.label_20.setText("")
        self.label_21.setText("")
        self.label_22.setText("")
        self.label_23.setText("")
        self.label_24.setText("")
        self.label_25.setText("")
        self.label_26.setText("")
        self.label_27.setText("")
        self.label_28.setText("")
        self.label_8.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"M\u1eadt kh\u1ea9u", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"M\u00e3 nh\u00e2n vi\u00ean", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"T\u00ean nh\u00e2n vi\u00ean", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Loai", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Nh\u1eadp l\u1ea1i m\u1eadt kh\u1ea9u", None))
        self.comboBox_position.setItemText(0, QCoreApplication.translate("MainWindow", u"K\u1ebf to\u00e1n", None))
        self.comboBox_position.setItemText(1, QCoreApplication.translate("MainWindow", u"Nh\u00e2n s\u1ef1", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Ch\u1ee9c v\u1ee5", None))
        self.comboBox_type.setItemText(0, QCoreApplication.translate("MainWindow", u"Admin", None))
        self.comboBox_type.setItemText(1, QCoreApplication.translate("MainWindow", u"Staff", None))

    # retranslateUi

