#!/usr/bin/env bash

# File:        software/install/flash_uarm.sh
# By:          Samuel Duclos
# For:         Myself
# Description: AVRDUDE upload command.
# Usage:       conda activate school && cd software && sudo bash install/flash_uarm.sh

# VERIFY TTY BEFORE FLASHING!
avrdude -patmega328p -carduino -P/dev/ttyUSB0 -b115200 -D -Uflash:w:install/firmware.hex:i

