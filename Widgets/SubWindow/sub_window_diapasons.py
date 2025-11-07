from PySide6.QtWidgets import QPushButton, QCheckBox, QSpinBox, QDoubleSpinBox

from Consts import JSON_WIDGET_SETTINGS
from FileManager import file_manager
from Widgets.SubWindow.sub_window_base import SubWindowBase


class SubWindowDiapasons(SubWindowBase):
    def __init__(self):
        super().__init__()

    def _setup_ui(self):
        self.pushButton_save_diapasons: QPushButton = self.findChild(QPushButton, "pushButton_save_diapasons")
        self.checkBox_diapasons_N: QCheckBox = self.findChild(QCheckBox, "checkBox_diapasons_N")
        self.checkBox_diapasons_alp: QCheckBox = self.findChild(QCheckBox, "checkBox_diapasons_alp")
        self.spinBox_diapasons_N0: QSpinBox = self.findChild(QSpinBox, "spinBox_diapasons_N0")
        self.spinBox_diapasons_Nn: QSpinBox = self.findChild(QSpinBox, "spinBox_diapasons_Nn")
        self.spinBox_diapasons_n: QSpinBox = self.findChild(QSpinBox, "spinBox_diapasons_n")
        self.doubleSpinBox_diapasons_alp0: QDoubleSpinBox = self.findChild(QDoubleSpinBox, "doubleSpinBox_diapasons_alp0")
        self.doubleSpinBox_diapasons_alp_k: QDoubleSpinBox = self.findChild(QDoubleSpinBox, "doubleSpinBox_diapasons_alp_k")
        self.doubleSpinBox_diapasons_n_alp: QDoubleSpinBox = self.findChild(QDoubleSpinBox, "doubleSpinBox_diapasons_n_alp")
        self.checkBox_diapasons_change_b: QCheckBox = self.findChild(QCheckBox, "checkBox_diapasons_change_b")
        self.checkBox_diapasons_change_h: QCheckBox = self.findChild(QCheckBox, "checkBox_diapasons_change_h")


        # Подключение сигналов
        self.pushButton_save_diapasons.clicked.connect(self.pushButton_save_diapasons_clicked)

        # Для удобства сохраним в списки
        self.widget_names = self.get_widgets_name()
        self.widgets = self.get_widgets()
        # Загрузка параметров из JSON
        self.load_params(widgets=self.widgets, widget_names=self.widget_names)


    def pushButton_save_diapasons_clicked(self):
        print("pushButton_save_diaposons_clicked")


    def get_widgets_name(self):
        return ["checkBox_diapasons_N", "checkBox_diapasons_alp",
                "spinBox_diapasons_N0", "spinBox_diapasons_Nn", "spinBox_diapasons_n",
                "doubleSpinBox_diapasons_alp0", "doubleSpinBox_diapasons_alp_k", "doubleSpinBox_diapasons_n_alp",
                "checkBox_diapasons_change_b", "checkBox_diapasons_change_h"]

    def get_widgets(self):
        return {
            "checkBox_diapasons_N": self.checkBox_diapasons_N,
            "checkBox_diapasons_alp": self.checkBox_diapasons_alp,
            "spinBox_diapasons_N0": self.spinBox_diapasons_N0,
            "spinBox_diapasons_Nn": self.spinBox_diapasons_Nn,
            "spinBox_diapasons_n": self.spinBox_diapasons_n,
            "doubleSpinBox_diapasons_alp0": self.doubleSpinBox_diapasons_alp0,
            "doubleSpinBox_diapasons_alp_k": self.doubleSpinBox_diapasons_alp_k,
            "doubleSpinBox_diapasons_n_alp": self.doubleSpinBox_diapasons_n_alp,
            "checkBox_diapasons_change_b": self.checkBox_diapasons_change_b,
            "checkBox_diapasons_change_h": self.checkBox_diapasons_change_h,
        }
