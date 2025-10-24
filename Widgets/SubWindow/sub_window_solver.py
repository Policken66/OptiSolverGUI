import os
import shutil
from pathlib import Path

from PySide6.QtWidgets import QPlainTextEdit, QPushButton
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

        self.pushButton_start_solver.clicked.connect(self.pushButton_start_solver_clicked)

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
        for f in Path(work_dir).iterdir():
            if f.suffix.lower() in (".out", ".rst", ".log", ".err"):
                target = results_dir / f.name
                shutil.copy2(f, target)
                produces_files.append(str(target))

        print(produces_files)
