from PySide6.QtWidgets import QSpinBox, QWidget


class SpinBoxQuantity(QSpinBox):
    def __init__(self, parent: QWidget | None) -> None:
        super().__init__()
        self.setSuffix(" шт")
