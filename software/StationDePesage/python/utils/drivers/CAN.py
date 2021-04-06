#!/usr/bin/env python3

# File:        python/utils/drivers/CAN.py
# By:          Samuel Duclos
# For:         My team.
# Description: Driver for CAN bus.

from __future__ import print_function
import can

class CAN_driver:
    def __init__(self, interface_type='can', bitrate=50000):
        self.CAN_init_driver(interface_type=interface_type, bitrate=bitrate)

    def CAN_init_driver(self, interface_type='can', bitrate=50000):
        self.CAN_initialize_default_arguments()
        self.CAN_initialize_configurable_arguments(interface_type=interface_type, bitrate=bitrate)

        constructor_arguments = self.CAN_initialize_inferred_arguments()

        print(constructor_arguments)

        self.sending_bus = can.interface.Bus(**constructor_arguments)
        self.receiving_bus = can.interface.Bus(**constructor_arguments)

        #self.handle_exit_signals()

    def CAN_initialize_default_arguments(self, is_extended_id=False):
        self.is_extended_id = is_extended_id

    def CAN_initialize_configurable_arguments(self, interface_type='can', bitrate=50000):
        self.interface_type = interface_type
        self.bitrate = bitrate

    def CAN_initialize_inferred_arguments(self):
        self.channel = self.interface_type + str(0)

        constructor_arguments = {'channel': self.channel}

        # Virtual CAN interface has no bitrate.
        if self.interface_type != 'can':
            self.bustype = 'virtual'
            self.bitrate = 0
        else:
            self.bustype = 'socketcan'
            constructor_arguments['bitrate'] = self.bitrate

        constructor_arguments['bustype'] = self.bustype

        return constructor_arguments

    def CAN_send(self, arbitration_id, data):
        CAN_message_send = can.Message(arbitration_id=arbitration_id, data=data, is_extended_id=self.is_extended_id)

        try:
            self.sending_bus.send(CAN_message_send)
            print('Message sent on {}.'.format(self.sending_bus.channel_info))
        except can.CanError:
            print('CAN ERROR WHILE SENDING MESSAGE!')

    def CAN_receive(self):
        try:
            CAN_message_received = self.receiving_bus.recv(0.0) # Non-blocking read.

            if CAN_message_received is not None:
                print('Message received on {}.'.format(self.receiving_bus.channel_info))

        except can.CanError:
            print('CAN ERROR WHILE RECEIVING MESSAGE!')

        return CAN_message_received

    '''
    def reset(self):
        print('CAN closed...')

    def __del__(self):
        self.reset()

    def handle_exit_signals(self):
        signal.signal(signal.SIGINT, self.reset) # Handles CTRL-C for clean up.
        signal.signal(signal.SIGHUP, self.reset) # Handles stalled process for clean up.
        signal.signal(signal.SIGTERM, self.reset) # Handles clean exits for clean up.
    '''

