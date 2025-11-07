import os
import shutil
from pathlib import Path

from PySide6.QtWidgets import QPlainTextEdit, QPushButton, QComboBox
from ansys.mapdl.core import launch_mapdl

import Consts
from FileManager import file_manager
from Widgets.SubWindow.sub_window_base import SubWindowBase


class SubWindowSolver(SubWindowBase):
    def __init__(self):
        super().__init__()

    def _setup_ui(self):
        self.pushButton_start_solver: QPushButton = self.findChild(QPushButton, "pushButton_start_solver")
        self.plainTextEdit_log_solver: QPlainTextEdit = self.findChild(QPlainTextEdit, "plainTextEdit_log_solver")
        self.plainTextEdit_log_solver.setReadOnly(True)
        self.comboBox_log_solver: QComboBox = self.findChild(QComboBox, "comboBox_log_solver")

        self.pushButton_start_solver.clicked.connect(self.pushButton_start_solver_clicked)
        self.comboBox_log_solver.currentIndexChanged.connect(self.comboBox_log_solver_currentIndexChanged)

    def pushButton_start_solver_clicked(self):
        work_dir = file_manager.dict_data_from_json(Consts.JSON_WIDGET_SETTINGS, ["lineEdit_work_dir"])["lineEdit_work_dir"]
        mapdl = launch_mapdl(
            run_location=str(work_dir),
            jobname="jobname",
        )
        mapdl.clear()
        absolute_path = os.path.abspath(Consts.TEMPLATE_TXT)
        mapdl.input(absolute_path)
        mapdl.finish()
        mapdl.exit()

        results_dir = Path(work_dir + "\\results\\")
        results_dir.mkdir(exist_ok=True)
        produces_files = []
        logs_files = []
        for f in Path(work_dir).iterdir():
            if f.suffix.lower() in (".out", ".rst", ".log", ".err"):
                target = results_dir / f.name
                shutil.copy2(f, target)
                full_path = str(target.absolute())  # ← ПОЛНЫЙ АБСОЛЮТНЫЙ ПУТЬ
                produces_files.append(full_path)

                if f.suffix.lower() in (".out", ".log", ".err"):
                    logs_files.append(full_path)

        self.comboBox_log_solver.clear()
        for log_path in logs_files:
            file_name = Path(log_path).name
            self.comboBox_log_solver.addItem(file_name, log_path)

    def comboBox_log_solver_currentIndexChanged(self):
        # Получить полный путь
        current_index = self.comboBox_log_solver.currentIndex()
        full_path = self.comboBox_log_solver.itemData(current_index)

        # Если данные не хранятся, получить текст
        if not full_path:
            full_path = self.comboBox_log_solver.currentText()

        text = file_manager.get_all_text(full_path)
        self.plainTextEdit_log_solver.setPlainText(text)

