from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTabBar, QVBoxLayout, QGridLayout, QLabel, QSlider, QPushButton, QStatusBar, QToolBar, QTabWidget
from PyQt5.QtMultimedia import QCameraInfo, QCamera
from PyQt5.QtMultimediaWidgets import QCameraViewfinder
from PyQt5.QtCore import Qt
# from PyQt5 import QtWidgets

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.layout = QVBoxLayout()

        # self.layout.addWidget(QPushButton('hello'))

        # self.status = QStatusBar()
        # self.setStatusBar(self.status)
        # self.status.setStatusTip('hello')

        # self.setStyleSheet('background-color: green')

        self.tabs = QTabBar()
        self.tabs.setDocumentMode(True)
        # self.setTabPosition()
        # self.tabs.setStyleSheet('color: green')
        # self.tabs.resize(300,200)
        # self.tabs.setTabTextColor()

        self.tool = QToolBar()
        self.tool.addWidget(QPushButton('hello'))
        self.tool.addWidget(self.tabs)
        self.tool.setMovable(False)
        self.tool.setStyleSheet('color: white')

        self.tabs.addTab('hello')
        # self.tabs.
        self.tabs.addTab('ok')
        self.tabs.addTab('ok')
        self.tabs.addTab('a')
        # self.tabs.setTabTextColor(0, Qt.red)

        # self.setCentralWidget(self.tool)
        self.addToolBar(self.tool)

        
        # self.tab = QTabBar()

if __name__ == '__main__':
    app = QApplication([])

    window = MainWindow()
    window.show()

    sys.exit(app.exec())