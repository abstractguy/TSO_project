#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File:        software/utils/loop.py
# By:          Samuel Duclos
# For:         Myself
# Description: This file implements the main loop for object detection with OpenCV.

IS_ARDUCAM = False

if IS_ARDUCAM:
    from utils_arducam import ArducamUtils

from utils.inference import ObjectCenter
from copy import deepcopy

import cv2, time

# gstreamer_pipeline returns a GStreamer pipeline for capturing from the CSI camera
# Defaults to 1280x720 @ 60fps
# Flip the image by setting the flip_method (most common values: 0 and 2)
# display_width and display_height determine the size of the window on the screen
def gstreamer_pipeline(
    capture_width=3820,
    capture_height=2464,
    display_width=960,
    display_height=616,
    framerate=21,
    flip_method=0,
):
    #return (
    #    "nvarguscamerasrc ! "
    #    "video/x-raw(memory:NVMM), "
    #    "width=(int)%d, height=(int)%d, "
    #    "format=(string)NV12, framerate=(fraction)%d/1 ! "
    #    "nvvidconv flip-method=%d ! "
    #    "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
    #    "videoconvert ! "
    #    "video/x-raw, format=(string)BGR ! appsink"
    #    % (
    #        capture_width,
    #        capture_height,
    #        framerate,
    #        flip_method,
    #        display_width,
    #        display_height,
    #    )
    #return (
    #    #'nvarguscamerasrc ! video/x-raw(memory:NVMM), width=3280, height=2464, format=(string)NV12, framerate=21/1 ! nvvidconv flip-method=0 ! video/x-raw, width=960, height=616, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink wait-on-eos=false max-buffers=1 drop=True'
    #    'nvarguscamerasrc ! video/x-raw(memory:NVMM), width=3820, height=2464, format=(string)NV12, framerate=21/1 ! nvvidconv flip-method=0 ! video/x-raw, width=960, height=616, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink wait-on-eos=false max-buffers=1 drop=True'
    #)
    return 'nvarguscamerasrc wbmode=3 tnr-mode=2 tnr-strength=1 ee-mode=2 ee-strength=1 ! video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method=0 ! video/x-raw, width=960, height=616, format=BGRx ! videoconvert ! video/x-raw, format=BGR ! videobalance contrast=1.5 brightness=-.2 saturation=1.2 ! appsink'

def loop(args, object_x=None, object_y=None, center_x=None, center_y=None):
    """Detection loop."""
    arducam_utils = None

    obj = ObjectCenter(args)

    # Read input.
    if args.input_type == 'image':
        image = cv2.imread(args.image)

    elif args.input_type == 'video':
        cap = cv2.VideoCapture(args.video)

    elif args.input_type == 'arducam':
        # Open camera.
        cap = cv2.VideoCapture(source, cv2.CAP_V4L2)

        # Set pixel format.
        if not cap.set(cv2.CAP_PROP_FOURCC, pixelformat):
            print('Failed to set pixel format.')

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

    elif args.input_type == 'camera':
        if args.is_rpi_cam:
            # To flip the image, modify the flip_method parameter (0 and 2 are the most common)
            print(gstreamer_pipeline(flip_method=0))
            cap = cv2.VideoCapture(gstreamer_pipeline(flip_method=0), cv2.CAP_GSTREAMER)

        else:
            cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        raise SystemExit('ERROR: failed to open camera!')

    # Prepare arguments early.
    show = not args.no_show
    (height, width) = args.image_shape
    full_scrn = False
    fps = 0.0

    if show:
        from utils.display import open_window, set_display, show_fps
        open_window(args.video_name, 'Camera inference', width, height)

    else:
        out = cv2.VideoWriter(args.video_name, cv2.VideoWriter_fourcc(*'mp4v'), 30, (width, height))

    tic = time.time()

    try:
        # Loop through frames.
        while True:
            if not (args.input_type == 'image' or cap.isOpened()):
                break

            # Read frame from video/camera.
            if args.input_type == 'image':
                frame = deepcopy(image)

            elif cap.isOpened():
                status, frame = cap.read()

                if frame is None:
                    status, frame = cap.read()

                if not status:
                    break

            if frame is not None:
                frame = obj.infer(frame, 
                                  object_x=object_x, 
                                  object_y=object_y, 
                                  center_x=center_x, 
                                  center_y=center_y)

            if show and frame is not None:
                frame = show_fps(frame, fps)

                if arducam_utils is not None:
                    if arducam_utils.convert2rgb == 0:
                        w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
                        h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
                        frame = frame.reshape(int(h), int(w))

                    frame = arducam_utils.convert(frame)

                if frame is not None:
                    # Show raw inference results.
                    cv2.imshow(args.video_name, frame)

            else:
                print('FPS:', fps)

            if args.save:
                # Save output.
                cv2.imwrite('object_detection_result.jpg', inferred_image)

            # Calculate an exponentially decaying average of FPS number.
            toc = time.time()
            curr_fps = 1.0 / (toc - tic)
            fps = curr_fps if fps == 0.0 else (fps * 0.95 + curr_fps * 0.05)
            tic = toc

            # Catch keyboard input.
            key = cv2.waitKey(1)

            # ESC key: quit program.
            if key == 27:
                break

            # Toggle fullscreen.
            elif show and (key == ord('F') or key == ord('f')):
                full_scrn = not full_scrn
                set_display(args.video_name, full_scrn)

    finally:
        # Release resources.
        if args.input_type != 'image':
            cap.release()

        cv2.destroyAllWindows()
