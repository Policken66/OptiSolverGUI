from PySide6.QtCore import Signal
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget


class SubWindowBase(QWidget):
    hide_sub_window_signal = Signal()

    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("Widgets/SubWindow/Resources/Icons/parameters_icon.png"))

    def closeEvent(self, event):
        event.ignore()
        self.hide_sub_window_signal.emit()

    @property
    def window_id(self)->str:
        return self.windowTitle()

    def _setup_ui(self):
        pass

