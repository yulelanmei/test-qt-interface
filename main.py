import sys
from frontend.Ui_design import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import QTimer, Qt
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
        self.windows.resize(540, 360)
        
        self.resources = utils.Resources_Manager()
        self.resources.set_load_mode(1)
        
        self.Button_start.clicked.connect(self.timer_start)
        self.Button_pause.clicked.connect(self.timer_pause)
        self.Button_load.clicked.connect(self.load_resources)
        
        self.files_list.addItems(self.resources.get_list())
        self.files_list.show()
        
    def load_resources(self):
        index = self.files_list.currentRow()
        item = self.files_list.currentItem()
        if item:
            target_name = item.text()
        else:
            self.massage.setText('no item selected')
            return
        self.resources.load(index)
        self.massage.setText(f'load target {target_name}')
        
    def timer_start(self):
        self.massage.setText('start playing')
        self.media_timer.start(20)
        
    def timer_pause(self):
        self.massage.setText('pause')
        self.media_timer.stop()
        
    def timer_stop(self):
        print('timeout')
        self.resources.reset()
        self.massage.setText('stop')
        self.media_timer.stop()
        
    def timer_timeout(self):
        frame = self.resources.get_frame()
        if frame is not None:
            self.windows.setPixmap(QPixmap.fromImage(QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)))
        else:
            self.timer_stop()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = UI_show()
    ui.show()
    sys.exit(app.exec_())