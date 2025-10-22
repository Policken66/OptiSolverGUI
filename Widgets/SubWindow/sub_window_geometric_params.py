from PySide6.QtWidgets import QDoubleSpinBox

from Widgets.SubWindow.sub_window_base import SubWindowBase


class SubWindowGeometricParams(SubWindowBase):
    def __init__(self):
        super().__init__()

    def _setup_ui(self):
        self.doubleSpinBox_R1 : QDoubleSpinBox = self.findChild(QDoubleSpinBox, "doubleSpinBox_R1")
        self.doubleSpinBox_R2 : QDoubleSpinBox = self.findChild(QDoubleSpinBox, "doubleSpinBox_R2")
        self.doubleSpinBox_H : QDoubleSpinBox = self.findChild(QDoubleSpinBox, "doubleSpinBox_H")