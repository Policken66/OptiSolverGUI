from PySide6.QtCore import Signal, QDate, QDateTime, QTime
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QSpinBox, QDoubleSpinBox, QSlider, QCheckBox, QLineEdit, QComboBox, QTextEdit, \
    QPlainTextEdit, QRadioButton, QDateEdit, QDateTimeEdit, QTimeEdit, QPushButton

from Consts import JSON_WIDGET_SETTINGS
from FileManager import file_manager


class SubWindowBase(QWidget):
    hide_sub_window_signal = Signal()

    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("Widgets/SubWindow/Resources/Icons/parameters_icon.png"))

    def closeEvent(self, event):
        event.ignore()
        self.hide_sub_window_signal.emit()

    @property
    def window_id(self) -> str:
        return self.windowTitle()

    def _setup_ui(self):
        pass

    def get_widget_value(self, widget):
        """Получение значения из виджета"""
        if isinstance(widget, (QSpinBox, QDoubleSpinBox, QSlider)):
            return widget.value()
        elif isinstance(widget, QCheckBox):
            return widget.isChecked()
        elif isinstance(widget, QLineEdit):
            return widget.text()
        elif isinstance(widget, QComboBox):
            return widget.currentText()  # или currentIndex() для индекса
        elif isinstance(widget, (QTextEdit, QPlainTextEdit)):
            return widget.toPlainText()
        elif isinstance(widget, QRadioButton):
            return widget.isChecked()
        elif isinstance(widget, QDateEdit):
            return widget.date().toString("yyyy-MM-dd")
        elif isinstance(widget, QDateTimeEdit):
            return widget.dateTime().toString("yyyy-MM-dd hh:mm:ss")
        elif isinstance(widget, QTimeEdit):
            return widget.time().toString("hh:mm:ss")
        elif isinstance(widget, QPushButton):
            return None  # Не сохраняем состояние кнопок
        return None

    def set_widget_value(self, widget, value):
        """Установка значения в виджет"""
        if value is None:
            return

        try:
            if isinstance(widget, (QSpinBox, QDoubleSpinBox)):
                widget.setValue(float(value))
            elif isinstance(widget, QSlider):
                widget.setValue(int(value))
            elif isinstance(widget, QCheckBox):
                widget.setChecked(bool(value))
            elif isinstance(widget, QLineEdit):
                widget.setText(str(value))
            elif isinstance(widget, QComboBox):
                # Пытаемся найти текст
                index = widget.findText(str(value))
                if index >= 0:
                    widget.setCurrentIndex(index)
                else:
                    # Если текст не найден, пробуем как индекс
                    try:
                        widget.setCurrentIndex(int(value))
                    except (ValueError, TypeError):
                        pass
            elif isinstance(widget, (QTextEdit, QPlainTextEdit)):
                widget.setPlainText(str(value))
            elif isinstance(widget, QRadioButton):
                widget.setChecked(bool(value))
            elif isinstance(widget, QDateEdit):
                date = QDate.fromString(str(value), "yyyy-MM-dd")
                if date.isValid():
                    widget.setDate(date)
            elif isinstance(widget, QDateTimeEdit):
                datetime = QDateTime.fromString(str(value), "yyyy-MM-dd hh:mm:ss")
                if datetime.isValid():
                    widget.setDateTime(datetime)
            elif isinstance(widget, QTimeEdit):
                time = QTime.fromString(str(value), "hh:mm:ss")
                if time.isValid():
                    widget.setTime(time)
        except (ValueError, TypeError) as e:
            print(f"Ошибка установки значения {value} для {widget}: {e}")

    def save_params(self, json_key=JSON_WIDGET_SETTINGS, widgets=None, widget_names=None):
        """
        Универсальное сохранение параметров для всех подклассов
        """
        if widgets is None: return
        if widget_names is None: return

        target_widgets = widgets
        target_names = widget_names

        data = []
        for widget_name in target_names:
            if widget_name in target_widgets:
                widget = target_widgets[widget_name]
                value = self.get_widget_value(widget)

                # Сохраняем только если значение не None (исключаем кнопки и т.д.)
                if value is not None:
                    data.append((widget_name, value))

        file_manager.json_update(json_key, data)

    def load_params(self, json_key=JSON_WIDGET_SETTINGS, widgets=None, widget_names=None):
        """
        Универсальная загрузка параметров для всех подклассов
        """
        if widgets is None: return
        if widget_names is None: return

        target_widgets = widgets
        target_names = widget_names

        values = file_manager.data_from_json(json_key, target_names)

        for widget_name, value in zip(target_names, values):
            if value is not None and widget_name in target_widgets:
                widget = target_widgets[widget_name]
                self.set_widget_value(widget, value)

    def get_widgets_name(self):
        pass

    def get_widgets(self):
        pass
