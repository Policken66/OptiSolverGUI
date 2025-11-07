from Consts import JSON_WIDGET_SETTINGS
from FileManager import file_manager
from Widgets.DoubleSpinBox.double_spin_box_mechanical import DoubleSpinBoxMechanical
from Widgets.SubWindow.sub_window_base import SubWindowBase


class SubWindowPhysicalMechanicalParams(SubWindowBase):
    def __init__(self):
        super().__init__()
        self.widget_names = [
            "doubleSpinBox_Ex_sp", "doubleSpinBox_Ex_ring", "doubleSpinBox_Ex_shp",
            "doubleSpinBox_Ey_sp", "doubleSpinBox_Ey_ring", "doubleSpinBox_Ey_shp",
            "doubleSpinBox_Ez_sp", "doubleSpinBox_Ez_ring", "doubleSpinBox_Ez_shp",
            "doubleSpinBox_Gxy_sp", "doubleSpinBox_Gxy_ring", "doubleSpinBox_Gxy_shp",
            "doubleSpinBox_Gyz_sp", "doubleSpinBox_Gyz_ring", "doubleSpinBox_Gyz_shp",
            "doubleSpinBox_Gxz_sp", "doubleSpinBox_Gxz_ring", "doubleSpinBox_Gxz_shp",
            "doubleSpinBox_v_sp", "doubleSpinBox_v_ring", "doubleSpinBox_v_shp",
            "doubleSpinBox_rho_sp", "doubleSpinBox_rho_ring", "doubleSpinBox_rho_shp"
        ]
        self.widgets = {}  # Словарь для хранения виджетов

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
        self.doubleSpinBox_v_sp: DoubleSpinBoxMechanical = self.findChild(DoubleSpinBoxMechanical, "doubleSpinBox_v_sp")
        self.doubleSpinBox_v_ring: DoubleSpinBoxMechanical = self.findChild(DoubleSpinBoxMechanical,
                                                                            "doubleSpinBox_v_ring")
        self.doubleSpinBox_v_shp: DoubleSpinBoxMechanical = self.findChild(DoubleSpinBoxMechanical,
                                                                           "doubleSpinBox_v_shp")
        self.doubleSpinBox_rho_sp: DoubleSpinBoxMechanical = self.findChild(DoubleSpinBoxMechanical,
                                                                            "doubleSpinBox_rho_sp")
        self.doubleSpinBox_rho_ring: DoubleSpinBoxMechanical = self.findChild(DoubleSpinBoxMechanical,
                                                                              "doubleSpinBox_rho_ring")
        self.doubleSpinBox_rho_shp: DoubleSpinBoxMechanical = self.findChild(DoubleSpinBoxMechanical,
                                                                             "doubleSpinBox_rho_shp")

        # Для удобства сохраним в списки
        self.widget_names = self.get_widgets_name()
        self.widgets = self.get_widgets()
        # Загрузка параметров из JSON
        self.load_params(widgets=self.widgets, widget_names=self.widget_names)

    def get_widgets_name(self):
        return ["doubleSpinBox_Ex_sp", "doubleSpinBox_Ex_ring", "doubleSpinBox_Ex_shp",
                "doubleSpinBox_Ey_sp", "doubleSpinBox_Ey_ring", "doubleSpinBox_Ey_shp",
                "doubleSpinBox_Ez_sp", "doubleSpinBox_Ez_ring", "doubleSpinBox_Ez_shp",
                "doubleSpinBox_Gxy_sp", "doubleSpinBox_Gxy_ring", "doubleSpinBox_Gxy_shp",
                "doubleSpinBox_Gyz_sp", "doubleSpinBox_Gyz_ring", "doubleSpinBox_Gyz_shp",
                "doubleSpinBox_Gxz_sp", "doubleSpinBox_Gxz_ring", "doubleSpinBox_Gxz_shp",
                "doubleSpinBox_v_sp", "doubleSpinBox_v_ring", "doubleSpinBox_v_shp",
                "doubleSpinBox_rho_sp", "doubleSpinBox_rho_ring", "doubleSpinBox_rho_shp"]

    def get_widgets(self):
        return {
            "doubleSpinBox_Ex_sp": self.doubleSpinBox_Ex_sp,
            "doubleSpinBox_Ex_ring": self.doubleSpinBox_Ex_ring,
            "doubleSpinBox_Ex_shp": self.doubleSpinBox_Ex_shp,
            "doubleSpinBox_Ey_sp": self.doubleSpinBox_Ey_sp,
            "doubleSpinBox_Ey_ring": self.doubleSpinBox_Ey_ring,
            "doubleSpinBox_Ey_shp": self.doubleSpinBox_Ey_shp,
            "doubleSpinBox_Ez_sp": self.doubleSpinBox_Ez_sp,
            "doubleSpinBox_Ez_ring": self.doubleSpinBox_Ez_ring,
            "doubleSpinBox_Ez_shp": self.doubleSpinBox_Ez_shp,
            "doubleSpinBox_Gxy_sp": self.doubleSpinBox_Gxy_sp,
            "doubleSpinBox_Gxy_ring": self.doubleSpinBox_Gxy_ring,
            "doubleSpinBox_Gxy_shp": self.doubleSpinBox_Gxy_shp,
            "doubleSpinBox_Gyz_sp": self.doubleSpinBox_Gyz_sp,
            "doubleSpinBox_Gyz_ring": self.doubleSpinBox_Gyz_ring,
            "doubleSpinBox_Gyz_shp": self.doubleSpinBox_Gyz_shp,
            "doubleSpinBox_Gxz_sp": self.doubleSpinBox_Gxz_sp,
            "doubleSpinBox_Gxz_ring": self.doubleSpinBox_Gxz_ring,
            "doubleSpinBox_Gxz_shp": self.doubleSpinBox_Gxz_shp,
            "doubleSpinBox_v_sp": self.doubleSpinBox_v_sp,
            "doubleSpinBox_v_ring": self.doubleSpinBox_v_ring,
            "doubleSpinBox_v_shp": self.doubleSpinBox_v_shp,
            "doubleSpinBox_rho_sp": self.doubleSpinBox_rho_sp,
            "doubleSpinBox_rho_ring": self.doubleSpinBox_rho_ring,
            "doubleSpinBox_rho_shp": self.doubleSpinBox_rho_shp,
        }
