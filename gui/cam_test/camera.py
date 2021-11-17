from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QCameraInfo, QCamera
from PyQt5.QtMultimediaWidgets import QVideoWidget, QCameraViewfinder
from PyQt5.QtCore import Qt, QUrl
import cv2
import sys

class CameraDisplay(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Video Testing')

        self.cameras = QCameraInfo.availableCameras()
        self.viewfinder = QCameraViewfinder()

        self.viewfinder.show()
        self.choose_camera(0) # add picker

        self.parent_widget = QWidget()
        self.setCentralWidget(self.parent_widget)

        self.layout = QGridLayout()
        self.layout.addWidget(self.viewfinder, 0,0,0,0)

        self.parent_widget.setLayout(self.layout)



    def choose_camera(self, index):
        self.camera = QCamera(self.cameras[index])
        self.camera.setViewfinder(self.viewfinder)
        self.camera.start()


if __name__ == '__main__':
    app = QApplication([])

    window = CameraDisplay()
    window.show()

    sys.exit(app.exec())