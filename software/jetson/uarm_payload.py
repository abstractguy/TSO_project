#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File:          software/jetson/uarm_payload.py
# By:            Samuel Duclos
# For:           Myself
# Description:   Do what the setup is made for...
# For help:      cd software/jetson && python3 uarm_payload.py --help # <-- Use --help for help using this file like this. <--

from utils.uarm_payload import add_uarm_args
from utils import uarm_payload
import argparse

def parse_args():
    """Parse input arguments."""
    parser = argparse.ArgumentParser(description='Test uARM for object detection using a camera to scan until object is found.', 
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser = add_uarm_args(parser)
    args = parser.parse_known_args()[0]
    print(vars(args))
    return args

def main():
    """Main function."""
    parser = parse_args()

    try:
        pay = uarm_payload.UArm(initial_x_position=args.first_x_position, 
                                initial_y_position=args.first_y_position, 
                                initial_z_position=args.first_z_position, 
                                second_x_position=args.second_x_position, 
                                second_y_position=args.second_y_position, 
                                second_z_position=args.second_z_position, 
                                third_x_position=args.third_x_position, 
                                third_y_position=args.third_y_position, 
                                third_z_position=args.third_z_position, 
                                uarm_speed=args.speed, 
                                uart_delay=args.uart_delay, 
                                servo_attach_delay=args.servo_attach_delay, 
                                set_position_delay=args.set_position_delay, 
                                servo_detach_delay=args.servo_detach_delay, 
                                pump_delay=args.pump_delay, 
                                transition_delay=args.transition_delay)

        pay.payload()

    except Exception as e:
        print(e)

    except KeyboardInterrupt:
        print('Program was interrupted by user: exiting.')

    finally:
        # Release resources.
        print('Done.')

if __name__ == '__main__':
    main()
