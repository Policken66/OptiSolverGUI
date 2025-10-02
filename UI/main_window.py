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

from Widgets.DoubleSpinBox.double_spin_box_geometry import DoubleSpinBoxGeometry
from Widgets.DoubleSpinBox.double_spin_box_mechanical import DoubleSpinBoxMechanical
from Widgets.SpinBox.spin_box_quantity import SpinBoxQuantity
from Widgets.SubWindow.sub_window_base import SubWindowBase

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1011, 767)
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
        self.pushButton_geometric_parameters.setCheckable(True)

        self.horizontalLayout.addWidget(self.pushButton_geometric_parameters)

        self.pushButton_physical_mechanical_parameters = QPushButton(self.subWindow_parameters_toolbox)
        self.pushButton_physical_mechanical_parameters.setObjectName(u"pushButton_physical_mechanical_parameters")
        self.pushButton_physical_mechanical_parameters.setCheckable(True)

        self.horizontalLayout.addWidget(self.pushButton_physical_mechanical_parameters)

        self.pushButton_edge_structure_parameters = QPushButton(self.subWindow_parameters_toolbox)
        self.pushButton_edge_structure_parameters.setObjectName(u"pushButton_edge_structure_parameters")
        self.pushButton_edge_structure_parameters.setCheckable(True)

        self.horizontalLayout.addWidget(self.pushButton_edge_structure_parameters)

        self.pushButton_construction_parameters = QPushButton(self.subWindow_parameters_toolbox)
        self.pushButton_construction_parameters.setObjectName(u"pushButton_construction_parameters")
        self.pushButton_construction_parameters.setCheckable(True)

        self.horizontalLayout.addWidget(self.pushButton_construction_parameters)

        self.pushButton_calculated_peremeters = QPushButton(self.subWindow_parameters_toolbox)
        self.pushButton_calculated_peremeters.setObjectName(u"pushButton_calculated_peremeters")
        self.pushButton_calculated_peremeters.setCheckable(True)

        self.horizontalLayout.addWidget(self.pushButton_calculated_peremeters)

        self.horizontalSpacer_parameters_toolbox = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_parameters_toolbox)

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
        self.subWindow_geometric_parameters.setMinimumSize(QSize(300, 0))
        self.verticalLayout_15 = QVBoxLayout(self.subWindow_geometric_parameters)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.horizontalLayout_R1 = QHBoxLayout()
        self.horizontalLayout_R1.setObjectName(u"horizontalLayout_R1")
        self.label_R1 = QLabel(self.subWindow_geometric_parameters)
        self.label_R1.setObjectName(u"label_R1")

        self.horizontalLayout_R1.addWidget(self.label_R1)

        self.horizontalSpacer_R1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_R1.addItem(self.horizontalSpacer_R1)

        self.doubleSpinBox_R1 = DoubleSpinBoxGeometry(self.subWindow_geometric_parameters)
        self.doubleSpinBox_R1.setObjectName(u"doubleSpinBox_R1")

        self.horizontalLayout_R1.addWidget(self.doubleSpinBox_R1)


        self.verticalLayout_15.addLayout(self.horizontalLayout_R1)

        self.horizontalLayout_R2 = QHBoxLayout()
        self.horizontalLayout_R2.setObjectName(u"horizontalLayout_R2")
        self.label_R2 = QLabel(self.subWindow_geometric_parameters)
        self.label_R2.setObjectName(u"label_R2")

        self.horizontalLayout_R2.addWidget(self.label_R2)

        self.horizontalSpacer_R2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_R2.addItem(self.horizontalSpacer_R2)

        self.doubleSpinBox_R2 = DoubleSpinBoxGeometry(self.subWindow_geometric_parameters)
        self.doubleSpinBox_R2.setObjectName(u"doubleSpinBox_R2")

        self.horizontalLayout_R2.addWidget(self.doubleSpinBox_R2)


        self.verticalLayout_15.addLayout(self.horizontalLayout_R2)

        self.horizontalLayout_H = QHBoxLayout()
        self.horizontalLayout_H.setObjectName(u"horizontalLayout_H")
        self.label_H = QLabel(self.subWindow_geometric_parameters)
        self.label_H.setObjectName(u"label_H")

        self.horizontalLayout_H.addWidget(self.label_H)

        self.horizontalSpacer_H = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_H.addItem(self.horizontalSpacer_H)

        self.doubleSpinBox_H = DoubleSpinBoxGeometry(self.subWindow_geometric_parameters)
        self.doubleSpinBox_H.setObjectName(u"doubleSpinBox_H")

        self.horizontalLayout_H.addWidget(self.doubleSpinBox_H)


        self.verticalLayout_15.addLayout(self.horizontalLayout_H)

        self.label_geometric_params_model = QLabel(self.subWindow_geometric_parameters)
        self.label_geometric_params_model.setObjectName(u"label_geometric_params_model")

        self.verticalLayout_15.addWidget(self.label_geometric_params_model)

        self.mdiArea.addSubWindow(self.subWindow_geometric_parameters)
        self.subWindow_edge_structure_parameters = SubWindowBase()
        self.subWindow_edge_structure_parameters.setObjectName(u"subWindow_edge_structure_parameters")
        self.subWindow_edge_structure_parameters.setMinimumSize(QSize(320, 0))
        self.verticalLayout_11 = QVBoxLayout(self.subWindow_edge_structure_parameters)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.groupBox_a_b_sp = QGroupBox(self.subWindow_edge_structure_parameters)
        self.groupBox_a_b_sp.setObjectName(u"groupBox_a_b_sp")
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_a_b_sp)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_a_sp = QHBoxLayout()
        self.horizontalLayout_a_sp.setObjectName(u"horizontalLayout_a_sp")
        self.label_a_sp = QLabel(self.groupBox_a_b_sp)
        self.label_a_sp.setObjectName(u"label_a_sp")

        self.horizontalLayout_a_sp.addWidget(self.label_a_sp)

        self.horizontalSpacer_a_sp = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_a_sp.addItem(self.horizontalSpacer_a_sp)

        self.doubleSpinBox_a_sp = DoubleSpinBoxGeometry(self.groupBox_a_b_sp)
        self.doubleSpinBox_a_sp.setObjectName(u"doubleSpinBox_a_sp")

        self.horizontalLayout_a_sp.addWidget(self.doubleSpinBox_a_sp)


        self.verticalLayout_10.addLayout(self.horizontalLayout_a_sp)

        self.horizontalLayout_b_sp = QHBoxLayout()
        self.horizontalLayout_b_sp.setObjectName(u"horizontalLayout_b_sp")
        self.label_b_sp = QLabel(self.groupBox_a_b_sp)
        self.label_b_sp.setObjectName(u"label_b_sp")

        self.horizontalLayout_b_sp.addWidget(self.label_b_sp)

        self.horizontalSpacer_b_sp = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_b_sp.addItem(self.horizontalSpacer_b_sp)

        self.doubleSpinBox_b_sp = DoubleSpinBoxGeometry(self.groupBox_a_b_sp)
        self.doubleSpinBox_b_sp.setObjectName(u"doubleSpinBox_b_sp")

        self.horizontalLayout_b_sp.addWidget(self.doubleSpinBox_b_sp)


        self.verticalLayout_10.addLayout(self.horizontalLayout_b_sp)


        self.verticalLayout_11.addWidget(self.groupBox_a_b_sp)

        self.groupBox_a_b_col = QGroupBox(self.subWindow_edge_structure_parameters)
        self.groupBox_a_b_col.setObjectName(u"groupBox_a_b_col")
        self.verticalLayout_18 = QVBoxLayout(self.groupBox_a_b_col)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.horizontalLayout_a_col = QHBoxLayout()
        self.horizontalLayout_a_col.setObjectName(u"horizontalLayout_a_col")
        self.label_a_col = QLabel(self.groupBox_a_b_col)
        self.label_a_col.setObjectName(u"label_a_col")

        self.horizontalLayout_a_col.addWidget(self.label_a_col)

        self.horizontalSpacer_a_col = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_a_col.addItem(self.horizontalSpacer_a_col)

        self.doubleSpinBox_a_col = DoubleSpinBoxGeometry(self.groupBox_a_b_col)
        self.doubleSpinBox_a_col.setObjectName(u"doubleSpinBox_a_col")

        self.horizontalLayout_a_col.addWidget(self.doubleSpinBox_a_col)


        self.verticalLayout_18.addLayout(self.horizontalLayout_a_col)

        self.horizontalLayout_b_col = QHBoxLayout()
        self.horizontalLayout_b_col.setObjectName(u"horizontalLayout_b_col")
        self.label_b_col = QLabel(self.groupBox_a_b_col)
        self.label_b_col.setObjectName(u"label_b_col")

        self.horizontalLayout_b_col.addWidget(self.label_b_col)

        self.horizontalSpacer_b_col = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_b_col.addItem(self.horizontalSpacer_b_col)

        self.doubleSpinBox_b_col = DoubleSpinBoxGeometry(self.groupBox_a_b_col)
        self.doubleSpinBox_b_col.setObjectName(u"doubleSpinBox_b_col")

        self.horizontalLayout_b_col.addWidget(self.doubleSpinBox_b_col)


        self.verticalLayout_18.addLayout(self.horizontalLayout_b_col)


        self.verticalLayout_11.addWidget(self.groupBox_a_b_col)

        self.groupBox_a_b_shp = QGroupBox(self.subWindow_edge_structure_parameters)
        self.groupBox_a_b_shp.setObjectName(u"groupBox_a_b_shp")
        self.verticalLayout_19 = QVBoxLayout(self.groupBox_a_b_shp)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.horizontalLayout_a_shp = QHBoxLayout()
        self.horizontalLayout_a_shp.setObjectName(u"horizontalLayout_a_shp")
        self.label_a_shp = QLabel(self.groupBox_a_b_shp)
        self.label_a_shp.setObjectName(u"label_a_shp")

        self.horizontalLayout_a_shp.addWidget(self.label_a_shp)

        self.horizontalSpacer_a_shp = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_a_shp.addItem(self.horizontalSpacer_a_shp)

        self.doubleSpinBox_a_shp = DoubleSpinBoxGeometry(self.groupBox_a_b_shp)
        self.doubleSpinBox_a_shp.setObjectName(u"doubleSpinBox_a_shp")

        self.horizontalLayout_a_shp.addWidget(self.doubleSpinBox_a_shp)


        self.verticalLayout_19.addLayout(self.horizontalLayout_a_shp)

        self.horizontalLayout_b_shp = QHBoxLayout()
        self.horizontalLayout_b_shp.setObjectName(u"horizontalLayout_b_shp")
        self.label_b_shp = QLabel(self.groupBox_a_b_shp)
        self.label_b_shp.setObjectName(u"label_b_shp")

        self.horizontalLayout_b_shp.addWidget(self.label_b_shp)

        self.horizontalSpacer_b_shp = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_b_shp.addItem(self.horizontalSpacer_b_shp)

        self.doubleSpinBox_b_shp = DoubleSpinBoxGeometry(self.groupBox_a_b_shp)
        self.doubleSpinBox_b_shp.setObjectName(u"doubleSpinBox_b_shp")

        self.horizontalLayout_b_shp.addWidget(self.doubleSpinBox_b_shp)


        self.verticalLayout_19.addLayout(self.horizontalLayout_b_shp)


        self.verticalLayout_11.addWidget(self.groupBox_a_b_shp)

        self.mdiArea.addSubWindow(self.subWindow_edge_structure_parameters)
        self.subWindow_physical_mechanical_parameters = SubWindowBase()
        self.subWindow_physical_mechanical_parameters.setObjectName(u"subWindow_physical_mechanical_parameters")
        self.subWindow_physical_mechanical_parameters.setMinimumSize(QSize(450, 0))
        self.horizontalLayout_6 = QHBoxLayout(self.subWindow_physical_mechanical_parameters)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.groupBox_spiral = QGroupBox(self.subWindow_physical_mechanical_parameters)
        self.groupBox_spiral.setObjectName(u"groupBox_spiral")
        sizePolicy1.setHeightForWidth(self.groupBox_spiral.sizePolicy().hasHeightForWidth())
        self.groupBox_spiral.setSizePolicy(sizePolicy1)
        self.groupBox_spiral.setMinimumSize(QSize(0, 0))
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_spiral)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_spiral = QVBoxLayout()
        self.verticalLayout_spiral.setObjectName(u"verticalLayout_spiral")
        self.horizontalLayout_Ex_spiral = QHBoxLayout()
        self.horizontalLayout_Ex_spiral.setObjectName(u"horizontalLayout_Ex_spiral")
        self.label_Ex_spiral = QLabel(self.groupBox_spiral)
        self.label_Ex_spiral.setObjectName(u"label_Ex_spiral")

        self.horizontalLayout_Ex_spiral.addWidget(self.label_Ex_spiral)

        self.horizontalSpacer_Ex_spiral = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_Ex_spiral.addItem(self.horizontalSpacer_Ex_spiral)

        self.doubleSpinBox_Ex_spiral = DoubleSpinBoxMechanical(self.groupBox_spiral)
        self.doubleSpinBox_Ex_spiral.setObjectName(u"doubleSpinBox_Ex_spiral")

        self.horizontalLayout_Ex_spiral.addWidget(self.doubleSpinBox_Ex_spiral)


        self.verticalLayout_spiral.addLayout(self.horizontalLayout_Ex_spiral)

        self.horizontalLayout_Ey_spiral = QHBoxLayout()
        self.horizontalLayout_Ey_spiral.setObjectName(u"horizontalLayout_Ey_spiral")
        self.label_Ey_spiral = QLabel(self.groupBox_spiral)
        self.label_Ey_spiral.setObjectName(u"label_Ey_spiral")

        self.horizontalLayout_Ey_spiral.addWidget(self.label_Ey_spiral)

        self.horizontalSpacer_Ey_spiral = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_Ey_spiral.addItem(self.horizontalSpacer_Ey_spiral)

        self.doubleSpinBox_Ey_spiral = DoubleSpinBoxMechanical(self.groupBox_spiral)
        self.doubleSpinBox_Ey_spiral.setObjectName(u"doubleSpinBox_Ey_spiral")

        self.horizontalLayout_Ey_spiral.addWidget(self.doubleSpinBox_Ey_spiral)


        self.verticalLayout_spiral.addLayout(self.horizontalLayout_Ey_spiral)

        self.horizontalLayout_Ez_spiral = QHBoxLayout()
        self.horizontalLayout_Ez_spiral.setObjectName(u"horizontalLayout_Ez_spiral")
        self.label_Ez_spiral = QLabel(self.groupBox_spiral)
        self.label_Ez_spiral.setObjectName(u"label_Ez_spiral")

        self.horizontalLayout_Ez_spiral.addWidget(self.label_Ez_spiral)

        self.horizontalSpacer_Ez_spiral = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_Ez_spiral.addItem(self.horizontalSpacer_Ez_spiral)

        self.doubleSpinBox_Ez_spiral = DoubleSpinBoxMechanical(self.groupBox_spiral)
        self.doubleSpinBox_Ez_spiral.setObjectName(u"doubleSpinBox_Ez_spiral")

        self.horizontalLayout_Ez_spiral.addWidget(self.doubleSpinBox_Ez_spiral)


        self.verticalLayout_spiral.addLayout(self.horizontalLayout_Ez_spiral)

        self.horizontalLayout_Gxy_spiral = QHBoxLayout()
        self.horizontalLayout_Gxy_spiral.setObjectName(u"horizontalLayout_Gxy_spiral")
        self.label_Gxy_spiral = QLabel(self.groupBox_spiral)
        self.label_Gxy_spiral.setObjectName(u"label_Gxy_spiral")

        self.horizontalLayout_Gxy_spiral.addWidget(self.label_Gxy_spiral)

        self.horizontalSpacer_Gxy_spiral = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_Gxy_spiral.addItem(self.horizontalSpacer_Gxy_spiral)

        self.doubleSpinBox_Gxy_spiral = DoubleSpinBoxMechanical(self.groupBox_spiral)
        self.doubleSpinBox_Gxy_spiral.setObjectName(u"doubleSpinBox_Gxy_spiral")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_Gxy_spiral.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_Gxy_spiral.setSizePolicy(sizePolicy2)

        self.horizontalLayout_Gxy_spiral.addWidget(self.doubleSpinBox_Gxy_spiral)


        self.verticalLayout_spiral.addLayout(self.horizontalLayout_Gxy_spiral)

        self.horizontalLayout_Gyz_spiral = QHBoxLayout()
        self.horizontalLayout_Gyz_spiral.setObjectName(u"horizontalLayout_Gyz_spiral")
        self.label_Gyz_spiral = QLabel(self.groupBox_spiral)
        self.label_Gyz_spiral.setObjectName(u"label_Gyz_spiral")

        self.horizontalLayout_Gyz_spiral.addWidget(self.label_Gyz_spiral)

        self.horizontalSpacer_Gyz_spiral = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_Gyz_spiral.addItem(self.horizontalSpacer_Gyz_spiral)

        self.doubleSpinBox_Gyz_spiral = DoubleSpinBoxMechanical(self.groupBox_spiral)
        self.doubleSpinBox_Gyz_spiral.setObjectName(u"doubleSpinBox_Gyz_spiral")

        self.horizontalLayout_Gyz_spiral.addWidget(self.doubleSpinBox_Gyz_spiral)


        self.verticalLayout_spiral.addLayout(self.horizontalLayout_Gyz_spiral)

        self.horizontalLayout_Gxz = QHBoxLayout()
        self.horizontalLayout_Gxz.setObjectName(u"horizontalLayout_Gxz")
        self.label_Gxz_spiral = QLabel(self.groupBox_spiral)
        self.label_Gxz_spiral.setObjectName(u"label_Gxz_spiral")

        self.horizontalLayout_Gxz.addWidget(self.label_Gxz_spiral)

        self.horizontalSpacer_Gxz_spiral = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_Gxz.addItem(self.horizontalSpacer_Gxz_spiral)

        self.doubleSpinBox_Gxz_spiral = DoubleSpinBoxMechanical(self.groupBox_spiral)
        self.doubleSpinBox_Gxz_spiral.setObjectName(u"doubleSpinBox_Gxz_spiral")

        self.horizontalLayout_Gxz.addWidget(self.doubleSpinBox_Gxz_spiral)


        self.verticalLayout_spiral.addLayout(self.horizontalLayout_Gxz)

        self.horizontalLayout_v_spiral = QHBoxLayout()
        self.horizontalLayout_v_spiral.setObjectName(u"horizontalLayout_v_spiral")
        self.label_v_spiral = QLabel(self.groupBox_spiral)
        self.label_v_spiral.setObjectName(u"label_v_spiral")

        self.horizontalLayout_v_spiral.addWidget(self.label_v_spiral)

        self.horizontalSpacer_v_spiral = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_v_spiral.addItem(self.horizontalSpacer_v_spiral)

        self.doubleSpinBox_v_spiral = DoubleSpinBoxMechanical(self.groupBox_spiral)
        self.doubleSpinBox_v_spiral.setObjectName(u"doubleSpinBox_v_spiral")

        self.horizontalLayout_v_spiral.addWidget(self.doubleSpinBox_v_spiral)


        self.verticalLayout_spiral.addLayout(self.horizontalLayout_v_spiral)


        self.verticalLayout_12.addLayout(self.verticalLayout_spiral)


        self.horizontalLayout_6.addWidget(self.groupBox_spiral)

        self.groupBox_shp = QGroupBox(self.subWindow_physical_mechanical_parameters)
        self.groupBox_shp.setObjectName(u"groupBox_shp")
        sizePolicy.setHeightForWidth(self.groupBox_shp.sizePolicy().hasHeightForWidth())
        self.groupBox_shp.setSizePolicy(sizePolicy)
        self.verticalLayout_13 = QVBoxLayout(self.groupBox_shp)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_shp = QVBoxLayout()
        self.verticalLayout_shp.setObjectName(u"verticalLayout_shp")
        self.horizontalLayout_Ex_shp = QHBoxLayout()
        self.horizontalLayout_Ex_shp.setObjectName(u"horizontalLayout_Ex_shp")
        self.label_Ex_shp = QLabel(self.groupBox_shp)
        self.label_Ex_shp.setObjectName(u"label_Ex_shp")

        self.horizontalLayout_Ex_shp.addWidget(self.label_Ex_shp)

        self.horizontalSpacer_Ex_shp = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_Ex_shp.addItem(self.horizontalSpacer_Ex_shp)

        self.doubleSpinBox_Ex_shp = DoubleSpinBoxMechanical(self.groupBox_shp)
        self.doubleSpinBox_Ex_shp.setObjectName(u"doubleSpinBox_Ex_shp")

        self.horizontalLayout_Ex_shp.addWidget(self.doubleSpinBox_Ex_shp)


        self.verticalLayout_shp.addLayout(self.horizontalLayout_Ex_shp)

        self.horizontalLayout_Ey_shp = QHBoxLayout()
        self.horizontalLayout_Ey_shp.setObjectName(u"horizontalLayout_Ey_shp")
        self.label_Ey_shp = QLabel(self.groupBox_shp)
        self.label_Ey_shp.setObjectName(u"label_Ey_shp")

        self.horizontalLayout_Ey_shp.addWidget(self.label_Ey_shp)

        self.horizontalSpacer_Ey_shp = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_Ey_shp.addItem(self.horizontalSpacer_Ey_shp)

        self.doubleSpinBox_Ey_shp = DoubleSpinBoxMechanical(self.groupBox_shp)
        self.doubleSpinBox_Ey_shp.setObjectName(u"doubleSpinBox_Ey_shp")

        self.horizontalLayout_Ey_shp.addWidget(self.doubleSpinBox_Ey_shp)


        self.verticalLayout_shp.addLayout(self.horizontalLayout_Ey_shp)

        self.horizontalLayout_Ez_shp = QHBoxLayout()
        self.horizontalLayout_Ez_shp.setObjectName(u"horizontalLayout_Ez_shp")
        self.label_Ez_shp = QLabel(self.groupBox_shp)
        self.label_Ez_shp.setObjectName(u"label_Ez_shp")

        self.horizontalLayout_Ez_shp.addWidget(self.label_Ez_shp)

        self.horizontalSpacer_Ez_shp = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_Ez_shp.addItem(self.horizontalSpacer_Ez_shp)

        self.doubleSpinBox_Ez_shp = DoubleSpinBoxMechanical(self.groupBox_shp)
        self.doubleSpinBox_Ez_shp.setObjectName(u"doubleSpinBox_Ez_shp")

        self.horizontalLayout_Ez_shp.addWidget(self.doubleSpinBox_Ez_shp)


        self.verticalLayout_shp.addLayout(self.horizontalLayout_Ez_shp)

        self.horizontalLayout_Gxy_shp = QHBoxLayout()
        self.horizontalLayout_Gxy_shp.setObjectName(u"horizontalLayout_Gxy_shp")
        self.label_Gxy_shp = QLabel(self.groupBox_shp)
        self.label_Gxy_shp.setObjectName(u"label_Gxy_shp")

        self.horizontalLayout_Gxy_shp.addWidget(self.label_Gxy_shp)

        self.horizontalSpacer_Gxy_shp = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_Gxy_shp.addItem(self.horizontalSpacer_Gxy_shp)

        self.doubleSpinBox_Gxy_shp = DoubleSpinBoxMechanical(self.groupBox_shp)
        self.doubleSpinBox_Gxy_shp.setObjectName(u"doubleSpinBox_Gxy_shp")

        self.horizontalLayout_Gxy_shp.addWidget(self.doubleSpinBox_Gxy_shp)


        self.verticalLayout_shp.addLayout(self.horizontalLayout_Gxy_shp)

        self.horizontalLayout_Gyz_shp = QHBoxLayout()
        self.horizontalLayout_Gyz_shp.setObjectName(u"horizontalLayout_Gyz_shp")
        self.label_Gyz_shp = QLabel(self.groupBox_shp)
        self.label_Gyz_shp.setObjectName(u"label_Gyz_shp")

        self.horizontalLayout_Gyz_shp.addWidget(self.label_Gyz_shp)

        self.horizontalSpacer_Gyz_shp = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_Gyz_shp.addItem(self.horizontalSpacer_Gyz_shp)

        self.doubleSpinBox_Gyz_shp = DoubleSpinBoxMechanical(self.groupBox_shp)
        self.doubleSpinBox_Gyz_shp.setObjectName(u"doubleSpinBox_Gyz_shp")

        self.horizontalLayout_Gyz_shp.addWidget(self.doubleSpinBox_Gyz_shp)


        self.verticalLayout_shp.addLayout(self.horizontalLayout_Gyz_shp)

        self.horizontalLayout_Gxz_shp = QHBoxLayout()
        self.horizontalLayout_Gxz_shp.setObjectName(u"horizontalLayout_Gxz_shp")
        self.label_Gxz_shp = QLabel(self.groupBox_shp)
        self.label_Gxz_shp.setObjectName(u"label_Gxz_shp")

        self.horizontalLayout_Gxz_shp.addWidget(self.label_Gxz_shp)

        self.horizontalSpacer_Gxz_shp = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_Gxz_shp.addItem(self.horizontalSpacer_Gxz_shp)

        self.doubleSpinBox_Gxz_shp = DoubleSpinBoxMechanical(self.groupBox_shp)
        self.doubleSpinBox_Gxz_shp.setObjectName(u"doubleSpinBox_Gxz_shp")

        self.horizontalLayout_Gxz_shp.addWidget(self.doubleSpinBox_Gxz_shp)


        self.verticalLayout_shp.addLayout(self.horizontalLayout_Gxz_shp)

        self.horizontalLayout_v_shp = QHBoxLayout()
        self.horizontalLayout_v_shp.setObjectName(u"horizontalLayout_v_shp")
        self.label_v_shp = QLabel(self.groupBox_shp)
        self.label_v_shp.setObjectName(u"label_v_shp")

        self.horizontalLayout_v_shp.addWidget(self.label_v_shp)

        self.horizontalSpacer_v_shp = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_v_shp.addItem(self.horizontalSpacer_v_shp)

        self.doubleSpinBox_v_shp = DoubleSpinBoxMechanical(self.groupBox_shp)
        self.doubleSpinBox_v_shp.setObjectName(u"doubleSpinBox_v_shp")

        self.horizontalLayout_v_shp.addWidget(self.doubleSpinBox_v_shp)


        self.verticalLayout_shp.addLayout(self.horizontalLayout_v_shp)


        self.verticalLayout_13.addLayout(self.verticalLayout_shp)


        self.horizontalLayout_6.addWidget(self.groupBox_shp)

        self.groupBox_ring = QGroupBox(self.subWindow_physical_mechanical_parameters)
        self.groupBox_ring.setObjectName(u"groupBox_ring")
        sizePolicy.setHeightForWidth(self.groupBox_ring.sizePolicy().hasHeightForWidth())
        self.groupBox_ring.setSizePolicy(sizePolicy)
        self.verticalLayout_16 = QVBoxLayout(self.groupBox_ring)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_ring = QVBoxLayout()
        self.verticalLayout_ring.setObjectName(u"verticalLayout_ring")
        self.horizontalLayout_Ex_ring = QHBoxLayout()
        self.horizontalLayout_Ex_ring.setObjectName(u"horizontalLayout_Ex_ring")
        self.label_Ex_ring = QLabel(self.groupBox_ring)
        self.label_Ex_ring.setObjectName(u"label_Ex_ring")

        self.horizontalLayout_Ex_ring.addWidget(self.label_Ex_ring)

        self.horizontalSpacer_Ex_ring = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_Ex_ring.addItem(self.horizontalSpacer_Ex_ring)

        self.doubleSpinBox_Ex_ring = DoubleSpinBoxMechanical(self.groupBox_ring)
        self.doubleSpinBox_Ex_ring.setObjectName(u"doubleSpinBox_Ex_ring")

        self.horizontalLayout_Ex_ring.addWidget(self.doubleSpinBox_Ex_ring)


        self.verticalLayout_ring.addLayout(self.horizontalLayout_Ex_ring)

        self.horizontalLayout_Ey_ring = QHBoxLayout()
        self.horizontalLayout_Ey_ring.setObjectName(u"horizontalLayout_Ey_ring")
        self.label_Ey_ring = QLabel(self.groupBox_ring)
        self.label_Ey_ring.setObjectName(u"label_Ey_ring")

        self.horizontalLayout_Ey_ring.addWidget(self.label_Ey_ring)

        self.horizontalSpacer_Ey_ring = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_Ey_ring.addItem(self.horizontalSpacer_Ey_ring)

        self.doubleSpinBox_Ey_ring = DoubleSpinBoxMechanical(self.groupBox_ring)
        self.doubleSpinBox_Ey_ring.setObjectName(u"doubleSpinBox_Ey_ring")

        self.horizontalLayout_Ey_ring.addWidget(self.doubleSpinBox_Ey_ring)


        self.verticalLayout_ring.addLayout(self.horizontalLayout_Ey_ring)

        self.horizontalLayout_Ez_ring = QHBoxLayout()
        self.horizontalLayout_Ez_ring.setObjectName(u"horizontalLayout_Ez_ring")
        self.label_Ez_ring = QLabel(self.groupBox_ring)
        self.label_Ez_ring.setObjectName(u"label_Ez_ring")

        self.horizontalLayout_Ez_ring.addWidget(self.label_Ez_ring)

        self.horizontalSpacer_Ez_ring = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_Ez_ring.addItem(self.horizontalSpacer_Ez_ring)

        self.doubleSpinBox_Ez_ring = DoubleSpinBoxMechanical(self.groupBox_ring)
        self.doubleSpinBox_Ez_ring.setObjectName(u"doubleSpinBox_Ez_ring")

        self.horizontalLayout_Ez_ring.addWidget(self.doubleSpinBox_Ez_ring)


        self.verticalLayout_ring.addLayout(self.horizontalLayout_Ez_ring)

        self.horizontalLayout_Gxy_ring = QHBoxLayout()
        self.horizontalLayout_Gxy_ring.setObjectName(u"horizontalLayout_Gxy_ring")
        self.label_Gxy_ring = QLabel(self.groupBox_ring)
        self.label_Gxy_ring.setObjectName(u"label_Gxy_ring")

        self.horizontalLayout_Gxy_ring.addWidget(self.label_Gxy_ring)

        self.horizontalSpacer_Gxy_ring = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_Gxy_ring.addItem(self.horizontalSpacer_Gxy_ring)

        self.doubleSpinBox_Gxy_ring = DoubleSpinBoxMechanical(self.groupBox_ring)
        self.doubleSpinBox_Gxy_ring.setObjectName(u"doubleSpinBox_Gxy_ring")

        self.horizontalLayout_Gxy_ring.addWidget(self.doubleSpinBox_Gxy_ring)


        self.verticalLayout_ring.addLayout(self.horizontalLayout_Gxy_ring)

        self.horizontalLayout_Gyz_ring = QHBoxLayout()
        self.horizontalLayout_Gyz_ring.setObjectName(u"horizontalLayout_Gyz_ring")
        self.label_Gyz_ring = QLabel(self.groupBox_ring)
        self.label_Gyz_ring.setObjectName(u"label_Gyz_ring")

        self.horizontalLayout_Gyz_ring.addWidget(self.label_Gyz_ring)

        self.horizontalSpacer_Gyz_ring = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_Gyz_ring.addItem(self.horizontalSpacer_Gyz_ring)

        self.doubleSpinBox_Gyz_ring = DoubleSpinBoxMechanical(self.groupBox_ring)
        self.doubleSpinBox_Gyz_ring.setObjectName(u"doubleSpinBox_Gyz_ring")

        self.horizontalLayout_Gyz_ring.addWidget(self.doubleSpinBox_Gyz_ring)


        self.verticalLayout_ring.addLayout(self.horizontalLayout_Gyz_ring)

        self.horizontalLayout_Gxz_ring = QHBoxLayout()
        self.horizontalLayout_Gxz_ring.setObjectName(u"horizontalLayout_Gxz_ring")
        self.label_Gxz_ring = QLabel(self.groupBox_ring)
        self.label_Gxz_ring.setObjectName(u"label_Gxz_ring")

        self.horizontalLayout_Gxz_ring.addWidget(self.label_Gxz_ring)

        self.horizontalSpacer_Gxz_ring = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_Gxz_ring.addItem(self.horizontalSpacer_Gxz_ring)

        self.doubleSpinBox_Gxz_ring = DoubleSpinBoxMechanical(self.groupBox_ring)
        self.doubleSpinBox_Gxz_ring.setObjectName(u"doubleSpinBox_Gxz_ring")

        self.horizontalLayout_Gxz_ring.addWidget(self.doubleSpinBox_Gxz_ring)


        self.verticalLayout_ring.addLayout(self.horizontalLayout_Gxz_ring)

        self.horizontalLayout_v_ring = QHBoxLayout()
        self.horizontalLayout_v_ring.setObjectName(u"horizontalLayout_v_ring")
        self.label_v_ring = QLabel(self.groupBox_ring)
        self.label_v_ring.setObjectName(u"label_v_ring")

        self.horizontalLayout_v_ring.addWidget(self.label_v_ring)

        self.horizontalSpacer_v_ring = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_v_ring.addItem(self.horizontalSpacer_v_ring)

        self.doubleSpinBox_v_ring = DoubleSpinBoxMechanical(self.groupBox_ring)
        self.doubleSpinBox_v_ring.setObjectName(u"doubleSpinBox_v_ring")

        self.horizontalLayout_v_ring.addWidget(self.doubleSpinBox_v_ring)


        self.verticalLayout_ring.addLayout(self.horizontalLayout_v_ring)


        self.verticalLayout_16.addLayout(self.verticalLayout_ring)


        self.horizontalLayout_6.addWidget(self.groupBox_ring)

        self.mdiArea.addSubWindow(self.subWindow_physical_mechanical_parameters)
        self.subWindow_calculated_parameters = SubWindowBase()
        self.subWindow_calculated_parameters.setObjectName(u"subWindow_calculated_parameters")
        self.subWindow_calculated_parameters.setMinimumSize(QSize(280, 0))
        self.verticalLayout_7 = QVBoxLayout(self.subWindow_calculated_parameters)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_calculated_parameters = QVBoxLayout()
        self.verticalLayout_calculated_parameters.setObjectName(u"verticalLayout_calculated_parameters")
        self.horizontalLayout_M1 = QHBoxLayout()
        self.horizontalLayout_M1.setObjectName(u"horizontalLayout_M1")
        self.label_M1 = QLabel(self.subWindow_calculated_parameters)
        self.label_M1.setObjectName(u"label_M1")

        self.horizontalLayout_M1.addWidget(self.label_M1)

        self.horizontalSpacer_M1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_M1.addItem(self.horizontalSpacer_M1)

        self.label_value_M1 = QLabel(self.subWindow_calculated_parameters)
        self.label_value_M1.setObjectName(u"label_value_M1")

        self.horizontalLayout_M1.addWidget(self.label_value_M1)


        self.verticalLayout_calculated_parameters.addLayout(self.horizontalLayout_M1)

        self.horizontalLayout_M2 = QHBoxLayout()
        self.horizontalLayout_M2.setObjectName(u"horizontalLayout_M2")
        self.label_M2 = QLabel(self.subWindow_calculated_parameters)
        self.label_M2.setObjectName(u"label_M2")

        self.horizontalLayout_M2.addWidget(self.label_M2)

        self.horizontalSpacer_M2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_M2.addItem(self.horizontalSpacer_M2)

        self.label_value_M2 = QLabel(self.subWindow_calculated_parameters)
        self.label_value_M2.setObjectName(u"label_value_M2")

        self.horizontalLayout_M2.addWidget(self.label_value_M2)


        self.verticalLayout_calculated_parameters.addLayout(self.horizontalLayout_M2)

        self.horizontalLayout_M3 = QHBoxLayout()
        self.horizontalLayout_M3.setObjectName(u"horizontalLayout_M3")
        self.label_M3 = QLabel(self.subWindow_calculated_parameters)
        self.label_M3.setObjectName(u"label_M3")

        self.horizontalLayout_M3.addWidget(self.label_M3)

        self.horizontalSpacer_M3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_M3.addItem(self.horizontalSpacer_M3)

        self.label_value_M3 = QLabel(self.subWindow_calculated_parameters)
        self.label_value_M3.setObjectName(u"label_value_M3")

        self.horizontalLayout_M3.addWidget(self.label_value_M3)


        self.verticalLayout_calculated_parameters.addLayout(self.horizontalLayout_M3)

        self.horizontalLayout_M4 = QHBoxLayout()
        self.horizontalLayout_M4.setObjectName(u"horizontalLayout_M4")
        self.label_M4 = QLabel(self.subWindow_calculated_parameters)
        self.label_M4.setObjectName(u"label_M4")

        self.horizontalLayout_M4.addWidget(self.label_M4)

        self.horizontalSpacer_M4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_M4.addItem(self.horizontalSpacer_M4)

        self.label_value_M4 = QLabel(self.subWindow_calculated_parameters)
        self.label_value_M4.setObjectName(u"label_value_M4")

        self.horizontalLayout_M4.addWidget(self.label_value_M4)


        self.verticalLayout_calculated_parameters.addLayout(self.horizontalLayout_M4)

        self.horizontalLayout_M = QHBoxLayout()
        self.horizontalLayout_M.setObjectName(u"horizontalLayout_M")
        self.label_M = QLabel(self.subWindow_calculated_parameters)
        self.label_M.setObjectName(u"label_M")

        self.horizontalLayout_M.addWidget(self.label_M)

        self.horizontalSpacer_M = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_M.addItem(self.horizontalSpacer_M)

        self.label_value_M = QLabel(self.subWindow_calculated_parameters)
        self.label_value_M.setObjectName(u"label_value_M")

        self.horizontalLayout_M.addWidget(self.label_value_M)


        self.verticalLayout_calculated_parameters.addLayout(self.horizontalLayout_M)

        self.horizontalLayout_V1 = QHBoxLayout()
        self.horizontalLayout_V1.setObjectName(u"horizontalLayout_V1")
        self.label_V1 = QLabel(self.subWindow_calculated_parameters)
        self.label_V1.setObjectName(u"label_V1")

        self.horizontalLayout_V1.addWidget(self.label_V1)

        self.horizontalSpacer_V1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_V1.addItem(self.horizontalSpacer_V1)

        self.label_value_V1 = QLabel(self.subWindow_calculated_parameters)
        self.label_value_V1.setObjectName(u"label_value_V1")

        self.horizontalLayout_V1.addWidget(self.label_value_V1)


        self.verticalLayout_calculated_parameters.addLayout(self.horizontalLayout_V1)

        self.horizontalLayout_V2 = QHBoxLayout()
        self.horizontalLayout_V2.setObjectName(u"horizontalLayout_V2")
        self.label_V2 = QLabel(self.subWindow_calculated_parameters)
        self.label_V2.setObjectName(u"label_V2")

        self.horizontalLayout_V2.addWidget(self.label_V2)

        self.horizontalSpacer_V2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_V2.addItem(self.horizontalSpacer_V2)

        self.label_value_V2 = QLabel(self.subWindow_calculated_parameters)
        self.label_value_V2.setObjectName(u"label_value_V2")

        self.horizontalLayout_V2.addWidget(self.label_value_V2)


        self.verticalLayout_calculated_parameters.addLayout(self.horizontalLayout_V2)

        self.horizontalLayout_V3 = QHBoxLayout()
        self.horizontalLayout_V3.setObjectName(u"horizontalLayout_V3")
        self.label_V3 = QLabel(self.subWindow_calculated_parameters)
        self.label_V3.setObjectName(u"label_V3")

        self.horizontalLayout_V3.addWidget(self.label_V3)

        self.horizontalSpacer_V3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_V3.addItem(self.horizontalSpacer_V3)

        self.label_value_V3 = QLabel(self.subWindow_calculated_parameters)
        self.label_value_V3.setObjectName(u"label_value_V3")

        self.horizontalLayout_V3.addWidget(self.label_value_V3)


        self.verticalLayout_calculated_parameters.addLayout(self.horizontalLayout_V3)

        self.horizontalLayout_V4 = QHBoxLayout()
        self.horizontalLayout_V4.setObjectName(u"horizontalLayout_V4")
        self.label_V4 = QLabel(self.subWindow_calculated_parameters)
        self.label_V4.setObjectName(u"label_V4")

        self.horizontalLayout_V4.addWidget(self.label_V4)

        self.horizontalSpacer_V4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_V4.addItem(self.horizontalSpacer_V4)

        self.label_value_V4 = QLabel(self.subWindow_calculated_parameters)
        self.label_value_V4.setObjectName(u"label_value_V4")

        self.horizontalLayout_V4.addWidget(self.label_value_V4)


        self.verticalLayout_calculated_parameters.addLayout(self.horizontalLayout_V4)

        self.horizontalLayout_p1 = QHBoxLayout()
        self.horizontalLayout_p1.setObjectName(u"horizontalLayout_p1")
        self.label_p1 = QLabel(self.subWindow_calculated_parameters)
        self.label_p1.setObjectName(u"label_p1")

        self.horizontalLayout_p1.addWidget(self.label_p1)

        self.horizontalSpacer_p1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_p1.addItem(self.horizontalSpacer_p1)

        self.label_value_p1 = QLabel(self.subWindow_calculated_parameters)
        self.label_value_p1.setObjectName(u"label_value_p1")

        self.horizontalLayout_p1.addWidget(self.label_value_p1)


        self.verticalLayout_calculated_parameters.addLayout(self.horizontalLayout_p1)

        self.horizontalLayout_p2 = QHBoxLayout()
        self.horizontalLayout_p2.setObjectName(u"horizontalLayout_p2")
        self.label_p2 = QLabel(self.subWindow_calculated_parameters)
        self.label_p2.setObjectName(u"label_p2")

        self.horizontalLayout_p2.addWidget(self.label_p2)

        self.horizontalSpacer_p2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_p2.addItem(self.horizontalSpacer_p2)

        self.label_value_p2 = QLabel(self.subWindow_calculated_parameters)
        self.label_value_p2.setObjectName(u"label_value_p2")

        self.horizontalLayout_p2.addWidget(self.label_value_p2)


        self.verticalLayout_calculated_parameters.addLayout(self.horizontalLayout_p2)


        self.verticalLayout_7.addLayout(self.verticalLayout_calculated_parameters)

        self.mdiArea.addSubWindow(self.subWindow_calculated_parameters)
        self.subWindow_construction_parameters = SubWindowBase()
        self.subWindow_construction_parameters.setObjectName(u"subWindow_construction_parameters")
        self.subWindow_construction_parameters.setMinimumSize(QSize(330, 0))
        self.verticalLayout_9 = QVBoxLayout(self.subWindow_construction_parameters)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_N = QHBoxLayout()
        self.horizontalLayout_N.setObjectName(u"horizontalLayout_N")
        self.label_N = QLabel(self.subWindow_construction_parameters)
        self.label_N.setObjectName(u"label_N")

        self.horizontalLayout_N.addWidget(self.label_N)

        self.horizontalSpacer_N = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_N.addItem(self.horizontalSpacer_N)

        self.spinBox_N = SpinBoxQuantity(self.subWindow_construction_parameters)
        self.spinBox_N.setObjectName(u"spinBox_N")

        self.horizontalLayout_N.addWidget(self.spinBox_N)


        self.verticalLayout_9.addLayout(self.horizontalLayout_N)

        self.horizontalLayout_m = QHBoxLayout()
        self.horizontalLayout_m.setObjectName(u"horizontalLayout_m")
        self.label_m = QLabel(self.subWindow_construction_parameters)
        self.label_m.setObjectName(u"label_m")

        self.horizontalLayout_m.addWidget(self.label_m)

        self.horizontalSpacer_m = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_m.addItem(self.horizontalSpacer_m)

        self.spinBox_m = SpinBoxQuantity(self.subWindow_construction_parameters)
        self.spinBox_m.setObjectName(u"spinBox_m")

        self.horizontalLayout_m.addWidget(self.spinBox_m)


        self.verticalLayout_9.addLayout(self.horizontalLayout_m)

        self.horizontalLayout_m_shp = QHBoxLayout()
        self.horizontalLayout_m_shp.setObjectName(u"horizontalLayout_m_shp")
        self.label_m_shp = QLabel(self.subWindow_construction_parameters)
        self.label_m_shp.setObjectName(u"label_m_shp")

        self.horizontalLayout_m_shp.addWidget(self.label_m_shp)

        self.horizontalSpacer_m_shp = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_m_shp.addItem(self.horizontalSpacer_m_shp)

        self.spinBox_m_shp = SpinBoxQuantity(self.subWindow_construction_parameters)
        self.spinBox_m_shp.setObjectName(u"spinBox_m_shp")

        self.horizontalLayout_m_shp.addWidget(self.spinBox_m_shp)


        self.verticalLayout_9.addLayout(self.horizontalLayout_m_shp)

        self.horizontalLayout_alp = QHBoxLayout()
        self.horizontalLayout_alp.setObjectName(u"horizontalLayout_alp")
        self.label_alp = QLabel(self.subWindow_construction_parameters)
        self.label_alp.setObjectName(u"label_alp")

        self.horizontalLayout_alp.addWidget(self.label_alp)

        self.horizontalSpacer_alp = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_alp.addItem(self.horizontalSpacer_alp)

        self.doubleSpinBox_alp = QDoubleSpinBox(self.subWindow_construction_parameters)
        self.doubleSpinBox_alp.setObjectName(u"doubleSpinBox_alp")

        self.horizontalLayout_alp.addWidget(self.doubleSpinBox_alp)


        self.verticalLayout_9.addLayout(self.horizontalLayout_alp)

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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"OptiSolver", None))
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
        self.groupBox_a_b_sp.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0440\u0430\u043b\u044c\u043d\u044b\u0435 \u0440\u0435\u0431\u0440\u0430", None))
        self.label_a_sp.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u043b\u0449\u0438\u043d\u0430 \u0440\u0435\u0431\u0440\u0430", None))
        self.label_b_sp.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0441\u043e\u0442\u0430 \u0440\u0435\u0431\u0440\u0430", None))
        self.groupBox_a_b_col.setTitle(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u044c\u0446\u0435\u0432\u044b\u0435 \u0440\u0435\u0431\u0440\u0430", None))
        self.label_a_col.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u043b\u0449\u0438\u043d\u0430 \u0440\u0435\u0431\u0440\u0430", None))
        self.label_b_col.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0441\u043e\u0442\u0430 \u0440\u0435\u0431\u0440\u0430", None))
        self.groupBox_a_b_shp.setTitle(QCoreApplication.translate("MainWindow", u"\u0428\u043f\u0430\u043d\u0433\u043e\u0443\u0442", None))
        self.label_a_shp.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u043b\u0449\u0438\u043d\u0430 \u0440\u0435\u0431\u0440\u0430", None))
        self.label_b_shp.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0441\u043e\u0442\u0430 \u0440\u0435\u0431\u0440\u0430", None))
        self.subWindow_physical_mechanical_parameters.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u0437\u0438\u043a\u043e-\u043c\u0435\u0445\u0430\u043d\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438", None))
        self.groupBox_spiral.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0440\u0430\u043b\u044c\u043d\u044b\u0435 \u0440\u0435\u0431\u0440\u0430", None))
        self.label_Ex_spiral.setText(QCoreApplication.translate("MainWindow", u"E_x", None))
        self.label_Ey_spiral.setText(QCoreApplication.translate("MainWindow", u"E_y", None))
        self.label_Ez_spiral.setText(QCoreApplication.translate("MainWindow", u"E_z", None))
        self.label_Gxy_spiral.setText(QCoreApplication.translate("MainWindow", u"G_xy", None))
        self.label_Gyz_spiral.setText(QCoreApplication.translate("MainWindow", u"G_yz", None))
        self.label_Gxz_spiral.setText(QCoreApplication.translate("MainWindow", u"G_xz", None))
        self.label_v_spiral.setText(QCoreApplication.translate("MainWindow", u"v", None))
        self.groupBox_shp.setTitle(QCoreApplication.translate("MainWindow", u"\u0428\u043f\u0430\u043d\u0433\u043e\u0443\u0442", None))
        self.label_Ex_shp.setText(QCoreApplication.translate("MainWindow", u"E_x", None))
        self.label_Ey_shp.setText(QCoreApplication.translate("MainWindow", u"E_y", None))
        self.label_Ez_shp.setText(QCoreApplication.translate("MainWindow", u"E_z", None))
        self.label_Gxy_shp.setText(QCoreApplication.translate("MainWindow", u"G_xy", None))
        self.label_Gyz_shp.setText(QCoreApplication.translate("MainWindow", u"G_yz", None))
        self.label_Gxz_shp.setText(QCoreApplication.translate("MainWindow", u"G_xz", None))
        self.label_v_shp.setText(QCoreApplication.translate("MainWindow", u"v", None))
        self.groupBox_ring.setTitle(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u044c\u0446\u0435\u0432\u044b\u0435 \u0440\u0435\u0431\u0440\u0430", None))
        self.label_Ex_ring.setText(QCoreApplication.translate("MainWindow", u"E_x", None))
        self.label_Ey_ring.setText(QCoreApplication.translate("MainWindow", u"E_y", None))
        self.label_Ez_ring.setText(QCoreApplication.translate("MainWindow", u"E_z", None))
        self.label_Gxy_ring.setText(QCoreApplication.translate("MainWindow", u"G_xy", None))
        self.label_Gyz_ring.setText(QCoreApplication.translate("MainWindow", u"G_yz", None))
        self.label_Gxz_ring.setText(QCoreApplication.translate("MainWindow", u"G_xz", None))
        self.label_v_ring.setText(QCoreApplication.translate("MainWindow", u"v", None))
        self.subWindow_calculated_parameters.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0447\u0438\u0441\u043b\u0435\u043d\u043d\u044b\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b", None))
        self.label_M1.setText(QCoreApplication.translate("MainWindow", u"M_1", None))
        self.label_value_M1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_M2.setText(QCoreApplication.translate("MainWindow", u"M_2", None))
        self.label_value_M2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_M3.setText(QCoreApplication.translate("MainWindow", u"M_3", None))
        self.label_value_M3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_M4.setText(QCoreApplication.translate("MainWindow", u"M_4", None))
        self.label_value_M4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_M.setText(QCoreApplication.translate("MainWindow", u"M", None))
        self.label_value_M.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_V1.setText(QCoreApplication.translate("MainWindow", u"V_1", None))
        self.label_value_V1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_V2.setText(QCoreApplication.translate("MainWindow", u"V_2", None))
        self.label_value_V2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_V3.setText(QCoreApplication.translate("MainWindow", u"V_3", None))
        self.label_value_V3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_V4.setText(QCoreApplication.translate("MainWindow", u"V_4", None))
        self.label_value_V4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_p1.setText(QCoreApplication.translate("MainWindow", u"p_1", None))
        self.label_value_p1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_p2.setText(QCoreApplication.translate("MainWindow", u"p_2", None))
        self.label_value_p2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.subWindow_construction_parameters.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0438\u0441\u0445\u043e\u0434\u043d\u043e\u0439 \u043a\u043e\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u0438", None))
        self.label_N.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0438\u0441\u043b\u043e \u0441\u043f\u0438\u0440\u0430\u043b\u044c\u043d\u044b\u0445 \u0440\u0435\u0431\u0435\u0440", None))
        self.label_m.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0438\u0441\u043b\u043e \u043a\u043e\u043b\u044c\u0446\u0435\u0432\u044b\u0445 \u0440\u0435\u0431\u0435\u0440", None))
        self.label_m_shp.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0438\u0441\u043b\u043e \u0448\u043f\u0430\u043d\u0433\u043e\u0443\u0442\u043e\u0432", None))
        self.label_alp.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0433\u043e\u043b", None))
    # retranslateUi

