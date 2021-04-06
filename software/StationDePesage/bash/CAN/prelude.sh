#!/bin/bash

# File:        bash/CAN/prelude.sh
# By:          Samuel Duclos
# For:         My team.
# Description: Post-deconfigures CAN.
# Usage:       sudo bash bash/CAN/prelude.sh <INTERFACE_TYPE> <ARBITRATION_ID> <BITRATE> <TIME_BASE>
# Example:     sudo bash bash/CAN/prelude.sh vcan 3 50000 0.02
# Arguments:   <INTERFACE_TYPE>: one of "vcan" or "can" (default is "vcan")
#              <ARBITRATION_ID>: identifier for the local node (default is "3")
#              <BITRATE>:        bitrate for CAN bus (default is "50000")
#              <TIME_BASE>:      time base between each CAN node in seconds (default is 0.02)

# Parse and set optional arguments from command-line.
INTERFACE_TYPE=$(echo "${1:-vcan}" | tr '[:upper:]' '[:lower:]')
ARBITRATION_ID="${2:-3}"
BITRATE="${3:-50000}"
TIME_BASE="${4:-0.02}"
INTERFACE="${INTERFACE_TYPE}0"

# Ensure kernel modules are loaded.
modprobe can can_bcm vcan

# Virtual CAN interface has no bitrate.
if [ "$INTERFACE_TYPE" == 'vcan' ]; then
    BITRATE=
else
    BITRATE="bitrate ${BITRATE}"
fi

# Setup interface if it doesn't exist.
if [ ! -e /sys/class/net/$INTERFACE ]
then
    ip link add dev $INTERFACE type $INTERFACE_TYPE
fi

# Making sure the interface is up.
eval "ip link set up $INTERFACE type $INTERFACE_TYPE $BITRATE"

# Increase sending buffer size.
ifconfig $INTERFACE txqueuelen 1000
