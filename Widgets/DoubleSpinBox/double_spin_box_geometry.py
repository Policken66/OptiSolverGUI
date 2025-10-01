from PySide6.QtGui import QDoubleValidator
from PySide6.QtWidgets import QDoubleSpinBox, QWidget


class DoubleSpinBoxGeometry(QDoubleSpinBox):
    def __init__(self, parent: QWidget | None) -> None:
        super().__init__()
        validator = QDoubleValidator(0.0, 1e6, 3, self)
        self.lineEdit().setValidator(validator)
        self.setDecimals(3)
        self.setSingleStep(0.001)
        self.setSuffix(" м")
