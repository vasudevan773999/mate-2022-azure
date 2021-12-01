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

        global cameras
        cameras = QCameraInfo.availableCameras()


        self.setWindowTitle('Azure User Interface')
        self.setStyleSheet(f'{"background: rgb(40,40,40)" if json_settings["theme"] == "dark" else "background: rgb(255,255,255)"}; border-radius: 10px')

        self.layout = QVBoxLayout()

        self.main = QWidget()
        self.main.setLayout(self.layout)

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

        #test

        self.cameras = QCameraInfo.availableCameras()

        ####
        self.camera_4_parent = QWidget()
        self.camera_4_parent.setStyleSheet(f'{"background: rgb(50,50,50)" if json_settings["theme"] == "dark" else "background: rgb(245,245,245)"}; padding: 5px; border-radius: 10px')
        self.camera_4_parent.setFixedSize(460,250)
        self.camera_4_parent.layout = QGridLayout()


        self.viewfinder_4 = QCameraViewfinder()

        self.camera_4 = QCamera(self.cameras[json_settings["camera_ports"]["camera_2"]])
        self.camera_4.setViewfinder(self.viewfinder_4)
        self.camera_4.start()


        self.slider_4 = QSlider()
        self.slider_4.setMaximum(10)

        self.camera_4_parent.layout.addWidget(self.viewfinder_4, 0,0)
        self.camera_4_parent.layout.addWidget(self.slider_4, 0,1)

        self.camera_4_parent.setLayout(self.camera_4_parent.layout)
        # self.cameras = QCameraInfo.availableCameras()

        # self.frame = QWidget()
        # self.frame.setStyleSheet(f'{"background: rgb(50,50,50)" if json_settings["theme"] == "dark" else "background: rgb(245,245,245)"}; padding: 5px; border-radius: 10px')
        # self.frame.setFixedSize(460,250)


        # self.viewfinder = QCameraViewfinder()

        # self.camera = QCamera(self.cameras[json_settings['camera_ports']['camera_1']])
        # self.camera.setViewfinder(self.viewfinder)
        # self.camera.start()


        # self.slider = QSlider()
        # self.slider.setMaximum(20)


        # self.frame.layout = QGridLayout()
        # self.frame.layout.addWidget(self.viewfinder, 0,0)
        # self.frame.layout.addWidget(self.slider, 0,1)

        # self.frame.setLayout(self.frame.layout)



        # end

        self.tab = QWidget()
        self.tab.layout = QGridLayout()

        self.tab.layout.addWidget(self.camera_4_parent, 0,0)
        self.tab.layout.addWidget(CameraLayout('camera_2').frame, 0,1)
        self.tab.layout.addWidget(CameraLayout('camera_3').frame, 1,0)
        self.tab.layout.addWidget(CameraLayout('camera_4').frame, 1,1)

        self.tab.setLayout(self.tab.layout)


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

class CameraLayout(QWidget):
    def __init__(self, selection):
        super().__init__()

        self.frame = QWidget()
        self.frame.setStyleSheet(f'{"background: rgb(50,50,50)" if json_settings["theme"] == "dark" else "background: rgb(245,245,245)"}; padding: 5px; border-radius: 10px')
        self.frame.setFixedSize(460,250)


        self.viewfinder = QCameraViewfinder()

        self.camera = QCamera(cameras[json_settings['camera_ports'][selection]])
        self.camera.setViewfinder(self.viewfinder)
        self.camera.start()


        self.slider = QSlider()
        self.slider.setMaximum(20)


        self.frame.layout = QGridLayout()
        self.frame.layout.addWidget(self.viewfinder, 0,0)
        self.frame.layout.addWidget(self.slider, 0,1)

        self.frame.setLayout(self.frame.layout)


if __name__ == '__main__':

    app = QApplication([])

    window = AzureUI()
    window.show()

    sys.exit(app.exec())