# File:        algorithm.py
# By:          Samuel Duclos
# For:         Myself and possibly others like school.
# Description: Pseudocode for TSO_project.

import math
import numpy as np
import pyuarm
import camera
import vision

center_threshold = 0.5
overlap_threshold = 0.5
speed = 100

image = camera.take_picture()
x_size, y_size = image.shape

arm = pyuarm.get_uarm()
arm.connect()

def calculate_overlap(x_size, y_size, x1, y1, x2, y2):
    image = np.zeros((y_size, x_size))
    image[y1:y2,x1:x2] = 1
    intersection = np.count_nonzero(image)
    return intersection / image.size

def weigh_center(x_size, y_size, x1, y1, x2, y2):
    x_weights = np.linspace(0, math.sqrt(2) / 2, num=x_size // 2)
    y_weights = np.linspace(0, math.sqrt(2) / 2, num=y_size // 2)
    if x_size % 2 == 0:
        x_weights = np.concatenate((x_weights, x_weights[::-1]))
    else:
        x_weights = np.concatenate((x_weights, [1.0], x_weights[::-1]))
    if y_size % 2 == 0:
        y_weights = np.concatenate((y_weights, y_weights[::-1]))
    else:
        y_weights = np.concatenate((y_weights, [1.0], y_weights[::-1]))
    xv, yv = np.meshgrid(x_weights, y_weights)
    euclidian_weights = np.sqrt(xv * xv + yv * yv)
    return euclidian_weights[(y2 - y1) // 2, (x2 - x1) // 2]

while True:
    arm.reset()
    while True:
        image = camera.take_picture()
        x1, y1, x2, y2 = vision.predict(image)
        if weigh_center(x_size, y_size, x1, y1, x2, y2) < center_threshold:
            arm.set_position(x=(x2 - x1) // 2, y=(y2 - y1) // 2, z=0, speed=speed)
        if calculate_overlap(x_size, y_size, x1, y1, x2, y2) > overlap_threshold:
            arm.set_pump(True)
            break
