#!/usr/bin/env bash

# File:  software/jetson/install/update_cmake.sh
# By:    Samuel Duclos
# For:   Myself
# Usage: cd ~/workspace/software/jetson && bash install/update_cmake.sh <JETSON_PASSWORD>

JETSON_PASSWORD=$1 && \
export CURRENT_DIR="${PWD}" && \
mkdir -p ~/installs && \
cd ~/installs && \
echo $JETSON_PASSWORD | sudo -S apt remove --yes --purge --auto-remove cmake && \
wget https://github.com/Kitware/CMake/releases/download/v3.13.5/cmake-3.13.5.tar.gz && \
tar xvf cmake-3.13.5.tar.gz && \
cd cmake-3.13.5 && \
bash configure && \
make -j$(nproc) && \
echo $JETSON_PASSWORD | sudo -S make install && \
echo $JETSON_PASSWORD | sudo -S ln -fs /usr/local/bin/cmake /usr/bin/cmake && \
echo $JETSON_PASSWORD | sudo -S rm -f cmake-3.13.5.tar.gz && \
cd $CURRENT_DIR

