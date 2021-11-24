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


        # Camera 1
        self.camera_1_parent = QWidget()
        self.camera_1_parent.setStyleSheet(f'{"background: rgb(50,50,50)" if self.json_settings["theme"] == "dark" else "background: rgb(245,245,245)"}; padding: 5px; border-radius: 10px')
        self.camera_1_parent.setFixedSize(460,250)
        self.camera_1_parent.layout = QGridLayout()


        self.viewfinder_1 = QCameraViewfinder()

        self.camera_1 = QCamera(self.cameras[self.json_settings['camera_ports']['camera_1']])
        self.camera_1.setViewfinder(self.viewfinder_1)
        self.camera_1.start()


        self.slider_1 = QSlider()
        self.slider_1.setMaximum(10)

        self.slider_1.valueChanged.connect(self.zoom_camera_1)


        self.camera_1_parent.layout.addWidget(self.viewfinder_1, 0,0)
        self.camera_1_parent.layout.addWidget(self.slider_1, 0,1)

        self.camera_1_parent.setLayout(self.camera_1_parent.layout)

        # Camera 2
        self.camera_2_parent = QWidget()
        self.camera_2_parent.setStyleSheet(f'{"background: rgb(50,50,50)" if self.json_settings["theme"] == "dark" else "background: rgb(245,245,245)"}; padding: 5px; border-radius: 10px')
        self.camera_2_parent.setFixedSize(460,250)
        self.camera_2_parent.layout = QGridLayout()


        self.viewfinder_2 = QCameraViewfinder()

        self.camera_2 = QCamera(self.cameras[self.json_settings['camera_ports']['camera_2']])
        self.camera_2.setViewfinder(self.viewfinder_2)
        self.camera_2.start()


        self.slider_2 = QSlider()
        self.slider_2.setMaximum(10)

        # self.slider_2.valueChanged.connect(self.zoom_camera_1)


        self.camera_2_parent.layout.addWidget(self.viewfinder_2, 0,0)
        self.camera_2_parent.layout.addWidget(self.slider_2, 0,1)

        self.camera_2_parent.setLayout(self.camera_2_parent.layout)

        # Camera 3
        self.camera_3_parent = QWidget()
        self.camera_3_parent.setStyleSheet(f'{"background: rgb(50,50,50)" if self.json_settings["theme"] == "dark" else "background: rgb(245,245,245)"}; padding: 5px; border-radius: 10px')
        self.camera_3_parent.setFixedSize(460,250)
        self.camera_3_parent.layout = QGridLayout()


        self.viewfinder_3 = QCameraViewfinder()

        self.camera_3 = QCamera(self.cameras[self.json_settings['camera_ports']['camera_3']])
        self.camera_3.setViewfinder(self.viewfinder_3)
        self.camera_3.start()


        self.slider_3 = QSlider()
        self.slider_3.setMaximum(10)

        # self.slider_2.valueChanged.connect(self.zoom_camera_1)


        self.camera_3_parent.layout.addWidget(self.viewfinder_3, 0,0)
        self.camera_3_parent.layout.addWidget(self.slider_3, 0,1)

        self.camera_3_parent.setLayout(self.camera_3_parent.layout)


        # Camera 4
        self.camera_4_parent = QWidget()
        self.camera_4_parent.setStyleSheet(f'{"background: rgb(50,50,50)" if self.json_settings["theme"] == "dark" else "background: rgb(245,245,245)"}; padding: 5px; border-radius: 10px')
        self.camera_4_parent.setFixedSize(460,250)
        self.camera_4_parent.layout = QGridLayout()


        self.viewfinder_4 = QCameraViewfinder()

        self.camera_4 = QCamera(self.cameras[self.json_settings['camera_ports']['camera_2']])
        self.camera_4.setViewfinder(self.viewfinder_4)
        self.camera_4.start()


        self.slider_4 = QSlider()
        self.slider_4.setMaximum(10)

        # self.slider_2.valueChanged.connect(self.zoom_camera_1)


        self.camera_4_parent.layout.addWidget(self.viewfinder_4, 0,0)
        self.camera_4_parent.layout.addWidget(self.slider_4, 0,1)

        self.camera_4_parent.setLayout(self.camera_4_parent.layout)

        #temp
        self.new = QWidget()
        self.new.layout = QGridLayout()
        self.new.setLayout(self.new.layout)
        self.new.layout.addWidget(self.camera_1_parent)


        # Camera layout
        self.camera_tab.layout = QGridLayout()
        self.camera_tab.layout.addWidget(self.new, 1,0)
        self.camera_tab.layout.addWidget(self.camera_2_parent, 1,1)
        self.camera_tab.layout.addWidget(self.camera_3_parent, 2,0)
        self.camera_tab.layout.addWidget(self.camera_4_parent, 2,1)

        self.camera_tab.setLayout(self.camera_tab.layout)


        # Settings tab
        self.settings_tab = QWidget()
        self.settings_tab.layout = QGridLayout()


        # Layout
        self.tabs.addTab(self.camera_tab, "Cameras")
        self.tabs.addTab(self.settings_tab, "Settings")

    def zoom_camera_1(self, e):
        # self.camera_1.


        self.new.resize(460-(e*10), 250-(10*e))
        # self.viewfinder_1.resize()
        # self.viewfinder_1.
        pass


if __name__ == '__main__':
    app = QApplication([])

    window = AzureUI()
    window.show()

    sys.exit(app.exec())