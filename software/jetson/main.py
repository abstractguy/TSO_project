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

#from utils.overclock_settings import Overclock
from utils.parsers import parse_args
from utils.manager import process_manager

def main():
    """Main function."""
    args = parse_args()

    #overclock = Overclock(jetson_devkit='xavier')
    #overclock.overclock()

    try:
        process_manager(args)

    except Exception as e:
        print(e)

    finally:
        # Release resources.
        #overclock.underclock()

if __name__ == '__main__':
    main()

