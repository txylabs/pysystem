# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'welcome_2vKXHJA.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.Widgets import QCustomSlideMenu
from Custom_Widgets.Widgets import QCustomStackedWidget

import resourses_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1107, 740)
        MainWindow.setStyleSheet(u"*{\n"
"  border:none;\n"
"  background-color:transparent;\n"
"  backgtound:transparent;\n"
"  padding:0;\n"
"  margin:0;\n"
"  color:#fff;\n"
"}\n"
"#centralwidget{\n"
"	background-color: #1f232a;\n"
"}\n"
"#left_menu{\n"
"    background-color: #16191d;\n"
"}\n"
"#left_menu QPushButton{\n"
"  text-align:left;\n"
"  padding:5px,10px;\n"
"  border-top-left-radius:10px;\n"
"  border-bottom-left-radius:10px;\n"
"}\n"
"#main_body_header{\n"
"   background-color: #2c313c;\n"
"}\n"
"QScrollBar:horizontal {\n"
"        height: 20px;\n"
"        background: transparent;\n"
"        margin-top: 3px;\n"
"        margin-bottom: 3px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"        height: 20px;\n"
"        min-width: 30px;\n"
"        background: rgb(68, 69, 73);\n"
"        margin-left: 15px;\n"
"        margin-right: 15px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"        background: rgb(80, 80, 80);\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"        width: 15px;\n"
"        background: transparent;\n"
""
                        "        image: url(:/Black/arrowLeft);\n"
"        subcontrol-position: left;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"        width: 15px;\n"
"        background: transparent;\n"
"        image: url(:/Black/arrowRight);\n"
"        subcontrol-position: right;\n"
"}\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"        background: rgb(68, 69, 73);\n"
"}\n"
"QScrollBar::add-line:horizontal:hover {\n"
"        background: rgb(68, 69, 73);\n"
"}\n"
"QScrollBar::add-page:horizontal,QScrollBar::sub-page:horizontal {\n"
"        background: transparent;\n"
"}\n"
"\n"
"/**********\u6eda\u52a8\u6761-\u5782\u76f4**********/\n"
"QScrollBar:vertical {\n"
"        width: 20px;\n"
"        background: transparent;\n"
"        margin-left: 3px;\n"
"        margin-right: 3px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"        width: 20px;\n"
"        min-height: 30px;\n"
"        background: rgb(68, 69, 73);\n"
"        margin-top: 15px;\n"
"        margin-bottom: 15px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {"
                        "\n"
"        background: rgb(80, 80, 80);\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"        height: 15px;\n"
"        background: transparent;\n"
"        image: url(:/Black/arrowTop);\n"
"        subcontrol-position: top;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"        height: 15px;\n"
"        background: transparent;\n"
"        image: url(:/Black/arrowBottom);\n"
"        subcontrol-position: bottom;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {\n"
"        background: rgb(68, 69, 73);\n"
"}\n"
"QScrollBar::add-line:vertical:hover {\n"
"        background: rgb(68, 69, 73);\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"        background: transparent;\n"
"}\n"
"\n"
"QScrollBar#verticalScrollBar:vertical {\n"
"        margin-top: 30px;\n"
"}\n"
"\n"
"QMessageBox {\n"
"   min-width: 160px; /* textLabel\u8bbe\u7f6e\u6700\u5c0f\u5bbd\u5ea6\u53ef\u4ee5\u76f8\u5e94\u7684\u6539\u53d8QMessageBox\u7684\u6700\u5c0f\u5bbd\u5ea6 */\n"
"	min-height: 80px; /* textLabel\u548cicon"
                        "Label\u9ad8\u5ea6\u4fdd\u6301\u4e00\u81f4 */\n"
"	background-color: #e3e3e3; /* QMessageBox\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QMessageBox QLabel { /* textLabel */\n"
"	color: #298DFF;\n"
"	background-color: transparent;\n"
"\n"
"}\n"
"\n"
"QMessageBox QLabel { /* iconLabel */\n"
"	\n"
"	\n"
"}\n"
"\n"
"QMessageBox QPushButton { /* QMessageBox\u4e2d\u7684QPushButton\u6837\u5f0f */\n"
"	border: 1px solid #298DFF;\n"
"	border-radius: 3px;\n"
"	background-color: #F2F2F2;\n"
"	color: #298DFF;\n"
"	font-family: \"Microsoft YaHei\";\n"
"	font-size: 10pt;\n"
"	min-width: 70px;\n"
"	min-height: 25px;\n"
"}\n"
"\n"
"QMessageBox QPushButton:hover {\n"
"	background-color: #298DFF;\n"
"	color: #F2F2F2;\n"
"}\n"
"\n"
"QMessageBox QPushButton:pressed {\n"
"	background-color: #257FE6;\n"
"}\n"
"\n"
"QMessageBox QDialogButtonBox#qt_msgbox_buttonbox { /* buttonBox */\n"
"	button-layout: 0; /* \u8bbe\u7f6eQPushButton\u5e03\u5c40\u597d\u50cf\u6ca1\u5565\u4f5c\u7528 */\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.left_menu = QCustomSlideMenu(self.centralwidget)
        self.left_menu.setObjectName(u"left_menu")
        self.left_menu.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout = QVBoxLayout(self.left_menu)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 0, 0, 0)
        self.frame = QFrame(self.left_menu)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(2, 2, 0, 10)
        self.menubtn = QPushButton(self.frame)
        self.menubtn.setObjectName(u"menubtn")
        self.menubtn.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menubtn.setIcon(icon)
        self.menubtn.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.menubtn)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.left_menu)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(2, 10, 0, 0)
        self.homebtn = QPushButton(self.frame_2)
        self.homebtn.setObjectName(u"homebtn")
        self.homebtn.setStyleSheet(u"background-color: #015371;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homebtn.setIcon(icon1)
        self.homebtn.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.homebtn)

        self.videobtn = QPushButton(self.frame_2)
        self.videobtn.setObjectName(u"videobtn")
        self.videobtn.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/film.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.videobtn.setIcon(icon2)
        self.videobtn.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.videobtn)

        self.loginbtn = QPushButton(self.frame_2)
        self.loginbtn.setObjectName(u"loginbtn")
        self.loginbtn.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/users.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.loginbtn.setIcon(icon3)
        self.loginbtn.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.loginbtn)

        self.cambtn = QPushButton(self.frame_2)
        self.cambtn.setObjectName(u"cambtn")
        self.cambtn.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/video.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.cambtn.setIcon(icon4)
        self.cambtn.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.cambtn)


        self.verticalLayout.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.left_menu)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(2, 0, 0, 2)
        self.ifobtn = QPushButton(self.frame_3)
        self.ifobtn.setObjectName(u"ifobtn")
        self.ifobtn.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ifobtn.setIcon(icon5)
        self.ifobtn.setIconSize(QSize(32, 32))

        self.verticalLayout_4.addWidget(self.ifobtn)


        self.verticalLayout.addWidget(self.frame_3, 0, Qt.AlignBottom)


        self.gridLayout_2.addWidget(self.left_menu, 0, 0, 1, 1)

        self.main_body = QWidget(self.centralwidget)
        self.main_body.setObjectName(u"main_body")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.main_body.sizePolicy().hasHeightForWidth())
        self.main_body.setSizePolicy(sizePolicy1)
        self.main_body.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.main_body)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.main_body_header = QWidget(self.main_body)
        self.main_body_header.setObjectName(u"main_body_header")
        self.main_body_header.setMinimumSize(QSize(0, 40))
        self.main_body_header.setMaximumSize(QSize(16777215, 60))
        self.horizontalLayout_4 = QHBoxLayout(self.main_body_header)
        self.horizontalLayout_4.setSpacing(15)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.main_body_header)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 30))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(11, 5, 341, 31))
        self.label.setMinimumSize(QSize(0, 20))
        font = QFont()
        font.setFamily(u"Microsoft Himalaya")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.horizontalLayout_4.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.main_body_header)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy2)
        self.frame_5.setLayoutDirection(Qt.LeftToRight)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.main_body_header)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 5, 0)
        self.minbtn = QPushButton(self.frame_6)
        self.minbtn.setObjectName(u"minbtn")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minbtn.setIcon(icon6)

        self.horizontalLayout_3.addWidget(self.minbtn)

        self.chanbtn = QPushButton(self.frame_6)
        self.chanbtn.setObjectName(u"chanbtn")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.chanbtn.setIcon(icon7)
        self.chanbtn.setIconSize(QSize(18, 18))

        self.horizontalLayout_3.addWidget(self.chanbtn)

        self.closebtn = QPushButton(self.frame_6)
        self.closebtn.setObjectName(u"closebtn")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closebtn.setIcon(icon8)

        self.horizontalLayout_3.addWidget(self.closebtn)


        self.horizontalLayout_4.addWidget(self.frame_6, 0, Qt.AlignRight)


        self.verticalLayout_5.addWidget(self.main_body_header)

        self.mainbody_body = QWidget(self.main_body)
        self.mainbody_body.setObjectName(u"mainbody_body")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.mainbody_body.sizePolicy().hasHeightForWidth())
        self.mainbody_body.setSizePolicy(sizePolicy3)
        self.horizontalLayout_5 = QHBoxLayout(self.mainbody_body)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.mainPages = QCustomStackedWidget(self.mainbody_body)
        self.mainPages.setObjectName(u"mainPages")
        self.mainPages.setStyleSheet(u"background-color: #343b47;")
        self.video_page = QWidget()
        self.video_page.setObjectName(u"video_page")
        self.gridLayout_3 = QGridLayout(self.video_page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.video_page)
        self.widget.setObjectName(u"widget")
        self.gridLayout_4 = QGridLayout(self.widget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.groupBox_2 = QGroupBox(self.widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 5, 0, 20)
        self.viewButton = QPushButton(self.groupBox_2)
        self.viewButton.setObjectName(u"viewButton")
        sizePolicy.setHeightForWidth(self.viewButton.sizePolicy().hasHeightForWidth())
        self.viewButton.setSizePolicy(sizePolicy)
        self.viewButton.setStyleSheet(u"background-color: rgb(0, 157, 235);\n"
"border-radius: 12px;")
        self.viewButton.setIconSize(QSize(24, 24))
        self.viewButton.setCheckable(True)

        self.horizontalLayout.addWidget(self.viewButton)

        self.playButton = QPushButton(self.groupBox_2)
        self.playButton.setObjectName(u"playButton")
        sizePolicy.setHeightForWidth(self.playButton.sizePolicy().hasHeightForWidth())
        self.playButton.setSizePolicy(sizePolicy)
        self.playButton.setStyleSheet(u"background-color: rgb(0, 157, 235);\n"
"border-radius: 12px;\n"
"")
        self.playButton.setIconSize(QSize(28, 28))

        self.horizontalLayout.addWidget(self.playButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 10)

        self.gridLayout_4.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.frame_9 = QFrame(self.widget)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.label_7 = QLabel(self.frame_9)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(180, 20, 301, 31))
        font1 = QFont()
        font1.setFamily(u"Microsoft JhengHei UI")
        font1.setPointSize(15)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_7.setFont(font1)
        self.label_7.setAlignment(Qt.AlignCenter)
        self.play_view = QLabel(self.frame_9)
        self.play_view.setObjectName(u"play_view")
        self.play_view.setGeometry(QRect(20, 60, 640, 480))
        self.play_view.setStyleSheet(u"\n"
"background-color: rgb(56, 56, 56);")

        self.gridLayout_4.addWidget(self.frame_9, 0, 0, 1, 1)

        self.gridLayout_4.setRowStretch(0, 8)
        self.gridLayout_4.setRowStretch(1, 1)

        self.gridLayout_3.addWidget(self.widget, 0, 0, 1, 1)

        self.widget_2 = QWidget(self.video_page)
        self.widget_2.setObjectName(u"widget_2")
        self.ifo_widget_2 = QWidget(self.widget_2)
        self.ifo_widget_2.setObjectName(u"ifo_widget_2")
        self.ifo_widget_2.setGeometry(QRect(30, 20, 171, 651))
        self.ifo_widget_2.setStyleSheet(u"background-color: #334456;\n"
"border-radius: 20px;")
        self.label_3 = QLabel(self.ifo_widget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 20, 91, 20))
        font2 = QFont()
        font2.setFamily(u"\u5b8b\u4f53")
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setWeight(75)
        self.label_3.setFont(font2)

        self.gridLayout_3.addWidget(self.widget_2, 0, 1, 1, 1)

        self.gridLayout_3.setColumnStretch(0, 6)
        self.gridLayout_3.setColumnStretch(1, 2)
        self.mainPages.addWidget(self.video_page)
        self.loginin_page = QWidget()
        self.loginin_page.setObjectName(u"loginin_page")
        self.layoutWidget = QWidget(self.loginin_page)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(-5, 0, 931, 711))
        self.gridLayout_5 = QGridLayout(self.layoutWidget)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.layoutWidget)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 10, 0)
        self.frame_10 = QFrame(self.widget_3)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_2 = QPushButton(self.frame_10)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy4)
        self.pushButton_2.setStyleSheet(u"")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon9)
        self.pushButton_2.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.pushButton_2, 0, Qt.AlignRight)

        self.searchEdit = QLineEdit(self.frame_10)
        self.searchEdit.setObjectName(u"searchEdit")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.searchEdit.sizePolicy().hasHeightForWidth())
        self.searchEdit.setSizePolicy(sizePolicy5)
        self.searchEdit.setStyleSheet(u"QLineEdit {\n"
"        border-top-left-radius: 4px;\n"
"border-bottom-left-radius: 4px;\n"
"        height: 25px;\n"
"        border: 1px solid rgb(100, 100, 100);\n"
"        background: rgb(72, 72, 73);\n"
"}\n"
"QLineEdit:enabled {\n"
"        color: rgb(175, 175, 175);\n"
"}\n"
"QLineEdit:enabled:hover, QLineEdit:enabled:focus {\n"
"        color: rgb(230, 230, 230);\n"
"}\n"
"QLineEdit:!enabled {\n"
"        color: rgb(155, 155, 155);\n"
"}")
        self.searchEdit.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.searchEdit.setClearButtonEnabled(True)

        self.horizontalLayout_2.addWidget(self.searchEdit)

        self.searchbtn = QPushButton(self.frame_10)
        self.searchbtn.setObjectName(u"searchbtn")
        sizePolicy4.setHeightForWidth(self.searchbtn.sizePolicy().hasHeightForWidth())
        self.searchbtn.setSizePolicy(sizePolicy4)
        self.searchbtn.setStyleSheet(u"background: rgb(0, 165, 235);\n"
"        color: white;\n"
"border-bottom-right-radius: 4px;\n"
"border-top-right-radius: 4px;\n"
"        border: none;\n"
" height: 27px;")

        self.horizontalLayout_2.addWidget(self.searchbtn)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 6)
        self.horizontalLayout_2.setStretch(2, 2)

        self.horizontalLayout_6.addWidget(self.frame_10)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.addifobtn = QPushButton(self.widget_3)
        self.addifobtn.setObjectName(u"addifobtn")
        self.addifobtn.setStyleSheet(u"background: rgb(0, 165, 235);\n"
"        color: white;\n"
" border-radius: 4px;\n"
"        border: none;\n"
"        width: 75px;\n"
"        height: 25px;")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/user-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.addifobtn.setIcon(icon10)

        self.horizontalLayout_6.addWidget(self.addifobtn)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

        self.refreshbtn = QPushButton(self.widget_3)
        self.refreshbtn.setObjectName(u"refreshbtn")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.refreshbtn.sizePolicy().hasHeightForWidth())
        self.refreshbtn.setSizePolicy(sizePolicy6)
        self.refreshbtn.setStyleSheet(u"QPushButton:hover{  \n"
"      color: white;\n"
" border-radius: 4px;\n"
"        border: none;\n"
"        width:35px;\n"
"        height:35px\n"
"}\n"
"QPushButton:pressed{\n"
"	color: green;\n"
"	border-color: blueviolet;\n"
"    background-color: #354759;\n"
"    width:35px;\n"
"    height:35px\n"
"}\n"
"      \n"
"")
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/refresh_1.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.refreshbtn.setIcon(icon11)
        self.refreshbtn.setIconSize(QSize(22, 22))

        self.horizontalLayout_6.addWidget(self.refreshbtn)

        self.horizontalLayout_6.setStretch(0, 7)
        self.horizontalLayout_6.setStretch(1, 1)
        self.horizontalLayout_6.setStretch(2, 3)
        self.horizontalLayout_6.setStretch(3, 10)
        self.horizontalLayout_6.setStretch(4, 1)

        self.gridLayout_5.addWidget(self.widget_3, 0, 0, 1, 1)

        self.feature_ifo = QTableWidget(self.layoutWidget)
        if (self.feature_ifo.columnCount() < 4):
            self.feature_ifo.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.feature_ifo.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.feature_ifo.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.feature_ifo.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.feature_ifo.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.feature_ifo.setObjectName(u"feature_ifo")
        self.feature_ifo.setStyleSheet(u"QHeaderView{\n"
"        border: none;\n"
"        border-bottom: 3px solid rgb(0, 160, 230);\n"
"        background: rgb(57, 58, 60);\n"
"        min-height: 30px;\n"
"}\n"
"QHeaderView::section:horizontal {\n"
"        border: none;\n"
"        color: white;\n"
"        background: transparent;\n"
"        padding-left: 5px;\n"
"}\n"
"QHeaderView::section:horizontal:hover {\n"
"        background: rgb(0, 160, 230);\n"
"}\n"
"QHeaderView::section:horizontal:pressed {\n"
"        background: rgb(0, 180, 255);\n"
"}\n"
"QHeaderView::up-arrow {\n"
"        width: 13px;\n"
"        height: 11px;\n"
"        padding-right: 5px;\n"
"        subcontrol-position: center right;\n"
"}\n"
"\n"
"QHeaderView::down-arrow {\n"
"        width: 13px;\n"
"        height: 11px;\n"
"        padding-right: 5px;\n"
"    \n"
"        subcontrol-position: center right;\n"
"}\n"
"\n"
"\n"
"QTableView {\n"
"        border: 1px solid rgb(45, 45, 45);\n"
"        background: rgb(57, 58, 60);\n"
"        gridline-color: rgb(60, 60, 60);\n"
""
                        "}\n"
"QTableView::item {\n"
"        padding-left: 5px;\n"
"        padding-right: 5px;\n"
"        border: none;\n"
"        background: rgb(72, 72, 74);\n"
"        border-right: 1px solid rgb(45, 45, 45);\n"
"        border-bottom: 1px solid rgb(45, 45, 45);\n"
"}\n"
"QTableView::item:selected {\n"
"        background: rgba(255, 255, 255, 40);\n"
"}\n"
"QTableView::item:selected:!active {\n"
"        color: white;\n"
"}\n"
"QTableView::indicator {\n"
"        width: 20px;\n"
"        height: 20px;\n"
"}\n"
"")

        self.gridLayout_5.addWidget(self.feature_ifo, 2, 0, 1, 1)

        self.mainPages.addWidget(self.loginin_page)
        self.camera_page = QWidget()
        self.camera_page.setObjectName(u"camera_page")
        self.layoutWidget1 = QWidget(self.camera_page)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(-1, -1, 921, 701))
        self.gridLayout = QGridLayout(self.layoutWidget1)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.layoutWidget1)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.ifo_widget = QWidget(self.frame_8)
        self.ifo_widget.setObjectName(u"ifo_widget")
        self.ifo_widget.setGeometry(QRect(22, 30, 160, 640))
        self.ifo_widget.setStyleSheet(u"background-color: #334456;\n"
"border-radius: 20px;\n"
"")
        self.label_4 = QLabel(self.ifo_widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 20, 91, 20))
        self.label_4.setFont(font2)

        self.gridLayout.addWidget(self.frame_8, 0, 1, 1, 1)

        self.frame_7 = QFrame(self.layoutWidget1)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.video_wight = QWidget(self.frame_7)
        self.video_wight.setObjectName(u"video_wight")
        self.video_wight.setGeometry(QRect(20, 40, 643, 483))
        sizePolicy.setHeightForWidth(self.video_wight.sizePolicy().hasHeightForWidth())
        self.video_wight.setSizePolicy(sizePolicy)
        self.video_wight.setStyleSheet(u"\n"
"background-color: rgb(56, 56, 56);")
        self.viedo_area = QLabel(self.video_wight)
        self.viedo_area.setObjectName(u"viedo_area")
        self.viedo_area.setGeometry(QRect(0, 0, 643, 483))
        self.viedo_area.setFrameShape(QFrame.StyledPanel)
        self.play_cutbtn = QPushButton(self.frame_7)
        self.play_cutbtn.setObjectName(u"play_cutbtn")
        self.play_cutbtn.setGeometry(QRect(20, 540, 121, 41))
        self.play_cutbtn.setStyleSheet(u"background-color: rgb(0, 157, 235);\n"
"border-radius: 12px;\n"
"selection-background-color: rgb(255, 0, 0);")
        self.label_5 = QLabel(self.frame_7)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(160, 10, 361, 31))
        font3 = QFont()
        font3.setFamily(u"Microsoft YaHei")
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setItalic(False)
        font3.setWeight(75)
        font3.setKerning(False)
        self.label_5.setFont(font3)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.frame_11 = QFrame(self.frame_7)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(300, 540, 371, 51))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.frame_11)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_8.addWidget(self.label_8)

        self.searchlabel = QLabel(self.frame_11)
        self.searchlabel.setObjectName(u"searchlabel")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.searchlabel.sizePolicy().hasHeightForWidth())
        self.searchlabel.setSizePolicy(sizePolicy7)
        self.searchlabel.setMaximumSize(QSize(16777215, 27))
        self.searchlabel.setStyleSheet(u"QLabel {\n"
"        border-top-left-radius: 4px;\n"
"        border-bottom-left-radius: 4px;\n"
"        height: 27px;\n"
"        border: 1px solid rgb(100, 100, 100);\n"
"        background: rgb(72, 72, 73);\n"
"}\n"
"")

        self.horizontalLayout_8.addWidget(self.searchlabel)

        self.searchbtn_3 = QPushButton(self.frame_11)
        self.searchbtn_3.setObjectName(u"searchbtn_3")
        sizePolicy4.setHeightForWidth(self.searchbtn_3.sizePolicy().hasHeightForWidth())
        self.searchbtn_3.setSizePolicy(sizePolicy4)
        self.searchbtn_3.setStyleSheet(u"background: rgb(0, 165, 235);\n"
"        color: white;\n"
"border-bottom-right-radius: 4px;\n"
"border-top-right-radius: 4px;\n"
"        border: none;\n"
" height: 27px;")
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/file-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.searchbtn_3.setIcon(icon12)

        self.horizontalLayout_8.addWidget(self.searchbtn_3)

        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 8)
        self.horizontalLayout_8.setStretch(2, 1)

        self.gridLayout.addWidget(self.frame_7, 0, 0, 1, 1)

        self.gridLayout.setColumnStretch(0, 7)
        self.gridLayout.setColumnStretch(1, 2)
        self.mainPages.addWidget(self.camera_page)
        self.info_page = QWidget()
        self.info_page.setObjectName(u"info_page")
        self.label_6 = QLabel(self.info_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(260, 260, 161, 81))
        font4 = QFont()
        font4.setPointSize(20)
        self.label_6.setFont(font4)
        self.label_6.setTextFormat(Qt.AutoText)
        self.mainPages.addWidget(self.info_page)
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.label_2 = QLabel(self.home_page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(260, 260, 401, 101))
        self.label_2.setFont(font4)
        self.label_2.setTextFormat(Qt.AutoText)
        self.mainPages.addWidget(self.home_page)

        self.horizontalLayout_5.addWidget(self.mainPages)


        self.verticalLayout_5.addWidget(self.mainbody_body)


        self.gridLayout_2.addWidget(self.main_body, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.mainPages.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.menubtn.setToolTip(QCoreApplication.translate("MainWindow", u"menu", None))
#endif // QT_CONFIG(tooltip)
        self.menubtn.setText("")
#if QT_CONFIG(tooltip)
        self.homebtn.setToolTip(QCoreApplication.translate("MainWindow", u"home", None))
#endif // QT_CONFIG(tooltip)
        self.homebtn.setText(QCoreApplication.translate("MainWindow", u"\u4e3b\u754c\u9762", None))
#if QT_CONFIG(tooltip)
        self.videobtn.setToolTip(QCoreApplication.translate("MainWindow", u"video", None))
#endif // QT_CONFIG(tooltip)
        self.videobtn.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u9891\u8eab\u4efd\u8bc6\u522b", None))
#if QT_CONFIG(tooltip)
        self.loginbtn.setToolTip(QCoreApplication.translate("MainWindow", u"login", None))
#endif // QT_CONFIG(tooltip)
        self.loginbtn.setText(QCoreApplication.translate("MainWindow", u"\u8eab\u4efd\u4fe1\u606f\u7ba1\u7406", None))
#if QT_CONFIG(tooltip)
        self.cambtn.setToolTip(QCoreApplication.translate("MainWindow", u"camera", None))
#endif // QT_CONFIG(tooltip)
        self.cambtn.setText(QCoreApplication.translate("MainWindow", u"\u6444\u50cf\u5934\u5b9e\u65f6\u8eab\u4efd\u8bc6\u522b ", None))
#if QT_CONFIG(tooltip)
        self.ifobtn.setToolTip(QCoreApplication.translate("MainWindow", u"info", None))
#endif // QT_CONFIG(tooltip)
        self.ifobtn.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u53d1\u8005\u4fe1\u606f", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u57fa\u4e8e\u751f\u6210\u5bf9\u6297\u7f51\u7edc\u7684\u8eab\u4efd\u8bc6\u522b\u7cfb\u7edf", None))
        self.minbtn.setText("")
        self.chanbtn.setText("")
        self.closebtn.setText("")
        self.groupBox_2.setTitle("")
        self.viewButton.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u89c6\u9891\u6587\u4ef6", None))
        self.playButton.setText(QCoreApplication.translate("MainWindow", u"\u64ad\u653e", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u9891\u8eab\u4efd\u8bc6\u522b", None))
        self.play_view.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u76f8\u5173\u4fe1\u606f", None))
        self.pushButton_2.setText("")
        self.searchEdit.setInputMask("")
        self.searchEdit.setText("")
        self.searchEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u59d3\u540d\u6216\u7f16\u53f7", None))
        self.searchbtn.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22", None))
        self.addifobtn.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u65b0\u4fe1\u606f", None))
        self.refreshbtn.setText("")
        ___qtablewidgetitem = self.feature_ifo.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u53f7", None));
        ___qtablewidgetitem1 = self.feature_ifo.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u59d3\u540d", None));
        ___qtablewidgetitem2 = self.feature_ifo.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u6b65\u6001\u7279\u5f81\u4fe1\u606f", None));
        ___qtablewidgetitem3 = self.feature_ifo.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u64cd\u4f5c", None));
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u76f8\u5173\u4fe1\u606f", None))
        self.viedo_area.setText("")
        self.play_cutbtn.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u6444\u50cf\u5934", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u5b9e\u65f6\u76d1\u63a7", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u9ed8\u8ba4\u4fdd\u5b58\u6587\u4ef6:", None))
        self.searchlabel.setText("")
        self.searchbtn_3.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u53d1\u8005\u4fe1\u606f", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u4e3b\u9875\u9762", None))
    # retranslateUi

