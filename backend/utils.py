import cv2
import os

class Video(object):
    def __init__(self):
        self.cap
        self.fps
        self.frame_size
        self.frame_count
        
    def get_target(self, target_path):
        if self.cap is not None:
            self.cap.release()
        
        self.cap = cv2.VideoCapture(target_path)
        assert self.cap.isOpened(), 'Cannot open target!'
        
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        self.frame_size = (int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
                           int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        self.frame_count = self.cap.get(cv2.CAP_PROP_FRAME_COUNT)
        
    def get_frame(self):
        ret, frame = self.cap.read()
        return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) if ret else None
    
class Image(object):
    def __init__(self):
        self.img_list
        self.frame_cout
        
    def get_target(self, target_path):
        self.img_list = os.listdir(target_path)
        self.frame_cout = len(self.img_list)
        self.n = 0
        
    def get_frame(self):
        self.n += 1
        if self.n <= self.frame_cout:
            return cv2.cvtColor(cv2.imread(self.img_list[self.n]), cv2.COLOR_BGR2RGB) 
        else:
            return None
        
class Resources_Manager(object):
    def __init__(self):
        
        self.video_list = os.listdir('the_olds_defender\resources\videos')
        self.image_list = os.listdir('the_olds_defender\resources\images')
        self.video_loader = Video()
        self.image_loader = Image()
        
    def load_video(self, index: int):
        assert index >= 0 and index < len(self.video_list), 'index over boundary!'
        self.video_loader.get_target(self.video_list[index])
        
    def get_video_frame(self):
        return self.video_loader.get_frame()
    
    def load_image(self, index: int):
        assert index >= 0 and index < len(self.image_list), 'index over boundary!'
        self.image_loader.get_target(self.image_list[index])
        
    def get_image_frame(self):
        return self.image_loader.get_frame()