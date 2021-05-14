#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File:        software/jetson/pyuarm/pyuarm/__init__.py
# By:          Samuel Duclos
# For:         Myself
# Description: This file runs before everything in the folder.

import sys

if sys.version > '3':
    PY3 = True
else:
    PY3 = False

from .uarm import add_uarm_args, UArm, get_default_logger
from .version import __version__

