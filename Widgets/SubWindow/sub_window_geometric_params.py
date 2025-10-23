from PySide6.QtWidgets import QDoubleSpinBox

from Consts import JSON_WIDGET_SETTINGS
from FileManager import file_manager
from Widgets.SubWindow.sub_window_base import SubWindowBase


class SubWindowGeometricParams(SubWindowBase):
    def __init__(self):
        super().__init__()
        self.widget_names = [
            "doubleSpinBox_R1", "doubleSpinBox_R2", "doubleSpinBox_H"
        ]
        self.widgets = {}  # Словарь для хранения виджетов

    def _setup_ui(self):
        # Находим и сохраняем все виджеты
        for widget_name in self.widget_names:
            widget = self.findChild(QDoubleSpinBox, widget_name)
            if widget:
                self.widgets[widget_name] = widget
                setattr(self, widget_name, widget)  # Для обратной совместимости

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
                self.widgets[widget_name].setValue(value)