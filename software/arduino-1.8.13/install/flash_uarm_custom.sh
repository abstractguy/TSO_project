#!/usr/bin/env bash

# File:        software/arduino-1.8.13/flash_uarm_custom.sh
# By:          Samuel Duclos
# For:         Myself
# Description: AVRDUDE upload command.
# Usage:       sudo bash flash.sh

/home/samuel/school/Projets/Final/TSO_project/software/arduino-1.8.13/hardware/tools/avr/bin/avrdude -C/home/samuel/school/Projets/Final/TSO_project/software/arduino-1.8.13/hardware/tools/avr/etc/avrdude.conf -v -patmega328p -carduino -P/dev/ttyUSB0 -b115200 -D -Uflash:w:/home/samuel/school/Projets/Final/TSO_project/software/arduino-1.8.13/firmware_custom.hex:i
