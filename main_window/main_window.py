from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QWidget, QMdiSubWindow

from UI.main_window import Ui_MainWindow
from Widgets.SubWindow.sub_window_base import SubWindowBase


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, main_window):
        super().setupUi(main_window)

        self.setWindowIcon(QIcon("main_window/Resources/Icons/satellite_icon.png"))

        # карта: окно -> кнопка
        self.sub_to_btn = self.collect_sub_to_btn()

        for sub, btn in self.sub_to_btn.items():
            btn.toggled.connect(lambda checked, s=sub: self.set_sub_window_visible(s, checked))

        for sub, btn in self.sub_to_btn.items():
            sub.hide_sub_window_signal.connect(lambda s=sub: self._on_request_hide(s))

        self.hide_all_sub_windows()
        self._sub_window_setup_ui()

    def set_sub_window_visible(self, sub_window: SubWindowBase, visible: bool):
        """
        Единая точка управления видимостью MDI-подокон.
        Показывает/скрывает именно QMdiSubWindow (рамку/вкладку), а не только содержимое.
        Дополнительно синхронизирует состояния соответствующей кнопки.

        :param sub_window: Виджет (наследник SubWindowBase).
        :param visible: True - показать, False - скрыть.
        """
        q_mdi_sub = self._q_mdi_sub_for(sub_window)
        if not q_mdi_sub:
            return
        q_mdi_sub.setVisible(visible)
        if visible:
            self.mdiArea.setActiveSubWindow(q_mdi_sub)

        btn = self.sub_to_btn.get(sub_window)
        if btn:
            old = btn.blockSignals(True)
            btn.setChecked(visible)
            btn.blockSignals(old)

    def _on_request_hide(self, sub_window: SubWindowBase):
        """Обработчик сигнала (закрыть) от 'подокна': просто скрываем подокно целиком."""
        self.set_sub_window_visible(sub_window, False)

    def _q_mdi_sub_for(self, inner_widget: QWidget) -> None | QMdiSubWindow:
        """
        Находит QMidSubWindow, в котором лежит указанный виджет.

        :param inner_widget: Виджет, добавленный как содержимое QMdiSubWindow.
        :return: Соответствующий QMdiSubWindow или None, если не найден.
        """
        for q_mdi_sub in self.mdiArea.subWindowList():
            if q_mdi_sub.widget() is inner_widget:
                return q_mdi_sub
        return None

    def hide_all_sub_windows(self):
        """Скрывает все 'подокна' в MDI-области (без удаления)."""
        for sub_window in self.mdiArea.subWindowList():
            sub_window.hide()

    def collect_sub_to_btn(self) -> dict:
        """
        Собрать все соответствия "подокно -> кнопка". Чтобы каждое подокно знало о кнопке которая его вызывает.
        Привязка выполняется один раз при инициализации. При добавлении нового подокна достаточно расширить словарь одной строкой.

        :return: Словарь {SubWindowBase: QPushButton}.
        """
        return {
            self.subWindow_geometric_parameters: self.pushButton_geometric_parameters,
            self.subWindow_construction_parameters: self.pushButton_construction_parameters,
            self.subWindow_physical_mechanical_parameters: self.pushButton_physical_mechanical_parameters,
            self.subWindow_edge_structure_parameters: self.pushButton_edge_structure_parameters,
            self.subWindow_calculated_parameters: self.pushButton_calculated_peremeters,
        }

    def _sub_window_setup_ui(self):
        for sub_window in self.findChildren(SubWindowBase, QRegularExpression("subWindow_*")):
            sub_window._setup_ui()