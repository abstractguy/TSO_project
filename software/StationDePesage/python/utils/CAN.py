#!/usr/bin/env python3

# File:        python/utils/CAN.py
# By:          Samuel Duclos
# For:         My team.
# Description: TSO protocol for CAN bus.

from __future__ import print_function
import os, signal, subprocess, time, utils.drivers.CAN

def add_CAN_args(parser):
    parser.add_argument('--can-interface-type', metavar='<can-interface-type>', type=str, required=False, default='can', help='One of \'vcan\' or \'can\'.')
    parser.add_argument('--can-arbitration-id', metavar='<can-arbitration-id>', type=int, required=False, default=3, help='The number of the station on the CAN network.')
    parser.add_argument('--can-bitrate', metavar='<can-bitrate>', type=int, required=False, default=50000, help='Bitrate on CAN network.')
    parser.add_argument('--can-time-base', metavar='<can-time-base>', type=float, required=False, default=0.02, help='Time base in seconds regulating the time lapse when each station can transmit in turn on the CAN network.')
    parser.add_argument('--can-number-of-stations', metavar='<can-number-of-stations>', type=int, required=False, default=4, help='Number of stations on the CAN network.')
    return parser

class Protocol(utils.drivers.CAN.CAN_driver):
    def __init__(self, interface_type='vcan', arbitration_id=3, bitrate=50000, time_base=0.02, number_of_stations=4):
        self.initialize_default_arguments()
        self.initialize_configurable_arguments(interface_type=interface_type, arbitration_id=arbitration_id, time_base=time_base, number_of_stations=number_of_stations)
        self.initialize_inferred_arguments()
        self.set_CAN_protocol()

        self.pre_configure_CAN(interface_type=interface_type, bitrate=bitrate)
        time.sleep(5)

        super().__init__(interface_type=interface_type, bitrate=bitrate)

        #self.handle_exit_signals()

    '''
    def reset(self):
        epilog = '/bin/bash /home/debian/workspace/StationDePesage/bash/CAN/epilog.sh %s'
        os.system(epilog % self.interface_type)
        print('CAN closed...')

    def __del__(self):
        self.reset()

    def handle_exit_signals(self):
        signal.signal(signal.SIGINT, self.reset) # Handles CTRL-C for clean up.
        signal.signal(signal.SIGHUP, self.reset) # Handles stalled process for clean up.
        signal.signal(signal.SIGTERM, self.reset) # Handles clean exits for clean up.
    '''

    def initialize_default_arguments(self):
        self.CAN_message_received_old = None
        self.CAN_message_received = None
        self.CAN_message_send = None

    def initialize_configurable_arguments(self, interface_type='can', arbitration_id=3, time_base=0.02, number_of_stations=4):
        self.arbitration_id = arbitration_id
        self.time_base = time_base
        self.number_of_stations = number_of_stations

    def initialize_inferred_arguments(self):
        self.time_base_in_microseconds = float(self.time_base) * 10000000.0

    def pre_configure_CAN(self, interface_type='can', bitrate=50000):
        prelude = '/bin/bash /home/debian/workspace/StationDePesage/bash/CAN/prelude.sh %s %d %d %.2f'
        os.system(prelude % (interface_type, self.arbitration_id, bitrate, self.time_base))

    def set_CAN_protocol(self):
        self.OFF = 0x00
        self.ON = 0x20
        self.WAIT = 0x40
        self.TEST = 0x60
        self.ERROR_UNSPECIFIED = 0x80
        self.ERROR_PROTOCOL = 0xA0
        self.ERROR_TIMEOUT = 0xC0
        self.ERROR_RETRANSMIT = 0xE0
        self.NOTHING = 0x00
        self.BLACK = 0x08
        self.ORANGE = 0x10
        self.OTHER = 0x18
        self.A = 0x00
        self.B = 0x02
        self.C = 0x04
        self.D = 0x06
        self.GRAMS = 0x00
        self.OZ = 0x01

    def is_error(self):
        return self.CAN_message_received.data[0] > 127

    def set_error_message(self, error_code=None):
        self.CAN_message_send = self.CAN_message_received

        if error_code is None:
            error_code = self.ERROR_UNSPECIFIED
        else:
            error_code &= 0xE0

        self.CAN_message_send.data[0] &= 0x1F
        self.CAN_message_send.data[0] |= error_code

    def get_mode(self, CAN_message_received):
        return CAN_message_received.data[0] & 0xE0

    def get_unit(self, CAN_message_received):
        return CAN_message_received.data[0] & 0x01

    def get_color(self, CAN_message_received):
        return CAN_message_received_old.data[0] & 0x18

    def atoi(self, a):
        return int(a.strip())

    def parse_balance_output(self, weight):
        weight = self.atoi()
        weight_eight_bits_max = 0xFF if weight > 0xFF else weight
        return bytearray([weight_eight_bits_max])

    def payload_received(self):
        old_mode = self.get_mode(self.CAN_message_received_old)
        mode = self.get_mode(self.CAN_message_received)

        old_color = self.get_color(self.CAN_message_received_old)
        color = self.get_color(self.CAN_message_received)

        unit = self.get_unit(self.CAN_message_received)

        if old_mode != mode and old_color != color and mode == self.ON and color == self.BLACK:
            return unit
        else:
            return None

    def prepare_CAN_message_for_weight_transmission(self, weight, unit):
        if weight is not None:
            self.CAN_message_send.data[1] = weight
            self.CAN_message_send.data[0] &= 0xFE
            self.CAN_message_send.data[0] |= unit

    def send(self, data):
        self.CAN_send(self.arbitration_id, data)

    def receive(self):
        if self.CAN_message_received is not None:
            self.CAN_message_received_old = self.CAN_message_received.copy()
        self.CAN_message_received = self.CAN_receive()

