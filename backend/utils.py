import cv2
import os
from glob import glob
from typing import Optional

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
        
    def get_frame(self):
        ret, frame = self.cap.read()
        return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) if ret else None
    
class Image(object):
    def __init__(self):
        self.img_list = None
        self.frame_cout = None
        
    def get_target(self, target_path: str):
        try:
            self.img_list = os.listdir(target_path)
        except FileNotFoundError:
            print(f'error path is {target_path}')
            
        self.frame_cout = len(self.img_list)
        self.n = 0
        
    def set_init(self):
        self.n = 0
        
    def get_frame(self, frame_size: Optional[tuple] = None):
        frame = cv2.imread(self.img_list[self.n])
        if frame is not None and self.n < self.frame_cout:
            if frame_size is not None:
                frame = cv2.resize(frame, frame_size)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 
            self.n += 1
        else:
            self.n = 0
            return None
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
        
    def get_video_list(self):
        return [os.path.basename(g) for g in self.video_list]
    
    def get_image_list(self):
        return [os.path.basename(g) for g in self.image_list]
        
    def load_video(self, index: int):
        assert index >= 0 and index < len(self.video_list), 'index over boundary!'
        self.video_loader.get_target(self.video_list[index])
        
    def get_video_frame(self):
        return self.video_loader.get_frame()
    
    def load_image(self, index: int):
        assert index >= 0 and index < len(self.image_list), 'index over boundary!'
        self.image_loader.get_target(self.image_list[index])
        
    def get_image_frame(self, frame_size: Optional[tuple] = None):
        return self.image_loader.get_frame(frame_size)
    
    def reset_image_loader(self):
        self.image_loader.set_init()