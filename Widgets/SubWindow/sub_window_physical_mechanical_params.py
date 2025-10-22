from Widgets.DoubleSpinBox.double_spin_box_mechanical import DoubleSpinBoxMechanical
from Widgets.SubWindow.sub_window_base import SubWindowBase


class SubWindowPhysicalMechanicalParams(SubWindowBase):
    def __init__(self):
        super().__init__()

    def _setup_ui(self):
        self.doubleSpinBox_Ex_sp: DoubleSpinBoxMechanical = self.findChild(DoubleSpinBoxMechanical,
                                                                           "doubleSpinBox_Ex_sp")
        self.doubleSpinBox_Ex_ring: DoubleSpinBoxMechanical = self.findChild(DoubleSpinBoxMechanical,
                                                                             "doubleSpinBox_Ex_ring")
        self.doubleSpinBox_Ex_shp: DoubleSpinBoxMechanical = self.findChild(DoubleSpinBoxMechanical,
                                                                            "doubleSpinBox_Ex_shp")

        self.doubleSpinBox_Ey_sp: DoubleSpinBoxMechanical = self.findChild(DoubleSpinBoxMechanical,
                                                                           "doubleSpinBox_Ey_sp")
        self.doubleSpinBox_Ey_ring: DoubleSpinBoxMechanical = self.findChild(DoubleSpinBoxMechanical,
                                                                             "doubleSpinBox_Ey_ring")
        self.doubleSpinBox_Ey_shp: DoubleSpinBoxMechanical = self.findChild(DoubleSpinBoxMechanical,
                                                                            "doubleSpinBox_Ey_shp")

        self.doubleSpinBox_Ez_sp: DoubleSpinBoxMechanical = self.findChild(DoubleSpinBoxMechanical,
                                                                           "doubleSpinBox_Ez_sp")
        self.doubleSpinBox_Ez_ring: DoubleSpinBoxMechanical = self.findChild(DoubleSpinBoxMechanical,
                                                                             "doubleSpinBox_Ez_ring")
        self.doubleSpinBox_Ez_shp: DoubleSpinBoxMechanical = self.findChild(DoubleSpinBoxMechanical,
                                                                            "doubleSpinBox_Ez_shp")

        self.doubleSpinBox_Gxy_sp: DoubleSpinBoxMechanical = self.findChild(DoubleSpinBoxMechanical,
                                                                           "doubleSpinBox_Gxy_sp")
        self.doubleSpinBox_Gxy_ring: DoubleSpinBoxMechanical = self.findChild(DoubleSpinBoxMechanical,
                                                                             "doubleSpinBox_Gxy_ring")
        self.doubleSpinBox_Gxy_shp: DoubleSpinBoxMechanical = self.findChild(DoubleSpinBoxMechanical,
                                                                            "doubleSpinBox_Gxy_shp")

        self.doubleSpinBox_Gyz_sp: DoubleSpinBoxMechanical = self.findChild(DoubleSpinBoxMechanical,
                                                                            "doubleSpinBox_Gyz_sp")
        self.doubleSpinBox_Gyz_ring: DoubleSpinBoxMechanical = self.findChild(DoubleSpinBoxMechanical,
                                                                              "doubleSpinBox_Gyz_ring")
        self.doubleSpinBox_Gyz_shp: DoubleSpinBoxMechanical = self.findChild(DoubleSpinBoxMechanical,
                                                                             "doubleSpinBox_Gyz_shp")

        self.doubleSpinBox_Gxz_sp: DoubleSpinBoxMechanical = self.findChild(DoubleSpinBoxMechanical,
                                                                            "doubleSpinBox_Gxz_sp")
        self.doubleSpinBox_Gxz_ring: DoubleSpinBoxMechanical = self.findChild(DoubleSpinBoxMechanical,
                                                                              "doubleSpinBox_Gxz_ring")
        self.doubleSpinBox_Gxz_shp: DoubleSpinBoxMechanical = self.findChild(DoubleSpinBoxMechanical,
                                                                             "doubleSpinBox_Gxz_shp")

        self.doubleSpinBox_v_sp: DoubleSpinBoxMechanical = self.findChild(DoubleSpinBoxMechanical,
                                                                            "doubleSpinBox_v_sp")
        self.doubleSpinBox_v_ring: DoubleSpinBoxMechanical = self.findChild(DoubleSpinBoxMechanical,
                                                                              "doubleSpinBox_v_ring")
        self.doubleSpinBox_v_shp: DoubleSpinBoxMechanical = self.findChild(DoubleSpinBoxMechanical,
                                                                             "doubleSpinBox_v_shp")
