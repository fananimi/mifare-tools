# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(922, 640)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setLineWidth(1)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBoxPCC = QGroupBox(self.frame_2)
        self.groupBoxPCC.setObjectName(u"groupBoxPCC")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBoxPCC.sizePolicy().hasHeightForWidth())
        self.groupBoxPCC.setSizePolicy(sizePolicy1)
        self.horizontalLayout = QHBoxLayout(self.groupBoxPCC)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_6 = QGroupBox(self.groupBoxPCC)
        self.groupBox_6.setObjectName(u"groupBox_6")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy2)
        self.groupBox_6.setStyleSheet(u"QGroupBox{\n"
"  border: none;\n"
"  margin-top: 2ex;\n"
"}\n"
" QGroupBox::title{\n"
"  subcontrol-origin: \n"
"  margin;subcontrol-position:\n"
"  top left;\n"
"  margin-left: 5px;\n"
"  padding:0px 3px;\n"
"}")
        self.horizontalLayout_10 = QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(9, 9, 9, 9)
        self.cmbReader = QComboBox(self.groupBox_6)
        self.cmbReader.setObjectName(u"cmbReader")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.cmbReader.sizePolicy().hasHeightForWidth())
        self.cmbReader.setSizePolicy(sizePolicy3)
        self.cmbReader.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_10.addWidget(self.cmbReader)

        self.btnReloadReader = QPushButton(self.groupBox_6)
        self.btnReloadReader.setObjectName(u"btnReloadReader")
        sizePolicy3.setHeightForWidth(self.btnReloadReader.sizePolicy().hasHeightForWidth())
        self.btnReloadReader.setSizePolicy(sizePolicy3)
        self.btnReloadReader.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_10.addWidget(self.btnReloadReader)


        self.horizontalLayout.addWidget(self.groupBox_6)


        self.horizontalLayout_2.addWidget(self.groupBoxPCC)

        self.groupBoxPICCC = QGroupBox(self.frame_2)
        self.groupBoxPICCC.setObjectName(u"groupBoxPICCC")
        self.groupBoxPICCC.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.groupBoxPICCC.sizePolicy().hasHeightForWidth())
        self.groupBoxPICCC.setSizePolicy(sizePolicy2)
        self.horizontalLayout_3 = QHBoxLayout(self.groupBoxPICCC)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.groupBox_9 = QGroupBox(self.groupBoxPICCC)
        self.groupBox_9.setObjectName(u"groupBox_9")
        sizePolicy2.setHeightForWidth(self.groupBox_9.sizePolicy().hasHeightForWidth())
        self.groupBox_9.setSizePolicy(sizePolicy2)
        self.groupBox_9.setStyleSheet(u"QGroupBox{\n"
"  border: none;\n"
"  margin-top: 2ex;\n"
"}\n"
" QGroupBox::title{\n"
"  subcontrol-origin: \n"
"  margin;subcontrol-position:\n"
"  top left;\n"
"  margin-left: 5px;\n"
"  padding:0px 3px;\n"
"}")
        self.horizontalLayout_13 = QHBoxLayout(self.groupBox_9)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(9, 9, 9, 9)
        self.btnConnetPICC = QPushButton(self.groupBox_9)
        self.btnConnetPICC.setObjectName(u"btnConnetPICC")
        sizePolicy3.setHeightForWidth(self.btnConnetPICC.sizePolicy().hasHeightForWidth())
        self.btnConnetPICC.setSizePolicy(sizePolicy3)
        self.btnConnetPICC.setMinimumSize(QSize(100, 0))
        self.btnConnetPICC.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_13.addWidget(self.btnConnetPICC)


        self.horizontalLayout_3.addWidget(self.groupBox_9)

        self.groupBox_7 = QGroupBox(self.groupBoxPICCC)
        self.groupBox_7.setObjectName(u"groupBox_7")
        sizePolicy2.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy2)
        self.groupBox_7.setStyleSheet(u"QGroupBox{\n"
"  border: none;\n"
"  margin-top: 2ex;\n"
"}\n"
" QGroupBox::title{\n"
"  subcontrol-origin: \n"
"  margin;subcontrol-position:\n"
"  top left;\n"
"  margin-left: 5px;\n"
"  padding:0px 3px;\n"
"}")
        self.horizontalLayout_11 = QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(9, 9, 9, 9)
        self.txtUID = QLineEdit(self.groupBox_7)
        self.txtUID.setObjectName(u"txtUID")
        sizePolicy3.setHeightForWidth(self.txtUID.sizePolicy().hasHeightForWidth())
        self.txtUID.setSizePolicy(sizePolicy3)
        self.txtUID.setMinimumSize(QSize(50, 0))
        self.txtUID.setReadOnly(True)

        self.horizontalLayout_11.addWidget(self.txtUID)


        self.horizontalLayout_3.addWidget(self.groupBox_7)

        self.groupBox_8 = QGroupBox(self.groupBoxPICCC)
        self.groupBox_8.setObjectName(u"groupBox_8")
        sizePolicy2.setHeightForWidth(self.groupBox_8.sizePolicy().hasHeightForWidth())
        self.groupBox_8.setSizePolicy(sizePolicy2)
        self.groupBox_8.setStyleSheet(u"QGroupBox{\n"
"  border: none;\n"
"  margin-top: 2ex;\n"
"}\n"
" QGroupBox::title{\n"
"  subcontrol-origin: \n"
"  margin;subcontrol-position:\n"
"  top left;\n"
"  margin-left: 5px;\n"
"  padding:0px 3px;\n"
"}")
        self.horizontalLayout_12 = QHBoxLayout(self.groupBox_8)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(9, 9, 9, 9)
        self.txtATR = QLineEdit(self.groupBox_8)
        self.txtATR.setObjectName(u"txtATR")
        self.txtATR.setMinimumSize(QSize(200, 0))
        self.txtATR.setReadOnly(True)

        self.horizontalLayout_12.addWidget(self.txtATR)


        self.horizontalLayout_3.addWidget(self.groupBox_8)


        self.horizontalLayout_2.addWidget(self.groupBoxPICCC)


        self.verticalLayout.addWidget(self.frame_2)

        self.tabMain = QTabWidget(self.centralwidget)
        self.tabMain.setObjectName(u"tabMain")
        self.tabMain.setEnabled(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_4 = QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame = QFrame(self.tab)
        self.frame.setObjectName(u"frame")
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.groupBox_3 = QGroupBox(self.frame)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.formLayout = QFormLayout(self.groupBox_3)
        self.formLayout.setObjectName(u"formLayout")
        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.spnBlock = QSpinBox(self.groupBox_3)
        self.spnBlock.setObjectName(u"spnBlock")
        self.spnBlock.setMaximum(3)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.spnBlock)

        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.spnSector = QSpinBox(self.groupBox_3)
        self.spnSector.setObjectName(u"spnSector")
        self.spnSector.setMaximum(15)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.spnSector)


        self.horizontalLayout_4.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.frame)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_3 = QFrame(self.groupBox_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.txtKeyA0 = QLineEdit(self.frame_3)
        self.txtKeyA0.setObjectName(u"txtKeyA0")
        sizePolicy3.setHeightForWidth(self.txtKeyA0.sizePolicy().hasHeightForWidth())
        self.txtKeyA0.setSizePolicy(sizePolicy3)
        self.txtKeyA0.setMaximumSize(QSize(30, 30))
        self.txtKeyA0.setMaxLength(2)

        self.horizontalLayout_5.addWidget(self.txtKeyA0)

        self.txtKeyA1 = QLineEdit(self.frame_3)
        self.txtKeyA1.setObjectName(u"txtKeyA1")
        sizePolicy3.setHeightForWidth(self.txtKeyA1.sizePolicy().hasHeightForWidth())
        self.txtKeyA1.setSizePolicy(sizePolicy3)
        self.txtKeyA1.setMaximumSize(QSize(30, 30))
        self.txtKeyA1.setMaxLength(2)

        self.horizontalLayout_5.addWidget(self.txtKeyA1)

        self.txtKeyA2 = QLineEdit(self.frame_3)
        self.txtKeyA2.setObjectName(u"txtKeyA2")
        sizePolicy3.setHeightForWidth(self.txtKeyA2.sizePolicy().hasHeightForWidth())
        self.txtKeyA2.setSizePolicy(sizePolicy3)
        self.txtKeyA2.setMaximumSize(QSize(30, 30))
        self.txtKeyA2.setMaxLength(2)

        self.horizontalLayout_5.addWidget(self.txtKeyA2)

        self.txtKeyA3 = QLineEdit(self.frame_3)
        self.txtKeyA3.setObjectName(u"txtKeyA3")
        sizePolicy3.setHeightForWidth(self.txtKeyA3.sizePolicy().hasHeightForWidth())
        self.txtKeyA3.setSizePolicy(sizePolicy3)
        self.txtKeyA3.setMaximumSize(QSize(30, 30))
        self.txtKeyA3.setMaxLength(2)

        self.horizontalLayout_5.addWidget(self.txtKeyA3)

        self.txtKeyA4 = QLineEdit(self.frame_3)
        self.txtKeyA4.setObjectName(u"txtKeyA4")
        sizePolicy3.setHeightForWidth(self.txtKeyA4.sizePolicy().hasHeightForWidth())
        self.txtKeyA4.setSizePolicy(sizePolicy3)
        self.txtKeyA4.setMaximumSize(QSize(30, 30))
        self.txtKeyA4.setMaxLength(2)

        self.horizontalLayout_5.addWidget(self.txtKeyA4)

        self.txtKeyA5 = QLineEdit(self.frame_3)
        self.txtKeyA5.setObjectName(u"txtKeyA5")
        sizePolicy3.setHeightForWidth(self.txtKeyA5.sizePolicy().hasHeightForWidth())
        self.txtKeyA5.setSizePolicy(sizePolicy3)
        self.txtKeyA5.setMaximumSize(QSize(30, 30))
        self.txtKeyA5.setMaxLength(2)

        self.horizontalLayout_5.addWidget(self.txtKeyA5)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.groupBox_4)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.btnAuthKeyA = QPushButton(self.frame_4)
        self.btnAuthKeyA.setObjectName(u"btnAuthKeyA")

        self.horizontalLayout_6.addWidget(self.btnAuthKeyA)

        self.btnFactoryKeyA = QPushButton(self.frame_4)
        self.btnFactoryKeyA.setObjectName(u"btnFactoryKeyA")

        self.horizontalLayout_6.addWidget(self.btnFactoryKeyA)


        self.verticalLayout_2.addWidget(self.frame_4)


        self.horizontalLayout_4.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.frame)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_5 = QFrame(self.groupBox_5)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.txtKeyB0 = QLineEdit(self.frame_5)
        self.txtKeyB0.setObjectName(u"txtKeyB0")
        sizePolicy3.setHeightForWidth(self.txtKeyB0.sizePolicy().hasHeightForWidth())
        self.txtKeyB0.setSizePolicy(sizePolicy3)
        self.txtKeyB0.setMaximumSize(QSize(30, 30))
        self.txtKeyB0.setMaxLength(2)

        self.horizontalLayout_7.addWidget(self.txtKeyB0)

        self.txtKeyB1 = QLineEdit(self.frame_5)
        self.txtKeyB1.setObjectName(u"txtKeyB1")
        sizePolicy3.setHeightForWidth(self.txtKeyB1.sizePolicy().hasHeightForWidth())
        self.txtKeyB1.setSizePolicy(sizePolicy3)
        self.txtKeyB1.setMaximumSize(QSize(30, 30))
        self.txtKeyB1.setMaxLength(2)

        self.horizontalLayout_7.addWidget(self.txtKeyB1)

        self.txtKeyB2 = QLineEdit(self.frame_5)
        self.txtKeyB2.setObjectName(u"txtKeyB2")
        sizePolicy3.setHeightForWidth(self.txtKeyB2.sizePolicy().hasHeightForWidth())
        self.txtKeyB2.setSizePolicy(sizePolicy3)
        self.txtKeyB2.setMaximumSize(QSize(30, 30))
        self.txtKeyB2.setMaxLength(2)

        self.horizontalLayout_7.addWidget(self.txtKeyB2)

        self.txtKeyB3 = QLineEdit(self.frame_5)
        self.txtKeyB3.setObjectName(u"txtKeyB3")
        sizePolicy3.setHeightForWidth(self.txtKeyB3.sizePolicy().hasHeightForWidth())
        self.txtKeyB3.setSizePolicy(sizePolicy3)
        self.txtKeyB3.setMaximumSize(QSize(30, 30))
        self.txtKeyB3.setMaxLength(2)

        self.horizontalLayout_7.addWidget(self.txtKeyB3)

        self.txtKeyB4 = QLineEdit(self.frame_5)
        self.txtKeyB4.setObjectName(u"txtKeyB4")
        sizePolicy3.setHeightForWidth(self.txtKeyB4.sizePolicy().hasHeightForWidth())
        self.txtKeyB4.setSizePolicy(sizePolicy3)
        self.txtKeyB4.setMaximumSize(QSize(30, 30))
        self.txtKeyB4.setMaxLength(2)

        self.horizontalLayout_7.addWidget(self.txtKeyB4)

        self.txtKeyB5 = QLineEdit(self.frame_5)
        self.txtKeyB5.setObjectName(u"txtKeyB5")
        sizePolicy3.setHeightForWidth(self.txtKeyB5.sizePolicy().hasHeightForWidth())
        self.txtKeyB5.setSizePolicy(sizePolicy3)
        self.txtKeyB5.setMaximumSize(QSize(30, 30))
        self.txtKeyB5.setMaxLength(2)

        self.horizontalLayout_7.addWidget(self.txtKeyB5)


        self.verticalLayout_3.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.groupBox_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.btnAuthKeyB = QPushButton(self.frame_6)
        self.btnAuthKeyB.setObjectName(u"btnAuthKeyB")

        self.horizontalLayout_8.addWidget(self.btnAuthKeyB)

        self.btnFactoryKeyB = QPushButton(self.frame_6)
        self.btnFactoryKeyB.setObjectName(u"btnFactoryKeyB")

        self.horizontalLayout_8.addWidget(self.btnFactoryKeyB)


        self.verticalLayout_3.addWidget(self.frame_6)


        self.horizontalLayout_4.addWidget(self.groupBox_5)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout_4.addWidget(self.frame)

        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.horizontalLayout_9 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.btnReadBlock = QPushButton(self.groupBox)
        self.btnReadBlock.setObjectName(u"btnReadBlock")
        sizePolicy3.setHeightForWidth(self.btnReadBlock.sizePolicy().hasHeightForWidth())
        self.btnReadBlock.setSizePolicy(sizePolicy3)

        self.horizontalLayout_9.addWidget(self.btnReadBlock)

        self.textEdit_4 = QTextEdit(self.groupBox)
        self.textEdit_4.setObjectName(u"textEdit_4")
        sizePolicy3.setHeightForWidth(self.textEdit_4.sizePolicy().hasHeightForWidth())
        self.textEdit_4.setSizePolicy(sizePolicy3)
        self.textEdit_4.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_9.addWidget(self.textEdit_4)

        self.textEdit_3 = QTextEdit(self.groupBox)
        self.textEdit_3.setObjectName(u"textEdit_3")
        sizePolicy3.setHeightForWidth(self.textEdit_3.sizePolicy().hasHeightForWidth())
        self.textEdit_3.setSizePolicy(sizePolicy3)
        self.textEdit_3.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_9.addWidget(self.textEdit_3)

        self.textEdit_5 = QTextEdit(self.groupBox)
        self.textEdit_5.setObjectName(u"textEdit_5")
        sizePolicy3.setHeightForWidth(self.textEdit_5.sizePolicy().hasHeightForWidth())
        self.textEdit_5.setSizePolicy(sizePolicy3)
        self.textEdit_5.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_9.addWidget(self.textEdit_5)

        self.textEdit_14 = QTextEdit(self.groupBox)
        self.textEdit_14.setObjectName(u"textEdit_14")
        sizePolicy3.setHeightForWidth(self.textEdit_14.sizePolicy().hasHeightForWidth())
        self.textEdit_14.setSizePolicy(sizePolicy3)
        self.textEdit_14.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_9.addWidget(self.textEdit_14)

        self.textEdit_15 = QTextEdit(self.groupBox)
        self.textEdit_15.setObjectName(u"textEdit_15")
        sizePolicy3.setHeightForWidth(self.textEdit_15.sizePolicy().hasHeightForWidth())
        self.textEdit_15.setSizePolicy(sizePolicy3)
        self.textEdit_15.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_9.addWidget(self.textEdit_15)

        self.textEdit_16 = QTextEdit(self.groupBox)
        self.textEdit_16.setObjectName(u"textEdit_16")
        sizePolicy3.setHeightForWidth(self.textEdit_16.sizePolicy().hasHeightForWidth())
        self.textEdit_16.setSizePolicy(sizePolicy3)
        self.textEdit_16.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_9.addWidget(self.textEdit_16)

        self.textEdit_6 = QTextEdit(self.groupBox)
        self.textEdit_6.setObjectName(u"textEdit_6")
        sizePolicy3.setHeightForWidth(self.textEdit_6.sizePolicy().hasHeightForWidth())
        self.textEdit_6.setSizePolicy(sizePolicy3)
        self.textEdit_6.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_9.addWidget(self.textEdit_6)

        self.textEdit_12 = QTextEdit(self.groupBox)
        self.textEdit_12.setObjectName(u"textEdit_12")
        sizePolicy3.setHeightForWidth(self.textEdit_12.sizePolicy().hasHeightForWidth())
        self.textEdit_12.setSizePolicy(sizePolicy3)
        self.textEdit_12.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_9.addWidget(self.textEdit_12)

        self.textEdit_13 = QTextEdit(self.groupBox)
        self.textEdit_13.setObjectName(u"textEdit_13")
        sizePolicy3.setHeightForWidth(self.textEdit_13.sizePolicy().hasHeightForWidth())
        self.textEdit_13.setSizePolicy(sizePolicy3)
        self.textEdit_13.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_9.addWidget(self.textEdit_13)

        self.textEdit_7 = QTextEdit(self.groupBox)
        self.textEdit_7.setObjectName(u"textEdit_7")
        sizePolicy3.setHeightForWidth(self.textEdit_7.sizePolicy().hasHeightForWidth())
        self.textEdit_7.setSizePolicy(sizePolicy3)
        self.textEdit_7.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_9.addWidget(self.textEdit_7)

        self.textEdit_8 = QTextEdit(self.groupBox)
        self.textEdit_8.setObjectName(u"textEdit_8")
        sizePolicy3.setHeightForWidth(self.textEdit_8.sizePolicy().hasHeightForWidth())
        self.textEdit_8.setSizePolicy(sizePolicy3)
        self.textEdit_8.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_9.addWidget(self.textEdit_8)

        self.textEdit_11 = QTextEdit(self.groupBox)
        self.textEdit_11.setObjectName(u"textEdit_11")
        sizePolicy3.setHeightForWidth(self.textEdit_11.sizePolicy().hasHeightForWidth())
        self.textEdit_11.setSizePolicy(sizePolicy3)
        self.textEdit_11.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_9.addWidget(self.textEdit_11)

        self.textEdit_9 = QTextEdit(self.groupBox)
        self.textEdit_9.setObjectName(u"textEdit_9")
        sizePolicy3.setHeightForWidth(self.textEdit_9.sizePolicy().hasHeightForWidth())
        self.textEdit_9.setSizePolicy(sizePolicy3)
        self.textEdit_9.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_9.addWidget(self.textEdit_9)

        self.textEdit_10 = QTextEdit(self.groupBox)
        self.textEdit_10.setObjectName(u"textEdit_10")
        sizePolicy3.setHeightForWidth(self.textEdit_10.sizePolicy().hasHeightForWidth())
        self.textEdit_10.setSizePolicy(sizePolicy3)
        self.textEdit_10.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_9.addWidget(self.textEdit_10)

        self.textEdit_2 = QTextEdit(self.groupBox)
        self.textEdit_2.setObjectName(u"textEdit_2")
        sizePolicy3.setHeightForWidth(self.textEdit_2.sizePolicy().hasHeightForWidth())
        self.textEdit_2.setSizePolicy(sizePolicy3)
        self.textEdit_2.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_9.addWidget(self.textEdit_2)

        self.textEdit = QTextEdit(self.groupBox)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy3.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy3)
        self.textEdit.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_9.addWidget(self.textEdit)


        self.verticalLayout_4.addWidget(self.groupBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.tabMain.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_2.setEnabled(False)
        self.gridLayout = QGridLayout(self.tab_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tableView = QTableView(self.tab_2)
        self.tableView.setObjectName(u"tableView")

        self.gridLayout.addWidget(self.tableView, 0, 0, 1, 1)

        self.tabMain.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_2 = QGridLayout(self.tab_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.txtAPDULog = QPlainTextEdit(self.tab_3)
        self.txtAPDULog.setObjectName(u"txtAPDULog")

        self.gridLayout_2.addWidget(self.txtAPDULog, 0, 0, 1, 1)

        self.frame_7 = QFrame(self.tab_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer)

        self.btnClearLog = QPushButton(self.frame_7)
        self.btnClearLog.setObjectName(u"btnClearLog")

        self.horizontalLayout_14.addWidget(self.btnClearLog)


        self.gridLayout_2.addWidget(self.frame_7, 1, 0, 1, 1)

        self.tabMain.addTab(self.tab_3, "")

        self.verticalLayout.addWidget(self.tabMain)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 922, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabMain.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBoxPCC.setTitle(QCoreApplication.translate("MainWindow", u"PCC", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Reader", None))
        self.btnReloadReader.setText(QCoreApplication.translate("MainWindow", u"Reload", None))
        self.groupBoxPICCC.setTitle(QCoreApplication.translate("MainWindow", u"PICC", None))
        self.groupBox_9.setTitle("")
        self.btnConnetPICC.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"UID", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"ATR", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Select", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Block", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Sector", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Key A", None))
        self.txtKeyA0.setText(QCoreApplication.translate("MainWindow", u"FF", None))
        self.txtKeyA1.setText(QCoreApplication.translate("MainWindow", u"FF", None))
        self.txtKeyA2.setText(QCoreApplication.translate("MainWindow", u"FF", None))
        self.txtKeyA3.setText(QCoreApplication.translate("MainWindow", u"FF", None))
        self.txtKeyA4.setText(QCoreApplication.translate("MainWindow", u"FF", None))
        self.txtKeyA5.setText(QCoreApplication.translate("MainWindow", u"FF", None))
        self.btnAuthKeyA.setText(QCoreApplication.translate("MainWindow", u"Authenticate", None))
        self.btnFactoryKeyA.setText(QCoreApplication.translate("MainWindow", u"Factory", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Key B", None))
        self.txtKeyB0.setText(QCoreApplication.translate("MainWindow", u"FF", None))
        self.txtKeyB1.setText(QCoreApplication.translate("MainWindow", u"FF", None))
        self.txtKeyB2.setText(QCoreApplication.translate("MainWindow", u"FF", None))
        self.txtKeyB3.setText(QCoreApplication.translate("MainWindow", u"FF", None))
        self.txtKeyB4.setText(QCoreApplication.translate("MainWindow", u"FF", None))
        self.txtKeyB5.setText(QCoreApplication.translate("MainWindow", u"FF", None))
        self.btnAuthKeyB.setText(QCoreApplication.translate("MainWindow", u"Authenticate", None))
        self.btnFactoryKeyB.setText(QCoreApplication.translate("MainWindow", u"Factory", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Data Block", None))
        self.btnReadBlock.setText(QCoreApplication.translate("MainWindow", u"Read", None))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Operations", None))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Utility", None))
        self.btnClearLog.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"APDU Log", None))
    # retranslateUi

