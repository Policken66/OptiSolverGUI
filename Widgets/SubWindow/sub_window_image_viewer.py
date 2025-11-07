from pathlib import Path

from PySide6.QtGui import QPixmap, Qt
from PySide6.QtWidgets import QPushButton, QComboBox, QGraphicsView, QGraphicsScene

import Consts
from FileManager import file_manager
from Widgets.SubWindow.sub_window_base import SubWindowBase


class SubWindowImageViewer(SubWindowBase):
    def __init__(self):
        super().__init__()

    def _setup_ui(self):
        self.pushButton_load_images: QPushButton = self.findChild(QPushButton, "pushButton_load_images")
        self.comboBox_select_images: QComboBox = self.findChild(QComboBox, "comboBox_select_images")
        self.graphicsView_image_viewer: QGraphicsView = self.findChild(QGraphicsView, "graphicsView_image_viewer")

        self.pushButton_load_images.clicked.connect(self.pushButton_load_images_clicked)
        self.comboBox_select_images.currentIndexChanged.connect(self.comboBox_select_images_currentIndexChanged)
    def pushButton_load_images_clicked(self):
        work_dir = file_manager.dict_data_from_json(Consts.JSON_WIDGET_SETTINGS, ["lineEdit_work_dir"])[
            "lineEdit_work_dir"]

        # Получить все PNG файлы
        png_files = []
        work_path = Path(work_dir)
        if work_path.exists():
            png_files = [str(f.absolute()) for f in work_path.glob("*.png")]

        # Добавить в комбобокс
        self.comboBox_select_images.clear()
        for png_path in png_files:
            file_name = Path(png_path).name
            self.comboBox_select_images.addItem(file_name, png_path)

    def comboBox_select_images_currentIndexChanged(self):
        current_index = self.comboBox_select_images.currentIndex()
        full_path = self.comboBox_select_images.itemData(current_index)

        if full_path and Path(full_path).exists():
            # Создать сцену и добавить изображение
            scene = QGraphicsScene()
            pixmap = QPixmap(full_path)
            scene.addPixmap(pixmap)

            # Установить сцену в graphicsView
            self.graphicsView_image_viewer.setScene(scene)
            self.graphicsView_image_viewer.fitInView(scene.itemsBoundingRect(), Qt.KeepAspectRatio)

