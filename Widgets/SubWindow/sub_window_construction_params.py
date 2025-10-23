from PySide6.QtWidgets import QSpinBox, QDoubleSpinBox

from Consts import JSON_WIDGET_SETTINGS
from FileManager import file_manager
from Widgets.SubWindow.sub_window_base import SubWindowBase


class SubWindowConstructionParams(SubWindowBase):
    def __init__(self):
        super().__init__()
        self.widget_names = [
            "spinBox_N", "spinBox_m", "spinBox_m_shp", "doubleSpinBox_alp"
        ]
        self.widgets = {}

    def _setup_ui(self):
        for widget_name in self.widget_names:
            widget = self.findChild(QSpinBox, widget_name)
            if not widget:
                widget = self.findChild(QDoubleSpinBox, widget_name)

            if widget:
                self.widgets[widget_name] = widget
                setattr(self, widget_name, widget)

        self._load_params()

    def _save_params(self):
        data = []
        for widget_name, widget in self.widgets.items():
            data.append((widget_name, widget.value()))

        file_manager.json_update(JSON_WIDGET_SETTINGS, data)

    def _load_params(self):
        values = file_manager.data_update_from_json(JSON_WIDGET_SETTINGS, self.widget_names)
        for widget_name, value in zip(self.widget_names, values):
            if value is not None and widget_name in self.widgets:
                widget = self.widgets[widget_name]
                widget.setValue(value)
