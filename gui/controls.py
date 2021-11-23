from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTabWidget, QVBoxLayout, QGridLayout, QLabel
from PyQt5.QtMultimedia import QCameraInfo, QCamera
from PyQt5.QtMultimediaWidgets import QCameraViewfinder
from PyQt5.QtGui import QKeyEvent # use for key
import json
import sys

class AzureUI(QMainWindow):
    def __init__(self):
        super().__init__()

        with open('gui/settings.json', 'r') as f:
            self.json_settings = json.load(f)

        # Setup
        self.setWindowTitle('Azure User Interface')
        self.setStyleSheet('background: rgb(40,40,40)' if self.json_settings['theme'] == 'dark' else 'background: rgb(255,255,255)')
        

        self.cameras = QCameraInfo.availableCameras()

        self.layout = QVBoxLayout()
        

        self.parent_widget = QWidget()
        self.parent_widget.setLayout(self.layout)

        self.setCentralWidget(self.parent_widget)



        # Tabs
        self.tabs = QTabWidget()
        self.camera_tab = QWidget()
        self.settings_tab = QWidget()

        self.tabs.setStyleSheet(f'{"background: rgb(50,50,50)" if self.json_settings["theme"] == "dark" else "background: rgb(245,245,245)"}; border-radius: 10px')
        self.layout.addWidget(self.tabs)


        # Camera 1
        self.viewfinder_1 = QCameraViewfinder()

        self.camera_1 = QCamera(self.cameras[self.json_settings['camera_ports']['camera_1']])
        self.camera_1.setViewfinder(self.viewfinder_1)
        self.camera_1.start()


        # Camera 2
        self.viewfinder_2 = QCameraViewfinder()

        self.camera_2 = QCamera(self.cameras[self.json_settings['camera_ports']['camera_2']])
        self.camera_2.setViewfinder(self.viewfinder_2)
        self.camera_2.start()


        # Camera 3
        self.viewfinder_3 = QCameraViewfinder()

        self.camera_3 = QCamera(self.cameras[self.json_settings['camera_ports']['camera_3']])
        self.camera_3.setViewfinder(self.viewfinder_3)
        self.camera_3.start()


        # Camera 4
        self.viewfinder_4 = QCameraViewfinder()

        self.camera_4 = QCamera(self.cameras[self.json_settings['camera_ports']['camera_4']])
        self.camera_4.setViewfinder(self.viewfinder_4)
        self.camera_4.start()


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

    window = AzureUI()
    window.show()

    sys.exit(app.exec())