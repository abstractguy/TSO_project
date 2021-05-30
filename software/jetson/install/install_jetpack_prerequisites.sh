#!/usr/bin/env bash

# File:     install/install_jetpack_prerequisites.sh
# By:       Samuel Duclos
# For:      Myself
# Usage:    sudo -H bash ~/school/Projets/Final/TSO_Project/Logiciels/jetson-containers/install/install_jetpack_prerequisites.sh

apt-key adv --fetch-key http://repo.download.nvidia.com/jetson/jetson-ota-public.asc && \
add-apt-repository "deb http://repo.download.nvidia.com/jetson/x86_64 $(lsb_release -cs) r32.4" && \
apt update && \
apt-get install -y nsight-graphics-for-l4t cuda-toolkit-10-2 cuda-cross-aarch64-10-2 libopencv libopencv-dev opencv-licenses libopencv-python libopencv-samples libvisionworks libvisionworks-dev libvisionworks-samples libvisionworks-sfm libvisionworks-sfm-dev libvisionworks-tracking libvisionworks-tracking-dev vpi vpi-dev vpi-samples nsight-systems-2020.2.3 ffmpeg vlc

