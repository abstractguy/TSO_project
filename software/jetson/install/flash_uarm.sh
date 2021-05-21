#!/usr/bin/env bash

# File:        software/jetson/install/flash_uarm.sh
# By:          Samuel Duclos
# For:         Myself
# Description: AVRDUDE upload command.
# Usage:       cd ~/workspace/jetson && sudo bash install/flash_uarm.sh

# VERIFY TTY BEFORE FLASHING!
avrdude -v -patmega328p -carduino -P/dev/ttyUSB0 -b115200 -D -Uflash:w:install/firmware.hex:i
