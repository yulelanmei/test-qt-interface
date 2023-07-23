import cv2
import os
from glob import glob
from typing import Optional
import base64
import numpy as np

class Video(object):
    def __init__(self):
        self.cap = None
        self.fps = None
        self.frame_size = None
        self.frame_count = None
        
    def get_target(self, target_path: str):
        if self.cap is not None:
            self.cap.release()
        
        self.cap = cv2.VideoCapture(target_path)
        assert self.cap.isOpened(), 'Cannot open target!'
        
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        self.frame_size = (int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
                           int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        self.frame_count = self.cap.get(cv2.CAP_PROP_FRAME_COUNT)
        
    def set_init(self):
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        
    def get_frame(self, frame_size: Optional[tuple] = None):
        ret, frame = self.cap.read()
        if ret:
            if frame_size is not None:
                frame = cv2.resize(frame, frame_size)
            return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
class Image(object):
    def __init__(self):
        self.img_list = None
        self.frame_cout = None
        self.n = 0
        
    def get_target(self, target_path: str):
        try:
            self.img_list = [os.path.join(target_path, path) for path in os.listdir(target_path)]
        except FileNotFoundError:
            print(f'error path is {target_path}')
            
        self.frame_cout = len(self.img_list)
        self.set_init()
        
    def set_init(self):
        self.n = 0
        
    def get_frame(self, frame_size: Optional[tuple] = None):
        if self.n < self.frame_cout:
            frame = cv2.imread(self.img_list[self.n])
        else:
            return None
        if frame is not None:
            if frame_size is not None:
                frame = cv2.resize(frame, frame_size)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 
            self.n += 1
        return frame
        
class Resources_Manager(object):
    def __init__(self):
        video_path = './resources/videos/*'
        image_path = './resources/images/*'
        self.video_list = glob(video_path)
        self.image_list = glob(image_path)
        if len(self.video_list) == 0: print('video list zero length')
        if len(self.image_list) == 0: print('image list zero length')
        self.video_loader = Video()
        self.image_loader = Image()
        self.if_video_loaded: bool = False
        self.if_image_loaded: bool = False
        self.load_mode = 0 # 0:'image' 1:'video'
        
    def set_load_mode(self, mode: int):
        if mode in (0, 1):
            if mode == 0: 
                self.load_mode = 0
                print('set mode 0: image')
            else:
                self.load_mode = 1
                print('set mode 1: video')
        else:
            print('mode should be set as 0 or 1')
            
    def load(self, index: int):
        if self.load_mode:
            self.load_video(index)
        else:
            self.load_image(index)
            
    def get_frame(self, frame_size: Optional[tuple] = None):
        if self.load_mode:
            return self.get_video_frame(frame_size)
        else:
            return self.get_image_frame(frame_size)
        
    def reset(self):
        if self.load_mode:
            return self.reset_video_loader()
        else:
            return self.reset_image_loader()
        
    def get_list(self):
        if self.load_mode:
            return self.get_video_list()
        else:
            return self.get_image_list()
        
    def get_video_list(self):
        return [os.path.basename(g) for g in self.video_list]
    
    def get_image_list(self):
        return [os.path.basename(g) for g in self.image_list]
        
    def load_video(self, index: int):
        if not index >= 0 and index < len(self.video_list):
            print(f'index over boundary! num:{len(self.video_list)}')
            return
        self.video_loader.get_target(self.video_list[index])
        self.if_video_loaded = True
        
    def load_image(self, index: int):
        if not index >= 0 and index < len(self.image_list):
            print(f'index over boundary! num:{len(self.image_list)}')
            return
        self.image_loader.get_target(self.image_list[index])
        self.if_image_loaded = True
        
    def get_video_frame(self, frame_size: Optional[tuple] = None):
        if self.if_video_loaded:
            return self.video_loader.get_frame(frame_size)
        
    def get_image_frame(self, frame_size: Optional[tuple] = None):
        if self.if_image_loaded:
            return self.image_loader.get_frame(frame_size)
    
    def reset_image_loader(self):
        self.image_loader.set_init()
        
    def reset_video_loader(self):
        self.video_loader.set_init()


def camera_stream_decode(image_base64):
    image_data = base64.b64decode(image_base64)
    image_array = cv2.imdecode(np.frombuffer(image_data, dtype= np.uint8), cv2.IMREAD_COLOR)        
    image_array = cv2.cvtColor(image_array, cv2.COLOR_BGR2RGB)
    return image_array
        
if __name__ == '__main__':
    
    test = Resources_Manager()
    test.set_load_mode(0)
    test.load(0)
    while True:
        frame = test.get_frame()
        print(type(frame))
        if frame is None:
            break