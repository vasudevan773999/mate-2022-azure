from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTabWidget, QVBoxLayout, QGridLayout, QLabel, QSlider
from PyQt5.QtMultimedia import QCameraInfo, QCamera, QCameraZoomControl
from PyQt5.QtMultimediaWidgets import QCameraViewfinder
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent# use for key

import json
import sys

class AzureUI(QMainWindow):
    def __init__(self):
        super().__init__()

        with open('gui/settings.json', 'r') as f:
            self.json_settings = json.load(f)

        # Setup
        self.setWindowTitle('Azure User Interface')
        self.setStyleSheet(f'{"background: rgb(40,40,40)" if self.json_settings["theme"] == "dark" else "background: rgb(255,255,255)"}; border-radius: 10px')
        

        self.cameras = QCameraInfo.availableCameras()

        self.layout = QVBoxLayout()

        self.parent_widget = QWidget()
        self.parent_widget.setLayout(self.layout)

        self.setCentralWidget(self.parent_widget)


        # Tabs
        self.tabs = QTabWidget()
        self.camera_tab = QWidget()
        self.settings_tab = QWidget()

        self.tabs.setStyleSheet(f'{"background: rgb(40,40,40)" if self.json_settings["theme"] == "dark" else "background: rgb(255,255,255)"}; border-radius: 10px')
        self.layout.addWidget(self.tabs)

        
        # Camera Tab

        self.tab = QWidget()
        self.tab.layout = QGridLayout()

        self.tab.layout.addWidget(self.camera_layout('camera_1'), 0,0)
        self.tab.layout.addWidget(self.camera_layout('camera_2'), 0,1)
        self.tab.layout.addWidget(self.camera_layout('camera_3'), 1,0)
        self.tab.layout.addWidget(self.camera_layout('camera_4'), 1,1)

        self.tab.setLayout(self.tab.layout)

        
        # Settings tab
        self.settings_tab = QWidget()
        self.settings_tab.layout = QGridLayout()


        # Layout
        self.tabs.addTab(self.camera_tab, "Cameras")
        self.tabs.addTab(self.settings_tab, "Settings")

    def camera_layout(self, selection):
        self.frame = QWidget()
        self.frame.setStyleSheet(f'{"background: rgb(50,50,50)" if self.json_settings["theme"] == "dark" else "background: rgb(245,245,245)"}; padding: 5px; border-radius: 10px')
        self.frame.setFixedSize(460,250)


        self.viewfinder = QCameraViewfinder()
        self.camera = QCamera(self.cameras[self.json_settings['camera_ports'][selection]])
        self.camera.setViewfinder(self.viewfinder)
        self.camera.start()

        self.slider = QSlider()
        self.slider.setMaximum(20)


        self.frame.layout = QGridLayout()
        self.frame.layout.addWidget(self.viewfinder, 0,0)
        self.frame.layout.addWidget(self.slider, 0,1)

        self.frame.setLayout(self.frame.layout)

        return self.frame


if __name__ == '__main__':
    app = QApplication([])

    window = AzureUI()
    window.show()

    sys.exit(app.exec())