#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File:        software/simple_opencv_detection.py
# By:          Samuel Duclos
# For:         Myself
# Usage:       python3 simple_opencv_detection.py --image doc/valid_test.png --input-type image
# Usage:       python3 simple_opencv_detection.py --video doc/valid_test.mp4 --input-type video
# Description: This file implements software plan A for TSO_project.

#from utils.overclock_settings import Overclock
from utils.camera import Camera
from utils.display import open_window, set_display, show_fps
from utils.visualization import BBoxVisualization
from utils.mjpeg import MjpegServer
from cvlib.object_detection import draw_bbox
from copy import deepcopy
import argparse, cv2, cvlib, time

def parse_args():
    """Parse input arguments."""
    parser = argparse.ArgumentParser(description='Simple OpenCV object detection test using one image.', 
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser = add_input_args(parser)
    parser = add_inference_args(parser)
    parser = add_output_args(parser)
    args = parser.parse_known_args()[0]
    args.image_shape *= 2 if len(args.image_shape) == 1 else 1
    if args.mjpeg_port is not None:
        args.no_show = True
    print(vars(args))
    return args

def add_input_args(parser):
    """Add parser augument for input options."""
    parser.add_argument('--image', metavar='<image>', type=str, required=False, default='./doc/valid_test.png', help='Path of input image.')
    parser.add_argument('--video', metavar='<video>', type=str, required=False, default='./doc/valid_test.mp4', help='Path of input video.')
    parser.add_argument('--input-type', metavar='<input-type>', type=str, required=False, choices=['image', 'video', 'camera'], default='video', help='Input type for inference.')
    parser.add_argument('--video_looping', action='store_true', help='Loop around the video file [False].')
    parser.add_argument('--rtsp', type=str, default=None, help='RTSP H.264 stream, e.g. rtsp://admin:123456@192.168.1.64:554.')
    parser.add_argument('--rtsp_latency', type=int, default=200, help='RTSP latency in ms [200].')
    parser.add_argument('--rtp', action='store_true', help='Use RTP through UDP.')
    parser.add_argument('--udp-port', metavar='<udp-port>', type=int, required=False, default=1337, help='UDP port to use for RTP.')
    parser.add_argument('--usb', type=int, default=None, help='USB webcam device id (/dev/video?) [None].')
    parser.add_argument('--onboard', type=int, default=None, help='Jetson onboard camera [None].')
    parser.add_argument('--width', type=int, default=640, help='Image width [640].')
    parser.add_argument('--height', type=int, default=480, help='Image height [480].')
    parser.add_argument('--copy_frame', action='store_true', help='Copy video frame internally [False].')
    parser.add_argument('--do_resize', action='store_true', help='Resize image/video [False].')
    parser.add_argument('--use-udp', action='store_true', help='Whether to use raw UDP.')
    return parser

def add_inference_args(parser):
    """Add parser augument for inference options."""
    parser.add_argument('--confidence-threshold', metavar='<confidence-threshold>', type=float, required=False, default=0.25, help='Confidence threshold.') # 0.5
    parser.add_argument('--nms-threshold', metavar='<nms-threshold>', type=float, required=False, default=0.3, help='NMS threshold.')
    parser.add_argument('--model', metavar='<model>', type=str, required=False, default='yolov4', help='Path of input image.')
    parser.add_argument('--disable-gpu', action='store_true', help='Disable GPU usage for inference.')
    return parser

def add_output_args(parser):
    """Add parser augument for output options."""
    parser.add_argument('--video-name', type=str, default='yolo_inference', help='Name of the video.')
    parser.add_argument('--image-shape', metavar='<image-shape>', nargs='+', type=int, required=False, default=[480, 640], help='Shape of image.')
    parser.add_argument('--output-image', metavar='<output-image>', type=str, required=False, default='./doc/object_detection_result.jpg', help='Path of saved output image.')
    parser.add_argument('--mjpeg-port', metavar='<mjpeg-port>', type=int, required=False, default=None, help='MJPEG server port [8080]')
    parser.add_argument('--save', action='store_true', help='Save output inference results to file.')
    parser.add_argument('--no-show', action='store_true', help='Don\'t display live results on screen. Can improve FPS.')
    return parser

def detect(args):
    """Detection loop."""
    # Prepare arguments early.
    enable_gpu = not args.disable_gpu
    show = not args.no_show
    (height, width) = args.image_shape
    full_scrn = False
    fps = 0.0
    tic = time.time()

    # Read input.
    if args.input_type == 'image':
        cap = 'image'
        image = cv2.imread(args.image)

    if not show:
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

        open_window(args.video_name, 'Camera inference', width, height)

        if args.mjpeg_port is None:
            mjpeg_server = None

        else:
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

            # Apply object detection.
            bbox, label, conf = cvlib.detect_common_objects(frame, 
                                                            confidence=args.confidence_threshold, 
                                                            nms_thresh=args.nms_threshold, 
                                                            model=args.model, 
                                                            enable_gpu=enable_gpu)

            predictions = bbox, label, conf
            if predictions is not None:
                boxes, confs, clss = predictions
                # Draw bounding box over detected objects.
                inferred_image = draw_bbox(frame, bbox, label, conf, write_conf=True)

            frame = show_fps(frame, fps)

            if show:
                # Show raw inference results.
                print(bbox, label, conf)
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

def main():
    """Main function."""
    args = parse_args()

    try:
        detect(args)

    except Exception as e:
        print(e)

    finally:
        # Release resources.
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

