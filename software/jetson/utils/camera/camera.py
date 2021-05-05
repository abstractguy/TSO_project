#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File:        software/utils/camera/camera.py
# By:          Samuel Duclos
# For:         Myself
# Description: This file implements a multi-threaded camera I/O streamer for the camera program.

from utils.camera.CountsPerSec import CountsPerSec
from utils.camera.VideoGet import VideoGet
from utils.camera.VideoShow import VideoShow

import cv2

def putIterationsPerSec(frame, iterations_per_sec):
    """Add iterations per second text to lower-left corner of a frame."""
    cv2.putText(frame, 
                "{:.0f} iterations/sec".format(iterations_per_sec), 
                (10, 450), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                1.0, 
                (255, 255, 255))
    return frame

def threadBoth(source=0):
    """Dedicated thread for grabbing video frames with VideoGet object.
       Dedicated thread for showing video frames with VideoShow object.
       Main thread serves only to pass frames between VideoGet and
       VideoShow objects/threads."""

    video_getter = VideoGet(source).start()
    video_shower = VideoShow(video_getter.frame).start()
    cps = CountsPerSec().start()

    while True:
        if video_getter.stopped or video_shower.stopped:
            video_shower.stop()
            video_getter.stop()
            break

    frame = video_getter.frame
    frame = putIterationsPerSec(frame, cps.countsPerSec())
    video_shower.frame = frame
    cps.increment()

def thread_camera(args):
    try:
        if args.input_type == 'camera':
            threadBoth(source=0)

        else:
            raise NotImplementedError("ERROR: 'image', 'video' and 'arducam' are not implemented yet!")

    except Exception as e:
        print(e)

    finally:
        # Release resources.
        print('Done.')

