#!/usr/bin/env python3

# File:        simple_opencv_detection.py
# By:          Samuel Duclos
# For:         Myself
# Usage:       python3 simple_opencv_detection.py --image doc/valid_test.jpg
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
    parser.add_argument('--image', metavar='<image>', type=str, required=False, default='/home/samuel/school/Projets/TSO_project/Logiciels/doc/valid_test.png', help='Path of input image.')
    return parser

def detect(image):
    image = cv2.imread(image)
    bbox, label, conf = cvlib.detect_common_objects(image)
    output_image = draw_bbox(image, bbox, label, conf)
    plt.imshow(output_image)
    plt.show

def main():
    args = parse_args()

    try:
        detect(image=args.image)

    except Exception as e:
        print(e)

    finally:
        print('Exited simple_opencv_detection.py main.')

if __name__ == '__main__':
    main()

