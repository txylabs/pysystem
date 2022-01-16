import os
import time
from PySide2 import QtGui
from PySide2.QtCore import QObject
import cv2
from PySide2.QtWidgets import QLabel

class camera_play(QObject):
    def __init__(self):
        super(camera_play, self).__init__()
        self.threadFlag = 0     #   控制线程退出
        self.play_on = 0
        self.loadpath=os.getcwd()+"\\output001.avi"
        self.cap = cv2.VideoCapture()
        self.CAM_NUM = 0  # 为0时表示视频流来自笔记本内置摄像头
        self.viedo_area=QLabel()
        self.focc=cv2.VideoWriter_fourcc(*'XVID')
    def show_camera(self):
        if self.play_on == 1:
            self.cap.open(self.CAM_NUM)  # 参数是0，表示打开笔记本的内置摄像头，参数是视频文件路径则打开视频
            self.out = cv2.VideoWriter(self.loadpath, self.focc, 5.0, (640, 480), True)
        while self.play_on==1:
            ret, self.image = self.cap.read()  # 从视频流中读取
            time.sleep(0.05)
            if ret:
                self.image = cv2.fastNlMeansDenoising(self.image, 5, 5, 5, 7)  # 图像降噪
                self.out.write(self.image)
                show = cv2.resize(self.image, (640, 480))  # 把读到的帧的大小重新设置为 640x480
                show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)  # 视频色彩转换回RGB，这样才是现实的颜色
                showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0],
                                 QtGui.QImage.Format_RGB888)  # 把读取到的视频数据变成QImage形式
                self.viedo_area.setPixmap(QtGui.QPixmap.fromImage(showImage))  # 往显示视频的Label里 显示QImage







