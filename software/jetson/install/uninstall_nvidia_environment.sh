#!/usr/bin/env bash

# File:      software/jetson/install/uninstall_nvidia_environment.sh
# By:        Samuel Duclos
# For:       Myself
# Usage:     cd ~/school/Projets/Final/TSO_project/software/jetson && bash install/uninstall_nvidia_environment.sh

sudo apt-get remove --auto-remove -y nvidia-cuda-toolkit
sudo apt-get --purge remove -y "*cublas*" "cuda*" "nsight*" && \
sudo apt-get --purge remove -y "*libcudnn*" && \
sudo apt-get --purge remove -y "*nvidia*" && \
sudo rm -rf /usr/local/cuda* && \
sudo sed -i.bak 's/^[^#].*nvidia.*$/#&/g' /etc/apt/sources.list && \
sudo apt-get update
sudo apt-get --fix-broken -y install
sudo apt-get --fix-missing -y install
sudo apt-get -y autoremove
sudo apt-get -y autoclean
sudo apt-get update

