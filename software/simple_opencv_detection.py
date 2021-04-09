#!/usr/bin/env python3

# File:        software/simple_opencv_detection.py
# By:          Samuel Duclos
# For:         Myself
# Usage:       python3 simple_opencv_detection.py --image doc/valid_test.png
# Description: This file implements software plan A for TSO_project.

from cvlib.object_detection import draw_bbox
import argparse, cv2, cvlib, matplotlib.pyplot as plt

def parse_args():
    """Parse input arguments."""
    parser = argparse.ArgumentParser(description='Simple OpenCV object detection test using one image.', 
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser = add_inference_args(parser)
    args = parser.parse_known_args()[0]
    print(vars(args))
    return args

def add_inference_args(parser):
    parser.add_argument('--image', metavar='<image>', type=str, required=False, default='./doc/valid_test.png', help='Path of input image.')
    parser.add_argument('--confidence-threshold', metavar='<confidence-threshold>', type=float, required=False, default=0.5, help='Confidence threshold.')
    parser.add_argument('--nms-threshold', metavar='<nms-threshold>', type=float, required=False, default=0.3, help='NMS threshold.')
    parser.add_argument('--model', metavar='<model>', type=str, required=False, default='yolov4-tiny', help='Path of input image.')
    parser.add_argument('--disable-gpu', action='store_true', help='Disable GPU usage for inference.')
    return parser

def detect(image_filename, 
           confidence_threshold=0.5, 
           nms_threshold=0.3, 
           model='yolov4-tiny', 
           enable_gpu=True):

    input_image = cv2.imread(image_filename)

    bbox, label, conf = cvlib.detect_common_objects(input_image, 
                                                    confidence=confidence_threshold, 
                                                    nms_thresh=nms_threshold, 
                                                    model=model, 
                                                    enable_gpu=enable_gpu)

    inferred_image = draw_bbox(input_image, bbox, label, conf)

    image_bgr = inferred_image
    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

    output_image = image_rgb
    plt.imshow(output_image)
    plt.show()

def main():
    args = parse_args()

    try:
        detect(image_filename=args.image, 
               confidence_threshold=args.confidence_threshold, 
               nms_threshold=args.nms_threshold, 
               model=args.model, 
               enable_gpu=not args.disable_gpu)

    except Exception as e:
        print(e)

    finally:
        print('Exited simple_opencv_detection.py main.')

if __name__ == '__main__':
    main()

