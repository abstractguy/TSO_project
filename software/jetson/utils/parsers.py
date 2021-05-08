#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File:        software/utils/parsers.py
# By:          Samuel Duclos
# For:         Myself
# Description: This file implements the different parsers for the program.

from pyuarm import add_uarm_args
import argparse

def parse_args():
    """Parse input arguments."""
    parser = argparse.ArgumentParser(description='Camera to motor feedback loop using OpenCV object detection test with one image, video or stream.', 
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser = add_uarm_args(parser)
    parser = add_input_args(parser)
    parser = add_inference_args(parser)
    parser = add_output_args(parser)
    args = parser.parse_known_args()[0]
    args.image_shape *= 2 if len(args.image_shape) == 1 else 1
    print(vars(args))
    return args

def add_input_args(parser):
    """Add parser arguments for input options."""
    parser.add_argument('--image', metavar='<image>', type=str, required=False, default='./doc/valid_test.png', help='Path of input image.')
    parser.add_argument('--video', metavar='<video>', type=str, required=False, default='./doc/valid_test.mp4', help='Path of input video.')
    parser.add_argument('--input-type', metavar='<input-type>', type=str, required=False, choices=['image', 'video', 'camera', 'arducam'], default='camera', help='Input type for inference ["image", "video", "camera", "arducam"].')
    parser.add_argument('--thread', metavar='<thread>', type=str, required=False, choices=['both', 'get', 'show', 'none', 'old'], default='show', help='Threading type ["both", "get", "show", "none", "old"].')
    parser.add_argument('--width', type=int, default=640, help='Image width [640].')
    parser.add_argument('--height', type=int, default=480, help='Image height [480].')
    parser.add_argument('--config-file-name', metavar='<config-file-name>', type=str, required=False, default='./utils/Config/USB2.0_UC-391_Rev.E+UC-625_Rev.B/OV9281/OV9281_1Lane/640x400/8b/OV9281_comb_A_640x400.cfg', help='Path of configuration file.')
    parser.add_argument('--flip-vertically', action='store_true', help='Flip image vertically.')
    parser.add_argument('--flip-horizontally', action='store_true', help='Flip image horizontally.')
    parser.add_argument('--is-arducam', action='store_true', help='If camera is Arducam Camarray.')
    return parser

def add_inference_args(parser):
    """Add parser arguments for inference options."""
    parser.add_argument('--object-category', metavar='<object-category>', type=str, required=False, default='scissors', help='COCO object category to select [person].')
    parser.add_argument('--confidence-threshold', metavar='<confidence-threshold>', type=float, required=False, default=0.25, help='Confidence threshold.') # 0.5
    parser.add_argument('--nms-threshold', metavar='<nms-threshold>', type=float, required=False, default=0.3, help='NMS threshold.')
    parser.add_argument('--model', metavar='<model>', type=str, required=False, default='yolov4', help='Path of input image.')
    parser.add_argument('--no-filter-object-category', action='store_true', help='Disable biggest single-object category selection.')
    parser.add_argument('--disable-gpu', action='store_true', help='Disable GPU usage for inference.')
    return parser

def add_output_args(parser):
    """Add parser arguments for output options."""
    parser.add_argument('--video-name', type=str, default='yolo_inference', help='Name of the video.')
    parser.add_argument('--image-shape', metavar='<image-shape>', nargs='+', type=int, required=False, default=[480, 640], help='Shape of image.')
    parser.add_argument('--output-image', metavar='<output-image>', type=str, required=False, default='./doc/object_detection_result.jpg', help='Path of saved output image.')
    parser.add_argument('--save', action='store_true', help='Save output inference results to file.')
    parser.add_argument('--no-show', action='store_true', help='Don\'t display live results on screen. Can improve FPS.')
    return parser

