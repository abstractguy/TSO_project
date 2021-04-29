#!/usr/bin/env bash

# File:        utils/internet/share_internet.sh
# By:          Samuel Duclos
# For:         Myself
# Description: Share internet through existing wired connection from a
#              Linux computer to a Linux device without internet access.
# Usage:       sudo bash utils/internet/share_internet.sh <OUT> <IN>
# Example 1:   sudo bash utils/internet/share_internet.sh wlp3s0 enp0s20f0u5
# Example 2:   sudo bash utils/internet/share_internet.sh wlan0 eth0
# Arguments:   <OUT>: interface with access to internet    (default is "wlp3s0")
#              <IN>:  interface without access to internet (default is "enp0s20f0u5")
# Note:        Repeat at each reboot.

# Parse and set optional arguments from command-line.
OUT=$(echo "${1:-wlp3s0}" | tr '[:upper:]' '[:lower:]')
IN=$(echo "${2:-enp0s20f0u5}" | tr '[:upper:]' '[:lower:]')

iptables --flush
iptables --table nat --flush
iptables --delete-chain
iptables --table nat --delete-chain
iptables --table nat --append POSTROUTING --out-interface $OUT -j MASQUERADE
iptables --append FORWARD --in-interface $IN -j ACCEPT
sysctl -w net.ipv4.ip_forward=1
