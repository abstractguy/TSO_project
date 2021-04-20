#!/usr/bin/env python3

# File:          python/utils/payload.py
# By:            Samuel Duclos
# For:           My team.
# Description:   Do what the setup is made for...

from __future__ import print_function
from utils import balance, buzzer, sensor, uarm

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
    parser.add_argument('--scan-x-displacement', metavar='<scan-x-displacement>', type=float, required=False, default=5.0, help='Relative position X axis displacement for scans.')
    parser.add_argument('--scan-y-displacement', metavar='<scan-y-displacement>', type=float, required=False, default=5.0, help='Relative position Y axis displacement for scans.')
    parser.add_argument('--scan-z-displacement', metavar='<scan-z-displacement>', type=float, required=False, default=0.0, help='Relative position Z axis displacement for scans.')
    parser.add_argument('--stride-x', metavar='<stride-x>', type=int, required=False, default=2, help='One step on X axis.')
    parser.add_argument('--stride-y', metavar='<stride-y>', type=int, required=False, default=2, help='One step on Y axis.')
    parser.add_argument('--stride-z', metavar='<stride-z>', type=int, required=False, default=0, help='One step on Z axis.')
    parser.add_argument('--speed', metavar='<speed>', type=int, required=False, default=150, help='Speed of uARM displacements.')
    parser.add_argument('--uarm-tty-port', metavar='<uarm-tty-port>', type=str, required=False, default='/dev/ttyUSB1', help='uARM UART TTY port.')
    parser.add_argument('--balance-tty-port', metavar='<balance-tty-port>', type=str, required=False, default='/dev/ttyUSB0', help='Balance UART TTY port.')
    parser.add_argument('--sensor-i2c-port', metavar='<sensor-i2c-port>', type=int, required=False, default=1, help='I2C port for Time-of-Flight (VL6180X) sensor.')
    parser.add_argument('--sensor-threshold', metavar='<sensor-threshold>', type=float, required=False, default=0.5, help='VL6180X sensor threshold for object detection.')
    parser.add_argument('--buzzer-frequency-multiplier', metavar='<buzzer-frequency-multiplier>', type=float, required=False, default=1.0, help='Buzzer frequency multiplier.')
    parser.add_argument('--buzzer-duration-multiplier', metavar='<buzzer-duration-multiplier>', type=float, required=False, default=3.0, help='Buzzer duration multiplier.')
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
                 vehicle_x_position=-232.97, 
                 vehicle_y_position=120.86, 
                 vehicle_z_position=126.59, 
                 balance_x_position=313.93, 
                 balance_y_position=18.76, 
                 balance_z_position=178.67, 
                 vehicle_position=None, 
                 balance_position=None, 
                 uarm_speed=150, 
                 sensor_i2c_port=1, 
                 sensor_threshold=0.5, 
                 buzzer_frequency_multiplier=1.0, 
                 buzzer_duration_multiplier=3.0, 
                 uarm_tty_port='/dev/ttyUSB1', 
                 balance_tty_port='/dev/ttyUSB0', 
                 uart_delay=2.0, 
                 servo_attach_delay=5.0, 
                 set_position_delay=5.0, 
                 servo_detach_delay=5.0, 
                 pump_delay=5.0, 
                 transition_delay=5.0, 
                 scan_x_displacement=5.0, 
                 scan_y_displacement=5.0, 
                 scan_z_displacement=0.0, 
                 stride_x=2.0, 
                 stride_y=2.0, 
                 stride_z=0.0):

        self.initial_x_position = initial_x_position
        self.initial_y_position = initial_y_position
        self.initial_z_position = initial_z_position
        self.vehicle_x_position = vehicle_x_position
        self.vehicle_y_position = vehicle_y_position
        self.vehicle_z_position = vehicle_z_position
        self.balance_x_position = balance_x_position
        self.balance_y_position = balance_y_position
        self.balance_z_position = balance_z_position
        self.uarm_speed = uarm_speed
        self.sensor_i2c_port = sensor_i2c_port
        self.sensor_threshold = sensor_threshold
        self.buzzer_frequency_multiplier = buzzer_frequency_multiplier
        self.buzzer_duration_multiplier = buzzer_duration_multiplier
        self.uarm_tty_port = uarm_tty_port
        self.balance_tty_port = balance_tty_port
        self.uart_delay = uart_delay
        self.servo_attach_delay = servo_attach_delay
        self.set_position_delay = set_position_delay
        self.servo_detach_delay = servo_detach_delay
        self.pump_delay = pump_delay
        self.transition_delay = transition_delay
        self.scan_x_displacement = scan_x_displacement
        self.scan_y_displacement = scan_y_displacement
        self.scan_z_displacement = scan_z_displacement
        self.stride_x = stride_x
        self.stride_y = stride_y
        self.stride_z = stride_z

        self.initial_position = {'x': self.initial_x_position, 'y': self.initial_y_position, 'z': self.initial_z_position, 'speed': self.uarm_speed, 'relative': False, 'wait': True}
        self.vehicle_position = {'x': self.vehicle_x_position, 'y': self.vehicle_y_position, 'z': self.vehicle_z_position, 'speed': self.uarm_speed, 'relative': False, 'wait': True}
        self.balance_position = {'x': self.balance_x_position, 'y': self.balance_y_position, 'z': self.balance_z_position, 'speed': self.uarm_speed, 'relative': False, 'wait': True}

        self.uarm = uarm.UARM(uarm_tty_port=self.uarm_tty_port, 
                              uart_delay=self.uart_delay, 
                              initial_position=self.initial_position, 
                              servo_attach_delay=self.servo_attach_delay, 
                              set_position_delay=self.set_position_delay, 
                              servo_detach_delay=self.servo_detach_delay, 
                              pump_delay=self.pump_delay, 
                              scan_x_displacement=self.scan_x_displacement, 
                              scan_y_displacement=self.scan_y_displacement, 
                              scan_z_displacement=self.scan_z_displacement, 
                              stride_x=self.stride_x, 
                              stride_y=self.stride_y, 
                              stride_z=self.stride_z)

        self.buzzer = buzzer.Buzzer(uarm=self.uarm.uarm, servo_detach_delay=self.uarm.servo_detach_delay, transition_delay=self.transition_delay)
        self.sensor = sensor.VL6180X(i2c_port=self.sensor_i2c_port)
        self.balance = balance.Balance(tty_port=self.balance_tty_port)
        self.handle_signals()
        self.uarm.reset()

    def uarm_payload(self, grab_position=None, drop_position=None):
        self.uarm.set_weight_to_somewhere(grab_position=grab_position, drop_position=drop_position, sensor=self.sensor, sensor_threshold=self.sensor_threshold)

    def buzzer_payload(self):
        self.buzzer.play_funky_town(frequency_multiplier=self.buzzer_frequency_multiplier, duration_multiplier=self.buzzer_duration_multiplier)

    def payload(self):
        self.uarm_payload(grab_position=self.vehicle_position, drop_position=self.balance_position)
        self.buzzer_payload()
        weight = self.balance.weigh()
        self.uarm_payload(grab_position=self.balance_position, drop_position=self.vehicle_position)
        self.buzzer_payload()
        print(weight) # Output weight to parent.

    def __del__(self):
        self.reset()

    def reset(self):
        self.uarm.reset()
        print('Factory reset!')

    def handle_exit_signals(self):
        signal.signal(signal.SIGINT, self.reset) # Handles CTRL-C for clean up.
        signal.signal(signal.SIGHUP, self.reset) # Handles stalled process for clean up.
        signal.signal(signal.SIGTERM, self.reset) # Handles clean exits for clean up.

    def handle_payload_signal(self):
        signal.signal(signal.SIGUSR1, self.payload) # Launches payload when requested from parent.

    def handle_signals(self):
        self.handle_payload_signal()
        self.handle_exit_signals()

