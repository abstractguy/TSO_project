#!/usr/bin/env bash

# File:     install/install_unetbootin.sh
# By:       Samuel Duclos
# For:      Myself
# Usage:    sudo -H bash ~/school/Projets/Final/TSO_Project/Logiciels/jetson-containers/install/install_unetbootin.sh

add-apt-repository ppa:gezakovacs/ppa
apt-get update
apt-get install unetbootin
unetbootin &

