#!/usr/bin/env python3

# File:        software/simple_opencv_detection.py
# By:          Samuel Duclos
# For:         Myself
# Usage:       python3 simple_opencv_detection.py --image doc/valid_test.png --input-type image
# Usage:       python3 simple_opencv_detection.py --video doc/valid_test.mp4 --input-type video
# Description: This file implements software plan A for TSO_project.

from cvlib.object_detection import draw_bbox
import argparse, cv2, cvlib, numpy as np, time

def parse_args():
    """Parse input arguments."""
    parser = argparse.ArgumentParser(description='Simple OpenCV object detection test using one image.', 
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser = add_input_args(parser)
    parser = add_inference_args(parser)
    parser = add_output_args(parser)
    args = parser.parse_known_args()[0]
    print(vars(args))
    return args

def add_input_args(parser):
    """Add parser augument for input options."""
    parser.add_argument('--video-name', type=str, default='yolo_inference', help='Name of the video.')
    parser.add_argument('--image', metavar='<image>', type=str, required=False, default='./doc/valid_test.png', help='Path of input image.')
    parser.add_argument('--video', metavar='<video>', type=str, required=False, default='./doc/valid_test.mp4', help='Path of input video.')
    parser.add_argument('--input-type', metavar='<input-type>', type=str, required=False, choices=['image', 'video', 'camera'], default='video', help='Input type for inference.')
    return parser

def add_inference_args(parser):
    """Add parser augument for inference options."""
    parser.add_argument('--confidence-threshold', metavar='<confidence-threshold>', type=float, required=False, default=0.5, help='Confidence threshold.') # 0.25
    parser.add_argument('--nms-threshold', metavar='<nms-threshold>', type=float, required=False, default=0.3, help='NMS threshold.')
    parser.add_argument('--model', metavar='<model>', type=str, required=False, default='yolov4-tiny', help='Path of input image.')
    parser.add_argument('--disable-gpu', action='store_true', help='Disable GPU usage for inference.')
    return parser

def add_output_args(parser):
    """Add parser augument for output options."""
    parser.add_argument('--output-image', metavar='<output-image>', type=str, required=False, default='./doc/object_detection_result.jpg', help='Path of saved output image.')
    parser.add_argument('--save-image', action='store_true', help='Save output image inference results to file.')
    parser.add_argument('--no-show', action='store_true', help='Don\'t display live results on screen. Can improve FPS.')
    return parser

def detect(args):
    """Detection loop."""
    # Invert arguments early.
    enable_gpu = not args.disable_gpu
    show = not args.no_show

    # Read input. Camera mode not yet implemented.
    if args.input_type == 'image':
        cap = 'image'
        image = cv2.imread(args.image)
    elif args.input_type == 'video':
        cap = cv2.VideoCapture(args.video)
    else:
        raise NotImplementedError('Streaming not yet implemented.')

    if cap != 'image' and not cap.isOpened():
        print("Could not open video.")
        exit()

    # Loop through frames.
    while True:
        if not (cap == 'image' or cap.isOpened()):
            break

        # Read frame from video/camera.
        if cap == 'image':
            frame = np.copy(image)
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

        # Show raw inference results.
        print(bbox, label, conf)

        # Draw bounding box over detected objects.
        inferred_image = draw_bbox(frame, bbox, label, conf, write_conf=True)

        if show:
            # Display output.
            cv2.imshow('Object detection', inferred_image)

        if args.save_image:
            # Save output.
            cv2.imwrite('object_detection_result.jpg', inferred_image)

        # Catch keyboard input.
        key = cv2.waitKey(1)

        # ESC key: quit program.
        if key == 27:
            break

def main():
    """Main function."""
    args = parse_args()

    try:
        detect(args)

    except Exception as e:
        print(e)

    finally:
        # Release resources.
        if args.input_type != 'image':
            cap.release()
        cv2.destroyAllWindows()

        print('Exited simple_opencv_detection.py main.')

if __name__ == '__main__':
    main()

