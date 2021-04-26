#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File:  software/jetson/utils/visualization.py
# By:    Samuel Duclos
# For:   Myself

import colorsys, cv2, math, numpy as np, random


def gen_colors(num_colors):
    hsvs = [[float(x) / num_colors, 1., 0.7] for x in range(num_colors)]
    random.seed(1337)
    random.shuffle(hsvs)
    rgbs = list(map(lambda x: list(colorsys.hsv_to_rgb(*x)), hsvs))
    bgrs = [(int(rgb[2] * 255), int(rgb[1] * 255),  int(rgb[0] * 255)) for rgb in rgbs]
    return bgrs


def draw_boxed_text(img, text, topleft, color):
    assert img.dtype == np.uint8
    img_h, img_w, _ = img.shape
    if topleft[0] >= img_w or topleft[1] >= img_h:
        return img
    size = cv2.getTextSize(text, cv2.FONT_HERSHEY_PLAIN, 1.0, 1)
    w = size[0][0] + 6
    h = size[0][1] + 6
    # the patch is used to draw boxed text
    patch = np.zeros((h, w, 3), dtype=np.uint8)
    patch[...] = color
    cv2.putText(patch, text, (4, h - 1), cv2.FONT_HERSHEY_PLAIN, 1.0, (255, 255, 255), thickness=1, lineType=cv2.LINE_8)
    cv2.rectangle(patch, (0, 0), (w - 1, h - 1), (0, 0, 0), thickness=1)
    w = int(min(w, img_w - topleft[0]))  # clip overlay at image boundary
    h = int(min(h, img_h - topleft[1]))
    # Overlay the boxed text onto region of interest (roi) in img
    topleft = (int(math.floor(topleft[0] + 0.5)), int(math.floor(topleft[1] + 0.5)))
    roi = img[topleft[1]:topleft[1] + h, topleft[0]:topleft[0] + w, :]
    cv2.addWeighted(patch[0:h, 0:w, :], 0.5, roi, 0.5, 0, roi)
    return img


class BBoxVisualization():
    def __init__(self, all_categories):
        self.all_categories = all_categories
        self.colors = gen_colors(len(all_categories))

    def draw_bboxes(self, image, boxes, confidences, categories):
        for box, confidence, category in zip(boxes, confidences, categories):
            #x_min, y_min, x_max, y_max = box[0], box[1], box[2], box[3]
            x_min, y_min, x_max, y_max = box
            cv2.rectangle(image, (x_min, y_min), (x_max, y_max), self.colors[int(category)], 2)
            text_location = (max(x_min + 2, 0), max(y_min + 2, 0))
            category_name = self.all_categories[int(category)]
            text = '%s %.2f' % (category_name, confidence)
            image = draw_boxed_text(image, text, text_location, self.colors[int(category)])
        return image


    '''
    def draw_bboxes(self, image, bboxes, confidences, categories):
        draw = ImageDraw.Draw(image)

        for box, confidence, category in zip(bboxes, confidences, categories):
            x_coord, y_coord, width, height = box

            left = max(0, np.floor(x_coord + 0.5).astype(int))
            top = max(0, np.floor(y_coord + 0.5).astype(int))

            right = min(image.width, np.floor(x_coord + width + 0.5).astype(int))
            bottom = min(image.height, np.floor(y_coord + height + 0.5).astype(int))

            draw.rectangle(((left, top), (right, bottom)), outline=self.colors[category])
            draw.text((left, top - 12), '{0} {1:.2f}'.format(self.all_categories[category], confidence), fill=self.colors[category])

        return image


    def plot_one_box(self, x, img, color=None, label=None, line_thickness=None):
        # Plots one bounding box on image img
        tl = line_thickness or round(0.002 * (img.shape[0] + img.shape[1]) / 2) + 1  # line thickness
        color = color or [random.randint(0, 255) for _ in range(3)]
        c1, c2 = (int(x[0]), int(x[1])), (int(x[2]), int(x[3]))
        cv2.rectangle(img, c1, c2, color, thickness=tl)
        if label:
            tf = max(tl - 1, 1)  # font thickness
            t_size = cv2.getTextSize(label, 0, fontScale=tl / 3, thickness=tf)[0]
            c2 = c1[0] + t_size[0], c1[1] - t_size[1] - 3
            cv2.rectangle(img, c1, c2, color, -1)  # filled
            cv2.putText(img, label, (c1[0], c1[1] - 2), 0, tl / 3, [225, 255, 255], thickness=tf, lineType=cv2.LINE_AA)

    def draw_bboxes(self, image, predictions, names, colors):
        for i, det in enumerate(predictions): # Detections per image.
            if det is not None and len(det):
                print(det)
                # Add predictions to image
                for *xyxy, conf, cls in det:
                    label = '%s %.2f' % (self.names[int(cls)], conf)
                    self.plot_one_box(xyxy, image, label=label, color=colors[int(cls)])
        return image
    '''
