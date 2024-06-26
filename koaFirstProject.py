# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'koaFirstProject.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys
from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform, QStandardItemModel, QStandardItem, QKeyEvent)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
    QDateTimeEdit, QFrame, QGridLayout, QGroupBox,
    QLabel, QLayout, QListWidget, QListWidgetItem,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpinBox, QStatusBar, QTextEdit, QVBoxLayout,
    QWidget, QTreeView, QLineEdit)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1104, 675)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(100, 30, 161, 41))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"background-color: rgb(80, 220, 255);")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 90, 802, 521))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.gridLayout.setHorizontalSpacing(7)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.taskBox = QGroupBox(self.gridLayoutWidget)
        self.taskBox.setObjectName(u"taskBox")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.taskBox.sizePolicy().hasHeightForWidth())
        self.taskBox.setSizePolicy(sizePolicy)
        self.taskBox.setMinimumSize(QSize(262, 125))
        self.taskBox.setMaximumSize(QSize(262, 125))
        self.taskBox.setAutoFillBackground(True)
        self.taskBox.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.dateTimeEdit = QDateTimeEdit(self.taskBox)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setGeometry(QRect(100, 10, 141, 22))
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.dateTimeEdit.sizePolicy().hasHeightForWidth())
        self.dateTimeEdit.setSizePolicy(sizePolicy1)
        self.dateTimeEdit.setStyleSheet(u"text-color: rgb(170, 170, 255)")
        self.dateTimeEdit.setCalendarPopup(True)
        self.textEdit = QTextEdit(self.taskBox)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(10, 40, 231, 51))
        self.pushButton_2 = QPushButton(self.taskBox)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(180, 100, 61, 20))
        self.checkBox_2 = QCheckBox(self.taskBox)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(10, 100, 91, 20))

        self.gridLayout.addWidget(self.taskBox, 0, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.gridLayoutWidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setMinimumSize(QSize(262, 125))
        self.groupBox_3.setMaximumSize(QSize(262, 125))
        self.groupBox_3.setAutoFillBackground(True)
        self.dateTimeEdit_6 = QDateTimeEdit(self.groupBox_3)
        self.dateTimeEdit_6.setObjectName(u"dateTimeEdit_6")
        self.dateTimeEdit_6.setGeometry(QRect(100, 10, 141, 22))
        sizePolicy1.setHeightForWidth(self.dateTimeEdit_6.sizePolicy().hasHeightForWidth())
        self.dateTimeEdit_6.setSizePolicy(sizePolicy1)
        self.dateTimeEdit_6.setStyleSheet(u"text-color: rgb(170, 170, 255)")
        self.dateTimeEdit_6.setCalendarPopup(True)
        self.textEdit_6 = QTextEdit(self.groupBox_3)
        self.textEdit_6.setObjectName(u"textEdit_6")
        self.textEdit_6.setGeometry(QRect(10, 40, 231, 51))
        self.pushButton_7 = QPushButton(self.groupBox_3)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(180, 100, 61, 20))
        self.checkBox_5 = QCheckBox(self.groupBox_3)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setGeometry(QRect(20, 100, 91, 20))

        self.gridLayout.addWidget(self.groupBox_3, 1, 0, 1, 1)

        self.groupBox = QGroupBox(self.gridLayoutWidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QSize(262, 125))
        self.groupBox.setMaximumSize(QSize(262, 125))
        self.groupBox.setAutoFillBackground(True)
        self.dateTimeEdit_4 = QDateTimeEdit(self.groupBox)
        self.dateTimeEdit_4.setObjectName(u"dateTimeEdit_4")
        self.dateTimeEdit_4.setGeometry(QRect(100, 10, 141, 22))
        sizePolicy1.setHeightForWidth(self.dateTimeEdit_4.sizePolicy().hasHeightForWidth())
        self.dateTimeEdit_4.setSizePolicy(sizePolicy1)
        self.dateTimeEdit_4.setStyleSheet(u"text-color: rgb(170, 170, 255)")
        self.dateTimeEdit_4.setCalendarPopup(True)
        self.textEdit_4 = QTextEdit(self.groupBox)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(10, 40, 231, 51))
        self.pushButton_5 = QPushButton(self.groupBox)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(180, 100, 61, 20))
        self.checkBox_3 = QCheckBox(self.groupBox)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QRect(20, 100, 91, 20))

        self.gridLayout.addWidget(self.groupBox, 0, 1, 1, 1)

        self.groupBox_2 = QGroupBox(self.gridLayoutWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QSize(262, 125))
        self.groupBox_2.setMaximumSize(QSize(262, 125))
        self.groupBox_2.setAutoFillBackground(True)
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setChecked(False)
        self.dateTimeEdit_2 = QDateTimeEdit(self.groupBox_2)
        self.dateTimeEdit_2.setObjectName(u"dateTimeEdit_2")
        self.dateTimeEdit_2.setGeometry(QRect(100, 10, 141, 22))
        sizePolicy1.setHeightForWidth(self.dateTimeEdit_2.sizePolicy().hasHeightForWidth())
        self.dateTimeEdit_2.setSizePolicy(sizePolicy1)
        self.dateTimeEdit_2.setStyleSheet(u"text-color: rgb(170, 170, 255)")
        self.dateTimeEdit_2.setCalendarPopup(True)
        self.textEdit_2 = QTextEdit(self.groupBox_2)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(10, 40, 231, 51))
        self.pushButton_3 = QPushButton(self.groupBox_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(180, 100, 61, 20))
        self.checkBox_4 = QCheckBox(self.groupBox_2)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setGeometry(QRect(20, 100, 91, 20))

        self.gridLayout.addWidget(self.groupBox_2, 0, 2, 1, 1)

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(830, 10, 258, 601))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Georgia"])
        font1.setPointSize(12)
        self.label.setFont(font1)
        self.label.setFrameShape(QFrame.NoFrame)
        self.label.setTextFormat(Qt.PlainText)
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label.setMargin(0)

        self.verticalLayout.addWidget(self.label)

        self.listWidget = QListWidget(self.verticalLayoutWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setSortingEnabled(False)

        self.verticalLayout.addWidget(self.listWidget)

        self.pushButton_4 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setUnderline(False)
        self.pushButton_4.setFont(font2)

        self.verticalLayout.addWidget(self.pushButton_4)

        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(480, 10, 311, 80))
        self.comboBox = QComboBox(self.groupBox_4)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(10, 20, 181, 41))
        font3 = QFont()
        font3.setPointSize(9)
        self.comboBox.setFont(font3)
        self.spinBox = QSpinBox(self.groupBox_4)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(190, 20, 101, 41))
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(True)
        self.spinBox.setFont(font4)
        self.spinBox.setStyleSheet(u"alternate-background-color: rgb(200,100,100);\n"
"background-color: rgb(100,200,100);\n"
"\n"
"")
        self.spinBox.setAlignment(Qt.AlignCenter)
        self.spinBox.setReadOnly(True)
        self.spinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1104, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Add new task", None))
        self.taskBox.setTitle(QCoreApplication.translate("MainWindow", u"Task", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Describe task...", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Completed", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Task", None))
        self.textEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Describe task...", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"Completed", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Task", None))
        self.textEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Describe task...", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Completed", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Task", None))
        self.textEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Describe task...", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"Completed", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Completed Tasks", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Clear Completed Tasks", None))
        self.groupBox_4.setTitle("")
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Tasks due today :", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Total Tasks due :", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Completed Tasks :", None))

    # retranslateUi

import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from koaFirstProject import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())