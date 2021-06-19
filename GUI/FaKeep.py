import datetime
import os
import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from ui_splash_screen import Ui_SplashScreen
from ui_login import Ui_Form
from main import *

class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.Btn_loggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))
        self.ui.pushButton_4.clicked.connect(lambda: exit())
        self.ui.pushButton_6.clicked.connect(lambda: self.showMinimized())
        self.ui.pushButton_5.clicked.connect(lambda:  UIFunctions.maximize_restore(self))
        self.ui.pushButton.clicked.connect(lambda: self.ui.Pages.setCurrentWidget(self.ui.PagesPage2_2))
        self.ui.pushButton_3.clicked.connect(lambda: self.logout())
        #Page Home
        self.ui.pushButton_1.clicked.connect(lambda: self.ui.Pages.setCurrentWidget(self.ui.PagesPage1_2))
        self.ui.control_bt.clicked.connect(lambda: UIFunctions.controlTimer1(self))
        self.timer = QTimer()
        self.timer.timeout.connect(lambda: UIFunctions.viewCam(self))
        self.ui.pushButton_7.clicked.connect(lambda: self.ui.Pages.setCurrentWidget(self.ui.page_3))
        self.ui.pushButton_22.clicked.connect(lambda : self.ui.Pages.setCurrentWidget(self.ui.page))
        self.ui.pushButton.clicked.connect(lambda : self.ui.Pages.setCurrentWidget(self.ui.PagesPage2_2))
        self.timer2 = QTimer()
        self.timer2.timeout.connect(lambda: creat.viewCam2(self))
        self.ui.pushButton_11.clicked.connect(lambda: creat.controlTimer2(self))
        self.ui.pushButton_13.clicked.connect(lambda : creat.xem_anh(self))
        self.ui.pushButton_12.clicked.connect(lambda: creat.mo_file(self))
        self.ui.pushButton_10.clicked.connect(lambda: creat.them(self))

        def moveWindow(event):
            if event.buttons == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()
        self.mouseMoveEvent = moveWindow
        self.show()
    def logout(self):
        self.login = SplashScreen.login(self)
        self.close()
        
class Login(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.pushButton.clicked.connect(lambda : self.login())
        self.ui.pushButton_2.clicked.connect(lambda : exit())

    def login(self):
        user = self.ui.lineEdit_3.text()
        password = self.ui.lineEdit_2.text()
        if user == '' and password == '':
            self.main = MainWindow()
            self.main.show()
            self.close()
        else:
            self.ui.notlogin.setText("Đăng nhập thất bại.")


counter = 0
class SplashScreen(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(35)
        QtCore.QTimer.singleShot(1500, lambda: self.ui.label_description.setText("<strong>LOADING</strong> DATABASE"))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.label_description.setText("<strong>LOADING</strong> USER INTERFACE"))
        self.show()

    def progress(self):
        global counter
        self.ui.progressBar.setValue(counter)
        if counter > 100:
            # STOP TIMER
            self.timer.stop()
            self.login()
            self.close()
        counter += 5
    def login(self):
        self.login = Login()
        self.login.show()


if __name__ == "__main__":
    app = QApplication()
    window = SplashScreen()
    sys.exit(app.exec_())
