#!/usr/bin/env python3

# File:        python/utils/uarm.py
# By:          Samuel Duclos
# For:         My team.
# Description: uARM control in Python for TSO_team.

import pyuarm, signal, time

initial_position = {'x': 21.6, 'y': 80.79, 'z': 186.11, 'speed': 150, 'relative': False, 'wait': True}

class UARM:
    def __init__(self, 
                 uarm_tty_port='/dev/ttyUSB0', 
                 uart_delay=2, 
                 initial_position=initial_position, 
                 servo_attach_delay=5, 
                 set_position_delay=5, 
                 servo_detach_delay=5, 
                 pump_delay=5):

        self.uarm_tty_port = uarm_tty_port
        self.uart_delay = uart_delay
        self.initial_position = initial_position
        self.servo_attach_delay = servo_attach_delay
        self.set_position_delay = set_position_delay
        self.servo_detach_delay = servo_detach_delay
        self.pump_delay = pump_delay

        self.uarm = pyuarm.UArm(port_name=self.uarm_tty_port)
        self.handle_exit_signals()

        time.sleep(self.uart_delay)

    def set_servo_attach(self):
        self.uarm.set_servo_attach()
        time.sleep(self.servo_attach_delay)

    def set_servo_detach(self):
        self.uarm.set_servo_detach()
        time.sleep(self.servo_detach_delay)

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

    def grab(self, grab_position=None, sensor=None, sensor_threshold=0.5):
        self.set_position(position=grab_position)
        if self.sensor.detect_object(sensor_threshold=sensor_threshold):
            self.set_pump(on=True)
            return True
        else:
            return False

    def drop(self, drop_position=None):
        self.set_position(position=drop_position)
        self.set_pump(on=False)

    def scan(self, position=None, sensor=None, sensor_threshold=0.5):
        return uarm.grab(grab_position=position, sensor=sensor, sensor_threshold=sensor_threshold)

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

    def set_weight_to_somewhere(self, grab_position=None, drop_position=None, sensor=None, sensor_threshold=0.5):
        self.scan(position=grab_position, sensor=sensor, sensor_threshold=sensor_threshold)
        self.drop(drop_position=drop_position)
        self.reset()

