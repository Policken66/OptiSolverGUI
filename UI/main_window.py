# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.3
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QGroupBox, QHBoxLayout,
    QLabel, QMainWindow, QMdiArea, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)

from Widgets.SubWindow.sub_window_base import SubWindowBase

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1158, 838)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.mdiArea_toolbox = QMdiArea(self.centralwidget)
        self.mdiArea_toolbox.setObjectName(u"mdiArea_toolbox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mdiArea_toolbox.sizePolicy().hasHeightForWidth())
        self.mdiArea_toolbox.setSizePolicy(sizePolicy)
        self.mdiArea_toolbox.setMaximumSize(QSize(16777215, 75))
        self.mdiArea_toolbox.setViewMode(QMdiArea.ViewMode.TabbedView)
        self.mdiArea_toolbox.setTabsMovable(True)
        self.subWindow_parameters_toolbox = QWidget()
        self.subWindow_parameters_toolbox.setObjectName(u"subWindow_parameters_toolbox")
        self.horizontalLayout = QHBoxLayout(self.subWindow_parameters_toolbox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_geometric_parameters = QPushButton(self.subWindow_parameters_toolbox)
        self.pushButton_geometric_parameters.setObjectName(u"pushButton_geometric_parameters")

        self.horizontalLayout.addWidget(self.pushButton_geometric_parameters)

        self.pushButton_physical_mechanical_parameters = QPushButton(self.subWindow_parameters_toolbox)
        self.pushButton_physical_mechanical_parameters.setObjectName(u"pushButton_physical_mechanical_parameters")

        self.horizontalLayout.addWidget(self.pushButton_physical_mechanical_parameters)

        self.pushButton_edge_structure_parameters = QPushButton(self.subWindow_parameters_toolbox)
        self.pushButton_edge_structure_parameters.setObjectName(u"pushButton_edge_structure_parameters")

        self.horizontalLayout.addWidget(self.pushButton_edge_structure_parameters)

        self.pushButton_construction_parameters = QPushButton(self.subWindow_parameters_toolbox)
        self.pushButton_construction_parameters.setObjectName(u"pushButton_construction_parameters")

        self.horizontalLayout.addWidget(self.pushButton_construction_parameters)

        self.pushButton_calculated_peremeters = QPushButton(self.subWindow_parameters_toolbox)
        self.pushButton_calculated_peremeters.setObjectName(u"pushButton_calculated_peremeters")

        self.horizontalLayout.addWidget(self.pushButton_calculated_peremeters)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.mdiArea_toolbox.addSubWindow(self.subWindow_parameters_toolbox)
        self.subwindow_4 = QWidget()
        self.subwindow_4.setObjectName(u"subwindow_4")
        self.mdiArea_toolbox.addSubWindow(self.subwindow_4)
        self.subwindow_5 = QWidget()
        self.subwindow_5.setObjectName(u"subwindow_5")
        self.mdiArea_toolbox.addSubWindow(self.subwindow_5)

        self.verticalLayout.addWidget(self.mdiArea_toolbox)

        self.mdiArea = QMdiArea(self.centralwidget)
        self.mdiArea.setObjectName(u"mdiArea")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mdiArea.sizePolicy().hasHeightForWidth())
        self.mdiArea.setSizePolicy(sizePolicy1)
        self.mdiArea.setViewMode(QMdiArea.ViewMode.SubWindowView)
        self.mdiArea.setDocumentMode(True)
        self.mdiArea.setTabsClosable(False)
        self.subWindow_geometric_parameters = SubWindowBase()
        self.subWindow_geometric_parameters.setObjectName(u"subWindow_geometric_parameters")
        self.verticalLayout_15 = QVBoxLayout(self.subWindow_geometric_parameters)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_R1 = QLabel(self.subWindow_geometric_parameters)
        self.label_R1.setObjectName(u"label_R1")

        self.horizontalLayout_2.addWidget(self.label_R1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.doubleSpinBox_input_R1 = QDoubleSpinBox(self.subWindow_geometric_parameters)
        self.doubleSpinBox_input_R1.setObjectName(u"doubleSpinBox_input_R1")

        self.horizontalLayout_2.addWidget(self.doubleSpinBox_input_R1)


        self.verticalLayout_15.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_R2 = QLabel(self.subWindow_geometric_parameters)
        self.label_R2.setObjectName(u"label_R2")

        self.horizontalLayout_3.addWidget(self.label_R2)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.doubleSpinBox_input_R2 = QDoubleSpinBox(self.subWindow_geometric_parameters)
        self.doubleSpinBox_input_R2.setObjectName(u"doubleSpinBox_input_R2")

        self.horizontalLayout_3.addWidget(self.doubleSpinBox_input_R2)


        self.verticalLayout_15.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_H = QLabel(self.subWindow_geometric_parameters)
        self.label_H.setObjectName(u"label_H")

        self.horizontalLayout_4.addWidget(self.label_H)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)

        self.doubleSpinBox_input_H = QDoubleSpinBox(self.subWindow_geometric_parameters)
        self.doubleSpinBox_input_H.setObjectName(u"doubleSpinBox_input_H")

        self.horizontalLayout_4.addWidget(self.doubleSpinBox_input_H)


        self.verticalLayout_15.addLayout(self.horizontalLayout_4)

        self.label_geometric_params_model = QLabel(self.subWindow_geometric_parameters)
        self.label_geometric_params_model.setObjectName(u"label_geometric_params_model")

        self.verticalLayout_15.addWidget(self.label_geometric_params_model)

        self.mdiArea.addSubWindow(self.subWindow_geometric_parameters)
        self.subWindow_edge_structure_parameters = SubWindowBase()
        self.subWindow_edge_structure_parameters.setObjectName(u"subWindow_edge_structure_parameters")
        self.verticalLayout_11 = QVBoxLayout(self.subWindow_edge_structure_parameters)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.groupBox_4 = QGroupBox(self.subWindow_edge_structure_parameters)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_a_sp = QLabel(self.groupBox_4)
        self.label_a_sp.setObjectName(u"label_a_sp")

        self.horizontalLayout_7.addWidget(self.label_a_sp)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_7)

        self.doubleSpinBox_input_thinkness_spiral = QDoubleSpinBox(self.groupBox_4)
        self.doubleSpinBox_input_thinkness_spiral.setObjectName(u"doubleSpinBox_input_thinkness_spiral")

        self.horizontalLayout_7.addWidget(self.doubleSpinBox_input_thinkness_spiral)


        self.verticalLayout_10.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_b_sp = QLabel(self.groupBox_4)
        self.label_b_sp.setObjectName(u"label_b_sp")

        self.horizontalLayout_8.addWidget(self.label_b_sp)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_8)

        self.doubleSpinBox_input_height_spiral = QDoubleSpinBox(self.groupBox_4)
        self.doubleSpinBox_input_height_spiral.setObjectName(u"doubleSpinBox_input_height_spiral")

        self.horizontalLayout_8.addWidget(self.doubleSpinBox_input_height_spiral)


        self.verticalLayout_10.addLayout(self.horizontalLayout_8)


        self.verticalLayout_11.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.subWindow_edge_structure_parameters)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_18 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_a_col = QLabel(self.groupBox_5)
        self.label_a_col.setObjectName(u"label_a_col")

        self.horizontalLayout_9.addWidget(self.label_a_col)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_9)

        self.doubleSpinBox_input_thinkness_ring = QDoubleSpinBox(self.groupBox_5)
        self.doubleSpinBox_input_thinkness_ring.setObjectName(u"doubleSpinBox_input_thinkness_ring")

        self.horizontalLayout_9.addWidget(self.doubleSpinBox_input_thinkness_ring)


        self.verticalLayout_18.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_b_col = QLabel(self.groupBox_5)
        self.label_b_col.setObjectName(u"label_b_col")

        self.horizontalLayout_10.addWidget(self.label_b_col)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_10)

        self.doubleSpinBox_input_height_ring = QDoubleSpinBox(self.groupBox_5)
        self.doubleSpinBox_input_height_ring.setObjectName(u"doubleSpinBox_input_height_ring")

        self.horizontalLayout_10.addWidget(self.doubleSpinBox_input_height_ring)


        self.verticalLayout_18.addLayout(self.horizontalLayout_10)


        self.verticalLayout_11.addWidget(self.groupBox_5)

        self.groupBox_6 = QGroupBox(self.subWindow_edge_structure_parameters)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_19 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_a_shp = QLabel(self.groupBox_6)
        self.label_a_shp.setObjectName(u"label_a_shp")

        self.horizontalLayout_11.addWidget(self.label_a_shp)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_11)

        self.doubleSpinBox_input_thinkness_shp = QDoubleSpinBox(self.groupBox_6)
        self.doubleSpinBox_input_thinkness_shp.setObjectName(u"doubleSpinBox_input_thinkness_shp")

        self.horizontalLayout_11.addWidget(self.doubleSpinBox_input_thinkness_shp)


        self.verticalLayout_19.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_b_shp = QLabel(self.groupBox_6)
        self.label_b_shp.setObjectName(u"label_b_shp")

        self.horizontalLayout_12.addWidget(self.label_b_shp)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_12)

        self.doubleSpinBox_input_height_shp = QDoubleSpinBox(self.groupBox_6)
        self.doubleSpinBox_input_height_shp.setObjectName(u"doubleSpinBox_input_height_shp")

        self.horizontalLayout_12.addWidget(self.doubleSpinBox_input_height_shp)


        self.verticalLayout_19.addLayout(self.horizontalLayout_12)


        self.verticalLayout_11.addWidget(self.groupBox_6)

        self.mdiArea.addSubWindow(self.subWindow_edge_structure_parameters)
        self.subWindow_physical_mechanical_parameters = SubWindowBase()
        self.subWindow_physical_mechanical_parameters.setObjectName(u"subWindow_physical_mechanical_parameters")
        self.horizontalLayout_6 = QHBoxLayout(self.subWindow_physical_mechanical_parameters)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.groupBox_7 = QGroupBox(self.subWindow_physical_mechanical_parameters)
        self.groupBox_7.setObjectName(u"groupBox_7")
        sizePolicy1.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy1)
        self.groupBox_7.setMinimumSize(QSize(0, 0))
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_E_x_spiral = QLabel(self.groupBox_7)
        self.label_E_x_spiral.setObjectName(u"label_E_x_spiral")

        self.horizontalLayout_13.addWidget(self.label_E_x_spiral)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_13)

        self.doubleSpinBox_input_E_x_spiral = QDoubleSpinBox(self.groupBox_7)
        self.doubleSpinBox_input_E_x_spiral.setObjectName(u"doubleSpinBox_input_E_x_spiral")

        self.horizontalLayout_13.addWidget(self.doubleSpinBox_input_E_x_spiral)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_E_y_spiral = QLabel(self.groupBox_7)
        self.label_E_y_spiral.setObjectName(u"label_E_y_spiral")

        self.horizontalLayout_14.addWidget(self.label_E_y_spiral)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_14)

        self.doubleSpinBox_input_E_y_spiral = QDoubleSpinBox(self.groupBox_7)
        self.doubleSpinBox_input_E_y_spiral.setObjectName(u"doubleSpinBox_input_E_y_spiral")

        self.horizontalLayout_14.addWidget(self.doubleSpinBox_input_E_y_spiral)


        self.verticalLayout_5.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_E_z_spiral = QLabel(self.groupBox_7)
        self.label_E_z_spiral.setObjectName(u"label_E_z_spiral")

        self.horizontalLayout_15.addWidget(self.label_E_z_spiral)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_15)

        self.doubleSpinBox_input_E_z_spiral = QDoubleSpinBox(self.groupBox_7)
        self.doubleSpinBox_input_E_z_spiral.setObjectName(u"doubleSpinBox_input_E_z_spiral")

        self.horizontalLayout_15.addWidget(self.doubleSpinBox_input_E_z_spiral)


        self.verticalLayout_5.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_G_xy_spiral = QLabel(self.groupBox_7)
        self.label_G_xy_spiral.setObjectName(u"label_G_xy_spiral")

        self.horizontalLayout_16.addWidget(self.label_G_xy_spiral)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_16)

        self.doubleSpinBox_input_G_xy_spiral = QDoubleSpinBox(self.groupBox_7)
        self.doubleSpinBox_input_G_xy_spiral.setObjectName(u"doubleSpinBox_input_G_xy_spiral")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_input_G_xy_spiral.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_input_G_xy_spiral.setSizePolicy(sizePolicy2)

        self.horizontalLayout_16.addWidget(self.doubleSpinBox_input_G_xy_spiral)


        self.verticalLayout_5.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_G_yz_spiral = QLabel(self.groupBox_7)
        self.label_G_yz_spiral.setObjectName(u"label_G_yz_spiral")

        self.horizontalLayout_17.addWidget(self.label_G_yz_spiral)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_17)

        self.doubleSpinBox_input_G_yz_spiral = QDoubleSpinBox(self.groupBox_7)
        self.doubleSpinBox_input_G_yz_spiral.setObjectName(u"doubleSpinBox_input_G_yz_spiral")

        self.horizontalLayout_17.addWidget(self.doubleSpinBox_input_G_yz_spiral)


        self.verticalLayout_5.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_G_xz_spiral = QLabel(self.groupBox_7)
        self.label_G_xz_spiral.setObjectName(u"label_G_xz_spiral")

        self.horizontalLayout_18.addWidget(self.label_G_xz_spiral)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_18)

        self.doubleSpinBox_input_G_xz_spiral = QDoubleSpinBox(self.groupBox_7)
        self.doubleSpinBox_input_G_xz_spiral.setObjectName(u"doubleSpinBox_input_G_xz_spiral")

        self.horizontalLayout_18.addWidget(self.doubleSpinBox_input_G_xz_spiral)


        self.verticalLayout_5.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_v_spiral = QLabel(self.groupBox_7)
        self.label_v_spiral.setObjectName(u"label_v_spiral")

        self.horizontalLayout_19.addWidget(self.label_v_spiral)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_19)

        self.doubleSpinBox_input_v_spiral = QDoubleSpinBox(self.groupBox_7)
        self.doubleSpinBox_input_v_spiral.setObjectName(u"doubleSpinBox_input_v_spiral")

        self.horizontalLayout_19.addWidget(self.doubleSpinBox_input_v_spiral)


        self.verticalLayout_5.addLayout(self.horizontalLayout_19)


        self.verticalLayout_12.addLayout(self.verticalLayout_5)


        self.horizontalLayout_6.addWidget(self.groupBox_7)

        self.groupBox_9 = QGroupBox(self.subWindow_physical_mechanical_parameters)
        self.groupBox_9.setObjectName(u"groupBox_9")
        sizePolicy.setHeightForWidth(self.groupBox_9.sizePolicy().hasHeightForWidth())
        self.groupBox_9.setSizePolicy(sizePolicy)
        self.verticalLayout_13 = QVBoxLayout(self.groupBox_9)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_E_x_shp = QLabel(self.groupBox_9)
        self.label_E_x_shp.setObjectName(u"label_E_x_shp")

        self.horizontalLayout_27.addWidget(self.label_E_x_shp)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_27)

        self.doubleSpinBox_input_E_x_shp = QDoubleSpinBox(self.groupBox_9)
        self.doubleSpinBox_input_E_x_shp.setObjectName(u"doubleSpinBox_input_E_x_shp")

        self.horizontalLayout_27.addWidget(self.doubleSpinBox_input_E_x_shp)


        self.verticalLayout_3.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_E_y_shp = QLabel(self.groupBox_9)
        self.label_E_y_shp.setObjectName(u"label_E_y_shp")

        self.horizontalLayout_28.addWidget(self.label_E_y_shp)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_28)

        self.doubleSpinBox_input_E_y_shp = QDoubleSpinBox(self.groupBox_9)
        self.doubleSpinBox_input_E_y_shp.setObjectName(u"doubleSpinBox_input_E_y_shp")

        self.horizontalLayout_28.addWidget(self.doubleSpinBox_input_E_y_shp)


        self.verticalLayout_3.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_E_z_shp = QLabel(self.groupBox_9)
        self.label_E_z_shp.setObjectName(u"label_E_z_shp")

        self.horizontalLayout_29.addWidget(self.label_E_z_shp)

        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_29)

        self.doubleSpinBox_input_E_z_shp = QDoubleSpinBox(self.groupBox_9)
        self.doubleSpinBox_input_E_z_shp.setObjectName(u"doubleSpinBox_input_E_z_shp")

        self.horizontalLayout_29.addWidget(self.doubleSpinBox_input_E_z_shp)


        self.verticalLayout_3.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_G_xy_shp = QLabel(self.groupBox_9)
        self.label_G_xy_shp.setObjectName(u"label_G_xy_shp")

        self.horizontalLayout_30.addWidget(self.label_G_xy_shp)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_30)

        self.doubleSpinBox_input_G_xy_shp = QDoubleSpinBox(self.groupBox_9)
        self.doubleSpinBox_input_G_xy_shp.setObjectName(u"doubleSpinBox_input_G_xy_shp")

        self.horizontalLayout_30.addWidget(self.doubleSpinBox_input_G_xy_shp)


        self.verticalLayout_3.addLayout(self.horizontalLayout_30)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_G_yz_shp = QLabel(self.groupBox_9)
        self.label_G_yz_shp.setObjectName(u"label_G_yz_shp")

        self.horizontalLayout_31.addWidget(self.label_G_yz_shp)

        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_31)

        self.doubleSpinBox_input_G_yz_shp = QDoubleSpinBox(self.groupBox_9)
        self.doubleSpinBox_input_G_yz_shp.setObjectName(u"doubleSpinBox_input_G_yz_shp")

        self.horizontalLayout_31.addWidget(self.doubleSpinBox_input_G_yz_shp)


        self.verticalLayout_3.addLayout(self.horizontalLayout_31)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_G_xz_shp = QLabel(self.groupBox_9)
        self.label_G_xz_shp.setObjectName(u"label_G_xz_shp")

        self.horizontalLayout_32.addWidget(self.label_G_xz_shp)

        self.horizontalSpacer_33 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_33)

        self.doubleSpinBox_input_G_xz_shp = QDoubleSpinBox(self.groupBox_9)
        self.doubleSpinBox_input_G_xz_shp.setObjectName(u"doubleSpinBox_input_G_xz_shp")

        self.horizontalLayout_32.addWidget(self.doubleSpinBox_input_G_xz_shp)


        self.verticalLayout_3.addLayout(self.horizontalLayout_32)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_v_shp = QLabel(self.groupBox_9)
        self.label_v_shp.setObjectName(u"label_v_shp")

        self.horizontalLayout_33.addWidget(self.label_v_shp)

        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_32)

        self.doubleSpinBox_input_v_shp = QDoubleSpinBox(self.groupBox_9)
        self.doubleSpinBox_input_v_shp.setObjectName(u"doubleSpinBox_input_v_shp")

        self.horizontalLayout_33.addWidget(self.doubleSpinBox_input_v_shp)


        self.verticalLayout_3.addLayout(self.horizontalLayout_33)


        self.verticalLayout_13.addLayout(self.verticalLayout_3)


        self.horizontalLayout_6.addWidget(self.groupBox_9)

        self.groupBox_8 = QGroupBox(self.subWindow_physical_mechanical_parameters)
        self.groupBox_8.setObjectName(u"groupBox_8")
        sizePolicy.setHeightForWidth(self.groupBox_8.sizePolicy().hasHeightForWidth())
        self.groupBox_8.setSizePolicy(sizePolicy)
        self.verticalLayout_16 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_E_x_ring = QLabel(self.groupBox_8)
        self.label_E_x_ring.setObjectName(u"label_E_x_ring")

        self.horizontalLayout_20.addWidget(self.label_E_x_ring)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_20)

        self.doubleSpinBox_input_E_x_ring = QDoubleSpinBox(self.groupBox_8)
        self.doubleSpinBox_input_E_x_ring.setObjectName(u"doubleSpinBox_input_E_x_ring")

        self.horizontalLayout_20.addWidget(self.doubleSpinBox_input_E_x_ring)


        self.verticalLayout_4.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_E_y_ring = QLabel(self.groupBox_8)
        self.label_E_y_ring.setObjectName(u"label_E_y_ring")

        self.horizontalLayout_21.addWidget(self.label_E_y_ring)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_21)

        self.doubleSpinBox_input_E_y_ring = QDoubleSpinBox(self.groupBox_8)
        self.doubleSpinBox_input_E_y_ring.setObjectName(u"doubleSpinBox_input_E_y_ring")

        self.horizontalLayout_21.addWidget(self.doubleSpinBox_input_E_y_ring)


        self.verticalLayout_4.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_E_z_ring = QLabel(self.groupBox_8)
        self.label_E_z_ring.setObjectName(u"label_E_z_ring")

        self.horizontalLayout_22.addWidget(self.label_E_z_ring)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_22)

        self.doubleSpinBox_input_E_z_ring = QDoubleSpinBox(self.groupBox_8)
        self.doubleSpinBox_input_E_z_ring.setObjectName(u"doubleSpinBox_input_E_z_ring")

        self.horizontalLayout_22.addWidget(self.doubleSpinBox_input_E_z_ring)


        self.verticalLayout_4.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_G_xy_ring = QLabel(self.groupBox_8)
        self.label_G_xy_ring.setObjectName(u"label_G_xy_ring")

        self.horizontalLayout_23.addWidget(self.label_G_xy_ring)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_23)

        self.doubleSpinBox_input_G_xy_ring = QDoubleSpinBox(self.groupBox_8)
        self.doubleSpinBox_input_G_xy_ring.setObjectName(u"doubleSpinBox_input_G_xy_ring")

        self.horizontalLayout_23.addWidget(self.doubleSpinBox_input_G_xy_ring)


        self.verticalLayout_4.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_G_yz_ring = QLabel(self.groupBox_8)
        self.label_G_yz_ring.setObjectName(u"label_G_yz_ring")

        self.horizontalLayout_24.addWidget(self.label_G_yz_ring)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_24)

        self.doubleSpinBox_input_G_yz_ring = QDoubleSpinBox(self.groupBox_8)
        self.doubleSpinBox_input_G_yz_ring.setObjectName(u"doubleSpinBox_input_G_yz_ring")

        self.horizontalLayout_24.addWidget(self.doubleSpinBox_input_G_yz_ring)


        self.verticalLayout_4.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_G_xz_ring = QLabel(self.groupBox_8)
        self.label_G_xz_ring.setObjectName(u"label_G_xz_ring")

        self.horizontalLayout_25.addWidget(self.label_G_xz_ring)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_25)

        self.doubleSpinBox_input_G_xz_ring = QDoubleSpinBox(self.groupBox_8)
        self.doubleSpinBox_input_G_xz_ring.setObjectName(u"doubleSpinBox_input_G_xz_ring")

        self.horizontalLayout_25.addWidget(self.doubleSpinBox_input_G_xz_ring)


        self.verticalLayout_4.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_v_ring = QLabel(self.groupBox_8)
        self.label_v_ring.setObjectName(u"label_v_ring")

        self.horizontalLayout_26.addWidget(self.label_v_ring)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_26)

        self.doubleSpinBox_input_v_ring = QDoubleSpinBox(self.groupBox_8)
        self.doubleSpinBox_input_v_ring.setObjectName(u"doubleSpinBox_input_v_ring")

        self.horizontalLayout_26.addWidget(self.doubleSpinBox_input_v_ring)


        self.verticalLayout_4.addLayout(self.horizontalLayout_26)


        self.verticalLayout_16.addLayout(self.verticalLayout_4)


        self.horizontalLayout_6.addWidget(self.groupBox_8)

        self.mdiArea.addSubWindow(self.subWindow_physical_mechanical_parameters)
        self.subWindow_calculated_parameters = SubWindowBase()
        self.subWindow_calculated_parameters.setObjectName(u"subWindow_calculated_parameters")
        self.verticalLayout_7 = QVBoxLayout(self.subWindow_calculated_parameters)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.label_M1 = QLabel(self.subWindow_calculated_parameters)
        self.label_M1.setObjectName(u"label_M1")

        self.horizontalLayout_41.addWidget(self.label_M1)

        self.horizontalSpacer_40 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_41.addItem(self.horizontalSpacer_40)

        self.label_value_M_1 = QLabel(self.subWindow_calculated_parameters)
        self.label_value_M_1.setObjectName(u"label_value_M_1")

        self.horizontalLayout_41.addWidget(self.label_value_M_1)


        self.verticalLayout_2.addLayout(self.horizontalLayout_41)

        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.label_M2 = QLabel(self.subWindow_calculated_parameters)
        self.label_M2.setObjectName(u"label_M2")

        self.horizontalLayout_42.addWidget(self.label_M2)

        self.horizontalSpacer_41 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_42.addItem(self.horizontalSpacer_41)

        self.label_value_M_2 = QLabel(self.subWindow_calculated_parameters)
        self.label_value_M_2.setObjectName(u"label_value_M_2")

        self.horizontalLayout_42.addWidget(self.label_value_M_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_42)

        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.label_M3 = QLabel(self.subWindow_calculated_parameters)
        self.label_M3.setObjectName(u"label_M3")

        self.horizontalLayout_43.addWidget(self.label_M3)

        self.horizontalSpacer_42 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_43.addItem(self.horizontalSpacer_42)

        self.label_value_M_3 = QLabel(self.subWindow_calculated_parameters)
        self.label_value_M_3.setObjectName(u"label_value_M_3")

        self.horizontalLayout_43.addWidget(self.label_value_M_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_43)

        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.label_M4 = QLabel(self.subWindow_calculated_parameters)
        self.label_M4.setObjectName(u"label_M4")

        self.horizontalLayout_44.addWidget(self.label_M4)

        self.horizontalSpacer_43 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_44.addItem(self.horizontalSpacer_43)

        self.label_value_M_4 = QLabel(self.subWindow_calculated_parameters)
        self.label_value_M_4.setObjectName(u"label_value_M_4")

        self.horizontalLayout_44.addWidget(self.label_value_M_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_44)

        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.label_M = QLabel(self.subWindow_calculated_parameters)
        self.label_M.setObjectName(u"label_M")

        self.horizontalLayout_45.addWidget(self.label_M)

        self.horizontalSpacer_44 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_45.addItem(self.horizontalSpacer_44)

        self.label_value_M = QLabel(self.subWindow_calculated_parameters)
        self.label_value_M.setObjectName(u"label_value_M")

        self.horizontalLayout_45.addWidget(self.label_value_M)


        self.verticalLayout_2.addLayout(self.horizontalLayout_45)

        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.label_V1 = QLabel(self.subWindow_calculated_parameters)
        self.label_V1.setObjectName(u"label_V1")

        self.horizontalLayout_46.addWidget(self.label_V1)

        self.horizontalSpacer_45 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_46.addItem(self.horizontalSpacer_45)

        self.label_value_V_1 = QLabel(self.subWindow_calculated_parameters)
        self.label_value_V_1.setObjectName(u"label_value_V_1")

        self.horizontalLayout_46.addWidget(self.label_value_V_1)


        self.verticalLayout_2.addLayout(self.horizontalLayout_46)

        self.horizontalLayout_47 = QHBoxLayout()
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.label_V2 = QLabel(self.subWindow_calculated_parameters)
        self.label_V2.setObjectName(u"label_V2")

        self.horizontalLayout_47.addWidget(self.label_V2)

        self.horizontalSpacer_46 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_47.addItem(self.horizontalSpacer_46)

        self.label_value_V_2 = QLabel(self.subWindow_calculated_parameters)
        self.label_value_V_2.setObjectName(u"label_value_V_2")

        self.horizontalLayout_47.addWidget(self.label_value_V_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_47)

        self.horizontalLayout_48 = QHBoxLayout()
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.label_V3 = QLabel(self.subWindow_calculated_parameters)
        self.label_V3.setObjectName(u"label_V3")

        self.horizontalLayout_48.addWidget(self.label_V3)

        self.horizontalSpacer_47 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_48.addItem(self.horizontalSpacer_47)

        self.label_value_V_3 = QLabel(self.subWindow_calculated_parameters)
        self.label_value_V_3.setObjectName(u"label_value_V_3")

        self.horizontalLayout_48.addWidget(self.label_value_V_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_48)

        self.horizontalLayout_49 = QHBoxLayout()
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.label_V4 = QLabel(self.subWindow_calculated_parameters)
        self.label_V4.setObjectName(u"label_V4")

        self.horizontalLayout_49.addWidget(self.label_V4)

        self.horizontalSpacer_48 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_49.addItem(self.horizontalSpacer_48)

        self.label_value_V_4 = QLabel(self.subWindow_calculated_parameters)
        self.label_value_V_4.setObjectName(u"label_value_V_4")

        self.horizontalLayout_49.addWidget(self.label_value_V_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_49)

        self.horizontalLayout_50 = QHBoxLayout()
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.label_p1 = QLabel(self.subWindow_calculated_parameters)
        self.label_p1.setObjectName(u"label_p1")

        self.horizontalLayout_50.addWidget(self.label_p1)

        self.horizontalSpacer_49 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_50.addItem(self.horizontalSpacer_49)

        self.label_value_p_1 = QLabel(self.subWindow_calculated_parameters)
        self.label_value_p_1.setObjectName(u"label_value_p_1")

        self.horizontalLayout_50.addWidget(self.label_value_p_1)


        self.verticalLayout_2.addLayout(self.horizontalLayout_50)

        self.horizontalLayout_51 = QHBoxLayout()
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.label_p2 = QLabel(self.subWindow_calculated_parameters)
        self.label_p2.setObjectName(u"label_p2")

        self.horizontalLayout_51.addWidget(self.label_p2)

        self.horizontalSpacer_50 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_51.addItem(self.horizontalSpacer_50)

        self.label_value_p_2 = QLabel(self.subWindow_calculated_parameters)
        self.label_value_p_2.setObjectName(u"label_value_p_2")

        self.horizontalLayout_51.addWidget(self.label_value_p_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_51)


        self.verticalLayout_7.addLayout(self.verticalLayout_2)

        self.mdiArea.addSubWindow(self.subWindow_calculated_parameters)
        self.subWindow_construction_parameters = SubWindowBase()
        self.subWindow_construction_parameters.setObjectName(u"subWindow_construction_parameters")
        self.verticalLayout_9 = QVBoxLayout(self.subWindow_construction_parameters)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.groupBox_11 = QGroupBox(self.subWindow_construction_parameters)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_11)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_a_sp_2 = QLabel(self.groupBox_11)
        self.label_a_sp_2.setObjectName(u"label_a_sp_2")

        self.horizontalLayout_35.addWidget(self.label_a_sp_2)

        self.horizontalSpacer_34 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_34)

        self.doubleSpinBox_input_thinkness_spiral_2 = QDoubleSpinBox(self.groupBox_11)
        self.doubleSpinBox_input_thinkness_spiral_2.setObjectName(u"doubleSpinBox_input_thinkness_spiral_2")

        self.horizontalLayout_35.addWidget(self.doubleSpinBox_input_thinkness_spiral_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_35)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_b_sp_2 = QLabel(self.groupBox_11)
        self.label_b_sp_2.setObjectName(u"label_b_sp_2")

        self.horizontalLayout_36.addWidget(self.label_b_sp_2)

        self.horizontalSpacer_35 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_35)

        self.doubleSpinBox_input_height_spiral_2 = QDoubleSpinBox(self.groupBox_11)
        self.doubleSpinBox_input_height_spiral_2.setObjectName(u"doubleSpinBox_input_height_spiral_2")

        self.horizontalLayout_36.addWidget(self.doubleSpinBox_input_height_spiral_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_36)


        self.verticalLayout_9.addWidget(self.groupBox_11)

        self.groupBox_12 = QGroupBox(self.subWindow_construction_parameters)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_12)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.label_a_col_2 = QLabel(self.groupBox_12)
        self.label_a_col_2.setObjectName(u"label_a_col_2")

        self.horizontalLayout_37.addWidget(self.label_a_col_2)

        self.horizontalSpacer_36 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_37.addItem(self.horizontalSpacer_36)

        self.doubleSpinBox_input_thinkness_ring_2 = QDoubleSpinBox(self.groupBox_12)
        self.doubleSpinBox_input_thinkness_ring_2.setObjectName(u"doubleSpinBox_input_thinkness_ring_2")

        self.horizontalLayout_37.addWidget(self.doubleSpinBox_input_thinkness_ring_2)


        self.verticalLayout_8.addLayout(self.horizontalLayout_37)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.label_b_col_2 = QLabel(self.groupBox_12)
        self.label_b_col_2.setObjectName(u"label_b_col_2")

        self.horizontalLayout_38.addWidget(self.label_b_col_2)

        self.horizontalSpacer_37 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_37)

        self.doubleSpinBox_input_height_ring_2 = QDoubleSpinBox(self.groupBox_12)
        self.doubleSpinBox_input_height_ring_2.setObjectName(u"doubleSpinBox_input_height_ring_2")

        self.horizontalLayout_38.addWidget(self.doubleSpinBox_input_height_ring_2)


        self.verticalLayout_8.addLayout(self.horizontalLayout_38)


        self.verticalLayout_9.addWidget(self.groupBox_12)

        self.groupBox_13 = QGroupBox(self.subWindow_construction_parameters)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.verticalLayout_17 = QVBoxLayout(self.groupBox_13)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.label_a_shp_2 = QLabel(self.groupBox_13)
        self.label_a_shp_2.setObjectName(u"label_a_shp_2")

        self.horizontalLayout_39.addWidget(self.label_a_shp_2)

        self.horizontalSpacer_38 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_39.addItem(self.horizontalSpacer_38)

        self.doubleSpinBox_input_thinkness_shp_2 = QDoubleSpinBox(self.groupBox_13)
        self.doubleSpinBox_input_thinkness_shp_2.setObjectName(u"doubleSpinBox_input_thinkness_shp_2")

        self.horizontalLayout_39.addWidget(self.doubleSpinBox_input_thinkness_shp_2)


        self.verticalLayout_17.addLayout(self.horizontalLayout_39)

        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.label_b_shp_2 = QLabel(self.groupBox_13)
        self.label_b_shp_2.setObjectName(u"label_b_shp_2")

        self.horizontalLayout_40.addWidget(self.label_b_shp_2)

        self.horizontalSpacer_39 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_40.addItem(self.horizontalSpacer_39)

        self.doubleSpinBox_input_height_shp_2 = QDoubleSpinBox(self.groupBox_13)
        self.doubleSpinBox_input_height_shp_2.setObjectName(u"doubleSpinBox_input_height_shp_2")

        self.horizontalLayout_40.addWidget(self.doubleSpinBox_input_height_shp_2)


        self.verticalLayout_17.addLayout(self.horizontalLayout_40)


        self.verticalLayout_9.addWidget(self.groupBox_13)

        self.mdiArea.addSubWindow(self.subWindow_construction_parameters)

        self.verticalLayout.addWidget(self.mdiArea)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.subWindow_parameters_toolbox.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b", None))
        self.pushButton_geometric_parameters.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0435\u043e\u043c\u0435\u0442\u0440\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b", None))
        self.pushButton_physical_mechanical_parameters.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u0437\u0438\u043a\u043e-\u043c\u0435\u0445\u0430\u043d\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438", None))
        self.pushButton_edge_structure_parameters.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0440\u0435\u0431\u0435\u0440\u043d\u043e\u0439 \u0441\u0442\u0440\u0443\u043a\u0442\u0443\u0440\u044b", None))
        self.pushButton_construction_parameters.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0438\u0441\u0445\u043e\u0434\u043d\u043e\u0439 \u043a\u043e\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u0438", None))
        self.pushButton_calculated_peremeters.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0447\u0438\u0441\u043b\u0435\u043d\u043d\u044b\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b", None))
        self.subwindow_4.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0433\u043e\u0442\u043e\u0432\u043a\u0430 \u0440\u0435\u0448\u0435\u043d\u0438\u044f", None))
        self.subwindow_5.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b \u0440\u0430\u0441\u0447\u0435\u0442\u0430", None))
        self.subWindow_geometric_parameters.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0413\u0435\u043e\u043c\u0435\u0442\u0440\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b", None))
        self.label_R1.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0434\u0438\u0443\u0441 \u0432\u0435\u0440\u0445\u043d\u0435\u0439 \u043a\u0440\u043e\u043c\u043a\u0438", None))
        self.label_R2.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0434\u0438\u0443\u0441 \u043d\u0438\u0436\u043d\u0435\u0439 \u043a\u0440\u043e\u043c\u043a\u0438", None))
        self.label_H.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0441\u043e\u0442\u0430 \u043a\u043e\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u0438", None))
        self.label_geometric_params_model.setText("")
        self.subWindow_edge_structure_parameters.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0440\u0435\u0431\u0435\u0440\u043d\u043e\u0439 \u0441\u0442\u0440\u0443\u043a\u0442\u0443\u0440\u044b", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0440\u0430\u043b\u044c\u043d\u044b\u0435 \u0440\u0435\u0431\u0440\u0430", None))
        self.label_a_sp.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u043b\u0449\u0438\u043d\u0430 \u0440\u0435\u0431\u0440\u0430", None))
        self.label_b_sp.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0441\u043e\u0442\u0430 \u0440\u0435\u0431\u0440\u0430", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u044c\u0446\u0435\u0432\u044b\u0435 \u0440\u0435\u0431\u0440\u0430", None))
        self.label_a_col.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u043b\u0449\u0438\u043d\u0430 \u0440\u0435\u0431\u0440\u0430", None))
        self.label_b_col.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0441\u043e\u0442\u0430 \u0440\u0435\u0431\u0440\u0430", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"\u0428\u043f\u0430\u043d\u0433\u043e\u0443\u0442", None))
        self.label_a_shp.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u043b\u0449\u0438\u043d\u0430 \u0440\u0435\u0431\u0440\u0430", None))
        self.label_b_shp.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0441\u043e\u0442\u0430 \u0440\u0435\u0431\u0440\u0430", None))
        self.subWindow_physical_mechanical_parameters.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u0437\u0438\u043a\u043e-\u043c\u0435\u0445\u0430\u043d\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0440\u0430\u043b\u044c\u043d\u044b\u0435 \u0440\u0435\u0431\u0440\u0430", None))
        self.label_E_x_spiral.setText(QCoreApplication.translate("MainWindow", u"E_x", None))
        self.label_E_y_spiral.setText(QCoreApplication.translate("MainWindow", u"E_y", None))
        self.label_E_z_spiral.setText(QCoreApplication.translate("MainWindow", u"E_z", None))
        self.label_G_xy_spiral.setText(QCoreApplication.translate("MainWindow", u"G_xy", None))
        self.label_G_yz_spiral.setText(QCoreApplication.translate("MainWindow", u"G_yz", None))
        self.label_G_xz_spiral.setText(QCoreApplication.translate("MainWindow", u"G_xz", None))
        self.label_v_spiral.setText(QCoreApplication.translate("MainWindow", u"v", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"\u0428\u043f\u0430\u043d\u0433\u043e\u0443\u0442", None))
        self.label_E_x_shp.setText(QCoreApplication.translate("MainWindow", u"E_x", None))
        self.label_E_y_shp.setText(QCoreApplication.translate("MainWindow", u"E_y", None))
        self.label_E_z_shp.setText(QCoreApplication.translate("MainWindow", u"E_z", None))
        self.label_G_xy_shp.setText(QCoreApplication.translate("MainWindow", u"G_xy", None))
        self.label_G_yz_shp.setText(QCoreApplication.translate("MainWindow", u"G_yz", None))
        self.label_G_xz_shp.setText(QCoreApplication.translate("MainWindow", u"G_xz", None))
        self.label_v_shp.setText(QCoreApplication.translate("MainWindow", u"v", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u044c\u0446\u0435\u0432\u044b\u0435 \u0440\u0435\u0431\u0440\u0430", None))
        self.label_E_x_ring.setText(QCoreApplication.translate("MainWindow", u"E_x", None))
        self.label_E_y_ring.setText(QCoreApplication.translate("MainWindow", u"E_y", None))
        self.label_E_z_ring.setText(QCoreApplication.translate("MainWindow", u"E_z", None))
        self.label_G_xy_ring.setText(QCoreApplication.translate("MainWindow", u"G_xy", None))
        self.label_G_yz_ring.setText(QCoreApplication.translate("MainWindow", u"G_yz", None))
        self.label_G_xz_ring.setText(QCoreApplication.translate("MainWindow", u"G_xz", None))
        self.label_v_ring.setText(QCoreApplication.translate("MainWindow", u"v", None))
        self.subWindow_calculated_parameters.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0447\u0438\u0441\u043b\u0435\u043d\u043d\u044b\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b", None))
        self.label_M1.setText(QCoreApplication.translate("MainWindow", u"M_1", None))
        self.label_value_M_1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_M2.setText(QCoreApplication.translate("MainWindow", u"M_2", None))
        self.label_value_M_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_M3.setText(QCoreApplication.translate("MainWindow", u"M_3", None))
        self.label_value_M_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_M4.setText(QCoreApplication.translate("MainWindow", u"M_4", None))
        self.label_value_M_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_M.setText(QCoreApplication.translate("MainWindow", u"M", None))
        self.label_value_M.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_V1.setText(QCoreApplication.translate("MainWindow", u"V_1", None))
        self.label_value_V_1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_V2.setText(QCoreApplication.translate("MainWindow", u"V_2", None))
        self.label_value_V_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_V3.setText(QCoreApplication.translate("MainWindow", u"V_3", None))
        self.label_value_V_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_V4.setText(QCoreApplication.translate("MainWindow", u"V_4", None))
        self.label_value_V_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_p1.setText(QCoreApplication.translate("MainWindow", u"p_1", None))
        self.label_value_p_1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_p2.setText(QCoreApplication.translate("MainWindow", u"p_2", None))
        self.label_value_p_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.subWindow_construction_parameters.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0438\u0441\u0445\u043e\u0434\u043d\u043e\u0439 \u043a\u043e\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u0438", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0440\u0430\u043b\u044c\u043d\u044b\u0435 \u0440\u0435\u0431\u0440\u0430", None))
        self.label_a_sp_2.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u043b\u0449\u0438\u043d\u0430 \u0440\u0435\u0431\u0440\u0430", None))
        self.label_b_sp_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0441\u043e\u0442\u0430 \u0440\u0435\u0431\u0440\u0430", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u044c\u0446\u0435\u0432\u044b\u0435 \u0440\u0435\u0431\u0440\u0430", None))
        self.label_a_col_2.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u043b\u0449\u0438\u043d\u0430 \u0440\u0435\u0431\u0440\u0430", None))
        self.label_b_col_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0441\u043e\u0442\u0430 \u0440\u0435\u0431\u0440\u0430", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("MainWindow", u"\u0428\u043f\u0430\u043d\u0433\u043e\u0443\u0442", None))
        self.label_a_shp_2.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u043b\u0449\u0438\u043d\u0430 \u0440\u0435\u0431\u0440\u0430", None))
        self.label_b_shp_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0441\u043e\u0442\u0430 \u0440\u0435\u0431\u0440\u0430", None))
    # retranslateUi

