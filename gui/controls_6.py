from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTabWidget, QToolBar, QGridLayout, QLabel, QPushButton
from PyQt5.QtMultimedia import QCameraInfo, QCamera
from PyQt5.QtMultimediaWidgets import QCameraViewfinder
from PyQt5.QtCore import Qt, QThread
# from PyQt5 import QtWidgets

import sys
from threading import Thread

class AzureUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Azure UI')
        self.setStyleSheet('background: rgb(40,40,40)')

        self.cameras = QCameraInfo.availableCameras()

        self.tabs = Tabs()

        self.setCentralWidget(self.tabs)

        self.camera_tab = self.tabs.camera_grid
        # x = self.add_camera(1)
        # y = self.add_camera(1)
        
        self.camera_tab.layout = QGridLayout()

        # Thread(target=self.add_camera, args=(0, (1,0))).start()

        # Thread(target=self.add_camera, args=(0, (1,1))).start()
        # Thread(target=self.add_camera, args=(0, (2,0))).start()
        # Thread(target=self.add_camera, args=(0, (2,1))).start()


        # self.camera_tab.layout.addWidget(x, 1,0)
        # self.camera_tab.layout.addWidget(x, 1,1)
        self.add_camera(0, (1,0))
        self.add_camera(0, (1,1))
        self.add_camera(0, (2,0))
        self.add_camera(1, (2,1))

        self.camera_tab.setLayout(self.camera_tab.layout)

    def add_camera(self, port, pos):
        self.viewfinder = QCameraViewfinder()

        self.camera = QCamera(self.cameras[port])
        self.camera.setViewfinder(self.viewfinder)
        self.camera.start()

        self.camera_tab.layout.addWidget(self.viewfinder, pos[0], pos[1])




class Tabs(QTabWidget):
    def __init__(self):
        super().__init__()

        self.camera_grid = QWidget()

        self.addTab(self.camera_grid, 'Cameras')
        self.addTab(QWidget(), 'okokok')
        self.setDocumentMode(True)
        self.setTabPosition(QTabWidget.West)

        # self.setMovable(False)


        # self.addWidget(QPushButton('okok'))
        # self.addWidget(self.tabs)
        # self.addWidget(QPushButton('ok'))
        # self.setStyleSheet('background-color: white; border-radius: 8px')

    def add_tab(self):
        pass

if __name__ == '__main__':
    app = QApplication([])

    # QtWidgets.QApplication.setStyle(ProxyStyle())

    window = AzureUI()
    window.show()

    sys.exit(app.exec())