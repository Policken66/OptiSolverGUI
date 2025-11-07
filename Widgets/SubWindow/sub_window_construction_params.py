from PySide6.QtWidgets import QSpinBox, QDoubleSpinBox
from Widgets.SubWindow.sub_window_base import SubWindowBase


class SubWindowConstructionParams(SubWindowBase):
    def __init__(self):
        super().__init__()

    def _setup_ui(self):
        self.spinBox_N: QSpinBox = self.findChild(QSpinBox, "spinBox_N")
        self.spinBox_m: QSpinBox = self.findChild(QSpinBox, "spinBox_m")
        self.spinBox_m_shp: QSpinBox = self.findChild(QSpinBox, "spinBox_m_shp")
        self.doubleSpinBox_alp: QDoubleSpinBox = self.findChild(QDoubleSpinBox, "doubleSpinBox_alp")

        # Для удобства сохраним в списки
        self.widget_names = self.get_widgets_name()
        self.widgets = self.get_widgets()
        # Загрузка параметров из JSON
        self.load_params(widgets=self.widgets, widget_names=self.widget_names)

    def get_widgets_name(self):
        return ["spinBox_N", "spinBox_m",
                "spinBox_m_shp", "doubleSpinBox_alp"]

    def get_widgets(self):
        return {
            "spinBox_N": self.spinBox_N,
            "spinBox_m": self.spinBox_m,
            "spinBox_m_shp": self.spinBox_m_shp,
            "doubleSpinBox_alp": self.doubleSpinBox_alp
        }
