#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File:        software/main.py
# By:          Samuel Duclos
# For:         Myself
# Before:      sudo /opt/conda/envs/school/bin/python3 -m pyuarm.tools.firmware -d
# Usage:       sudo /opt/conda/envs/school/bin/python3 main.py
# Usage:       sudo /opt/conda/envs/school/bin/python3 main.py --input-type camera
# Usage:       sudo /opt/conda/envs/school/bin/python3 main.py --video doc/valid_test.mp4 --input-type video
# Usage:       sudo /opt/conda/envs/school/bin/python3 main.py --image doc/valid_test.png --input-type image
# Description: This file tests object detection with OpenCV.

from utils.parsers import parse_args
from utils.manager import process_manager

def main():
    """Main function."""
    args = parse_args()
    process_manager(args)

if __name__ == '__main__':
    main()

