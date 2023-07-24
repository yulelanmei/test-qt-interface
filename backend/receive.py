from flask import Flask, request
import json
from queue import Queue
import threading
from backend.utils import camera_stream_decode

class Data_Receiver(object):
    def __init__(self, maxQueueSize= 32):
        self.app = Flask(__name__)
        
        self.INFO = {
            'action' : '',
            'timestamp': '',
            "gait" : '',#正常步态或者摔倒状态
            "squat_count" : 0,#深蹲计数
            "situp_count" : 0,#仰卧起坐计数
        }
        
        self.Queue_frame = Queue(maxsize= maxQueueSize)
        self.Queue_info = Queue(maxsize= maxQueueSize)
        
        self.app_thread = None
        
        @self.app.route('/receive', methods=['POST'])
        def receive_data():
            self.INFO['action'] = request.get_json()['action']
            self.INFO['timestamp'] = request.get_json()['timestamp']
            self.INFO['gait'] = request.get_json()['gait']
            self.INFO['squat_count'] = request.get_json()['squat_count']
            self.INFO['situp_count'] = request.get_json()['situp_count']

            image_base64 = request.get_json()['image_data']
            image_array = camera_stream_decode(image_base64)

            # store data(test)
            # cv2.imwrite(f'./resources/img/{self.INFO["timestamp"]}.jpg', image_array)
            # with open(f'./resources/json/{self.INFO["timestamp"][:10]}.json', 'a') as f:
            #     json.dump(self.INFO, f, indent=4)
            #     f.write('\n')
            
            if not self.Queue_frame.full():
                self.Queue_frame.put(image_array)
            
            if not self.Queue_info.full():
                self.Queue_info.put(self.INFO.copy())

            return 'Received'
        
    def get_data(self):
        frame = None
        info = None
        if not self.Queue_frame.empty():
            frame = self.Queue_frame.get_nowait()
        if not self.Queue_info.empty():    
            info = self.Queue_info.get_nowait()
        return frame, info
        
    def start(self):
        self.app_thread = threading.Thread(target= self.app.run, kwargs= {'host':'0.0.0.0', 'port':5001})
        self.app_thread.setDaemon(True)
        self.app_thread.start()
        # self.app.run(host= '0.0.0.0', port= 5001)

if __name__ == '__main__':
    test = Data_Receiver()
    test.start()