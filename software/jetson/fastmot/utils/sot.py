#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File:        software/jetson/fastmot/utils/sot.py
# By:          Samuel Duclos
# For:         Myself
# Description: This file returns detection results from an image.

from cvlib.object_detection import draw_bbox

class ObjectCenter(object):
    def __init__(self, args):
        """Initialize variables."""
        self.args = args

    def _filter_(self, frame, predictions):
        """Apply object detection."""

        if not self.args.no_filter_object_category:
            predictions = self.filter_inference_results(predictions, 
                                                        object_category=object_category)

        return predictions

    def filter_inference_results(self, predictions, object_category=1):
        """Return bounding box of biggest object of selected category."""
        if predictions is not None and len(predictions) > 0:
            biggest_bbox = None
            biggest_label = None
            biggest_conf = None
            most_pixels = 0

            for prediction in predictions:
                bbox, label, conf = predictions

                if label == object_category:
                    for (bbox, label, conf) in category_bboxes:
                        (x, y, w, h) = bbox
                        n_pixels = w * h

                        if n_pixels > most_pixels:
                            most_pixels = n_pixels
                            biggest_bbox = bbox
                            biggest_label = label
                            biggest_conf = conf

                category_bboxes = [(biggest_bbox, biggest_label, biggest_conf)]

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

    def filter(self, frame, object_x=None, object_y=None, center_x=None, center_y=None):
        """Apply object detection."""

        predictions = self._filter_(frame)

        if predictions is not None and len(predictions) > 0:
            bbox, label, conf = predictions[0][0]

            # Calculate the center of the frame since we will be trying to keep the object there.
            (H, W) = frame.shape[:2]
            center_x.value = W // 2
            center_y.value = H // 2

            object_location = self.update(predictions, frame, (center_x.value, center_y.value))
            ((object_x.value, object_y.value), predictions) = object_location

            if self.args.no_show:
                return None

            else:
                # Draw bounding box over detected objects.
                inferred_image = draw_bbox(frame, bbox, label, conf, write_conf=True)
                return inferred_image

