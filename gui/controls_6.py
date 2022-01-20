from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTabWidget, QToolBar, QGridLayout, QLabel, QPushButton
from PyQt5.QtMultimedia import QCameraInfo, QCamera
from PyQt5.QtMultimediaWidgets import QCameraViewfinder
from PyQt5.QtCore import Qt
# from PyQt5 import QtWidgets

import sys

class AzureUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.tool_bar = Tabs()

        self.setCentralWidget(Tabs())

class Tabs(QTabWidget):
    def __init__(self):
        super().__init__()

        self.camera_grid = QWidget()

        self.addTab(self.camera_grid, 'Cameras')
        self.addTab(QWidget(), 'okokok')
        self.setDocumentMode(True)
        self.setTabPosition(QTabWidget.West)

        # self.setMovable(False)


        # self.addWidget(QPushButton('okok'))
        # self.addWidget(self.tabs)
        # self.addWidget(QPushButton('ok'))
        # self.setStyleSheet('background-color: white; border-radius: 8px')

    def add_camera(self):
        pass

if __name__ == '__main__':
    app = QApplication([])

    # QtWidgets.QApplication.setStyle(ProxyStyle())

    window = AzureUI()
    window.show()

    sys.exit(app.exec())