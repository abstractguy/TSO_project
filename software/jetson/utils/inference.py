#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File:        software/utils/inference.py
# By:          Samuel Duclos
# For:         Myself
# Description: This file returns detection results from an image.

import cvlib

def add_inference_args(parser):
    """Add parser arguments for inference options."""
    parser.add_argument('--object-category', metavar='<object-category>', type=str, required=False, default='person', help='COCO object category to select [person].')
    parser.add_argument('--confidence-threshold', metavar='<confidence-threshold>', type=float, required=False, default=0.25, help='Confidence threshold.') # 0.5
    parser.add_argument('--nms-threshold', metavar='<nms-threshold>', type=float, required=False, default=0.3, help='NMS threshold.')
    parser.add_argument('--model', metavar='<model>', type=str, required=False, default='yolov4', help='Path of input image.')
    parser.add_argument('--disable-gpu', action='store_true', help='Disable GPU usage for inference.')
    parser.add_argument('--no-filter-object-category', action='store_true', help='Disable biggest single-object category selection.')
    return parser

class ObjectCenter(object):
    def __init__(self, args, enable_gpu=False, show=False):
        """Initialize variables."""
        self.args = args
        self.enable_gpu = enable_gpu
        self.show = show

    def infer(self, frame, confidence=0.25, nms_thresh=0.3, model='yolov4', object_category='person', filter_objects=False):
        """Apply object detection."""
        predictions = cvlib.detect_common_objects(frame, confidence=confidence, nms_thresh=nms_thresh, model=model, enable_gpu=self.enable_gpu)

        if predictions is not None:
            if filter_objects:
                predictions = self.filter_inference_results(predictions, object_category=object_category)

            bbox, label, conf = predictions

            if self.show:
                # Show raw inference results.
                print(bbox, label, conf)

        return bbox, label, conf

    def filter_inference_results(self, predictions, object_category='person'):
        """Return bounding box of biggest object of selected category."""
        if predictions is not None:
            bboxes, labels, confs = predictions

            # Only return bounding boxes for the selected object category.
            category_bboxes = [(bbox, label, conf) for (bbox, label, conf) in zip(bboxes, labels, confs) if label == object_category]

            if len(category_bboxes) > 0:
                # Choose biggest object of selected category.
                biggest_bbox = None
                biggest_label = None
                biggest_conf = None
                most_pixels = 0

                for (bbox, label, conf) in category_bboxes:
                    (x, y, w, h) = bbox
                    n_pixels = w * h

                    if n_pixels > most_pixels:
                        most_pixels = n_pixels
                        biggest_bbox = bbox
                        biggest_label = label
                        biggest_conf = conf

                category_bboxes = ([biggest_bbox], [biggest_label], [biggest_conf])

            predictions = category_bboxes

        return predictions

    def update(self, predictions, frame, frameCenter):
        """Asynchronous update of detection results to return object center."""
        if len(predictions) > 0:
            (x, y, w, h) = predictions[0][0]
            objectX = int(x + (w / 2.0))
            objectY = int(y + (h / 2.0))
            return ((objectX, objectY), predictions)

        else:
            return (frameCenter, None)

