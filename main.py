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
        self.media_timer.setSingleShot(False)

        self.windows = QLabel(self.media_windows)
        self.windows.setWindowTitle('media window')
        self.windows.setScaledContents(True)
        
        self.resources = utils.Resources_Manager()
        
        self.Button_start.clicked.connect(self.timer_start)
        self.Button_pause.clicked.connect(self.timer_pause)
        self.Button_load.clicked.connect(self.load_resources)
        
        # print(len(self.resources.image_list))
        self.files_list.addItems(self.resources.get_image_list())
        self.files_list.show()
        
    def load_resources(self):
        index = self.files_list.currentRow()
        item = self.files_list.currentItem()
        if item:
            target_name = item.text()
        self.resources.load_image(index)
        self.massage.setText(f'load target {target_name}')
        
    def timer_start(self):
        self.massage.setText('start playing')
        self.media_timer.start(1000)
        
    def timer_pause(self):
        self.massage.setText('pause')
        self.media_timer.stop()
        
    def timer_stop(self):
        self.resources.reset_image_loader()
        self.massage.setText('stop')
        self.media_timer.stop()
        
    def timer_timeout(self):
        frame = self.resources.get_image_frame()
        if frame is not None:
            print('load successfully', frame)
            self.windows.setPixmap(QPixmap.fromImage(QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)))
        else:
            self.timer_stop()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = UI_show()
    ui.show()
    sys.exit(app.exec_())