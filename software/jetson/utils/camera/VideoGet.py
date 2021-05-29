#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File:        software/utils/camera/VideoGet.py
# By:          Samuel Duclos
# For:         Myself
# Description: This file implements a frame grabber on a dedicated thread for the camera program.
# Reference:   https://github.com/nrsyed/computer-vision.git

from threading import Thread
import cv2

class VideoGet:
    """Class that continuously gets frames from a VideoCapture object
       with a dedicated thread."""

    def __init__(self, src=0, is_rpi_cam=False):
        if is_rpi_cam:
            # To flip the image, modify the flip_method parameter (0 and 2 are the most common)
            print(gstreamer_pipeline(flip_method=0))
            self.stream = cv2.VideoCapture(gstreamer_pipeline(flip_method=0), cv2.CAP_GSTREAMER)

        else:
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

