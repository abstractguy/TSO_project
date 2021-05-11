#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File:        software/jetson/fastmot/utils/decoder.py
# By:          Samuel Duclos
# For:         Myself
# Description: This file was adapted from FastMOT for uARM feedback control.
# Reference:   https://github.com/GeekAlexis/FastMOT.git

import json

class ConfigDecoder(json.JSONDecoder):
    def __init__(self, **kwargs):
        json.JSONDecoder.__init__(self, **kwargs)
        # Use the custom JSONArray
        self.parse_array = self.JSONArray
        # Use the python implemenation of the scanner
        self.scan_once = json.scanner.py_make_scanner(self)

    def JSONArray(self, s_and_end, scan_once, **kwargs):
        values, end = json.decoder.JSONArray(s_and_end, scan_once, **kwargs)
        return tuple(values), end

