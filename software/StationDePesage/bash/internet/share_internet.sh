#!/bin/bash

# File:        bash/internet/share_internet.sh
# By:          Samuel Duclos
# For:         My team.
# Description: Share internet through existing wired connection from a
#              Linux computer to a Linux device without internet access.
# Usage:       sudo bash bash/internet/share_internet.sh <OUT> <IN>
# Example:     sudo bash bash/internet/share_internet.sh wlan0 eth0
# Arguments:   <OUT>: interface with access to internet    (default is "wlan0")
#              <IN>:  interface without access to internet (default is "eth0")
# Note:        Repeat at each reboot.

# Parse and set optional arguments from command-line.
OUT=$(echo "${1:-wlan0}" | tr '[:upper:]' '[:lower:]')
IN=$(echo "${2:-eth0}" | tr '[:upper:]' '[:lower:]')

iptables --flush
iptables --table nat --flush
iptables --delete-chain
iptables --table nat --delete-chain
iptables --table nat --append POSTROUTING --out-interface $OUT -j MASQUERADE
iptables --append FORWARD --in-interface $IN -j ACCEPT
sysctl -w net.ipv4.ip_forward=1
