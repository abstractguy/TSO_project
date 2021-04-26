#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File:          software/jetson/uarm_payload.py
# By:            Samuel Duclos
# For:           Myself
# Description:   Do what the setup is made for...
# For help:      cd software/jetson && python3 uarm_payload.py --help # <-- Use --help for help using this file like this. <--

from utils.uarm_payload import add_payload_args
from utils import uarm_payload
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Test uARM for object detection using I2C VL6180X Time-of-Flight sensor to scan until object is found.', 
                                     formatter_class=argparse.RawTextHelpFormatter)

    parser = add_payload_args(parser)
    return parser

def main():
    parser = parse_args()
    args = parser.parse_args()
    print(vars(args))

    pay = uarm_payload.Payload(initial_x_position=args.first_x_position, 
                               initial_y_position=args.first_y_position, 
                               initial_z_position=args.first_z_position, 
                               vehicle_x_position=args.second_x_position, 
                               vehicle_y_position=args.second_y_position, 
                               vehicle_z_position=args.second_z_position, 
                               balance_x_position=args.third_x_position, 
                               balance_y_position=args.third_y_position, 
                               balance_z_position=args.third_z_position, 
                               uarm_speed=args.speed, 
                               uarm_tty_port=args.uarm_tty_port, 
                               uart_delay=args.uart_delay, 
                               servo_attach_delay=args.servo_attach_delay, 
                               set_position_delay=args.set_position_delay, 
                               servo_detach_delay=args.servo_detach_delay, 
                               pump_delay=args.pump_delay, 
                               transition_delay=args.transition_delay)

    pay.payload()

if __name__ == '__main__':
    main()

