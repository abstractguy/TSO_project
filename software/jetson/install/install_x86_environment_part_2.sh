#!/usr/bin/env bash

# File:  software/jetson/install/install_x86_environment_part_2.sh
# By:    Samuel Duclos
# For:   Myself
# Usage: cd ~/school/Projets/Final/TSO_project/software/jetson && bash install/install_x86_environment_part_2.sh
# Notes: Run bash install/install_x86_environment_part_1.sh first!
# Notes: NOT TESTED YET (this script and all subscripts)!

bash install/install_pipenv.sh && \
#bash install/install_tensorrt.sh && \
bash install/install_pipenv_environment.sh

