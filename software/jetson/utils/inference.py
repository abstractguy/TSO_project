#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File:        software/utils/inference.py
# By:          Samuel Duclos
# For:         Myself
# Description: This file returns detection results from an image.

import cvlib

class ObjectCenter(object):
    def __init__(self, args):
        """Initialize variables."""
        self.args = args

    def infer(self, frame, confidence=0.25, nms_thresh=0.3, model='yolov4', object_category='person', filter_objects=False):
        """Apply object detection."""

        if self.args.flip_vertically:
            frame = cv2.flip(frame, 0)

        if self.args.flip_horizontally:
            frame = cv2.flip(frame, 1)

        predictions = cvlib.detect_common_objects(frame, confidence=confidence, nms_thresh=nms_thresh, model=model, enable_gpu=not self.args.disable_gpu)

        if predictions is not None:
            if filter_objects:
                predictions = self.filter_inference_results(predictions, object_category=object_category)

        return predictions

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

