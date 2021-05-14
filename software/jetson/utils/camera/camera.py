#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File:        software/utils/camera/camera.py
# By:          Samuel Duclos
# For:         Myself
# Description: This file implements a multi-threaded camera I/O streamer for the camera program.
# Reference:   https://github.com/nrsyed/computer-vision.git

IS_ARDUCAM = False

if IS_ARDUCAM:
    from utils import ArducamUtils

from utils.camera.CountsPerSec import CountsPerSec
from utils.camera.VideoGet import VideoGet
from utils.camera.VideoShow import VideoShow
from utils.inference import ObjectCenter
from copy import deepcopy

import cv2

def fourcc(a, b, c, d):
    return ord(a) | (ord(b) << 8) | (ord(c) << 16) | (ord(d) << 24)

def pixelformat(string):
    if len(string) != 3 and len(string) != 4:
        msg = "{} is not a pixel format".format(string)
        raise argparse.ArgumentTypeError(msg)
    if len(string) == 3:
        return fourcc(string[0], string[1], string[2], ' ')
    else:
        return fourcc(string[0], string[1], string[2], string[3])

def show_info(arducam_utils):
    _, firmware_version = arducam_utils.read_dev(ArducamUtils.FIRMWARE_VERSION_REG)
    _, sensor_id = arducam_utils.read_dev(ArducamUtils.FIRMWARE_SENSOR_ID_REG)
    _, serial_number = arducam_utils.read_dev(ArducamUtils.SERIAL_NUMBER_REG)
    print("Firmware Version: {}".format(firmware_version))
    print("Sensor ID: 0x{:04X}".format(sensor_id))
    print("Serial Number: 0x{:08X}".format(serial_number))

def resize(frame, dst_width):
    height, width = frame.shape[:2]
    scale = dst_width * 1.0 / width
    return cv2.resize(frame, (int(scale * width), int(scale * height)))

def putIterationsPerSec(frame, iterations_per_sec):
    """Add iterations per second text to lower-left corner of a frame."""
    cv2.putText(frame, 
                "{:.0f} iterations/sec".format(iterations_per_sec), 
                (10, 450), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                1.0, 
                (255, 255, 255))
    return frame

def noThreading(args, source=0, object_x=None, object_y=None, center_x=None, center_y=None):
    """Grab and show video frames without multithreading."""

    arducam_utils = None

    obj = ObjectCenter(args)

    try:
        if IS_ARDUCAM:
            # Open camera.
            cap = cv2.VideoCapture(source, cv2.CAP_V4L2)

            # Set pixel format.
            
            if not cap.set(cv2.CAP_PROP_FOURCC, pixelformat):
                print("Failed to set pixel format.")

            arducam_utils = ArducamUtils(source)

            show_info(arducam_utils)

            # Turn off RGB conversion.
            if arducam_utils.convert2rgb == 0:
                cap.set(cv2.CAP_PROP_CONVERT_RGB, arducam_utils.convert2rgb)

            # Set width.
            if args.width != None:
                cap.set(cv2.CAP_PROP_FRAME_WIDTH, args.width)

            # Set height.
            if args.height != None:
                cap.set(cv2.CAP_PROP_FRAME_HEIGHT, args.height)

        else:
            cap = cv2.VideoCapture(source)

        cps = CountsPerSec().start()

        while True:
            grabbed, frame = cap.read()
            if not grabbed or cv2.waitKey(1) == ord('q'):
                break

            frame = obj.infer(frame, 
                              object_x=object_x, 
                              object_y=object_y, 
                              center_x=center_x, 
                              center_y=center_y)

            frame = putIterationsPerSec(frame, cps.countsPerSec())

            if frame is not None:
                if arducam_utils is not None:
                    if arducam_utils.convert2rgb == 0:
                        w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
                        h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
                        frame = frame.reshape(int(h), int(w))

                    frame = arducam_utils.convert(frame)

                cv2.imshow('uARM', frame)

            cps.increment()

    except KeyboardInterrupt:
        print('User terminated stream process.')

    except Exception as e:
        print(e)

    finally:
        # Release resources.
        print('Stream process done.')

def threadVideoGet(args, source=0, object_x=None, object_y=None, center_x=None, center_y=None):
    """Dedicated thread for grabbing video frames with VideoGet object.
       Main thread shows video frames."""

    arducam_utils = None

    obj = ObjectCenter(args)

    try:

        if IS_ARDUCAM:
            # Open camera.
            cap = cv2.VideoCapture(source, cv2.CAP_V4L2)

            # Set pixel format.
            
            if not cap.set(cv2.CAP_PROP_FOURCC, pixelformat):
                print("Failed to set pixel format.")

            arducam_utils = ArducamUtils(source)

            show_info(arducam_utils)

            # Turn off RGB conversion.
            if arducam_utils.convert2rgb == 0:
                cap.set(cv2.CAP_PROP_CONVERT_RGB, arducam_utils.convert2rgb)

            # Set width.
            if args.width != None:
                cap.set(cv2.CAP_PROP_FRAME_WIDTH, args.width)

            # Set height.
            if args.height != None:
                cap.set(cv2.CAP_PROP_FRAME_HEIGHT, args.height)

        else:
            video_getter = VideoGet(source).start()

        cps = CountsPerSec().start()

        while True:
            if (cv2.waitKey(1) == ord('q')) or video_getter.stopped:
                video_getter.stop()
                break

            frame = video_getter.frame
            if arducam_utils is not None:
                if arducam_utils.convert2rgb == 0:
                    w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
                    h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
                    frame = frame.reshape(int(h), int(w))

                frame = arducam_utils.convert(frame)

            frame = obj.infer(frame, 
                              object_x=object_x, 
                              object_y=object_y, 
                              center_x=center_x, 
                              center_y=center_y)

            frame = putIterationsPerSec(frame, cps.countsPerSec())

            if frame is not None:
                cv2.imshow('uARM', frame)

            cps.increment()

    except KeyboardInterrupt:
        print('User terminated stream process.')

    except Exception as e:
        print(e)

    finally:
        # Release resources.
        print('Stream process done.')

def threadVideoShow(args, source=0, object_x=None, object_y=None, center_x=None, center_y=None):
    """Dedicated thread for showing video frames with VideoShow object.
       Main thread grabs video frames."""

    arducam_utils = None

    obj = ObjectCenter(args)

    try:

        # Read input.
        if args.input_type == 'image':
            image = cv2.imread(args.image)

        elif args.input_type == 'video':
            cap = cv2.VideoCapture(args.video)

        elif args.input_type == 'camera':
            cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            raise SystemExit('ERROR: failed to open camera!')

        # Prepare arguments early.
        (height, width) = args.image_shape

        if args.no_show:
            out = cv2.VideoWriter(args.video_name, 
                                  cv2.VideoWriter_fourcc(*'mp4v'), 
                                  30, 
                                  (width, height))

        (grabbed, frame) = cap.read()
        video_shower = VideoShow(frame).start()
        cps = CountsPerSec().start()

        while True:
            # Read frame from video/camera.
            if args.input_type == 'image':
                frame = deepcopy(image)
                grabbed = True

            else:
                (grabbed, frame) = cap.read()

            if not grabbed or video_shower.stopped:
                video_shower.stop()
                break

            frame = obj.infer(frame, 
                              object_x=object_x, 
                              object_y=object_y, 
                              center_x=center_x, 
                              center_y=center_y)

            if frame is not None:
                frame = putIterationsPerSec(frame, cps.countsPerSec())
                video_shower.frame = frame
                cps.increment()

    except KeyboardInterrupt:
        print('User terminated stream process.')

    except Exception as e:
        print(e)

    finally:
        # Release resources.
        print('Stream process done.')

def threadBoth(args, source=0, object_x=None, object_y=None, center_x=None, center_y=None):
    """Dedicated thread for grabbing video frames with VideoGet object.
       Dedicated thread for showing video frames with VideoShow object.
       Main thread serves only to pass frames between VideoGet and
       VideoShow objects/threads."""

    arducam_utils = None

    obj = ObjectCenter(args)

    try:

        video_getter = VideoGet(source).start()
        video_shower = VideoShow(video_getter.frame).start()
        cps = CountsPerSec().start()

        while True:
            if video_getter.stopped or video_shower.stopped:
                video_shower.stop()
                video_getter.stop()
                break

        frame = video_getter.frame

        if frame is not None:
            frame = obj.infer(frame, 
                              object_x=object_x, 
                              object_y=object_y, 
                              center_x=center_x, 
                              center_y=center_y)

        if frame is not None:
            frame = putIterationsPerSec(frame, cps.countsPerSec())
            video_shower.frame = frame
            cps.increment()

    except KeyboardInterrupt:
        print('User terminated stream process.')

    except Exception as e:
        print(e)

    finally:
        # Release resources.
        print('Stream process done.')

def loop(args, object_x=None, object_y=None, center_x=None, center_y=None):
    """Threading type selector for multi-threading strategy."""
    try:
        if args.input_type == 'arducam' or args.thread == 'both':
            threadBoth(args, source=0, object_x=object_x, object_y=object_y, center_x=center_x, center_y=center_y)

        elif args.thread == 'get':
            threadVideoGet(args, source=0, object_x=object_x, object_y=object_y, center_x=center_x, center_y=center_y)

        elif args.thread == 'show':
            threadVideoShow(args, source=0, object_x=object_x, object_y=object_y, center_x=center_x, center_y=center_y)

        elif args.thread == 'none':
            noThreading(args, source=0, object_x=object_x, object_y=object_y, center_x=center_x, center_y=center_y)

        else:
            raise NotImplementedError('{} is not implemented!' % args.thread)

    except KeyboardInterrupt:
        print('User terminated stream process.')

    except Exception as e:
        print(e)

    finally:
        # Release resources.
        print('Stream process done.')

