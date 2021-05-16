#!/usr/bin/env bash

# File:          software/arduino-1.8.13/flash_uarm_custom.sh
# By:            Samuel Duclos
# For:           Myself
# Description:   AVRDUDE upload command.
# Usage:         cd ~/workspace/TSO_project/software/arduino-1.8.13 && sudo bash install/flash_uarm_custom.sh
# Critical note: VERIFY YOU HAVE THE CORRECT TTY BEFORE FLASHING!

${PWD}/hardware/tools/avr/bin/avrdude -C${PWD}/hardware/tools/avr/etc/avrdude.conf -v -patmega328p -carduino -P/dev/ttyUSB0 -b115200 -D -Uflash:w:install/firmware_custom.hex:i

