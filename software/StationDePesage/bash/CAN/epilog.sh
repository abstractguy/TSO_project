#!/bin/bash

# File:        bash/CAN/epilog.sh
# By:          Samuel Duclos
# For:         My team.
# Description: Post-deconfigures CAN.
# Usage:       sudo bash bash/CAN/epilog.sh <INTERFACE_TYPE>
# Example:     sudo bash bash/CAN/epilog.sh vcan
# Arguments:   <INTERFACE_TYPE>: one of "vcan" or "can" (default is "vcan")

# Parse and set optional arguments from command-line.
INTERFACE_TYPE=$(echo "${1:-vcan}" | tr '[:upper:]' '[:lower:]')
INTERFACE="${INTERFACE_TYPE}0"

# Destroy network interface.
ip link set down $INTERFACE
ip link delete dev $INTERFACE type $INTERFACE_TYPE
