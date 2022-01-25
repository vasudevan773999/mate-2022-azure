from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTabWidget, QTabBar, QToolBar, QGridLayout, QLabel, QPushButton, QStatusBar
from PyQt5.QtMultimedia import QCameraInfo, QCamera
from PyQt5.QtMultimediaWidgets import QCameraViewfinder
from PyQt5.QtCore import Qt

import sys
import yaml
import logging

class AzureUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Azure UI')
        self.setStyleSheet('background: rgb(40,40,40)')

        self.tabs = Tabs()
        # self.tabs.setStyleSheet('border-top: rgb(40,40,40)')


        self.setCentralWidget(self.tabs)


class Tabs(QTabWidget):
    def __init__(self):
        super().__init__()

        self.camera_tab = CameraTab()
        self.logs_tab = LogsTab()
        self.settings_tab = SettingsTab()

        self.addTab(self.camera_tab, 'Camera Grid')
        self.addTab(Camera(settings_yml['camera-ports']['cam-1']), 'Camera 1')
        self.addTab(Camera(settings_yml['camera-ports']['cam-2']), 'Camera 2')
        self.addTab(Camera(settings_yml['camera-ports']['cam-3']), 'Camera 3')
        self.addTab(Camera(settings_yml['camera-ports']['cam-4']), 'Camera 4')
        self.addTab(self.logs_tab, 'Logs')
        self.addTab(self.settings_tab, 'Settings')

        self.setDocumentMode(True)

        self.setTabPosition(QTabWidget.West if settings_yml['vertical-tabs'] else QTabWidget.North)

    def add_tab(self):
        pass

class CameraTab(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QGridLayout()
        self.layout.setSpacing(0)

        self.cam1 = Camera(settings_yml['camera-ports']['cam-1'])
        self.cam2 = Camera(settings_yml['camera-ports']['cam-2'])
        self.cam3 = Camera(settings_yml['camera-ports']['cam-3'])
        self.cam4 = Camera(settings_yml['camera-ports']['cam-4'])

        self.layout.addWidget(self.cam1, 0,0)
        self.layout.addWidget(self.cam2, 0,1)
        self.layout.addWidget(self.cam3, 1,0)
        self.layout.addWidget(self.cam4, 1,1)

        self.setLayout(self.layout)

class Camera(QCameraViewfinder):
    def __init__(self, port):
        super().__init__()

        self.camera = QCamera(cameras[port])
        self.camera.setViewfinder(self)
        self.camera.start()

class LogsTab(QWidget):
    def __init__(self):
        super().__init__()

class SettingsTab(QWidget):
    def __init__(self):
        super().__init__()



if __name__ == '__main__':
    # Defining global variables
    cameras = QCameraInfo.availableCameras()

    with open('gui/settings.yml', 'r') as f:
        settings_yml = yaml.safe_load(f)
    print(settings_yml)

    # Create UI application
    app = QApplication([])

    window = AzureUI()
    window.show()

    sys.exit(app.exec())