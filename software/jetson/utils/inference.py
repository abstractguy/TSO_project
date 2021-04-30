#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File:        software/utils/inference.py
# By:          Samuel Duclos
# For:         Myself
# Description: This file returns detection results from an image.

import cv2, cvlib, time

def add_inference_args(parser):
    """Add parser augument for inference options."""
    parser.add_argument('--confidence-threshold', metavar='<confidence-threshold>', type=float, required=False, default=0.25, help='Confidence threshold.') # 0.5
    parser.add_argument('--nms-threshold', metavar='<nms-threshold>', type=float, required=False, default=0.3, help='NMS threshold.')
    parser.add_argument('--model', metavar='<model>', type=str, required=False, default='yolov4', help='Path of input image.')
    parser.add_argument('--disable-gpu', action='store_true', help='Disable GPU usage for inference.')
    return parser

def infer(frame, confidence=0.25, nms_thresh=0.3, model='yolov4', enable_gpu=False, show=False):
    """Apply object detection."""
    predictions = cvlib.detect_common_objects(frame, confidence=confidence, nms_thresh=nms_thresh, model=model, enable_gpu=enable_gpu)

    if predictions is not None:
        bbox, label, conf = predictions

    if show:
        # Show raw inference results.
        print(bbox, label, conf)

    return bbox, label, conf

