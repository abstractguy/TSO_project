#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File:        software/utils/loop.py
# By:          Samuel Duclos
# For:         Myself
# Description: This file implements the main loop for object detection with OpenCV.

#from utils.overclock_settings import Overclock
from utils.inference import ObjectCenter
from copy import deepcopy
import cv2, time

def add_output_args(parser):
    """Add parser arguments for output options."""
    parser.add_argument('--video-name', type=str, default='yolo_inference', help='Name of the video.')
    parser.add_argument('--image-shape', metavar='<image-shape>', nargs='+', type=int, required=False, default=[480, 640], help='Shape of image.')
    parser.add_argument('--output-image', metavar='<output-image>', type=str, required=False, default='./doc/object_detection_result.jpg', help='Path of saved output image.')
    parser.add_argument('--mjpeg-port', metavar='<mjpeg-port>', type=int, required=False, default=None, help='MJPEG server port [8080]')
    parser.add_argument('--save', action='store_true', help='Save output inference results to file.')
    parser.add_argument('--no-show', action='store_true', help='Don\'t display live results on screen. Can improve FPS.')
    return parser

def loop(args, object_x=None, object_y=None, center_x=None, center_y=None):
    """Detection loop."""
    # Prepare arguments early.
    enable_gpu = not args.disable_gpu
    show = not args.no_show
    (height, width) = args.image_shape
    full_scrn = False
    fps = 0.0

    obj = ObjectCenter(args, enable_gpu=enable_gpu, show=show)

    tic = time.time()

    # Read input.
    if args.input_type == 'image':
        cap = 'image'
        image = cv2.imread(args.image)

    if show:
        from cvlib.object_detection import draw_bbox
        from utils.display import open_window, set_display, show_fps

    else:
        out = cv2.VideoWriter(args.video_name, cv2.VideoWriter_fourcc(*'mp4v'), 30, (width, height))

    if args.input_type == 'video':
        cap = cv2.VideoCapture(args.video)

    elif args.input_type == 'camera':
        cap = cv2.VideoCapture(0)

    if cap != 'image' and not cap.isOpened():
        raise SystemExit('ERROR: failed to open camera!')

    try:
        #overclock = Overclock(jetson_devkit='xavier')
        #overclock.overclock()

        if show:
            open_window(args.video_name, 'Camera inference', width, height)

        if args.mjpeg_port is None:
            mjpeg_server = None

        else:
            from utils.mjpeg import MjpegServer
            mjpeg_server = MjpegServer(port=args.mjpeg_port)
            print('MJPEG server started...')

        # Loop through frames.
        while True:
            if not (cap == 'image' or cap.isOpened()):
                break

            # Read frame from video/camera.
            if cap == 'image':
                frame = deepcopy(image)
                status = True
            elif cap.isOpened():
                status, frame = cap.read()
                if frame is None:
                    status, frame = cap.read()

            if not status:
                break

            if args.flip_vertically:
               frame = cv2.flip(frame, 0)

            if args.flip_horizontally:
               frame = cv2.flip(frame, 1)

            # Apply object detection.
            predictions = obj.infer(frame, 
                                    confidence=args.confidence_threshold, 
                                    nms_thresh=args.nms_threshold, 
                                    model=args.model, 
                                    object_category=args.object_category, 
                                    filter_objects=not args.no_filter_object_category)

            if predictions is not None:
                bbox, label, conf = predictions

                # Calculate the center of the frame since we will be trying to keep the object there.
                (H, W) = frame.shape[:2]
                #center_x.value = W // 2
                #center_y.value = H // 2

                #object_location = obj.update(predictions, frame, (center_x.value, center_y.value))
                #((object_x.value, object_y.value), predictions) = object_location

                center_x = W // 2
                center_y = H // 2

                object_location = obj.update(predictions, frame, (center_x, center_y))
                ((object_x, object_y), predictions) = object_location

                if show:
                    # Draw bounding box over detected objects.
                    inferred_image = draw_bbox(frame, bbox, label, conf, write_conf=True)

            if show:
                frame = show_fps(frame, fps)
                # Show raw inference results.
                cv2.imshow(args.video_name, frame)
            else:
                print('FPS:', fps)

            if mjpeg_server is not None:
                mjpeg_server.send_img(frame)

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

    finally: # Release resources.
        if args.mjpeg_port is not None:
            mjpeg_server.shutdown()

        if args.input_type != 'image':
            cap.release()

        #overclock.underclock()

