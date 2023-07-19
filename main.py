import sys
from frontend.Ui_design import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import QTimer, QDir
from PyQt5.QtGui import QImage, QPixmap
from backend import utils

class UI_show(Ui_MainWindow, QMainWindow):
    def __init__(self, parent= None):
        super(UI_show, self).__init__(parent)   
        self.setupUi(self)
        
        self.media_timer = QTimer(self)
        self.media_timer.timeout.connect(self.timer_timeout)

        self.windows = QLabel(self.media_windows)
        
        self.resources = utils.Resources_Manager()
        
        self.Button_start.clicked.connect(self.timer_start)
        self.Button_pause.clicked.connect(self.timer_pause)
        # self.Button_load.clicked.connect()
        
        self.files_list.
        
    # def load_resources(self):
        
        
        

    def timer_start(self):
        self.media_timer.start(10)
        
    def timer_pause(self):
        self.media_timer.stop()
        
    def timer_timeout(self):
        
        self.windows.setPixmap(QPixmap.fromImage(QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = UI_show()
    ui.show()
    sys.exit(app.exec_())