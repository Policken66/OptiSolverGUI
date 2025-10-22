from PySide6.QtWidgets import QSpinBox, QDoubleSpinBox

from Widgets.SubWindow.sub_window_base import SubWindowBase


class SubWindowConstructionParams(SubWindowBase):
    def __init__(self):
        super().__init__()

    def _setup_ui(self):
        self.spinBox_N : QSpinBox = self.findChild(QSpinBox, "spinBox_N")
        self.spinBox_m : QSpinBox = self.findChild(QSpinBox, "spinBox_m")
        self.spinBox_m_shp : QSpinBox = self.findChild(QSpinBox, "spinBox_m_shp")
        self.doubleSpinBox_alp : QDoubleSpinBox = self.findChild(QDoubleSpinBox, "doubleSpinBox_alp")

