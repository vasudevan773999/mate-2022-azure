from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTabWidget, QVBoxLayout, QGridLayout, QLabel, QSlider, QPushButton
from PyQt5.QtMultimedia import QCameraInfo, QCamera
from PyQt5.QtMultimediaWidgets import QCameraViewfinder
from PyQt5.QtCore import Qt

import json
import sys

class AzureUI(QMainWindow):
    def __init__(self):
        super().__init__()
        with open('gui/settings.json', 'r') as f:
            global json_settings
            json_settings = json.load(f)


        self.setWindowTitle('Azure User Interface')
        self.setStyleSheet(f'{"background: rgb(40,40,40)" if json_settings["theme"] == "dark" else "background: rgb(255,255,255)"}; border-radius: 10px')

        self.layout = QVBoxLayout()

        # self.main = QWidget()
        # self.main.setLayout(self.layout)

        self.tabs = Tabs().tabs
        self.layout.addWidget(self.tabs)

        self.setCentralWidget(self.tabs)



class Tabs(QTabWidget):
    def __init__(self):
        super().__init__()

        self.tabs = QTabWidget()
        self.camera_tab = CameraTab().tab
        self.settings_tab = SettingsTab().tab

        self.tabs.setStyleSheet(f'{"background: rgb(40,40,40)" if json_settings["theme"] == "dark" else "background: rgb(255,255,255)"}; border-radius: 10px')

        self.tabs.addTab(self.camera_tab, 'Cameras')
        self.tabs.addTab(self.settings_tab, 'Settings')


class CameraTab(QWidget):
    def __init__(self):
        super().__init__()

        self.cameras = QCameraInfo.availableCameras()

        self.tab = QWidget()
        self.tab.layout = QGridLayout()

        self.tab.layout.addWidget(self.camera_layout('camera_1'), 0,0)
        self.tab.layout.addWidget(self.camera_layout('camera_2'), 0,1)
        self.tab.layout.addWidget(self.camera_layout('camera_3'), 1,0)
        self.tab.layout.addWidget(self.camera_layout('camera_4'), 1,1)

        self.tab.setLayout(self.tab.layout)

    def camera_layout(self, selection):
        self.frame = QWidget()
        self.frame.setStyleSheet(f'{"background: rgb(50,50,50)" if json_settings["theme"] == "dark" else "background: rgb(245,245,245)"}; padding: 5px; border-radius: 10px')
        self.frame.setFixedSize(460,250)


        self.viewfinder = QCameraViewfinder()
        self.camera = QCamera(self.cameras[json_settings['camera_ports'][selection]])
        self.camera.setViewfinder(self.viewfinder)
        self.camera.start()

        self.slider = QSlider()
        self.slider.setMaximum(20)


        self.frame.layout = QGridLayout()
        self.frame.layout.addWidget(self.viewfinder, 0,0)
        self.frame.layout.addWidget(self.slider, 0,1)

        self.frame.setLayout(self.frame.layout)

        return self.frame


class SettingsTab(QWidget):
    def __init__(self):
        super().__init__()

        self.tab = QWidget()
        self.tab.layout = QGridLayout()

        # self.boom = QPushButton('implode')
        # self.boom.setFixedSize(100,50)
        # self.boom.setStyleSheet('background: red; color: white; font: 20px bold')

        # self.tab.layout.addWidget(self.boom)



        # something

        
        self.tab.setLayout(self.tab.layout)

# class CameraLayout(QWidget):
#     def __init__(self, selection):
#         super().__init__()

#         self.cameras = QCameraInfo.availableCameras()
#         # print(f'asdfsdasifvjdadsi {self.cameras}\n\n\n\n')

#         self.frame = QWidget()
#         self.frame.setStyleSheet(f'{"background: rgb(50,50,50)" if json_settings["theme"] == "dark" else "background: rgb(245,245,245)"}; padding: 5px; border-radius: 10px')
#         self.frame.setFixedSize(460,250)


#         self.viewfinder = QCameraViewfinder()

#         self.camera = QCamera(self.cameras[json_settings['camera_ports'][selection]])
#         self.camera.setViewfinder(self.viewfinder)
#         self.camera.start()

#         # self.viewfinder.setLayout(self.layout)


#         self.slider = QSlider()
#         self.slider.setMaximum(20)


#         self.frame.layout = QGridLayout()
#         self.frame.layout.addWidget(self.viewfinder, 0,0)
#         self.frame.layout.addWidget(self.slider, 0,1)

#         self.frame.setLayout(self.frame.layout)
    


if __name__ == '__main__':

    app = QApplication([])

    window = AzureUI()
    window.show()

    sys.exit(app.exec())