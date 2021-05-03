#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File:        software/main.py
# By:          Samuel Duclos
# For:         Myself
# Usage:       sudo /opt/conda/envs/school/bin/python3 main.py
# Usage:       sudo /opt/conda/envs/school/bin/python3 main.py --input-type camera
# Usage:       sudo /opt/conda/envs/school/bin/python3 main.py --video doc/valid_test.mp4 --input-type video
# Usage:       sudo /opt/conda/envs/school/bin/python3 main.py --image doc/valid_test.png --input-type image
# Description: This file tests object detection with OpenCV.

from utils.camera import add_input_args
from utils.inference import add_inference_args
from utils.loop import add_output_args
from utils.uarm import add_uarm_args
from utils.manager import process_manager
import argparse

def parse_args():
    """Parse input arguments."""
    parser = argparse.ArgumentParser(description='Camera to motor feedback loop using OpenCV object detection test with one image, video or stream.', 
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser = add_input_args(parser)
    parser = add_inference_args(parser)
    parser = add_output_args(parser)
    parser = add_uarm_args(parser)
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
        process_manager(args)

    except Exception as e:
        print(e)

    finally: # Release resources.
        print('Done.')

if __name__ == '__main__':
    main()

