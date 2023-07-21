import sys
from frontend.Ui_design import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
from backend.utils import Resources_Manager
from backend.receive import Data_Receiver

class UI_show(Ui_MainWindow, QMainWindow):
    def __init__(self, parent= None):
        super(UI_show, self).__init__(parent)   
        self.setupUi(self)
        
        self.media_timer = QTimer(self)
        self.media_timer.setSingleShot(False)

        self.windows = QLabel(self.media_windows)
        self.windows.setWindowTitle('media window')
        self.windows.setScaledContents(True)
        self.windows.resize(540, 360)
        
        self.resources = Resources_Manager()
        self.resources.set_load_mode(1)
        
        self.stream = Data_Receiver()
        
        self.Button_start.clicked.connect(self.timer_start)
        self.Button_pause.clicked.connect(self.timer_pause)
        self.Button_load.clicked.connect(self.load_resources)
        self.Button_receive.clicked.connect(self.start_get_stream_data)
        
        self.files_list.addItems(self.resources.get_list())
        self.files_list.show()
        
    def start_get_stream_data(self):
        self.stream.start()
        self.media_timer.stop()
        self.media_timer.timeout.connect(self.timer_timeout_stream)
        self.media_timer.start(20)
    
    def timer_timeout_stream(self):
        frame, info = self.stream.get_data()
        # To DO: info process and show
        if frame is not None:
            self.set_window_show(frame)
        
    def load_resources(self):
        self.media_timer.timeout.connect(self.timer_timeout_resources)
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
        self.resources.reset()
        self.massage.setText('stop')
        self.media_timer.stop()
        
    def timer_timeout_resources(self):
        frame = self.resources.get_frame()
        if frame is not None:
            self.set_window_show(frame)
        else:
            self.timer_stop()
            
    def set_window_show(self, frame):
        self.windows.setPixmap(QPixmap.fromImage(QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = UI_show()
    ui.show()
    sys.exit(app.exec_())