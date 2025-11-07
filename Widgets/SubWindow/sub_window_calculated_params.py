from PySide6.QtWidgets import QLabel

from Widgets.SubWindow.sub_window_base import SubWindowBase


class SubWindowCalculatedParams(SubWindowBase):
    def __init__(self):
        super().__init__()
        self.label_names = [
            "label_value_M1", "label_value_M2", "label_value_M3", "label_value_M4",
            "label_value_M", "label_value_V1", "label_value_V2", "label_value_V3",
            "label_value_V4", "label_value_p1", "label_value_p2"
        ]

    def _setup_ui(self):
        for label_name in self.label_names:
            label = self.findChild(QLabel, label_name)
            if label:
                setattr(self, label_name, label)
