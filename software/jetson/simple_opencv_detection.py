#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File:        software/simple_opencv_detection.py
# By:          Samuel Duclos
# For:         Myself
# Usage:       python3 simple_opencv_detection.py --image doc/valid_test.png --input-type image
# Usage:       python3 simple_opencv_detection.py --video doc/valid_test.mp4 --input-type video
# Usage:       python3 simple_opencv_detection.py --input-type camera
# Description: This file tests object detection with OpenCV.

from utils.camera import add_input_args
from utils.inference import add_inference_args
from utils.loop import add_output_args, loop
import argparse, cv2

def parse_args():
    """Parse input arguments."""
    parser = argparse.ArgumentParser(description='Simple OpenCV object detection test using one image, video or stream.', 
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

def main():
    """Main function."""
    args = parse_args()

    try:
        loop(args)

    except Exception as e:
        print(e)

    finally:
        # Release resources.
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

