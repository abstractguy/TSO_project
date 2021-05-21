#!/usr/bin/env bash

# File:          software/jetson/install/flash_uarm_custom.sh
# By:            Samuel Duclos
# For:           Myself
# Description:   AVRDUDE upload command.
# Usage:         cd ~/workspace/TSO_project/software/jetson && sudo bash install/flash_uarm_custom.sh
# Critical note: VERIFY YOU HAVE THE CORRECT TTY BEFORE FLASHING!

avrdude -v -patmega328p -carduino -P/dev/ttyUSB0 -b115200 -D -Uflash:w:install/firmware_custom.hex:i
