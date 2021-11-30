from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTabWidget, QVBoxLayout, QGridLayout, QLabel, QSlider
from PyQt5.QtMultimedia import QCameraInfo, QCamera
from PyQt5.QtMultimediaWidgets import QCameraViewfinder
from PyQt5.QtCore import Qt

import json
import sys


class AzureUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Azure User Interface')
        self.setStyleSheet(f'{"background: rgb(40,40,40)" if json_settings["theme"] == "dark" else "background: rgb(255,255,255)"}; border-radius: 10px')

        self.layout = QVBoxLayout()

        self.parent_widget = QWidget()
        self.parent_widget.setLayout(self.layout)

        self.setCentralWidget(self.parent_widget)

        self.tabs = QTabWidget()
        self.camera_tab = QWidget()
        self.settings_tab = QWidget()

        self.tabs.setStyleSheet(f'{"background: rgb(40,40,40)" if json_settings["theme"] == "dark" else "background: rgb(255,255,255)"}; border-radius: 10px')
        self.layout.addWidget(self.tabs)

        self.camera_tab.layout = QGridLayout()

        self.camera_tab.layout.addWidget(CameraLayout('camera_1').frame, 0,0)
        self.camera_tab.layout.addWidget(CameraLayout('camera_2').frame, 0,1)
        self.camera_tab.layout.addWidget(CameraLayout('camera_3').frame, 1,0)
        self.camera_tab.layout.addWidget(CameraLayout('camera_4').frame, 1,1)

        self.camera_tab.setLayout(self.camera_tab.layout)

        self.tabs.addTab(self.camera_tab, 'Cameras')
        self.tabs.addTab(self.settings_tab, 'Settings')

class CameraLayout(QWidget):
    def __init__(self, camera_selection):
        super().__init__()



        self.frame = QWidget()
        self.frame.setStyleSheet(f'{"background: rgb(50,50,50)" if json_settings["theme"] == "dark" else "background: rgb(245,245,245)"}; padding: 5px; border-radius: 10px')
        self.frame.setFixedSize(460,250)


        self.viewfinder = QCameraViewfinder()

        print(json_settings['camera_ports'][camera_selection])
        self.camera = QCamera(cameras[json_settings['camera_ports'][camera_selection]])
        self.camera.setViewfinder(self.viewfinder)
        self.camera.start()


        self.slider = QSlider()
        self.slider.setMaximum(10)


        self.frame.layout = QGridLayout()
        self.frame.layout.addWidget(self.viewfinder, 0,0)
        self.frame.layout.addWidget(self.slider, 0,1)

        self.frame.setLayout(self.frame.layout)
        
if __name__ == '__main__':
    with open('gui/settings.json', 'r') as f:
        json_settings = json.load(f)

    cameras = QCameraInfo.availableCameras()

    app = QApplication([])

    window = AzureUI()
    window.show()

    sys.exit(app.exec())