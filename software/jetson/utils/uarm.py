#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File:        software/jetson/utils/uarm.py
# By:          Samuel Duclos
# For:         My team.
# Description: uARM control in Python for TSO_team.

import logging, pyuarm, signal, time

def add_uarm_args(parser):
    parser.add_argument('--uarm-speed', metavar='<uarm-speed>', type=int, required=False, default=100, help='Speed of uARM displacements.')
    parser.add_argument('--uart-delay', metavar='<uart-delay>', type=float, required=False, default=3.0, help='Delay after configuring uARM\'s UART port.')
    parser.add_argument('--grab-delay', metavar='<grab-delay>', type=float, required=False, default=3.0, help='Delay after uARM grabs object.')
    parser.add_argument('--drop-delay', metavar='<drop-delay>', type=float, required=False, default=3.0, help='Delay after uARM drops object.')
    parser.add_argument('--pump-delay', metavar='<pump-delay>', type=float, required=False, default=3.0, help='Delay after uARM (de-)pumps object.')
    parser.add_argument('--servo-attach-delay', metavar='<servo-attach-delay>', type=float, required=False, default=3.0, help='Delay after uARM attaches servos.')
    parser.add_argument('--servo-detach-delay', metavar='<servo-detach-delay>', type=float, required=False, default=3.0, help='Delay after uARM detaches servos.')
    parser.add_argument('--set-position-delay', metavar='<set-position-delay>', type=float, required=False, default=3.0, help='Delay after uARM set to position.')
    parser.add_argument('--transition-delay', metavar='<transition-delay>', type=float, required=False, default=3.0, help='Delay between whole payload iterations.')
    return parser

class UArm(object):
    SERVO_MIN = -90
    SERVO_MAX = 90

    def __init__(self, 
                 uart_delay=2, 
                 servo_attach_delay=5, 
                 set_position_delay=5, 
                 servo_detach_delay=5, 
                 pump_delay=5):

        self.uart_delay = uart_delay
        self.servo_attach_delay = servo_attach_delay
        self.set_position_delay = set_position_delay
        self.servo_detach_delay = servo_detach_delay
        self.pump_delay = pump_delay

        self.uarm = self.get_uarm()

        time.sleep(self.uart_delay)

        self.set_servo_attach()

        self.initialize()

    def get_uarm(self):
        ports = pyuarm.tools.list_uarms.uarm_ports()
        if len(ports) > 0:
            return pyuarm.UArm(port_name=ports[0])
        else:
            return None

    def set_servo_attach(self):
        self.uarm.set_servo_attach()
        time.sleep(self.servo_attach_delay)

    def set_servo_detach(self):
        self.uarm.set_servo_detach()
        time.sleep(self.servo_detach_delay)

    def in_range(self, val, start, end):
        """Checks if the input value is in the supplied range."""
        return (val >= start and val <= end)

    def get_servo_angle(self, servo_number=None):
        return self.uarm.get_servo_angle(servo_number=servo_number)

    def set_servo_angle(self, servo, angle):
        if self.in_range(angle, self.SERVO_MIN, self.SERVO_MAX):
            self.uarm.set_servo_angle(servo, angle)
            time.sleep(self.set_position_delay)
        else:
            logging.info(f'angle not in range {angle}')

    def set_position(self, position=None):
        self.uarm.set_position(**position)
        time.sleep(self.set_position_delay)
        self.set_servo_detach()

    def set_pump(self, on=False):
        self.uarm.set_pump(ON=on)
        time.sleep(self.pump_delay)
        self.set_servo_detach()

    def drop(self, drop_position=None):
        self.set_position(position=drop_position)
        self.set_pump(on=False)

    def grab(self, grab_position=None, condition=True):
        self.set_position(position=grab_position)
        if condition:
            self.set_pump(on=True)
        return condition

    def set_weight_to_somewhere(self, grab_position=None, drop_position=None, sensor=True, detach=False):
        self.grab(grab_position=grab_position, condition=sensor)
        self.drop(drop_position=drop_position)
        self.reset(detach=detach)

    def initial_position(self):
        """Homes back to the initial position."""
        self.set_servo_angle(0, 90)
        self.set_servo_angle(1, 90)
        self.set_servo_angle(2, 90)
        self.set_servo_angle(3, 90)

    def initialize(self):
        self.set_pump(on=False)
        self.initial_position()

    def reset(self, detach=False):
        self.initialize()

        if detach:
            self.set_servo_detach()
            self.uarm.disconnect()

        print('uARM closed...')

    def __del__(self):
        self.reset()

