#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File:        software/jetson/utils/parsers.py
# By:          Samuel Duclos
# For:         Myself
# Description: This file implements the different parsers for the program.

from pathlib import Path
import argparse

def parse_args():
    """Parse input arguments."""
    parser = argparse.ArgumentParser(description='Camera to motor feedback loop using OpenCV object detection test with one image, video or stream.', 
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser = add_uarm_args(parser)
    parser = add_input_args(parser)
    parser = add_inference_args(parser)
    parser = add_sot_args(parser)
    parser = add_output_args(parser)
    args = parser.parse_known_args()[0]
    args.image_shape *= 2 if len(args.image_shape) == 1 else 1
    print(vars(args))
    return args

def add_uarm_args(parser):
    parser.add_argument('--uarm-speed', metavar='<uarm-speed>', type=int, required=False, default=150, help='Speed of uARM displacements.')
    parser.add_argument('--pump-delay', metavar='<pump-delay>', type=float, required=False, default=3.0, help='Delay after uARM (de-)pumps object.')
    parser.add_argument('--servo-attach-delay', metavar='<servo-attach-delay>', type=float, required=False, default=4.0, help='Delay after uARM attaches servos.')
    parser.add_argument('--set-position-delay', metavar='<set-position-delay>', type=float, required=False, default=2.0, help='Delay after uARM set to position.')
    parser.add_argument('--servo-detach-delay', metavar='<servo-detach-delay>', type=float, required=False, default=2.0, help='Delay after uARM detaches servos.')
    return parser

def add_input_args(parser):
    """Add parser arguments for input options."""
    parser.add_argument('--image', metavar='<image>', type=str, required=False, default='./doc/valid_test.png', help='Path of input image.')
    parser.add_argument('--video', metavar='<video>', type=str, required=False, default='./doc/valid_test.mp4', help='Path of input video.')
    parser.add_argument('--test-type', metavar='<test-type>', type=str, required=False, choices=['x86_64', 'xavier', 'nano'], default='x86_64', help='Input type for inference ["x86_64", "xavier", "nano"].')
    parser.add_argument('--input-type', metavar='<input-type>', type=str, required=False, choices=['image', 'video', 'camera', 'arducam'], default='camera', help='Input type for inference ["image", "video", "camera", "arducam"].')
    parser.add_argument('--thread', metavar='<thread>', type=str, required=False, choices=['both', 'get', 'show', 'none', 'old'], default='show', help='Threading type ["both", "get", "show", "none", "old"].')
    parser.add_argument('--width', type=int, default=640, help='Image width [640].')
    parser.add_argument('--height', type=int, default=480, help='Image height [480].')
    parser.add_argument('--is-rpi-cam', action='store_true', help='Is Raspberry Pi camera v2.')
    parser.add_argument('--flip-vertically', action='store_true', help='Flip image vertically.')
    parser.add_argument('--flip-horizontally', action='store_true', help='Flip image horizontally.')
    return parser

def add_inference_args(parser):
    """Add parser arguments for inference options."""
    parser.add_argument('--inference-type', metavar='<inference-type>', type=str, required=False, choices=['cvlib', 'fastmot'], default='cvlib', help='Input type for inference ["cvlib", "fastmot"].')
    parser.add_argument('--names', metavar='<names>', type=str, required=False, default='./utils/cfg/coco.names', help='Path to *.names.')
    parser.add_argument('--object-category', metavar='<object-category>', type=str, required=False, default='scissors', help='COCO object category to select [scissors].')
    parser.add_argument('--confidence-threshold', metavar='<confidence-threshold>', type=float, required=False, default=0.25, help='Confidence threshold.') # 0.5
    parser.add_argument('--nms-threshold', metavar='<nms-threshold>', type=float, required=False, default=0.3, help='NMS threshold.')
    parser.add_argument('--model', metavar='<model>', type=str, required=False, default='yolov4', help='Path of input image.')
    parser.add_argument('--no-filter-object-category', action='store_true', help='Disable biggest single-object category selection.')
    parser.add_argument('--disable-gpu', action='store_true', help='Disable GPU usage for inference.')
    return parser

def add_sot_args(parser):
    parser.add_argument('-i', '--input_uri', metavar='<URI>', required=False, default='/dev/video0', 
                        help='URI to input stream\n'
                             '1) image sequence (e.g. img_%%06d.jpg)\n'
                             '2) video file (e.g. video.mp4)\n'
                             '3) MIPI CSI camera (e.g. csi://0)\n'
                             '4) USB/V4L2 camera (e.g. /dev/video0)\n'
                             '5) RTSP stream (rtsp://<user>:<password>@<ip>:<port>/<path>)\n'
                             '6) HTTP stream (http://<user>:<password>@<ip>:<port>/<path>)\n')
    parser.add_argument('-c', '--config', metavar='<FILE>', default=Path(__file__).parent / 'cfg' / 'mot.json', help='Path to configuration JSON file.')
    parser.add_argument('-o', '--output_uri', metavar='<URI>', help='URI to output video (e.g. output.mp4).')
    parser.add_argument('-l', '--log', metavar='<FILE>', help='Output a MOT Challenge format log (e.g. eval/results/mot17-04.txt).')
    parser.add_argument('-m', '--no_mot', action='store_true', help='Run multiple object tracker.')
    parser.add_argument('-g', '--no_gui', action='store_true', help='Enable display.')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output for debugging.')
    return parser

def add_output_args(parser):
    """Add parser arguments for output options."""
    parser.add_argument('--video-name', type=str, default='yolo_inference', help='Name of the video.')
    parser.add_argument('--image-shape', metavar='<image-shape>', nargs='+', type=int, required=False, default=[480, 640], help='Shape of image.')
    parser.add_argument('--output-image', metavar='<output-image>', type=str, required=False, default='./doc/object_detection_result.jpg', help='Path of saved output image.')
    parser.add_argument('--save', action='store_true', help='Save output inference results to file.')
    parser.add_argument('--no-show', action='store_true', help='Don\'t display live results on screen. Can improve FPS.')
    parser.add_argument('--no-uarm', action='store_true', help='Don\'t assume a uARM is connected (for tests).')
    return parser
