#!/usr/bin/env python3

# File:        python/utils/balance.py
# By:          Samuel Duclos
# For:         My team.
# Description: Outputs current weight from balance.

from __future__ import print_function
import subprocess, time

class Balance:
    def __init__(self, tty_port='/dev/ttyUSB0'):
        self.tty_port = tty_port
        self.reset_balance()

    def weigh(self):
        self.print()
        self.reset_balance()

    def print(self):
        subprocess.check_output('echo -ne "P\n\r" > ' + self.tty_port, stderr=subprocess.STDOUT, shell=True)
        time.sleep(5)

    def reset_balance(self):
        subprocess.run('echo -ne "T\n\r" > ' + self.tty_port, stderr=subprocess.STDOUT, shell=True)
        time.sleep(1)
        subprocess.run('echo -ne "Z\n\r" > ' + self.tty_port, stderr=subprocess.STDOUT, shell=True)
        time.sleep(1)
        self.print()
        subprocess.run('echo -ne "T0.0\n\r" > ' + self.tty_port, stderr=subprocess.STDOUT, shell=True)
        time.sleep(1)
        self.print()

