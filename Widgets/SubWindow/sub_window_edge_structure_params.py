from PySide6.QtWidgets import QDoubleSpinBox

from Widgets.SubWindow.sub_window_base import SubWindowBase


class SubWindowEdgeStructureParams(SubWindowBase):
    def __init__(self):
        super().__init__()

    def _setup_ui(self):
        self.doubleSpinBox_a_sp : QDoubleSpinBox = self.findChild(QDoubleSpinBox, "doubleSpinBox_a_sp")
        self.doubleSpinBox_b_sp : QDoubleSpinBox = self.findChild(QDoubleSpinBox, "doubleSpinBox_b_sp")

        self.doubleSpinBox_a_ring: QDoubleSpinBox = self.findChild(QDoubleSpinBox, "doubleSpinBox_a_ring")
        self.doubleSpinBox_b_ring: QDoubleSpinBox = self.findChild(QDoubleSpinBox, "doubleSpinBox_b_ring")

        self.doubleSpinBox_a_shp: QDoubleSpinBox = self.findChild(QDoubleSpinBox, "doubleSpinBox_a_shp")
        self.doubleSpinBox_b_shp: QDoubleSpinBox = self.findChild(QDoubleSpinBox, "doubleSpinBox_b_shp")
