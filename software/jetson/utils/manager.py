#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File:        software/jetson/utils/manager.py
# By:          Samuel Duclos
# For:         Myself
# Description: This file implements a multiprocessing manager for motor control after object detection.


from multiprocessing import Value, Process, Manager
from utils.camera2 import run_pantilt_detect
from utils.pid import PIDController
from pyuarm.protocol import *

import logging, pyuarm, signal, sys


logging.basicConfig()
LOGLEVEL = logging.getLogger().getEffectiveLevel()

RESOLUTION = (320, 320)

SERVO_MIN = -90
SERVO_MAX = 90

CENTER = (RESOLUTION[0] // 2, RESOLUTION[1] // 2)


def signal_handler(sig, frame):
    """Handles keyboard interrupt."""
    print("[INFO] You pressed `CTRL + C`! Exiting...")
    pyuarm.set_servo_detach()
    sys.exit()


def in_range(val, start, end):
    """Checks if the input value is in the supplied range."""
    return (val >= start and val <= end)


def set_servos(pan, tilt):
    # Signal trap to handle keyboard interrupt.
    signal.signal(signal.SIGINT, signal_handler)

    while True:
        pan_angle = -1 * pan.value
        tilt_angle = tilt.value

        # If the pan angle is within the range: pan.
        if in_range(pan_angle, SERVO_MIN, SERVO_MAX):
            pyuarm.set_servo_angle(SERVO_BOTTOM, pan_angle) # Verify this is the correct servo!!!
        else:
            logging.info(f'pan_angle not in range {pan_angle}')

        if in_range(tilt_angle, SERVO_MIN, SERVO_MAX):
            pyuarm.set_servo_angle(SERVO_LEFT, tilt_angle) # Verify this is the correct servo!!!
        else:
            logging.info(f'tilt_angle not in range {tilt_angle}')


def pid_process(output, p, i, d, box_coord, origin_coord, action):
    # Signal trap to handle keyboard interrupt.
    signal.signal(signal.SIGINT, signal_handler)

    # Create a PID and initialize it.
    p = PIDController(p.value, i.value, d.value)
    p.reset()

    # Loop indefinitely.
    while True:
        error = origin_coord - box_coord.value
        output.value = p.update(error)
        # logging.info(f'{action} error {error} angle: {output.value}')

# ('person',)
#('orange', 'apple', 'sports ball')


def pantilt_process_manager(model_cls, labels=('person',), rotation=0):
    pyuarm.set_servo_attach()
    with Manager() as manager:
        # Set initial bounding box (x, y)-coordinates to center of frame.
        center_x = manager.Value('i', 0)
        center_y = manager.Value('i', 0)

        center_x.value = RESOLUTION[0] // 2
        center_y.value = RESOLUTION[1] // 2

        # Pan and tilt angles updated by independent PID processes.
        pan = manager.Value('i', 0)
        tilt = manager.Value('i', 0)

        # PID gains for panning.
        pan_p = manager.Value('f', 0.05)
        # 0 time integral gain until inferencing is faster than ~50ms.
        pan_i = manager.Value('f', 0.1)
        pan_d = manager.Value('f', 0)

        # PID gains for tilting.
        tilt_p = manager.Value('f', 0.15)
        # 0 time integral gain until inferencing is faster than ~50ms.
        tilt_i = manager.Value('f', 0.2)
        tilt_d = manager.Value('f', 0)

        detect_process = Process(target=run_pantilt_detect, args=(center_x, center_y, labels, model_cls, rotation))
        pan_process = Process(target=pid_process, args=(pan, pan_p, pan_i, pan_d, center_x, CENTER[0], 'pan'))
        tilt_process = Process(target=pid_process, args=(tilt, tilt_p, tilt_i, tilt_d, center_y, CENTER[1], 'tilt'))
        servo_process = Process(target=set_servos, args=(pan, tilt))

        detect_process.start()
        pan_process.start()
        tilt_process.start()
        servo_process.start()

        detect_process.join()
        pan_process.join()
        tilt_process.join()
        servo_process.join()


if __name__ == '__main__':
    pantilt_process_manager(model_cls, labels=('person',), rotation=0)

