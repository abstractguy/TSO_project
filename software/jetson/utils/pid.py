#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File:        software/jetson/utils/pid.py
# By:          Samuel Duclos
# For:         Myself
# Description: This class calculates the PID to control motors.


import time

class PIDController(object):
    def __init__(self, kP=1, kI=0, kD=0):
        # Initialize gains.
        self.kP = kP
        self.kI = kI
        self.kD = kD

    def reset(self):
        # Initialize current and previous time.
        self.time_curr = time.time()
        self.time_prev = self.time_curr

        # Initialize previous error.
        self.error_prev = 0

        # Initialize the term result variables.
        self.cP = 0
        self.cI = 0
        self.cD = 0

    def update(self, error, sleep=0.01):
        time.sleep(sleep)

        # Grab the current time and calculate delta time / error.
        self.time_curr = time.time()
        time_delta = self.time_curr - self.time_prev
        error_delta = error - self.error_prev

        # Proportional term.
        self.cP = error

        # Integral term.
        self.cI += error * time_delta

        # Derivative term and prevent divide by zero.
        self.cD = (error_delta / time_delta) if time_delta > 0 else 0

        # Save previous time and error for the next update.
        self.time_prev = self.time_curr
        self.error_prev = error

        # Sum the terms and return.
        return sum([
            self.kP * self.cP,
            self.kI * self.cI,
            self.kD * self.cD
        ])

