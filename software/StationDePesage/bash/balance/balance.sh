#!/bin/bash

# File:        bash/utils/balance.sh
# By:          Samuel Duclos
# For:         My team.
# Description: Outputs current weight from balance to UART.
# Usage:       sudo bash bash/balance.sh &
# Example:     sudo bash bash/balance.sh &

if [ "$#" -ne 1 ]; then
    echo "Usage:    sudo bash bash/balance.sh &"
    exit
else
    #TTY=/dev/ttyUSB0
    TTY=$1
fi

echo -ne "T\n\r" > $TTY
sleep 1
echo -ne "Z\n\r" > $TTY
sleep 1
echo -ne "P\n\r" > $TTY
sleep 5
echo -ne "T0.0\n\r" > $TTY
sleep 1

cat -v < $TTY &
PID=$!

echo -ne "P\n\r" > $TTY
sleep 5

kill $PID > /dev/null
