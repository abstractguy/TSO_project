#!/usr/bin/env python3

# File:      yolo_inference/utils/display.py
# By:        Samuel Duclos
# For:       Myself
# Reference: https://github.com/jkjung-avt/tensorrt_demos.git

from __future__ import print_function

import cv2


def open_window(window_name, title, width=None, height=None):
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.setWindowTitle(window_name, title)
    if width and height:
        cv2.resizeWindow(window_name, width, height)


def show_help_text(img, help_text):
    cv2.putText(img, help_text, (11, 20), cv2.FONT_HERSHEY_PLAIN, 1.0, (32, 32, 32), 4, cv2.LINE_AA)
    cv2.putText(img, help_text, (10, 20), cv2.FONT_HERSHEY_PLAIN, 1.0, (240, 240, 240), 1, cv2.LINE_AA)
    return img


def show_fps(img, fps):
    font = cv2.FONT_HERSHEY_PLAIN
    line = cv2.LINE_AA
    fps_text = 'FPS: {:.2f}'.format(fps)
    cv2.putText(img, fps_text, (11, 20), font, 1.0, (32, 32, 32), 4, line)
    cv2.putText(img, fps_text, (10, 20), font, 1.0, (240, 240, 240), 1, line)
    return img


def set_display(window_name, full_scrn):
    if full_scrn:
        cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    else:
        cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL)
