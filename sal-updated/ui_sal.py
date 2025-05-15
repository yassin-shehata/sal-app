# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sal.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QTabWidget, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1326, 859)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        MainWindow.setStyleSheet(u"\n"
"QWidget {\n"
"    background-color: rgb(225,225,225);  \n"
"}\n"
"#centralwidget {\n"
"    background-color: transparent;\n"
"}\n"
"QMainWindow {\n"
"    background-color: rgb(227, 229, 123);\n"
"}\n"
"QPushButton {\n"
"    border: 1px solid black;\n"
"    border-radius: 10px;\n"
"    color: black;            \n"
"    padding: 5px;                \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #ffffff;   \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #d9d9d9;   \n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	border: 1px solid rgb(150, 150, 150); /* Gray border */\n"
"    color: rgb(150, 150, 150);\n"
"}\n"
"\n"
"QTextEdit, QComboBox, QSpinBox { \n"
"	border: 1px solid black; \n"
"	background-color: white;\n"
"}\n"
"\n"
"QTabWidget, QFrame { \n"
"	border: 1px solid black; \n"
"}\n"
"\n"
"QLabel {\n"
"	border: none; \n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_title = QHBoxLayout()
        self.horizontalLayout_title.setObjectName(u"horizontalLayout_title")
        self.title_label = QLabel(self.centralwidget)
        self.title_label.setObjectName(u"title_label")
        sizePolicy.setHeightForWidth(self.title_label.sizePolicy().hasHeightForWidth())
        self.title_label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet(u"background-color: transparent\n"
"")

        self.horizontalLayout_title.addWidget(self.title_label)

        self.logo = QLabel(self.centralwidget)
        self.logo.setObjectName(u"logo")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy1)
        self.logo.setMaximumSize(QSize(300, 16777215))
        self.logo.setStyleSheet(u"image: url(:/newPrefix/logo.png);\n"
"background-color: transparent;\n"
"")

        self.horizontalLayout_title.addWidget(self.logo)

        self.horizontalLayout_title.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_title)

        self.horizontalLayout_middle = QHBoxLayout()
        self.horizontalLayout_middle.setObjectName(u"horizontalLayout_middle")
        self.verticalLayout_system_check = QVBoxLayout()
        self.verticalLayout_system_check.setObjectName(u"verticalLayout_system_check")
        self.system_check_label = QLabel(self.centralwidget)
        self.system_check_label.setObjectName(u"system_check_label")
        sizePolicy.setHeightForWidth(self.system_check_label.sizePolicy().hasHeightForWidth())
        self.system_check_label.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        self.system_check_label.setFont(font1)
        self.system_check_label.setStyleSheet(u"background-color: transparent")

        self.verticalLayout_system_check.addWidget(self.system_check_label)

        self.system_connection_horizontal_layout = QHBoxLayout()
        self.system_connection_horizontal_layout.setObjectName(u"system_connection_horizontal_layout")
        self.system_check_button_frame = QFrame(self.centralwidget)
        self.system_check_button_frame.setObjectName(u"system_check_button_frame")
        sizePolicy.setHeightForWidth(self.system_check_button_frame.sizePolicy().hasHeightForWidth())
        self.system_check_button_frame.setSizePolicy(sizePolicy)
        self.system_check_button_frame.setMinimumSize(QSize(184, 0))
        self.system_check_button_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.system_check_button_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.system_check_button_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_system_connect = QPushButton(self.system_check_button_frame)
        self.btn_system_connect.setObjectName(u"btn_system_connect")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_system_connect.sizePolicy().hasHeightForWidth())
        self.btn_system_connect.setSizePolicy(sizePolicy2)
        self.btn_system_connect.setFont(font)

        self.horizontalLayout.addWidget(self.btn_system_connect)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lbl_connection_status = QLabel(self.system_check_button_frame)
        self.lbl_connection_status.setObjectName(u"lbl_connection_status")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.lbl_connection_status.setFont(font2)

        self.horizontalLayout_2.addWidget(self.lbl_connection_status)

        self.system_check_circle = QFrame(self.system_check_button_frame)
        self.system_check_circle.setObjectName(u"system_check_circle")
        self.system_check_circle.setMinimumSize(QSize(30, 30))
        self.system_check_circle.setMaximumSize(QSize(30, 30))
        self.system_check_circle.setStyleSheet(u"border-radius: 15px;  \n"
"    border: 1px solid black;\n"
"    width: 30px;\n"
"    height: 30px;\n"
"    background: qradialgradient(\n"
"        cx:0.5,cy:0.3,radius:1\n"
"        stop: 0 rgb(240, 240, 240),  \n"
"        stop: 0.8 rgb(100, 100, 100),\n"
"        stop: 1 rgb(240, 240, 240)   \n"
"    );")
        self.system_check_circle.setFrameShape(QFrame.Shape.StyledPanel)
        self.system_check_circle.setFrameShadow(QFrame.Shadow.Raised)
        self.indicator_connection = QFrame(self.system_check_circle)
        self.indicator_connection.setObjectName(u"indicator_connection")
        self.indicator_connection.setGeometry(QRect(0, 0, 30, 30))
        self.indicator_connection.setMinimumSize(QSize(30, 30))
        self.indicator_connection.setMaximumSize(QSize(30, 30))
        self.indicator_connection.setStyleSheet(u"border-radius: 15px;  \n"
"    border: 1px solid black;\n"
"    width: 30px;\n"
"    height: 30px;\n"
"    background: qradialgradient(\n"
"        cx:0.5,cy:0.3,radius:1\n"
"        stop: 0 rgb(240, 240, 240),  \n"
"        stop: 0.8 rgb(100, 100, 100),\n"
"        stop: 1 rgb(240, 240, 240)   \n"
"    );")
        self.indicator_connection.setFrameShape(QFrame.Shape.StyledPanel)
        self.indicator_connection.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_2.addWidget(self.system_check_circle)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.system_connection_horizontal_layout.addWidget(self.system_check_button_frame)

        self.table_frame = QFrame(self.centralwidget)
        self.table_frame.setObjectName(u"table_frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.table_frame.sizePolicy().hasHeightForWidth())
        self.table_frame.setSizePolicy(sizePolicy3)
        self.table_frame.setMinimumSize(QSize(0, 0))
        self.table_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.table_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.table_frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lbl_system_note = QLabel(self.table_frame)
        self.lbl_system_note.setObjectName(u"lbl_system_note")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.lbl_system_note.sizePolicy().hasHeightForWidth())
        self.lbl_system_note.setSizePolicy(sizePolicy4)
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.lbl_system_note.setFont(font3)
        self.lbl_system_note.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.lbl_system_note)

        self.indicator_note_status = QFrame(self.table_frame)
        self.indicator_note_status.setObjectName(u"indicator_note_status")
        self.indicator_note_status.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.indicator_note_status.sizePolicy().hasHeightForWidth())
        self.indicator_note_status.setSizePolicy(sizePolicy3)
        self.indicator_note_status.setMinimumSize(QSize(30, 30))
        self.indicator_note_status.setMaximumSize(QSize(30, 30))
        self.indicator_note_status.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.indicator_note_status.setStyleSheet(u"border-radius: 15px;  \n"
"    border: 1px solid black;\n"
"    width: 30px;\n"
"    height: 30px;\n"
"    background: qradialgradient(\n"
"        cx:0.5,cy:0.3,radius:1\n"
"        stop: 0 rgb(240, 240, 240),  \n"
"        stop: 0.8 rgb(100, 100, 100),\n"
"        stop: 1 rgb(240, 240, 240)   \n"
"    );")
        self.indicator_note_status.setFrameShape(QFrame.Shape.StyledPanel)
        self.indicator_note_status.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_3.addWidget(self.indicator_note_status)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.lbl_note_status_tag = QLabel(self.table_frame)
        self.lbl_note_status_tag.setObjectName(u"lbl_note_status_tag")

        self.verticalLayout_6.addWidget(self.lbl_note_status_tag)


        self.horizontalLayout_4.addLayout(self.verticalLayout_6)

        self.inner_table_frame = QFrame(self.table_frame)
        self.inner_table_frame.setObjectName(u"inner_table_frame")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(1)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.inner_table_frame.sizePolicy().hasHeightForWidth())
        self.inner_table_frame.setSizePolicy(sizePolicy5)
        self.inner_table_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.inner_table_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.inner_table_frame)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.txt_system_note = QLabel(self.inner_table_frame)
        self.txt_system_note.setObjectName(u"txt_system_note")

        self.verticalLayout_9.addWidget(self.txt_system_note)

        self.lbl_progress_status = QLabel(self.inner_table_frame)
        self.lbl_progress_status.setObjectName(u"lbl_progress_status")

        self.verticalLayout_9.addWidget(self.lbl_progress_status)

        self.bar_progress = QProgressBar(self.inner_table_frame)
        self.bar_progress.setObjectName(u"bar_progress")
        self.bar_progress.setValue(24)

        self.verticalLayout_9.addWidget(self.bar_progress)


        self.horizontalLayout_4.addWidget(self.inner_table_frame)


        self.system_connection_horizontal_layout.addWidget(self.table_frame)

        self.system_connection_horizontal_layout.setStretch(1, 1)

        self.verticalLayout_system_check.addLayout(self.system_connection_horizontal_layout)

        self.data_frame = QFrame(self.centralwidget)
        self.data_frame.setObjectName(u"data_frame")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(1)
        sizePolicy6.setVerticalStretch(1)
        sizePolicy6.setHeightForWidth(self.data_frame.sizePolicy().hasHeightForWidth())
        self.data_frame.setSizePolicy(sizePolicy6)
        self.data_frame.setStyleSheet(u"b")
        self.data_frame.setFrameShape(QFrame.Shape.Box)
        self.data_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.data_frame)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.graph_frame = QFrame(self.data_frame)
        self.graph_frame.setObjectName(u"graph_frame")
        sizePolicy2.setHeightForWidth(self.graph_frame.sizePolicy().hasHeightForWidth())
        self.graph_frame.setSizePolicy(sizePolicy2)
        self.graph_frame.setMinimumSize(QSize(360, 0))
        self.graph_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.graph_frame.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_11.addWidget(self.graph_frame)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.potential_label = QLabel(self.data_frame)
        self.potential_label.setObjectName(u"potential_label")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.potential_label.sizePolicy().hasHeightForWidth())
        self.potential_label.setSizePolicy(sizePolicy7)
        self.potential_label.setMaximumSize(QSize(16777215, 40))
        font4 = QFont()
        font4.setPointSize(11)
        font4.setBold(True)
        self.potential_label.setFont(font4)

        self.verticalLayout_4.addWidget(self.potential_label)

        self.potential_input = QTextEdit(self.data_frame)
        self.potential_input.setObjectName(u"potential_input")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.potential_input.sizePolicy().hasHeightForWidth())
        self.potential_input.setSizePolicy(sizePolicy8)
        self.potential_input.setMinimumSize(QSize(0, 28))
        self.potential_input.setMaximumSize(QSize(16777215, 36))

        self.verticalLayout_4.addWidget(self.potential_input)

        self.cl_conc_label = QLabel(self.data_frame)
        self.cl_conc_label.setObjectName(u"cl_conc_label")
        sizePolicy7.setHeightForWidth(self.cl_conc_label.sizePolicy().hasHeightForWidth())
        self.cl_conc_label.setSizePolicy(sizePolicy7)
        self.cl_conc_label.setMinimumSize(QSize(0, 0))
        self.cl_conc_label.setMaximumSize(QSize(16777215, 40))
        self.cl_conc_label.setFont(font4)

        self.verticalLayout_4.addWidget(self.cl_conc_label)

        self.cl_conc_input = QTextEdit(self.data_frame)
        self.cl_conc_input.setObjectName(u"cl_conc_input")
        sizePolicy8.setHeightForWidth(self.cl_conc_input.sizePolicy().hasHeightForWidth())
        self.cl_conc_input.setSizePolicy(sizePolicy8)
        self.cl_conc_input.setMinimumSize(QSize(0, 28))
        self.cl_conc_input.setMaximumSize(QSize(16777215, 36))

        self.verticalLayout_4.addWidget(self.cl_conc_input)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.r_squared_label = QLabel(self.data_frame)
        self.r_squared_label.setObjectName(u"r_squared_label")
        self.r_squared_label.setEnabled(False)
        sizePolicy7.setHeightForWidth(self.r_squared_label.sizePolicy().hasHeightForWidth())
        self.r_squared_label.setSizePolicy(sizePolicy7)
        self.r_squared_label.setMinimumSize(QSize(0, 0))
        self.r_squared_label.setMaximumSize(QSize(16777215, 40))
        self.r_squared_label.setFont(font4)

        self.horizontalLayout_5.addWidget(self.r_squared_label)

        self.r_squared_label_2 = QLabel(self.data_frame)
        self.r_squared_label_2.setObjectName(u"r_squared_label_2")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.r_squared_label_2.sizePolicy().hasHeightForWidth())
        self.r_squared_label_2.setSizePolicy(sizePolicy9)
        self.r_squared_label_2.setMinimumSize(QSize(0, 0))
        self.r_squared_label_2.setMaximumSize(QSize(16777215, 40))
        self.r_squared_label_2.setFont(font4)

        self.horizontalLayout_5.addWidget(self.r_squared_label_2)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 1)

        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.r_squared_input = QComboBox(self.data_frame)
        self.r_squared_input.setObjectName(u"r_squared_input")
        sizePolicy9.setHeightForWidth(self.r_squared_input.sizePolicy().hasHeightForWidth())
        self.r_squared_input.setSizePolicy(sizePolicy9)
        self.r_squared_input.setMinimumSize(QSize(0, 28))
        self.r_squared_input.setMaximumSize(QSize(16777215, 36))
        self.r_squared_input.setStyleSheet(u"b")
        self.r_squared_input.setFrame(True)

        self.verticalLayout_4.addWidget(self.r_squared_input)

        self.refresh_plot_button = QPushButton(self.data_frame)
        self.refresh_plot_button.setObjectName(u"refresh_plot_button")
        self.refresh_plot_button.setEnabled(False)
        sizePolicy9.setHeightForWidth(self.refresh_plot_button.sizePolicy().hasHeightForWidth())
        self.refresh_plot_button.setSizePolicy(sizePolicy9)
        font5 = QFont()
        font5.setPointSize(16)
        font5.setBold(True)
        self.refresh_plot_button.setFont(font5)

        self.verticalLayout_4.addWidget(self.refresh_plot_button)

        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 1)
        self.verticalLayout_4.setStretch(2, 1)
        self.verticalLayout_4.setStretch(3, 1)
        self.verticalLayout_4.setStretch(4, 1)
        self.verticalLayout_4.setStretch(5, 1)
        self.verticalLayout_4.setStretch(6, 1)

        self.horizontalLayout_11.addLayout(self.verticalLayout_4)

        self.horizontalLayout_11.setStretch(0, 1)

        self.verticalLayout_system_check.addWidget(self.data_frame)


        self.horizontalLayout_middle.addLayout(self.verticalLayout_system_check)

        self.verticalLayout_sample_measurement = QVBoxLayout()
        self.verticalLayout_sample_measurement.setObjectName(u"verticalLayout_sample_measurement")
        self.sample_measurement_label = QLabel(self.centralwidget)
        self.sample_measurement_label.setObjectName(u"sample_measurement_label")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.sample_measurement_label.sizePolicy().hasHeightForWidth())
        self.sample_measurement_label.setSizePolicy(sizePolicy10)
        self.sample_measurement_label.setFont(font1)
        self.sample_measurement_label.setStyleSheet(u"background-color: transparent\n"
"")

        self.verticalLayout_sample_measurement.addWidget(self.sample_measurement_label)

        self.sample_measurement_tab_frame = QFrame(self.centralwidget)
        self.sample_measurement_tab_frame.setObjectName(u"sample_measurement_tab_frame")
        self.sample_measurement_tab_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.sample_measurement_tab_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout = QFormLayout(self.sample_measurement_tab_frame)
        self.formLayout.setObjectName(u"formLayout")
        self.sample_measurement_tab_widget = QTabWidget(self.sample_measurement_tab_frame)
        self.sample_measurement_tab_widget.setObjectName(u"sample_measurement_tab_widget")
        self.calibration = QWidget()
        self.calibration.setObjectName(u"calibration")
        self.verticalLayout_3 = QVBoxLayout(self.calibration)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_calibration = QHBoxLayout()
        self.horizontalLayout_calibration.setObjectName(u"horizontalLayout_calibration")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_calibration.addItem(self.horizontalSpacer)

        self.reset_button_measurement = QPushButton(self.calibration)
        self.reset_button_measurement.setObjectName(u"reset_button_measurement")
        self.reset_button_measurement.setEnabled(False)

        self.horizontalLayout_calibration.addWidget(self.reset_button_measurement)

        self.apply_button_measurement = QPushButton(self.calibration)
        self.apply_button_measurement.setObjectName(u"apply_button_measurement")
        self.apply_button_measurement.setEnabled(False)

        self.horizontalLayout_calibration.addWidget(self.apply_button_measurement)

        self.horizontalLayout_calibration.setStretch(0, 2)
        self.horizontalLayout_calibration.setStretch(1, 1)
        self.horizontalLayout_calibration.setStretch(2, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_calibration)

        self.calibration_frame = QFrame(self.calibration)
        self.calibration_frame.setObjectName(u"calibration_frame")
        self.calibration_frame.setEnabled(False)
        self.calibration_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.calibration_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.calibration_frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.STD5000MeasurementButton = QPushButton(self.calibration_frame)
        self.STD5000MeasurementButton.setObjectName(u"STD5000MeasurementButton")
        self.STD5000MeasurementButton.setEnabled(False)

        self.gridLayout_2.addWidget(self.STD5000MeasurementButton, 3, 2, 1, 1)

        self.STD100Measurement = QLabel(self.calibration_frame)
        self.STD100Measurement.setObjectName(u"STD100Measurement")
        self.STD100Measurement.setEnabled(False)
        self.STD100Measurement.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.STD100Measurement, 1, 0, 1, 1)

        self.STD100ppmEditField = QTextEdit(self.calibration_frame)
        self.STD100ppmEditField.setObjectName(u"STD100ppmEditField")
        self.STD100ppmEditField.setEnabled(False)
        self.STD100ppmEditField.setMinimumSize(QSize(150, 28))
        self.STD100ppmEditField.setMaximumSize(QSize(150, 26))
        self.STD100ppmEditField.setAutoFillBackground(False)
        self.STD100ppmEditField.setFrameShape(QFrame.Shape.Box)
        self.STD100ppmEditField.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)

        self.gridLayout_2.addWidget(self.STD100ppmEditField, 1, 1, 1, 1)

        self.STD10MeasurementButton = QPushButton(self.calibration_frame)
        self.STD10MeasurementButton.setObjectName(u"STD10MeasurementButton")
        self.STD10MeasurementButton.setEnabled(False)

        self.gridLayout_2.addWidget(self.STD10MeasurementButton, 0, 2, 1, 1)

        self.STD100MeasurementButton = QPushButton(self.calibration_frame)
        self.STD100MeasurementButton.setObjectName(u"STD100MeasurementButton")
        self.STD100MeasurementButton.setEnabled(False)

        self.gridLayout_2.addWidget(self.STD100MeasurementButton, 1, 2, 1, 1)

        self.STD1000Measurement = QLabel(self.calibration_frame)
        self.STD1000Measurement.setObjectName(u"STD1000Measurement")
        self.STD1000Measurement.setEnabled(False)
        self.STD1000Measurement.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.STD1000Measurement, 2, 0, 1, 1)

        self.STD5000Measurement = QLabel(self.calibration_frame)
        self.STD5000Measurement.setObjectName(u"STD5000Measurement")
        self.STD5000Measurement.setEnabled(False)
        self.STD5000Measurement.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.STD5000Measurement, 3, 0, 1, 1)

        self.STD1000ppmEditField = QTextEdit(self.calibration_frame)
        self.STD1000ppmEditField.setObjectName(u"STD1000ppmEditField")
        self.STD1000ppmEditField.setEnabled(False)
        self.STD1000ppmEditField.setMinimumSize(QSize(150, 28))
        self.STD1000ppmEditField.setMaximumSize(QSize(150, 26))
        self.STD1000ppmEditField.setAutoFillBackground(False)
        self.STD1000ppmEditField.setFrameShape(QFrame.Shape.Box)
        self.STD1000ppmEditField.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)

        self.gridLayout_2.addWidget(self.STD1000ppmEditField, 2, 1, 1, 1)

        self.STD5000ppmEditField = QTextEdit(self.calibration_frame)
        self.STD5000ppmEditField.setObjectName(u"STD5000ppmEditField")
        self.STD5000ppmEditField.setEnabled(False)
        self.STD5000ppmEditField.setMinimumSize(QSize(150, 28))
        self.STD5000ppmEditField.setMaximumSize(QSize(150, 26))
        self.STD5000ppmEditField.setAutoFillBackground(False)
        self.STD5000ppmEditField.setFrameShape(QFrame.Shape.Box)
        self.STD5000ppmEditField.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)

        self.gridLayout_2.addWidget(self.STD5000ppmEditField, 3, 1, 1, 1)

        self.STD10Measurement = QLabel(self.calibration_frame)
        self.STD10Measurement.setObjectName(u"STD10Measurement")
        self.STD10Measurement.setEnabled(False)
        self.STD10Measurement.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.STD10Measurement, 0, 0, 1, 1)

        self.STD1000MeasurementButton = QPushButton(self.calibration_frame)
        self.STD1000MeasurementButton.setObjectName(u"STD1000MeasurementButton")
        self.STD1000MeasurementButton.setEnabled(False)

        self.gridLayout_2.addWidget(self.STD1000MeasurementButton, 2, 2, 1, 1)

        self.CalibrationCurveFittingButton = QPushButton(self.calibration_frame)
        self.CalibrationCurveFittingButton.setObjectName(u"CalibrationCurveFittingButton")
        self.CalibrationCurveFittingButton.setEnabled(False)

        self.gridLayout_2.addWidget(self.CalibrationCurveFittingButton, 4, 2, 1, 1)

        self.STD10ppmEditField = QTextEdit(self.calibration_frame)
        self.STD10ppmEditField.setObjectName(u"STD10ppmEditField")
        self.STD10ppmEditField.setEnabled(False)
        self.STD10ppmEditField.setMinimumSize(QSize(150, 28))
        self.STD10ppmEditField.setMaximumSize(QSize(150, 26))
        self.STD10ppmEditField.setAutoFillBackground(False)
        self.STD10ppmEditField.setFrameShape(QFrame.Shape.Box)
        self.STD10ppmEditField.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)

        self.gridLayout_2.addWidget(self.STD10ppmEditField, 0, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.calibration_frame)

        self.sample_measurement_tab_widget.addTab(self.calibration, "")
        self.sample_information = QWidget()
        self.sample_information.setObjectName(u"sample_information")
        self.verticalLayout_5 = QVBoxLayout(self.sample_information)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.sample_information_top_grid_layout = QGridLayout()
        self.sample_information_top_grid_layout.setObjectName(u"sample_information_top_grid_layout")
        self.project_name_label = QLabel(self.sample_information)
        self.project_name_label.setObjectName(u"project_name_label")
        self.project_name_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.sample_information_top_grid_layout.addWidget(self.project_name_label, 0, 0, 1, 1)

        self.project_name_input = QTextEdit(self.sample_information)
        self.project_name_input.setObjectName(u"project_name_input")
        self.project_name_input.setMinimumSize(QSize(150, 28))
        self.project_name_input.setMaximumSize(QSize(150, 26))
        self.project_name_input.setAutoFillBackground(False)
        self.project_name_input.setFrameShape(QFrame.Shape.Box)
        self.project_name_input.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)

        self.sample_information_top_grid_layout.addWidget(self.project_name_input, 0, 1, 1, 1)

        self.sample_no_label = QLabel(self.sample_information)
        self.sample_no_label.setObjectName(u"sample_no_label")

        self.sample_information_top_grid_layout.addWidget(self.sample_no_label, 0, 2, 1, 1)

        self.sample_no_spinbox = QSpinBox(self.sample_information)
        self.sample_no_spinbox.setObjectName(u"sample_no_spinbox")
        self.sample_no_spinbox.setMinimumSize(QSize(150, 28))
        self.sample_no_spinbox.setMaximumSize(QSize(150, 26))
        self.sample_no_spinbox.setStyleSheet(u"")

        self.sample_information_top_grid_layout.addWidget(self.sample_no_spinbox, 0, 3, 1, 1)

        self.sample_id_label = QLabel(self.sample_information)
        self.sample_id_label.setObjectName(u"sample_id_label")
        self.sample_id_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.sample_information_top_grid_layout.addWidget(self.sample_id_label, 1, 0, 1, 1)

        self.sample_id_input = QTextEdit(self.sample_information)
        self.sample_id_input.setObjectName(u"sample_id_input")
        self.sample_id_input.setMinimumSize(QSize(150, 28))
        self.sample_id_input.setMaximumSize(QSize(150, 26))
        self.sample_id_input.setAutoFillBackground(False)
        self.sample_id_input.setFrameShape(QFrame.Shape.Box)
        self.sample_id_input.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)

        self.sample_information_top_grid_layout.addWidget(self.sample_id_input, 1, 1, 1, 1)

        self.replication_label = QLabel(self.sample_information)
        self.replication_label.setObjectName(u"replication_label")

        self.sample_information_top_grid_layout.addWidget(self.replication_label, 1, 2, 1, 1)

        self.replication_spinbox = QSpinBox(self.sample_information)
        self.replication_spinbox.setObjectName(u"replication_spinbox")
        self.replication_spinbox.setMinimumSize(QSize(150, 28))
        self.replication_spinbox.setMaximumSize(QSize(150, 26))

        self.sample_information_top_grid_layout.addWidget(self.replication_spinbox, 1, 3, 1, 1)

        self.auto_sample_naming_checkbox = QCheckBox(self.sample_information)
        self.auto_sample_naming_checkbox.setObjectName(u"auto_sample_naming_checkbox")

        self.sample_information_top_grid_layout.addWidget(self.auto_sample_naming_checkbox, 2, 0, 1, 1)

        self.sample_type_label = QLabel(self.sample_information)
        self.sample_type_label.setObjectName(u"sample_type_label")

        self.sample_information_top_grid_layout.addWidget(self.sample_type_label, 2, 2, 1, 1)

        self.sample_type_combobox_2 = QComboBox(self.sample_information)
        self.sample_type_combobox_2.setObjectName(u"sample_type_combobox_2")
        self.sample_type_combobox_2.setMinimumSize(QSize(150, 28))
        self.sample_type_combobox_2.setMaximumSize(QSize(150, 26))
        self.sample_type_combobox_2.setStyleSheet(u"b")
        self.sample_type_combobox_2.setFrame(True)

        self.sample_information_top_grid_layout.addWidget(self.sample_type_combobox_2, 2, 3, 1, 1)


        self.verticalLayout_5.addLayout(self.sample_information_top_grid_layout)

        self.sample_information_frame = QFrame(self.sample_information)
        self.sample_information_frame.setObjectName(u"sample_information_frame")
        self.sample_information_frame.setEnabled(False)
        self.sample_information_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.sample_information_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.sample_information_frame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.sample_information_grid_layout_ = QGridLayout()
        self.sample_information_grid_layout_.setObjectName(u"sample_information_grid_layout_")
        self.bore_hole_id_label = QLabel(self.sample_information_frame)
        self.bore_hole_id_label.setObjectName(u"bore_hole_id_label")
        self.bore_hole_id_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.sample_information_grid_layout_.addWidget(self.bore_hole_id_label, 0, 0, 1, 1)

        self.bore_hole_id_input = QTextEdit(self.sample_information_frame)
        self.bore_hole_id_input.setObjectName(u"bore_hole_id_input")
        self.bore_hole_id_input.setMinimumSize(QSize(150, 28))
        self.bore_hole_id_input.setMaximumSize(QSize(150, 26))
        self.bore_hole_id_input.setAutoFillBackground(False)
        self.bore_hole_id_input.setFrameShape(QFrame.Shape.Box)
        self.bore_hole_id_input.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)

        self.sample_information_grid_layout_.addWidget(self.bore_hole_id_input, 0, 1, 1, 1)

        self.bore_hole_no_label = QLabel(self.sample_information_frame)
        self.bore_hole_no_label.setObjectName(u"bore_hole_no_label")
        self.bore_hole_no_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.sample_information_grid_layout_.addWidget(self.bore_hole_no_label, 0, 2, 1, 1)

        self.bore_hole_no_input = QTextEdit(self.sample_information_frame)
        self.bore_hole_no_input.setObjectName(u"bore_hole_no_input")
        self.bore_hole_no_input.setMinimumSize(QSize(150, 28))
        self.bore_hole_no_input.setMaximumSize(QSize(150, 26))
        self.bore_hole_no_input.setAutoFillBackground(False)
        self.bore_hole_no_input.setFrameShape(QFrame.Shape.Box)
        self.bore_hole_no_input.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)

        self.sample_information_grid_layout_.addWidget(self.bore_hole_no_input, 0, 3, 1, 1)

        self.top_depth_label = QLabel(self.sample_information_frame)
        self.top_depth_label.setObjectName(u"top_depth_label")
        self.top_depth_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.sample_information_grid_layout_.addWidget(self.top_depth_label, 1, 0, 1, 1)

        self.top_depth_input = QTextEdit(self.sample_information_frame)
        self.top_depth_input.setObjectName(u"top_depth_input")
        self.top_depth_input.setMinimumSize(QSize(150, 28))
        self.top_depth_input.setMaximumSize(QSize(150, 26))
        self.top_depth_input.setAutoFillBackground(False)
        self.top_depth_input.setFrameShape(QFrame.Shape.Box)
        self.top_depth_input.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)

        self.sample_information_grid_layout_.addWidget(self.top_depth_input, 1, 1, 1, 1)

        self.bottom_depth_label = QLabel(self.sample_information_frame)
        self.bottom_depth_label.setObjectName(u"bottom_depth_label")
        self.bottom_depth_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.sample_information_grid_layout_.addWidget(self.bottom_depth_label, 1, 2, 1, 1)

        self.bottom_depth_input = QTextEdit(self.sample_information_frame)
        self.bottom_depth_input.setObjectName(u"bottom_depth_input")
        self.bottom_depth_input.setMinimumSize(QSize(150, 28))
        self.bottom_depth_input.setMaximumSize(QSize(150, 26))
        self.bottom_depth_input.setAutoFillBackground(False)
        self.bottom_depth_input.setFrameShape(QFrame.Shape.Box)
        self.bottom_depth_input.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)

        self.sample_information_grid_layout_.addWidget(self.bottom_depth_input, 1, 3, 1, 1)


        self.gridLayout_5.addLayout(self.sample_information_grid_layout_, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.sample_information_frame)

        self.sample_measurement_tab_widget.addTab(self.sample_information, "")
        self.guideline = QWidget()
        self.guideline.setObjectName(u"guideline")
        self.verticalLayout_7 = QVBoxLayout(self.guideline)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_guideline = QHBoxLayout()
        self.horizontalLayout_guideline.setObjectName(u"horizontalLayout_guideline")
        self.single_guideline_checkbox = QCheckBox(self.guideline)
        self.single_guideline_checkbox.setObjectName(u"single_guideline_checkbox")

        self.horizontalLayout_guideline.addWidget(self.single_guideline_checkbox)

        self.multiple_guideline_checkbox = QCheckBox(self.guideline)
        self.multiple_guideline_checkbox.setObjectName(u"multiple_guideline_checkbox")

        self.horizontalLayout_guideline.addWidget(self.multiple_guideline_checkbox)

        self.reset_button_guideline = QPushButton(self.guideline)
        self.reset_button_guideline.setObjectName(u"reset_button_guideline")
        self.reset_button_guideline.setEnabled(False)

        self.horizontalLayout_guideline.addWidget(self.reset_button_guideline)

        self.apply_button_guideline = QPushButton(self.guideline)
        self.apply_button_guideline.setObjectName(u"apply_button_guideline")
        self.apply_button_guideline.setEnabled(False)

        self.horizontalLayout_guideline.addWidget(self.apply_button_guideline)

        self.horizontalLayout_guideline.setStretch(0, 1)
        self.horizontalLayout_guideline.setStretch(1, 1)
        self.horizontalLayout_guideline.setStretch(2, 1)
        self.horizontalLayout_guideline.setStretch(3, 1)

        self.verticalLayout_7.addLayout(self.horizontalLayout_guideline)

        self.guideline_frame = QFrame(self.guideline)
        self.guideline_frame.setObjectName(u"guideline_frame")
        self.guideline_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.guideline_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_6 = QGridLayout(self.guideline_frame)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.guideline_type_label = QLabel(self.guideline_frame)
        self.guideline_type_label.setObjectName(u"guideline_type_label")

        self.gridLayout_6.addWidget(self.guideline_type_label, 0, 0, 1, 1)

        self.guideline_type_combobox = QComboBox(self.guideline_frame)
        self.guideline_type_combobox.setObjectName(u"guideline_type_combobox")
        self.guideline_type_combobox.setMinimumSize(QSize(150, 28))
        self.guideline_type_combobox.setMaximumSize(QSize(150, 26))
        self.guideline_type_combobox.setStyleSheet(u"b")
        self.guideline_type_combobox.setFrame(True)

        self.gridLayout_6.addWidget(self.guideline_type_combobox, 0, 1, 1, 1)

        self.main_parameter_label = QLabel(self.guideline_frame)
        self.main_parameter_label.setObjectName(u"main_parameter_label")

        self.gridLayout_6.addWidget(self.main_parameter_label, 1, 0, 1, 1)

        self.main_parameter_input = QTextEdit(self.guideline_frame)
        self.main_parameter_input.setObjectName(u"main_parameter_input")
        self.main_parameter_input.setMinimumSize(QSize(150, 28))
        self.main_parameter_input.setMaximumSize(QSize(150, 26))
        self.main_parameter_input.setFrameShape(QFrame.Shape.Box)
        self.main_parameter_input.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)

        self.gridLayout_6.addWidget(self.main_parameter_input, 1, 1, 1, 1)

        self.sub_parameter_label = QLabel(self.guideline_frame)
        self.sub_parameter_label.setObjectName(u"sub_parameter_label")

        self.gridLayout_6.addWidget(self.sub_parameter_label, 1, 2, 1, 1)

        self.sub_parameter_input = QTextEdit(self.guideline_frame)
        self.sub_parameter_input.setObjectName(u"sub_parameter_input")
        self.sub_parameter_input.setMinimumSize(QSize(150, 28))
        self.sub_parameter_input.setMaximumSize(QSize(150, 26))
        self.sub_parameter_input.setFrameShape(QFrame.Shape.Box)
        self.sub_parameter_input.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)

        self.gridLayout_6.addWidget(self.sub_parameter_input, 1, 3, 1, 1)

        self.chloride_label = QLabel(self.guideline_frame)
        self.chloride_label.setObjectName(u"chloride_label")

        self.gridLayout_6.addWidget(self.chloride_label, 2, 0, 1, 1)

        self.chloride_input = QTextEdit(self.guideline_frame)
        self.chloride_input.setObjectName(u"chloride_input")
        self.chloride_input.setMinimumSize(QSize(150, 28))
        self.chloride_input.setMaximumSize(QSize(150, 26))
        self.chloride_input.setFrameShape(QFrame.Shape.Box)
        self.chloride_input.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)

        self.gridLayout_6.addWidget(self.chloride_input, 2, 1, 1, 1)


        self.verticalLayout_7.addWidget(self.guideline_frame)

        self.sample_measurement_tab_widget.addTab(self.guideline, "")
        self.options = QWidget()
        self.options.setObjectName(u"options")
        self.verticalLayout_8 = QVBoxLayout(self.options)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.options_horizontal_layout = QHBoxLayout()
        self.options_horizontal_layout.setObjectName(u"options_horizontal_layout")
        self.moisture_label = QLabel(self.options)
        self.moisture_label.setObjectName(u"moisture_label")
        sizePolicy2.setHeightForWidth(self.moisture_label.sizePolicy().hasHeightForWidth())
        self.moisture_label.setSizePolicy(sizePolicy2)
        self.moisture_label.setMinimumSize(QSize(0, 26))
        self.moisture_label.setMaximumSize(QSize(100, 26))
        self.moisture_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.options_horizontal_layout.addWidget(self.moisture_label)

        self.moisture_combobox = QComboBox(self.options)
        self.moisture_combobox.setObjectName(u"moisture_combobox")
        self.moisture_combobox.setMinimumSize(QSize(150, 28))
        self.moisture_combobox.setMaximumSize(QSize(150, 26))
        self.moisture_combobox.setStyleSheet(u"b")
        self.moisture_combobox.setFrame(True)

        self.options_horizontal_layout.addWidget(self.moisture_combobox)

        self.buffer_range_label = QLabel(self.options)
        self.buffer_range_label.setObjectName(u"buffer_range_label")
        sizePolicy2.setHeightForWidth(self.buffer_range_label.sizePolicy().hasHeightForWidth())
        self.buffer_range_label.setSizePolicy(sizePolicy2)
        self.buffer_range_label.setMinimumSize(QSize(0, 26))
        self.buffer_range_label.setMaximumSize(QSize(100, 26))
        self.buffer_range_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.options_horizontal_layout.addWidget(self.buffer_range_label)

        self.buffer_range_combobox = QComboBox(self.options)
        self.buffer_range_combobox.setObjectName(u"buffer_range_combobox")
        self.buffer_range_combobox.setMinimumSize(QSize(150, 28))
        self.buffer_range_combobox.setMaximumSize(QSize(150, 26))
        self.buffer_range_combobox.setStyleSheet(u"b")
        self.buffer_range_combobox.setFrame(True)

        self.options_horizontal_layout.addWidget(self.buffer_range_combobox)

        self.options_horizontal_layout.setStretch(0, 1)
        self.options_horizontal_layout.setStretch(1, 1)
        self.options_horizontal_layout.setStretch(2, 1)
        self.options_horizontal_layout.setStretch(3, 1)

        self.verticalLayout_8.addLayout(self.options_horizontal_layout)

        self.advanced_parameters_checkbox = QCheckBox(self.options)
        self.advanced_parameters_checkbox.setObjectName(u"advanced_parameters_checkbox")

        self.verticalLayout_8.addWidget(self.advanced_parameters_checkbox)

        self.options_frame = QFrame(self.options)
        self.options_frame.setObjectName(u"options_frame")
        self.options_frame.setEnabled(False)
        self.options_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.options_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.options_frame)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.stabilization_time_label = QLabel(self.options_frame)
        self.stabilization_time_label.setObjectName(u"stabilization_time_label")

        self.horizontalLayout_10.addWidget(self.stabilization_time_label)

        self.StabilizationTimeEditField = QSpinBox(self.options_frame)
        self.StabilizationTimeEditField.setObjectName(u"StabilizationTimeEditField")

        self.horizontalLayout_10.addWidget(self.StabilizationTimeEditField)

        self.baseline_label = QLabel(self.options_frame)
        self.baseline_label.setObjectName(u"baseline_label")
        sizePolicy2.setHeightForWidth(self.baseline_label.sizePolicy().hasHeightForWidth())
        self.baseline_label.setSizePolicy(sizePolicy2)
        self.baseline_label.setMinimumSize(QSize(0, 26))
        self.baseline_label.setMaximumSize(QSize(100, 26))

        self.horizontalLayout_10.addWidget(self.baseline_label)

        self.baseline_combobox = QComboBox(self.options_frame)
        self.baseline_combobox.setObjectName(u"baseline_combobox")
        self.baseline_combobox.setMinimumSize(QSize(150, 28))
        self.baseline_combobox.setMaximumSize(QSize(150, 26))
        self.baseline_combobox.setStyleSheet(u"b")
        self.baseline_combobox.setFrame(True)

        self.horizontalLayout_10.addWidget(self.baseline_combobox)


        self.verticalLayout_8.addWidget(self.options_frame)

        self.sample_measurement_tab_widget.addTab(self.options, "")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.sample_measurement_tab_widget)


        self.verticalLayout_sample_measurement.addWidget(self.sample_measurement_tab_frame)

        self.measurement_frame = QFrame(self.centralwidget)
        self.measurement_frame.setObjectName(u"measurement_frame")
        sizePolicy2.setHeightForWidth(self.measurement_frame.sizePolicy().hasHeightForWidth())
        self.measurement_frame.setSizePolicy(sizePolicy2)
        self.measurement_frame.setStyleSheet(u"b")
        self.measurement_frame.setFrameShape(QFrame.Shape.Box)
        self.measurement_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_7 = QGridLayout(self.measurement_frame)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.measurement_frame_grid_layout = QGridLayout()
        self.measurement_frame_grid_layout.setObjectName(u"measurement_frame_grid_layout")
        self.std_check_button = QPushButton(self.measurement_frame)
        self.std_check_button.setObjectName(u"std_check_button")
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.std_check_button.sizePolicy().hasHeightForWidth())
        self.std_check_button.setSizePolicy(sizePolicy11)
        font6 = QFont()
        font6.setBold(True)
        self.std_check_button.setFont(font6)

        self.measurement_frame_grid_layout.addWidget(self.std_check_button, 0, 0, 1, 1)

        self.average_potential_label = QLabel(self.measurement_frame)
        self.average_potential_label.setObjectName(u"average_potential_label")
        sizePolicy12 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.average_potential_label.sizePolicy().hasHeightForWidth())
        self.average_potential_label.setSizePolicy(sizePolicy12)
        self.average_potential_label.setFont(font6)

        self.measurement_frame_grid_layout.addWidget(self.average_potential_label, 0, 1, 1, 1)

        self.average_potential_input = QTextEdit(self.measurement_frame)
        self.average_potential_input.setObjectName(u"average_potential_input")
        sizePolicy13 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.average_potential_input.sizePolicy().hasHeightForWidth())
        self.average_potential_input.setSizePolicy(sizePolicy13)
        self.average_potential_input.setMinimumSize(QSize(150, 28))
        self.average_potential_input.setMaximumSize(QSize(150, 26))
        self.average_potential_input.setFrameShape(QFrame.Shape.Box)
        self.average_potential_input.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)

        self.measurement_frame_grid_layout.addWidget(self.average_potential_input, 0, 2, 1, 1)

        self.measurement_button = QPushButton(self.measurement_frame)
        self.measurement_button.setObjectName(u"measurement_button")
        sizePolicy14 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy14.setHorizontalStretch(0)
        sizePolicy14.setVerticalStretch(30)
        sizePolicy14.setHeightForWidth(self.measurement_button.sizePolicy().hasHeightForWidth())
        self.measurement_button.setSizePolicy(sizePolicy14)
        self.measurement_button.setMinimumSize(QSize(0, 60))
        self.measurement_button.setFont(font3)

        self.measurement_frame_grid_layout.addWidget(self.measurement_button, 1, 0, 2, 1)

        self.salt_in_liquid_label = QLabel(self.measurement_frame)
        self.salt_in_liquid_label.setObjectName(u"salt_in_liquid_label")
        sizePolicy12.setHeightForWidth(self.salt_in_liquid_label.sizePolicy().hasHeightForWidth())
        self.salt_in_liquid_label.setSizePolicy(sizePolicy12)
        self.salt_in_liquid_label.setFont(font6)

        self.measurement_frame_grid_layout.addWidget(self.salt_in_liquid_label, 1, 1, 1, 1)

        self.salt_in_liquid_input = QTextEdit(self.measurement_frame)
        self.salt_in_liquid_input.setObjectName(u"salt_in_liquid_input")
        sizePolicy13.setHeightForWidth(self.salt_in_liquid_input.sizePolicy().hasHeightForWidth())
        self.salt_in_liquid_input.setSizePolicy(sizePolicy13)
        self.salt_in_liquid_input.setMinimumSize(QSize(150, 28))
        self.salt_in_liquid_input.setMaximumSize(QSize(150, 26))
        self.salt_in_liquid_input.setFrameShape(QFrame.Shape.Box)
        self.salt_in_liquid_input.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)

        self.measurement_frame_grid_layout.addWidget(self.salt_in_liquid_input, 1, 2, 1, 1)

        self.salt_in_ground_label = QLabel(self.measurement_frame)
        self.salt_in_ground_label.setObjectName(u"salt_in_ground_label")
        sizePolicy12.setHeightForWidth(self.salt_in_ground_label.sizePolicy().hasHeightForWidth())
        self.salt_in_ground_label.setSizePolicy(sizePolicy12)
        self.salt_in_ground_label.setFont(font6)

        self.measurement_frame_grid_layout.addWidget(self.salt_in_ground_label, 2, 1, 1, 1)

        self.salt_in_ground_input = QTextEdit(self.measurement_frame)
        self.salt_in_ground_input.setObjectName(u"salt_in_ground_input")
        sizePolicy13.setHeightForWidth(self.salt_in_ground_input.sizePolicy().hasHeightForWidth())
        self.salt_in_ground_input.setSizePolicy(sizePolicy13)
        self.salt_in_ground_input.setMinimumSize(QSize(150, 28))
        self.salt_in_ground_input.setMaximumSize(QSize(150, 26))
        self.salt_in_ground_input.setFrameShape(QFrame.Shape.Box)
        self.salt_in_ground_input.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)

        self.measurement_frame_grid_layout.addWidget(self.salt_in_ground_input, 2, 2, 1, 1)

        self.measurement_circle = QFrame(self.measurement_frame)
        self.measurement_circle.setObjectName(u"measurement_circle")
        sizePolicy15 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy15.setHorizontalStretch(0)
        sizePolicy15.setVerticalStretch(0)
        sizePolicy15.setHeightForWidth(self.measurement_circle.sizePolicy().hasHeightForWidth())
        self.measurement_circle.setSizePolicy(sizePolicy15)
        self.measurement_circle.setMinimumSize(QSize(30, 30))
        self.measurement_circle.setMaximumSize(QSize(30, 30))
        self.measurement_circle.setSizeIncrement(QSize(0, 0))
        self.measurement_circle.setBaseSize(QSize(0, 0))
        self.measurement_circle.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.measurement_circle.setAutoFillBackground(False)
        self.measurement_circle.setStyleSheet(u"border-radius: 15px;  \n"
"    border: 1px solid black;\n"
"    width: 15px;\n"
"    height: 15\n"
"px;\n"
"    background: qradialgradient(\n"
"        cx:0.5,cy:0.3,radius:1\n"
"        stop: 0 rgb(240, 240, 240),  \n"
"        stop: 0.8 rgb(100, 100, 100),\n"
"        stop: 1 rgb(240, 240, 240)   \n"
"    );")
        self.measurement_circle.setFrameShape(QFrame.Shape.NoFrame)
        self.measurement_circle.setFrameShadow(QFrame.Shadow.Raised)

        self.measurement_frame_grid_layout.addWidget(self.measurement_circle, 2, 3, 1, 1)

        self.recalculation_button = QPushButton(self.measurement_frame)
        self.recalculation_button.setObjectName(u"recalculation_button")
        sizePolicy11.setHeightForWidth(self.recalculation_button.sizePolicy().hasHeightForWidth())
        self.recalculation_button.setSizePolicy(sizePolicy11)
        self.recalculation_button.setFont(font6)

        self.measurement_frame_grid_layout.addWidget(self.recalculation_button, 3, 0, 1, 1)

        self.cl_criteria_label = QLabel(self.measurement_frame)
        self.cl_criteria_label.setObjectName(u"cl_criteria_label")
        sizePolicy12.setHeightForWidth(self.cl_criteria_label.sizePolicy().hasHeightForWidth())
        self.cl_criteria_label.setSizePolicy(sizePolicy12)
        font7 = QFont()
        font7.setPointSize(7)
        font7.setBold(True)
        self.cl_criteria_label.setFont(font7)

        self.measurement_frame_grid_layout.addWidget(self.cl_criteria_label, 3, 1, 1, 1)

        self.cl_criteria_input = QTextEdit(self.measurement_frame)
        self.cl_criteria_input.setObjectName(u"cl_criteria_input")
        sizePolicy13.setHeightForWidth(self.cl_criteria_input.sizePolicy().hasHeightForWidth())
        self.cl_criteria_input.setSizePolicy(sizePolicy13)
        self.cl_criteria_input.setMinimumSize(QSize(150, 28))
        self.cl_criteria_input.setMaximumSize(QSize(150, 26))
        self.cl_criteria_input.setFrameShape(QFrame.Shape.Box)
        self.cl_criteria_input.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)

        self.measurement_frame_grid_layout.addWidget(self.cl_criteria_input, 3, 2, 1, 1)

        self.measurement_frame_grid_layout.setRowStretch(0, 1)
        self.measurement_frame_grid_layout.setRowStretch(1, 1)
        self.measurement_frame_grid_layout.setRowStretch(2, 1)
        self.measurement_frame_grid_layout.setRowStretch(3, 1)

        self.gridLayout_7.addLayout(self.measurement_frame_grid_layout, 0, 0, 1, 1)


        self.verticalLayout_sample_measurement.addWidget(self.measurement_frame)


        self.horizontalLayout_middle.addLayout(self.verticalLayout_sample_measurement)

        self.horizontalLayout_middle.setStretch(0, 1)
        self.horizontalLayout_middle.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_middle)

        self.tab_frame = QFrame(self.centralwidget)
        self.tab_frame.setObjectName(u"tab_frame")
        sizePolicy2.setHeightForWidth(self.tab_frame.sizePolicy().hasHeightForWidth())
        self.tab_frame.setSizePolicy(sizePolicy2)
        self.tab_frame.setMinimumSize(QSize(0, 150))
        self.tab_frame.setStyleSheet(u"b")
        self.tab_frame.setFrameShape(QFrame.Shape.Box)
        self.tab_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout_7 = QFormLayout(self.tab_frame)
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.tabWidget = QTabWidget(self.tab_frame)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy6.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy6)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet(u"")
        self.check = QWidget()
        self.check.setObjectName(u"check")
        self.tabWidget.addTab(self.check, "")
        self.date = QWidget()
        self.date.setObjectName(u"date")
        self.tabWidget.addTab(self.date, "")
        self.project_name = QWidget()
        self.project_name.setObjectName(u"project_name")
        self.tabWidget.addTab(self.project_name, "")
        self.sample_no = QWidget()
        self.sample_no.setObjectName(u"sample_no")
        self.tabWidget.addTab(self.sample_no, "")
        self.sample_id = QWidget()
        self.sample_id.setObjectName(u"sample_id")
        self.tabWidget.addTab(self.sample_id, "")
        self.replication = QWidget()
        self.replication.setObjectName(u"replication")
        self.tabWidget.addTab(self.replication, "")
        self.chloride_in_soil = QWidget()
        self.chloride_in_soil.setObjectName(u"chloride_in_soil")
        self.tabWidget.addTab(self.chloride_in_soil, "")
        self.chloride_in_liquid = QWidget()
        self.chloride_in_liquid.setObjectName(u"chloride_in_liquid")
        self.tabWidget.addTab(self.chloride_in_liquid, "")
        self.potential = QWidget()
        self.potential.setObjectName(u"potential")
        self.tabWidget.addTab(self.potential, "")
        self.cl_criteria = QWidget()
        self.cl_criteria.setObjectName(u"cl_criteria")
        self.tabWidget.addTab(self.cl_criteria, "")

        self.formLayout_7.setWidget(0, QFormLayout.ItemRole.SpanningRole, self.tabWidget)


        self.verticalLayout_2.addWidget(self.tab_frame)

        self.horizontalLayout_bottom = QHBoxLayout()
        self.horizontalLayout_bottom.setObjectName(u"horizontalLayout_bottom")
        self.measurement_range_label = QLabel(self.centralwidget)
        self.measurement_range_label.setObjectName(u"measurement_range_label")
        sizePolicy16 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy16.setHorizontalStretch(0)
        sizePolicy16.setVerticalStretch(0)
        sizePolicy16.setHeightForWidth(self.measurement_range_label.sizePolicy().hasHeightForWidth())
        self.measurement_range_label.setSizePolicy(sizePolicy16)
        self.measurement_range_label.setFont(font6)
        self.measurement_range_label.setStyleSheet(u"background: transparent")

        self.horizontalLayout_bottom.addWidget(self.measurement_range_label)

        self.auto_file_naming_checkbox = QCheckBox(self.centralwidget)
        self.auto_file_naming_checkbox.setObjectName(u"auto_file_naming_checkbox")
        sizePolicy17 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy17.setHorizontalStretch(0)
        sizePolicy17.setVerticalStretch(0)
        sizePolicy17.setHeightForWidth(self.auto_file_naming_checkbox.sizePolicy().hasHeightForWidth())
        self.auto_file_naming_checkbox.setSizePolicy(sizePolicy17)
        self.auto_file_naming_checkbox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.auto_file_naming_checkbox.setStyleSheet(u"background: transparent\n"
"")

        self.horizontalLayout_bottom.addWidget(self.auto_file_naming_checkbox)

        self.file_name_label = QLabel(self.centralwidget)
        self.file_name_label.setObjectName(u"file_name_label")
        sizePolicy9.setHeightForWidth(self.file_name_label.sizePolicy().hasHeightForWidth())
        self.file_name_label.setSizePolicy(sizePolicy9)
        self.file_name_label.setFont(font4)
        self.file_name_label.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.file_name_label.setStyleSheet(u"background: transparent")

        self.horizontalLayout_bottom.addWidget(self.file_name_label)

        self.file_name_input = QTextEdit(self.centralwidget)
        self.file_name_input.setObjectName(u"file_name_input")
        self.file_name_input.setEnabled(False)
        self.file_name_input.setMinimumSize(QSize(150, 28))
        self.file_name_input.setMaximumSize(QSize(150, 26))
        self.file_name_input.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.file_name_input.setAutoFillBackground(False)
        self.file_name_input.setFrameShape(QFrame.Shape.Box)
        self.file_name_input.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)

        self.horizontalLayout_bottom.addWidget(self.file_name_input)

        self.export_data_button = QPushButton(self.centralwidget)
        self.export_data_button.setObjectName(u"export_data_button")
        sizePolicy18 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy18.setHorizontalStretch(0)
        sizePolicy18.setVerticalStretch(0)
        sizePolicy18.setHeightForWidth(self.export_data_button.sizePolicy().hasHeightForWidth())
        self.export_data_button.setSizePolicy(sizePolicy18)
        self.export_data_button.setFont(font3)

        self.horizontalLayout_bottom.addWidget(self.export_data_button)

        self.horizontalLayout_bottom.setStretch(0, 1)
        self.horizontalLayout_bottom.setStretch(4, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_bottom)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.sample_measurement_tab_widget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(7)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"AISCT\u00ae SAL ", None))
        self.logo.setText("")
        self.system_check_label.setText(QCoreApplication.translate("MainWindow", u"1. System Check/Calibration", None))
        self.btn_system_connect.setText(QCoreApplication.translate("MainWindow", u"System \n"
"Connection", None))
        self.lbl_connection_status.setText(QCoreApplication.translate("MainWindow", u"Connection", None))
        self.lbl_system_note.setText(QCoreApplication.translate("MainWindow", u"System\n"
"Note", None))
        self.lbl_note_status_tag.setText("")
        self.txt_system_note.setText("")
        self.lbl_progress_status.setText("")
        self.potential_label.setText(QCoreApplication.translate("MainWindow", u"Potential (mV)", None))
        self.cl_conc_label.setText(QCoreApplication.translate("MainWindow", u"Cl Conc. in Liquid (mg/L)", None))
        self.r_squared_label.setText(QCoreApplication.translate("MainWindow", u"R squared:", None))
        self.r_squared_label_2.setText("")
        self.refresh_plot_button.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.sample_measurement_label.setText(QCoreApplication.translate("MainWindow", u"2. Sample Measurement", None))
        self.reset_button_measurement.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.apply_button_measurement.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.STD5000MeasurementButton.setText(QCoreApplication.translate("MainWindow", u"Measurement", None))
        self.STD100Measurement.setText(QCoreApplication.translate("MainWindow", u"STD 100 ppm", None))
        self.STD10MeasurementButton.setText(QCoreApplication.translate("MainWindow", u"Measurement", None))
        self.STD100MeasurementButton.setText(QCoreApplication.translate("MainWindow", u"Measurement", None))
        self.STD1000Measurement.setText(QCoreApplication.translate("MainWindow", u"STD 1000 ppm", None))
        self.STD5000Measurement.setText(QCoreApplication.translate("MainWindow", u"STD 5000 ppm", None))
        self.STD10Measurement.setText(QCoreApplication.translate("MainWindow", u"STD 10 ppm", None))
        self.STD1000MeasurementButton.setText(QCoreApplication.translate("MainWindow", u"Measurement", None))
        self.CalibrationCurveFittingButton.setText(QCoreApplication.translate("MainWindow", u"Calibration Curve Fitting", None))
        self.sample_measurement_tab_widget.setTabText(self.sample_measurement_tab_widget.indexOf(self.calibration), QCoreApplication.translate("MainWindow", u"Calibration", None))
        self.project_name_label.setText(QCoreApplication.translate("MainWindow", u"Project Name", None))
        self.sample_no_label.setText(QCoreApplication.translate("MainWindow", u"Sample No", None))
        self.sample_id_label.setText(QCoreApplication.translate("MainWindow", u"Sample ID", None))
        self.replication_label.setText(QCoreApplication.translate("MainWindow", u"Replication", None))
        self.auto_sample_naming_checkbox.setText(QCoreApplication.translate("MainWindow", u"Auto Sample Naming", None))
        self.sample_type_label.setText(QCoreApplication.translate("MainWindow", u"Sample Type", None))
        self.bore_hole_id_label.setText(QCoreApplication.translate("MainWindow", u"Bore Hole ID", None))
        self.bore_hole_no_label.setText(QCoreApplication.translate("MainWindow", u"Bore Hole No", None))
        self.top_depth_label.setText(QCoreApplication.translate("MainWindow", u"Top Depth (m)", None))
        self.bottom_depth_label.setText(QCoreApplication.translate("MainWindow", u"Bottom Depth (m)", None))
        self.sample_measurement_tab_widget.setTabText(self.sample_measurement_tab_widget.indexOf(self.sample_information), QCoreApplication.translate("MainWindow", u"Sample Information", None))
        self.single_guideline_checkbox.setText(QCoreApplication.translate("MainWindow", u"Single Guideline", None))
        self.multiple_guideline_checkbox.setText(QCoreApplication.translate("MainWindow", u"Multiple Guideline", None))
        self.reset_button_guideline.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.apply_button_guideline.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.guideline_type_label.setText(QCoreApplication.translate("MainWindow", u"Guideline Type", None))
        self.main_parameter_label.setText(QCoreApplication.translate("MainWindow", u"Main Parameter", None))
        self.sub_parameter_label.setText(QCoreApplication.translate("MainWindow", u"Sub Parameter", None))
        self.chloride_label.setText(QCoreApplication.translate("MainWindow", u"Chloride (mg/kg)", None))
        self.sample_measurement_tab_widget.setTabText(self.sample_measurement_tab_widget.indexOf(self.guideline), QCoreApplication.translate("MainWindow", u"Guideline", None))
        self.moisture_label.setText(QCoreApplication.translate("MainWindow", u"Moisture (%)", None))
        self.buffer_range_label.setText(QCoreApplication.translate("MainWindow", u"Buffer (%)", None))
        self.advanced_parameters_checkbox.setText(QCoreApplication.translate("MainWindow", u"Advanced Parameters", None))
        self.stabilization_time_label.setText(QCoreApplication.translate("MainWindow", u"Stabilization Time (s)", None))
        self.baseline_label.setText(QCoreApplication.translate("MainWindow", u"Baseline", None))
        self.sample_measurement_tab_widget.setTabText(self.sample_measurement_tab_widget.indexOf(self.options), QCoreApplication.translate("MainWindow", u"Options", None))
        self.std_check_button.setText(QCoreApplication.translate("MainWindow", u"STD check", None))
        self.average_potential_label.setText(QCoreApplication.translate("MainWindow", u"Average Potential (mV)", None))
        self.measurement_button.setText(QCoreApplication.translate("MainWindow", u"Measurement", None))
        self.salt_in_liquid_label.setText(QCoreApplication.translate("MainWindow", u"Cl Conc. inExtract(mg/L)", None))
        self.salt_in_ground_label.setText(QCoreApplication.translate("MainWindow", u"Cl Conc. in Soil (mg/kg)", None))
        self.recalculation_button.setText(QCoreApplication.translate("MainWindow", u"Recalculation", None))
        self.cl_criteria_label.setText(QCoreApplication.translate("MainWindow", u"Cl Criteria (mg/kg)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.check), QCoreApplication.translate("MainWindow", u"Check", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.date), QCoreApplication.translate("MainWindow", u"Date", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.project_name), QCoreApplication.translate("MainWindow", u"Project Name", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sample_no), QCoreApplication.translate("MainWindow", u"Sample No", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sample_id), QCoreApplication.translate("MainWindow", u"Sample ID", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.replication), QCoreApplication.translate("MainWindow", u"Replication", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.chloride_in_soil), QCoreApplication.translate("MainWindow", u"Chloride in Soil (mg/kg)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.chloride_in_liquid), QCoreApplication.translate("MainWindow", u"Chloride in Liquid (mg/L)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.potential), QCoreApplication.translate("MainWindow", u"Potential (mV)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.cl_criteria), QCoreApplication.translate("MainWindow", u"Cl Criteria (mg/kg)", None))
        self.measurement_range_label.setText(QCoreApplication.translate("MainWindow", u"*Measurement Range (mg/kg): 50~5,000, N.D. = non detective, M.C. = meet criteria", None))
        self.auto_file_naming_checkbox.setText(QCoreApplication.translate("MainWindow", u"Auto File Naming", None))
        self.file_name_label.setText(QCoreApplication.translate("MainWindow", u"File Name:", None))
        self.export_data_button.setText(QCoreApplication.translate("MainWindow", u"Export Data", None))
    # retranslateUi

