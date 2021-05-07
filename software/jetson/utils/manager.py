#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File:        software/jetson/utils/manager.py
# By:          Samuel Duclos
# For:         Myself
# Description: This file implements a multiprocessing manager for PID motor control with object detection.

from multiprocessing import Value, Process, Manager
from utils.loop import loop
from utils.camera.camera import thread
from utils.pid import PIDController
from utils.uarm import UArm

import logging

logging.basicConfig()
LOGLEVEL = logging.getLogger().getEffectiveLevel()

def set_servos(pan, tilt, uarm, height, width, flip_vertically=False, flip_horizontally=False):
    """Servomotor loop for motor control."""
    try:
        while True:
            pan_grad = (-1 if flip_vertically else 1) * pan.value
            tilt_grad = (-1 if flip_horizontally else 1) * tilt.value

            # Remember depth!
            uarm.set_relative_position_from_center_in_grad(x=pan_grad, 
                                                           y=tilt_grad, 
                                                           z=0, 
                                                           speed=25, 
                                                           height=height, 
                                                           width=width)

    except KeyboardInterrupt:
        print('User terminated servo process.')

    except Exception as e:
        print(e)

    finally:
        # Release resources.
        print('Servo process done.')

def pid_process(output, p, i, d, box_coord, origin_coord, action):
    """PID loop for single motor control."""
    try:
        # Create a PID and initialize it.
        p = PIDController(p.value, i.value, d.value)
        p.reset()

        # Loop indefinitely.
        while True:
            #error = ((origin_coord - box_coord.value) / origin_coord) * 100.0 # Grad.
            error = origin_coord - box_coord.value

            output.value = p.update(error)
            logging.info(f'{action} error {error} angle: {output.value}')

    except KeyboardInterrupt:
        print('User terminated PID process.')

    except Exception as e:
        print(e)

    finally: # Release resources.
        print('PID process done.')

#('person',)
#('orange', 'apple', 'sports ball')
def process_manager(args):
    """Main process manager."""
    image_shape = args.image_shape
    (height, width) = image_shape

    try:
        uarm = UArm(uarm_speed=args.uarm_speed, 
                    uart_delay=args.uart_delay, 
                    servo_attach_delay=args.servo_attach_delay, 
                    set_position_delay=args.set_position_delay, 
                    servo_detach_delay=args.servo_detach_delay, 
                    pump_delay=args.pump_delay)

        with Manager() as manager:
            # Set initial bounding box (x, y)-coordinates to center of frame.
            center_x = manager.Value('i', 0)
            center_y = manager.Value('i', 0)

            object_x = manager.Value('i', 0)
            object_y = manager.Value('i', 0)

            center_x.value = height // 2
            center_y.value = width // 2

            # Pan and tilt angles updated by independent PID processes.
            pan = manager.Value('i', 0)
            tilt = manager.Value('i', 0)

            # PID gains for panning.
            pan_p = manager.Value('f', 1.0)
            # 0 time integral gain until inferencing is faster than ~50ms.
            pan_i = manager.Value('f', 0)
            pan_d = manager.Value('f', 0)
        
            # PID gains for tilting.
            tilt_p = manager.Value('f', 1.0)
            # 0 time integral gain until inferencing is faster than ~50ms.
            tilt_i = manager.Value('f', 0)
            tilt_d = manager.Value('f', 0)

            detector = loop if args.thread == 'old' else thread

            detect_process = Process(target=detector, args=(args, object_x, object_y, center_x, center_y))
            pan_process = Process(target=pid_process, args=(pan, pan_p, pan_i, pan_d, center_x, center_x.value, 'pan'))
            tilt_process = Process(target=pid_process, args=(tilt, tilt_p, tilt_i, tilt_d, center_y, center_y.value, 'tilt'))
            servo_process = Process(target=set_servos, args=(pan, tilt, uarm, height, width, args.flip_vertically, args.flip_horizontally))

            detect_process.start()
            pan_process.start()
            tilt_process.start()
            servo_process.start()

            detect_process.join()
            pan_process.join()
            tilt_process.join()
            servo_process.join()

    except KeyboardInterrupt:
        print('User terminated manager process.')

    except Exception as e:
        print(e)

    finally: # Release resources.
        print('Manager process done.')

