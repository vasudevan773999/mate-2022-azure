from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTabWidget, QVBoxLayout
from PyQt5.QtMultimedia import QCameraInfo, QCamera
from PyQt5.QtMultimediaWidgets import QCameraViewfinder
from PyQt5.QtGui import QKeyEvent # use for key
import sys

class CameraDisplay(QMainWindow):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()

        self.parent_widget = QWidget()
        self.setCentralWidget(self.parent_widget)

        self.parent_widget.setLayout(self.layout)

        # Setup
        self.setWindowTitle('Azure Controls')
        self.cameras = QCameraInfo.availableCameras()


        # Tabs
        self.tabs = QTabWidget()
        self.camera_tab = QWidget()
        self.settings_tab = QWidget()



        self.test = QWidget()
        # Camera 1
        self.viewfinder = QCameraViewfinder()

        self.camera = QCamera(self.cameras[0])
        self.camera.setViewfinder(self.viewfinder)
        self.camera.start()

        self.viewfinder.show()

        # self.viewfinder.setStyleSheet('border-size')
        ####fix layout for camera tab

        self.camera_tab = QVBoxLayout()
        self.camera_tab.addWidget(self.viewfinder)

        

        # self.tabs.addTab(self.viewfinder, 'Cameras')
        # self.tabs.addTab(self.settings_tab, 'UI Settings')
        # self.tabs.addTab(self.test, 'testing')



        # Camera 2
        # self.viewfinder2 = QCameraViewfinder()

        # self.camera2 = QCamera(self.cameras[0])
        # self.camera2.setViewfinder(self.viewfinder2)
        # self.camera2.start()

        # self.viewfinder2.show()


        # Layout

        # self.camera_tab.layout.addWidget(QPushButton('hi'), 0,1)


        self.layout.addWidget(self.tabs)
        # self.layout.addWidget(self.viewfinder)



if __name__ == '__main__':
    app = QApplication([])

    window = CameraDisplay()
    window.show()

    sys.exit(app.exec())