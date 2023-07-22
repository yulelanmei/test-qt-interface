import sys
from frontend.Ui_design import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
from backend.utils import Resources_Manager, MyTableModel
from backend.receive import Data_Receiver
from qt_material import apply_stylesheet

class UI_show(Ui_MainWindow, QMainWindow):
    def __init__(self, parent= None):
        super(UI_show, self).__init__(parent)   
        self.setupUi(self)
        
        self.media_timer = QTimer(self)
        self.media_timer.setSingleShot(False)
        
        self.media_timer2 = QTimer(self)
        self.media_timer2.setSingleShot(False)

        self.media_windows.setWindowTitle('media window')
        self.media_windows.setScaledContents(True)
        self.media_windows.resize(720, 540)
        
        self.media_windows2.setWindowTitle('media window 2')
        self.media_windows2.setScaledContents(True)
        self.media_windows2.resize(720, 540)
        
        self.resources = Resources_Manager()
        self.resources.set_load_mode(1)
        
        self.stream = Data_Receiver()
        
        self.Button_start.clicked.connect(self.timer_start)
        self.Button_pause.clicked.connect(self.timer_pause)
        self.Button_load.clicked.connect(self.load_resources)
        
        self.Button_receive.setStyleSheet('text-align:center')
        self.Button_receive.clicked.connect(self.start_get_stream_data)
        
        self.files_list.addItems(self.resources.get_list())
        self.files_list.show()

        # init info table
        self.info_data = []
        headers = ['action', 'timestamp']
        self.table_model = MyTableModel(self.info_data, headers)
        self.info_tbview.setModel(self.table_model)
        
    def start_get_stream_data(self):
        self.stream.start()
        self.media_timer2.timeout.connect(self.timer_timeout_stream)
        self.media_timer2.start(10)
        self.massage2.setText('waiting for camera data...')
    
    def timer_timeout_stream(self):
        frame, info = self.stream.get_data()
        # To DO: info process and show
        if frame is not None:
            self.set_window2_show(frame)
        if info is not None:
            massage = ''.join(info['action'] + '\n' + info['timestamp'])
            self.massage2.setText(massage)
            self.info_data.append((info['action'], info['timestamp']))
            self.table_model.updateData(self.info_data)
        
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
            self.set_window1_show(frame)
        else:
            self.timer_stop()
            
    def set_window1_show(self, frame):
        self.media_windows.setPixmap(QPixmap.fromImage(QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)))

    def set_window2_show(self, frame):
        self.media_windows2.setPixmap(QPixmap.fromImage(QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = UI_show()
    apply_stylesheet(app, theme= 'dark_teal.xml')
    ui.show()
    sys.exit(app.exec_())