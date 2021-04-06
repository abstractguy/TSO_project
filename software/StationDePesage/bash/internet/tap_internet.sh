#!/bin/bash

# File:        bash/internet/tap_internet.sh
# By:          Samuel Duclos
# For:         My team.
# Description: Tap internet on a Linux device without internet from an existing 
#              wired connection to a Linux computer with internet access.
# Usage:       sudo bash bash/internet/tap_internet.sh <GATEWAY>
# Example:     sudo bash bash/internet/tap_internet.sh 192.168.7.1
# Note:        Repeat at each reboot.

# Parse and set optional arguments from command-line.
GATEWAY="${1:-192.168.7.1}"

/sbin/route add default gw $GATEWAY
#/usr/sbin/ntpdate -b -s -u ie.pool.ntp.org
echo 'nameserver 8.8.8.8' >> /etc/resolv.conf
#echo 'nameserver 8.8.4.4' >> /etc/resolv.conf
