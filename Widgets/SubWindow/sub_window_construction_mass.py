from PySide6.QtWidgets import QCheckBox

from Widgets.SubWindow.sub_window_base import SubWindowBase


class SubWindowConstructionMass(SubWindowBase):
    def __init__(self):
        super().__init__()

    def _setup_ui(self):
        self.checkBox_constMass_Mc : QCheckBox = self.findChild(QCheckBox, "checkBox_constMass_Mc")
        self.checkBox_constMass_M : QCheckBox = self.findChild(QCheckBox, "checkBox_constMass_M")

        # Для удобства сохраним в списки
        self.widget_names = self.get_widgets_name()
        self.widgets = self.get_widgets()
        # Загрузка параметров из JSON
        self.load_params(widgets=self.widgets, widget_names=self.widget_names)


    def get_widgets_name(self):
        return ["checkBox_constMass_Mc", "checkBox_constMass_M"]

    def get_widgets(self):
        return {
            "checkBox_constMass_Mc": self.checkBox_constMass_Mc,
            "checkBox_constMass_M": self.checkBox_constMass_M,
        }