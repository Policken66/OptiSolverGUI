from PySide6.QtWidgets import QPushButton

from Widgets.SubWindow.sub_window_base import SubWindowBase


class SubWindowGenerator(SubWindowBase):
    def __init__(self):
        super().__init__()

    def _setup_ui(self):
        self.pushButton_start_generation: QPushButton = self.findChild(QPushButton, "pushButton_start_generation")
        self.pushButton_start_generation.clicked.connect(self.pushButton_start_generation_clicked)

    def pushButton_start_generation_clicked(self):
        print("pushButton_start_generation_clicked")
