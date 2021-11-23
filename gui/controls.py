from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTabWidget, QVBoxLayout, QGridLayout, QLabel
from PyQt5.QtMultimedia import QCameraInfo, QCamera
from PyQt5.QtMultimediaWidgets import QCameraViewfinder
from PyQt5.QtGui import QKeyEvent # use for key
import json
import sys

class CameraDisplay(QMainWindow):
    def __init__(self):
        super().__init__()

        # Setup
        self.setWindowTitle('Azure Controls')
        self.cameras = QCameraInfo.availableCameras()

        self.layout = QVBoxLayout()

        self.parent_widget = QWidget()
        self.parent_widget.setLayout(self.layout)

        self.setCentralWidget(self.parent_widget)


        with open('gui/settings.json', 'r') as f:
            self.json_settings = json.load(f)


        # Tabs
        self.tabs = QTabWidget()
        self.camera_tab = QWidget()
        self.settings_tab = QWidget()

        self.layout.addWidget(self.tabs)


        # Camera 1
        self.viewfinder_1 = QCameraViewfinder()

        self.camera_1 = QCamera(self.cameras[self.json_settings['camera_ports']['camera_1']])
        self.camera_1.setViewfinder(self.viewfinder_1)
        self.camera_1.start()

        self.viewfinder_1.show()


        # Camera 2
        self.viewfinder_2 = QCameraViewfinder()

        self.camera_2 = QCamera(self.cameras[self.json_settings['camera_ports']['camera_2']])
        self.camera_2.setViewfinder(self.viewfinder_2)
        self.camera_2.start()

        self.viewfinder_2.show()


        # Camera 3
        self.viewfinder_3 = QCameraViewfinder()

        self.camera_3 = QCamera(self.cameras[self.json_settings['camera_ports']['camera_3']])
        self.camera_3.setViewfinder(self.viewfinder_3)
        self.camera_3.start()

        self.viewfinder_3.show()


        # Camera 4
        self.viewfinder_4 = QCameraViewfinder()

        self.camera_4 = QCamera(self.cameras[self.json_settings['camera_ports']['camera_4']])
        self.camera_4.setViewfinder(self.viewfinder_4)
        self.camera_4.start()

        self.viewfinder_4.show()


        # Camera layout
        self.camera_tab.layout = QGridLayout()
        self.camera_tab.layout.addWidget(self.viewfinder_1, 1,0)
        self.camera_tab.layout.addWidget(self.viewfinder_2, 1,1)
        self.camera_tab.layout.addWidget(self.viewfinder_3, 2,0)
        self.camera_tab.layout.addWidget(self.viewfinder_4, 2,1)

        self.camera_tab.setLayout(self.camera_tab.layout)


        # Settings tab
        self.settings_tab = QWidget()
        self.settings_tab.layout = QGridLayout()


        # Layout
        self.tabs.addTab(self.camera_tab, "Cameras")
        self.tabs.addTab(self.settings_tab, "Settings")



if __name__ == '__main__':
    app = QApplication([])

    window = CameraDisplay()
    window.show()

    sys.exit(app.exec())