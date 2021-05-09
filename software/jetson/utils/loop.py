#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File:        software/utils/loop.py
# By:          Samuel Duclos
# For:         Myself
# Description: This file implements the main loop for object detection with OpenCV.

IS_ARDUCAM = False

if IS_ARDUCAM:
    from utils import ArducamUtils

from cvlib.object_detection import draw_bbox
from utils.inference import ObjectCenter
from copy import deepcopy

import cv2, os, sys, threading, time

def infer(frame, args, object_x=None, object_y=None, center_x=None, center_y=None):
    # Apply object detection.

    obj = ObjectCenter(args)

    predictions = obj.infer(frame, 
                            confidence=args.confidence_threshold, 
                            nms_thresh=args.nms_threshold, 
                            model=args.model, 
                            object_category=args.object_category, 
                            filter_objects=not args.no_filter_object_category)

    if predictions is not None and len(predictions) > 0:
        bbox, label, conf = predictions

        # Calculate the center of the frame since we will be trying to keep the object there.
        (H, W) = frame.shape[:2]
        center_x.value = W // 2
        center_y.value = H // 2

        object_location = obj.update(predictions, frame, (center_x.value, center_y.value))
        ((object_x.value, object_y.value), predictions) = object_location

        if args.no_show:
            return None

        else:
            # Draw bounding box over detected objects.
            inferred_image = draw_bbox(frame, bbox, label, conf, write_conf=True)
            return inferred_image

def loop(args, object_x=None, object_y=None, center_x=None, center_y=None):
    """Detection loop."""
    arducam_utils = None

    

    # Read input.
    if args.input_type == 'image':
        image = cv2.imread(args.image)

    elif args.input_type == 'video':
        cap = cv2.VideoCapture(args.video)

    elif args.input_type == 'camera':
        if args.input_type == 'arducam':
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

            inferred_image = infer(frame, 
                                   args, 
                                   object_x=object_x, 
                                   object_y=object_y, 
                                   center_x=center_x, 
                                   center_y=center_y)

            if show:
                frame = show_fps(frame, fps)

                if arducam_utils is not None:
                    if arducam_utils.convert2rgb == 0:
                        w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
                        h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
                        frame = frame.reshape(int(h), int(w))

                    frame = arducam_utils.convert(frame)

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

