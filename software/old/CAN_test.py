#!/usr/bin/env python3

# File:        python/CAN_test.py
# By:          Samuel Duclos
# For:         My team.
# Description: CAN test in Python for TSO_team.

from __future__ import print_function
from utils import CAN
import time

def parse_args():
    import argparse
    parser = argparse.ArgumentParser(description='Simple read/write CAN test using virtual CAN bus by default (see --help).', 
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser = CAN.add_CAN_args(parser)
    parser.add_argument('--can-message-byte-0', metavar='<can-message-byte-0>', type=int, required=False, default=0x40, help='First byte of test CAN message.')
    parser.add_argument('--can-message-byte-1', metavar='<can-message-byte-1>', type=int, required=False, default=0xAA, help='Second byte of test CAN message.')
    parser.add_argument('--can-delay', metavar='<can-delay>', type=float, required=False, default=3.0, help='Delay before reading CAN bus after sending.')
    return parser.parse_args()

def main():
    args = parse_args()
    print(vars(args))

    TSO_protocol = CAN.Protocol(interface_type=args.can_interface_type, 
                                arbitration_id=args.can_arbitration_id, 
                                bitrate=args.can_bitrate, 
                                time_base=args.can_time_base, 
                                number_of_stations=args.can_number_of_stations)

    CAN_message_send = [args.can_message_byte_0, args.can_message_byte_1]

    TSO_protocol.send(data=CAN_message_send)
    time.sleep(args.can_delay)

    TSO_protocol.receive()
    CAN_message_received = TSO_protocol.CAN_message_received
    if CAN_message_received is not None:
        print(CAN_message_received)

if __name__ == '__main__':
    main()

