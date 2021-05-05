#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File:        software/utils/camera/VideoShow.py
# By:          Samuel Duclos
# For:         Myself
# Description: This file implements a frame "show"-er on a dedicated thread for the camera program.
# Reference:   https://github.com/nrsyed/computer-vision.git

IS_ARDUCAM = False

if IS_ARDUCAM:
    from utils import arducam_config_parser
    from utils import ArducamSDK
    from utils.ImageConvert import *

from threading import Thread
import cv2, os, sys, time

global cfg, handle, running, Width, Height, save_flag, color_mode, save_raw

running = True
save_flag = False
save_raw = False
cfg = {}
handle = {}

class VideoShow:
    """Class that continuously shows a frame using a dedicated thread."""

    def __init__(self, frame=None):
        self.frame = frame
        self.stopped = False

    def start(self):
        Thread(target=self.show, args=()).start()
        return self

    def show(self):
        while not self.stopped:
            cv2.imshow("Video", self.frame)
            if cv2.waitKey(1) == ord("q"):
                self.stopped = True

    def stop(self):
        self.stopped = True

def readImage_thread():
    global handle, running, Width, Height, save_flag, cfg, color_mode, save_raw
    global COLOR_BayerGB2BGR, COLOR_BayerRG2BGR, COLOR_BayerGR2BGR, COLOR_BayerBG2BGR

    count = 0
    totalFrame = 0

    time0 = time.time()
    time1 = time.time()

    data = {}

    cv2.namedWindow("ArduCam Camarray", 1)

    if not os.path.exists("images"):
        os.makedirs("images")

    while running:
        display_time = time.time()

        if ArducamSDK.Py_ArduCam_availableImage(handle) > 0:		
            rtn_val, data, rtn_cfg = ArducamSDK.Py_ArduCam_readImage(handle)
            datasize = rtn_cfg['u32Size']

            if rtn_val != 0 or datasize == 0:
                ArducamSDK.Py_ArduCam_del(handle)

                print("Read data fail!")

                continue

            image = convert_image(data, rtn_cfg, color_mode)

            time1 = time.time()

            if time1 - time0 >= 1:
                print("%s %d %s\n" % ("fps:", count, "/s"))

                count = 0
                time0 = time1

            count += 1

            if save_flag:
                cv2.imwrite("images/image%d.jpg" % totalFrame, image)

                if save_raw:
                    with open("images/image%d.raw" % totalFrame, 'wb') as f:
                        f.write(data)

                totalFrame += 1

            image = cv2.resize(image, (640, 480), interpolation=cv2.INTER_LINEAR)

            cv2.imshow("ArduCam Demo", image)
            cv2.waitKey(10)

            ArducamSDK.Py_ArduCam_del(handle)

        else:
            time.sleep(0.001)

