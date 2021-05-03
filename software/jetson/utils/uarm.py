#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File:        software/jetson/utils/uarm.py
# By:          Samuel Duclos
# For:         My team.
# Description: uARM control in Python for TSO_team.

import pyuarm, signal, time

initial_position = {'x': 21.6, 'y': 80.79, 'z': 186.11, 'speed': 150, 'relative': False, 'wait': True}

def add_uarm_args(parser):
    parser.add_argument('--first-x-position', metavar='<first-x-position>', type=float, required=False, default=21.6, help='First position on X axis.')
    parser.add_argument('--first-y-position', metavar='<first-y-position>', type=float, required=False, default=80.79, help='First position on Y axis.')
    parser.add_argument('--first-z-position', metavar='<first-z-position>', type=float, required=False, default=186.11, help='First position on Z axis.')
    parser.add_argument('--second-x-position', metavar='<second-x-position>', type=float, required=False, default=-232.97, help='Second absolute position to X axis.')
    parser.add_argument('--second-y-position', metavar='<second-y-position>', type=float, required=False, default=120.86, help='Second absolute position to Y axis.')
    parser.add_argument('--second-z-position', metavar='<second-z-position>', type=float, required=False, default=126.59, help='Second absolute position to Z axis.')
    parser.add_argument('--third-x-position', metavar='<third-x-position>', type=float, required=False, default=313.93, help='Third absolute position to X axis.')
    parser.add_argument('--third-y-position', metavar='<third-y-position>', type=float, required=False, default=18.76, help='Third absolute position to Y axis.')
    parser.add_argument('--third-z-position', metavar='<third-z-position>', type=float, required=False, default=178.67, help='Third absolute position to Z axis.')
    parser.add_argument('--speed', metavar='<speed>', type=int, required=False, default=150, help='Speed of uARM displacements.')
    parser.add_argument('--uart-delay', metavar='<uart-delay>', type=float, required=False, default=2.0, help='Delay after configuring uARM\'s UART port.')
    parser.add_argument('--grab-delay', metavar='<grab-delay>', type=float, required=False, default=5.0, help='Delay after uARM grabs object.')
    parser.add_argument('--drop-delay', metavar='<drop-delay>', type=float, required=False, default=5.0, help='Delay after uARM drops object.')
    parser.add_argument('--pump-delay', metavar='<pump-delay>', type=float, required=False, default=5.0, help='Delay after uARM (de-)pumps object.')
    parser.add_argument('--servo-attach-delay', metavar='<servo-attach-delay>', type=float, required=False, default=5.0, help='Delay after uARM attaches servos.')
    parser.add_argument('--servo-detach-delay', metavar='<servo-detach-delay>', type=float, required=False, default=5.0, help='Delay after uARM detaches servos.')
    parser.add_argument('--set-position-delay', metavar='<set-position-delay>', type=float, required=False, default=5.0, help='Delay after uARM set to position.')
    parser.add_argument('--transition-delay', metavar='<transition-delay>', type=float, required=False, default=5.0, help='Delay after using uARM buzzer signals the end of a phase and allows world to react.')
    return parser

class UArm(object):
    def __init__(self, 
                 uart_delay=2, 
                 initial_position=initial_position, 
                 servo_attach_delay=5, 
                 set_position_delay=5, 
                 servo_detach_delay=5, 
                 pump_delay=5):

        self.uart_delay = uart_delay
        self.initial_position = initial_position
        self.servo_attach_delay = servo_attach_delay
        self.set_position_delay = set_position_delay
        self.servo_detach_delay = servo_detach_delay
        self.pump_delay = pump_delay

        self.uarm = self.get_uarm()
        self.handle_exit_signals()

        time.sleep(self.uart_delay)

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

    def set_servo_angle(self, servo, angle):
        self.uarm.set_servo_angle(servo, angle)
        time.sleep(self.set_position_delay)

    def set_position(self, position=None):
        self.set_servo_attach()
        self.uarm.set_position(**position)
        time.sleep(self.set_position_delay)
        self.set_servo_detach()

    def set_pump(self, on=False):
        self.set_servo_attach()
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

    def set_weight_to_somewhere(self, grab_position=None, drop_position=None, sensor=True):
        self.grab(grab_position=grab_position, condition=sensor)
        self.drop(drop_position=drop_position)
        self.reset()

    def reset(self):
        self.set_pump(on=False)
        self.set_position(position=self.initial_position)
        self.set_servo_detach()
        print('uARM closed...')

    def __del__(self):
        self.reset()

    def handle_exit_signals(self):
        signal.signal(signal.SIGINT, self.reset) # Handles CTRL-C for clean up.
        signal.signal(signal.SIGHUP, self.reset) # Handles disconnected TTY for clean up.
        signal.signal(signal.SIGTERM, self.reset) # Handles clean exits for clean up.

