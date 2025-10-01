from PySide6.QtCore import QMargins
from PySide6.QtGui import QDoubleValidator
from PySide6.QtWidgets import QDoubleSpinBox


class DoubleSpinBoxMechanical(QDoubleSpinBox):
    def __init__(self, parent):
        super().__init__()
        validator = QDoubleValidator(0.0, 1e12, 3, self)
        self.lineEdit().setValidator(validator)
        self.setDecimals(3)
        self.setSingleStep(1000.0)
        self.setMinimumWidth(150)



    def setObjectName(self, name, /):
        super().setObjectName(name)

        if "v_" in name:
            self.setRange(0.0, 0.5)
            self.setSingleStep(0.001)
        else:
            self.setSuffix(" Па")
            self.setRange(0.0, 1e12)  # До 1 триллиона Па doubleSpinBox_input_v_shp,