from PySide6.QtCore import Signal
from PySide6.QtWidgets import QPushButton, QPlainTextEdit, QLineEdit, QToolButton

import Consts
from FileManager import file_manager
from Widgets.SubWindow.sub_window_base import SubWindowBase


class SubWindowGenerator(SubWindowBase):
    start_generation_signal = Signal()

    def __init__(self):
        super().__init__()
        self.widget_names = [
            "lineEdit_work_dir"
        ]

    def _setup_ui(self):
        self.pushButton_start_generation: QPushButton = self.findChild(QPushButton, "pushButton_start_generation")
        self.plainTextEdit_generator: QPlainTextEdit = self.findChild(QPlainTextEdit, "plainTextEdit_generator")
        self.plainTextEdit_generator.setReadOnly(True)
        self.lineEdit_work_dir: QLineEdit = self.findChild(QLineEdit, "lineEdit_work_dir")
        self.toolButton_select_work_dir: QToolButton = self.findChild(QToolButton, "toolButton_select_work_dir")

        self.pushButton_start_generation.clicked.connect(self.pushButton_start_generation_clicked)
        self.toolButton_select_work_dir.clicked.connect(self.toolButton_select_work_dir_clicked)

        self._load_params()

    def pushButton_start_generation_clicked(self):
        self.start_generation_signal.emit()
        self._convert_params()

    def toolButton_select_work_dir_clicked(self):
        print("ddd")

    def _convert_params(self):
        names = ["doubleSpinBox_a_sp", "doubleSpinBox_b_sp", "doubleSpinBox_a_ring",
                 "doubleSpinBox_b_ring", "doubleSpinBox_a_shp", "doubleSpinBox_b_shp",
                 "spinBox_N", "spinBox_m", "doubleSpinBox_R1", "doubleSpinBox_R2",
                 "doubleSpinBox_H", "doubleSpinBox_alp"]
        data = file_manager.dict_data_from_json(Consts.JSON_WIDGET_SETTINGS, names)

        # Вычисление диаметра с проверкой
        r1 = data["doubleSpinBox_R1"] or 0
        r2 = data["doubleSpinBox_R2"] or 0
        diameter = (r1 + r2) / 2 if r1 and r2 else 0

        parametrs_for_mapdl_model = []

        parametrs_for_mapdl_model.append(('a11', data["doubleSpinBox_a_sp"]))
        parametrs_for_mapdl_model.append(('b11', data["doubleSpinBox_b_sp"]))
        parametrs_for_mapdl_model.append(('c', data["doubleSpinBox_a_ring"]))
        parametrs_for_mapdl_model.append(('dd', data["doubleSpinBox_b_ring"]))
        parametrs_for_mapdl_model.append(('a22', data["doubleSpinBox_a_shp"]))
        parametrs_for_mapdl_model.append(('b22', data["doubleSpinBox_b_shp"]))
        parametrs_for_mapdl_model.append(('N', data["spinBox_N"]))
        parametrs_for_mapdl_model.append(('m', data["spinBox_m"]))
        # Вычисляем диаметр
        r1 = data["doubleSpinBox_R1"] or 0
        r2 = data["doubleSpinBox_R2"] or 0
        diameter = (r1 + r2) / 2 if r1 and r2 else 0
        parametrs_for_mapdl_model.append(('d', diameter))

        parametrs_for_mapdl_model.append(('HH', data["doubleSpinBox_H"]))
        parametrs_for_mapdl_model.append(('alp', data["doubleSpinBox_alp"]))

        file_manager.json_update(Consts.JSON_APDL_PARAMS, parametrs_for_mapdl_model)

        print("Успешная генерация JSON файла")

        params_for_temlate = file_manager.extract_parameters_from_json(Consts.JSON_APDL_PARAMS)
        file_manager.change_params_in_template(Consts.TEMPLATE_TXT, params_for_temlate)

        template_text = file_manager.get_all_text(Consts.TEMPLATE_TXT)
        self.plainTextEdit_generator.setPlainText(template_text)

    def _save_params(self):
        data = []
        data.append(("lineEdit_work_dir", self.lineEdit_work_dir.text()))
        file_manager.json_update(Consts.JSON_WIDGET_SETTINGS, data)

    def _load_params(self):
        values = file_manager.data_from_json(Consts.JSON_WIDGET_SETTINGS, self.widget_names)
        self.lineEdit_work_dir.setText(values[0])
