from PySide6.QtWidgets import QPushButton

from Widgets.SubWindow.sub_window_base import SubWindowBase


class SubWindowDiapasons(SubWindowBase):
    def __init__(self):
        super().__init__()

    def _setup_ui(self):
        self.pushButton_save_diapasons: QPushButton = self.findChild(QPushButton, "pushButton_save_diapasons")

        self.pushButton_save_diapasons.clicked.connect(self.pushButton_save_diapasons_clicked)


    def pushButton_save_diapasons_clicked(self):
        print("pushButton_save_diaposons_clicked")