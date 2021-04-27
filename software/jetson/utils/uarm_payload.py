#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File:          software/jetson/utils/uarm_payload.py
# By:            Samuel Duclos
# For:           Myself
# Description:   Do what the setup is made for...

from utils import uarm
import signal

def add_payload_args(parser):
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

class Payload:
    def __init__(self, 
                 initial_x_position=21.6, 
                 initial_y_position=80.79, 
                 initial_z_position=186.11, 
                 second_x_position=-232.97, 
                 second_y_position=120.86, 
                 second_z_position=126.59, 
                 third_x_position=313.93, 
                 third_y_position=18.76, 
                 third_z_position=178.67, 
                 second_position=None, 
                 third_position=None, 
                 uarm_speed=150, 
                 uart_delay=2.0, 
                 servo_attach_delay=5.0, 
                 set_position_delay=5.0, 
                 servo_detach_delay=5.0, 
                 pump_delay=5.0, 
                 transition_delay=5.0):

        self.initial_x_position = initial_x_position
        self.initial_y_position = initial_y_position
        self.initial_z_position = initial_z_position
        self.second_x_position = second_x_position
        self.second_y_position = second_y_position
        self.second_z_position = second_z_position
        self.third_x_position = third_x_position
        self.third_y_position = third_y_position
        self.third_z_position = third_z_position
        self.uarm_speed = uarm_speed
        self.uart_delay = uart_delay
        self.servo_attach_delay = servo_attach_delay
        self.set_position_delay = set_position_delay
        self.servo_detach_delay = servo_detach_delay
        self.pump_delay = pump_delay
        self.transition_delay = transition_delay

        self.initial_position = {'x': self.initial_x_position, 'y': self.initial_y_position, 'z': self.initial_z_position, 'speed': self.uarm_speed, 'relative': False, 'wait': True}
        self.second_position = {'x': self.second_x_position, 'y': self.second_y_position, 'z': self.second_z_position, 'speed': self.uarm_speed, 'relative': False, 'wait': True}
        self.third_position = {'x': self.third_x_position, 'y': self.third_y_position, 'z': self.third_z_position, 'speed': self.uarm_speed, 'relative': False, 'wait': True}

        self.uarm = uarm.UARM(uart_delay=self.uart_delay, 
                              initial_position=self.initial_position, 
                              servo_attach_delay=self.servo_attach_delay, 
                              set_position_delay=self.set_position_delay, 
                              servo_detach_delay=self.servo_detach_delay, 
                              pump_delay=self.pump_delay)

    def uarm_payload(self, grab_position=None, drop_position=None, sensor=True):
        self.uarm.set_weight_to_somewhere(grab_position=grab_position, drop_position=drop_position, sensor=True if sensor is None else sensor)

    def payload(self, sensor=True):
        self.uarm_payload(grab_position=self.second_position, drop_position=self.third_position, sensor=sensor)
        self.uarm_payload(grab_position=self.third_position, drop_position=self.second_position, sensor=None)
