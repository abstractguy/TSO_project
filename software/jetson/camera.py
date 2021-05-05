#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File:        software/jetson/camera.py
# By:          Samuel Duclos
# For:         Myself
# Description: This file implements the main program for a multi-threaded camera I/O streamer.

from utils.parsers import parse_args
from utils.camera.camera import thread_camera

def main():
    """Main program for a multi-threaded camera I/O streamer."""
    args = parse_args()
    thread_camera(args)

if __name__ == "__main__":
    main()

