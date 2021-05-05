#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File:        software/utils/camera/VideoGet.py
# By:          Samuel Duclos
# For:         Myself
# Description: This file implements a frame grabber on a dedicated thread for the camera program.
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

class VideoGet:
    """Class that continuously gets frames from a VideoCapture object
       with a dedicated thread."""

    def __init__(self, src=0):
        self.stream = cv2.VideoCapture(src)
        (self.grabbed, self.frame) = self.stream.read()
        self.stopped = False

    def start(self):    
        Thread(target=self.get, args=()).start()
        return self

    def get(self):
        while not self.stopped:
            if not self.grabbed:
                self.stop()
            else:
                (self.grabbed, self.frame) = self.stream.read()

    def stop(self):
        self.stopped = True

def captureImage_thread():
    global handle, running

    rtn_val = ArducamSDK.Py_ArduCam_beginCaptureImage(handle)

    if rtn_val != 0:
        print("Error beginning capture, rtn_val = ", rtn_val)

        running = False

        return

    else:
        print("Capture began, rtn_val = ", rtn_val)

    while running:
        rtn_val = ArducamSDK.Py_ArduCam_captureImage(handle)

        if rtn_val > 255:
            print("Error capture image, rtn_val = ", rtn_val)

            if rtn_val == ArducamSDK.USB_CAMERA_USB_TASK_ERROR:
                break

        time.sleep(0.005)

    running = False
    ArducamSDK.Py_ArduCam_endCaptureImage(handle)

