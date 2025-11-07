from PySide6.QtWidgets import QDoubleSpinBox

from Consts import JSON_WIDGET_SETTINGS
from FileManager import file_manager
from Widgets.SubWindow.sub_window_base import SubWindowBase


class SubWindowEdgeStructureParams(SubWindowBase):
    def __init__(self):
        super().__init__()
        self.widget_names = [
            "doubleSpinBox_a_sp", "doubleSpinBox_b_sp",
            "doubleSpinBox_a_ring", "doubleSpinBox_b_ring",
            "doubleSpinBox_a_shp", "doubleSpinBox_b_shp"
        ]
        self.widgets = {}  # Словарь для хранения виджетов

    def _setup_ui(self):
        self.doubleSpinBox_a_sp: QDoubleSpinBox = self.findChild(QDoubleSpinBox, "doubleSpinBox_a_sp")
        self.doubleSpinBox_b_sp: QDoubleSpinBox = self.findChild(QDoubleSpinBox, "doubleSpinBox_b_sp")
        self.doubleSpinBox_a_ring: QDoubleSpinBox = self.findChild(QDoubleSpinBox, "doubleSpinBox_a_ring")
        self.doubleSpinBox_b_ring: QDoubleSpinBox = self.findChild(QDoubleSpinBox, "doubleSpinBox_b_ring")
        self.doubleSpinBox_a_shp: QDoubleSpinBox = self.findChild(QDoubleSpinBox, "doubleSpinBox_a_shp")
        self.doubleSpinBox_b_shp: QDoubleSpinBox = self.findChild(QDoubleSpinBox, "doubleSpinBox_b_shp")

        # Для удобства сохраним в списки
        self.widget_names = self.get_widgets_name()
        self.widgets = self.get_widgets()
        # Загрузка параметров из JSON
        self.load_params(widgets=self.widgets, widget_names=self.widget_names)

    def get_widgets_name(self):
        return ["doubleSpinBox_a_sp", "doubleSpinBox_b_sp",
                "doubleSpinBox_a_ring", "doubleSpinBox_b_ring",
                "doubleSpinBox_a_shp", "doubleSpinBox_b_shp"]

    def get_widgets(self):
        return {
            "doubleSpinBox_a_sp": self.doubleSpinBox_a_sp,
            "doubleSpinBox_b_sp": self.doubleSpinBox_b_sp,
            "doubleSpinBox_a_ring": self.doubleSpinBox_a_ring,
            "doubleSpinBox_b_ring": self.doubleSpinBox_b_ring,
            "doubleSpinBox_a_shp": self.doubleSpinBox_a_shp,
            "doubleSpinBox_b_shp": self.doubleSpinBox_b_shp,
        }

