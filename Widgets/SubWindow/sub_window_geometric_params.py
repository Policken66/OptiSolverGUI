from PySide6.QtWidgets import QDoubleSpinBox
from Widgets.SubWindow.sub_window_base import SubWindowBase


class SubWindowGeometricParams(SubWindowBase):
    def __init__(self):
        super().__init__()

    def _setup_ui(self):
        self.doubleSpinBox_R1: QDoubleSpinBox = self.findChild(QDoubleSpinBox, "doubleSpinBox_R1")
        self.doubleSpinBox_R2: QDoubleSpinBox = self.findChild(QDoubleSpinBox, "doubleSpinBox_R2")
        self.doubleSpinBox_H: QDoubleSpinBox = self.findChild(QDoubleSpinBox, "doubleSpinBox_H")

        # Для удобства сохраним в списки
        self.widget_names = self.get_widgets_name()
        self.widgets = self.get_widgets()
        # Загрузка параметров из JSON
        self.load_params(widgets=self.widgets, widget_names=self.widget_names)

    def get_widgets_name(self):
        return ["doubleSpinBox_R1", "doubleSpinBox_R2",
                "doubleSpinBox_H"]

    def get_widgets(self):
        return {
            "doubleSpinBox_R1": self.doubleSpinBox_R1,
            "doubleSpinBox_R2": self.doubleSpinBox_R2,
            "doubleSpinBox_H": self.doubleSpinBox_H,
        }
