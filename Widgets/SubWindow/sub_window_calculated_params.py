from PySide6.QtWidgets import QLabel

from Widgets.SubWindow.sub_window_base import SubWindowBase


class SubWindowCalculatedParams(SubWindowBase):
    def __init__(self):
        super().__init__()

    def _setup_ui(self):
        self.label_value_M1: QLabel = self.findChild(QLabel, "label_value_M1")
        self.label_value_M2: QLabel = self.findChild(QLabel, "label_value_M2")
        self.label_value_M3: QLabel = self.findChild(QLabel, "label_value_M3")
        self.label_value_M4: QLabel = self.findChild(QLabel, "label_value_M4")
        self.label_value_M: QLabel = self.findChild(QLabel, "label_value_M")
        self.label_value_V1: QLabel = self.findChild(QLabel, "label_value_V1")
        self.label_value_V2: QLabel = self.findChild(QLabel, "label_value_V2")
        self.label_value_V3: QLabel = self.findChild(QLabel, "label_value_V3")
        self.label_value_V4: QLabel = self.findChild(QLabel, "label_value_V4")
        self.label_value_p1: QLabel = self.findChild(QLabel, "label_value_p1")
        self.label_value_p2: QLabel = self.findChild(QLabel, "label_value_p2")


