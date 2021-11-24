from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTabWidget, QVBoxLayout, QGridLayout, QLabel, QSlider
from PyQt5.QtMultimedia import QCameraInfo, QCamera
from PyQt5.QtMultimediaWidgets import QCameraViewfinder
from PyQt5.QtCore import Qt

import json
import sys


class AzureUI(QMainWindow):
    def __init__(self):
        super().__init__()

        with open('gui/settings.json', 'r') as f:
            self.json_settings = json.load(f)

        self.setWindowTitle('Azure User Interface')
        self.setStyleSheet(f'{"background: rgb(40,40,40)" if self.json_settings["theme"] == "dark" else "background: rgb(255,255,255)"}; border-radius: 10px')

        self.layout = QVBoxLayout()

        self.parent_widget = QWidget()
        self.parent_widget.setLayout(self.layout)

        self.setCentralWidget(self.parent_widget)

        self.tabs = QTabWidget()
        self.camera_tab = QWidget()
        self.settings_tab = QWidget()

        self.tabs.setStyleSheet(f'{"background: rgb(40,40,40)" if self.json_settings["theme"] == "dark" else "background: rgb(255,255,255)"}; border-radius: 10px')
        self.layout.addWidget(self.tabs)

        self.camera_tab.layout = QGridLayout()
        self.camera_tab.layout.addWidget(CameraLayout().frame, 1,0)



        self.tabs.addTab(self.camera_tab, "Cameras")
        self.tabs.addTab(self.settings_tab, "Settings")

class CameraLayout(QWidget):
    def __init__(self):
        super(AzureUI).__init__()

        with open('gui/settings.json', 'r') as f:
            self.json_settings = json.load(f)

        self.cameras = QCameraInfo.availableCameras()

        self.frame = QWidget()
        self.frame.setStyleSheet(f'{"background: rgb(50,50,50)" if self.json_settings["theme"] == "dark" else "background: rgb(245,245,245)"}; padding: 5px; border-radius: 10px')
        self.frame.setFixedSize(460,250)


        self.viewfinder = QCameraViewfinder()

        self.camera = QCamera(self.cameras[self.json_settings['camera_ports']['camera_1']])
        self.camera.setViewfinder(self.viewfinder)
        self.camera.start()


        self.slider = QSlider()
        self.slider.setMaximum(10)


        self.frame.layout = QGridLayout()
        self.frame.layout.addWidget(self.viewfinder, 0,0)
        self.frame.layout.addWidget(self.slider, 0,1)

        self.frame.setLayout(self.frame.layout)
        
if __name__ == '__main__':
    app = QApplication([])

    window = AzureUI()
    window.show()

    sys.exit(app.exec())