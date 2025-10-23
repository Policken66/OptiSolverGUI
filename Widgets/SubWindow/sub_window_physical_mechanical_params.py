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
            "doubleSpinBox_v_sp", "doubleSpinBox_v_ring", "doubleSpinBox_v_shp"
        ]
        self.widgets = {}  # Словарь для хранения виджетов

    def _setup_ui(self):
        # Находим и сохраняем все виджеты
        for widget_name in self.widget_names:
            widget = self.findChild(DoubleSpinBoxMechanical, widget_name)
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
        values = file_manager.data_from_json(JSON_WIDGET_SETTINGS, self.widget_names)

        for widget_name, value in zip(self.widget_names, values):
            if value is not None and widget_name in self.widgets:
                self.widgets[widget_name].setValue(value)