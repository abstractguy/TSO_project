#!/usr/bin/env bash

# File:  software/jetson/install/install_x86_environment_part_1.sh
# By:    Samuel Duclos
# For:   Myself
# Usage: cd ~/school/Projets/Final/TSO_project/software/jetson && bash install/install_x86_environment_part_1.sh
# Notes: Reboot after this and run bash install/install_x86_environment_part_2.sh after!
# Notes: NOT TESTED YET (this script and all subscripts)!

bash install/uninstall_conda.sh && \
bash install/install_nvidia_environment.sh

