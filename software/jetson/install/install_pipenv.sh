#!/usr/bin/env bash

# File:      software/install/install_pipenv.sh
# By:        Samuel Duclos
# For:       Myself
# Usage:     cd ~/school/Projets/Final/TSO_project/software/jetson && bash install/install_pipenv.sh
# Notes:     Ensure CUDATOOLKIT is installed!

BASE_PATH="${HOME}/school/Projets/Final/TSO_project/software/jetson"
PYTHON_VERSION='3.7'

# Install Python.
sudo apt-get update && \
sudo apt-get install -y python3.6 && \
sudo apt-get install -y software-properties-common && \
sudo add-apt-repository ppa:deadsnakes/ppa && \
sudo apt-get update && \
sudo apt-get install -y python${PYTHON_VERSION} && \
python3 --version

# Install pipenv.
cd && \
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
python3 get-pip.py && \
pip3 install --user pipenv && \
echo 'export PATH="$(python3 -m site --user-base)/bin:/usr/local/cuda-10.2/bin${HOME}/bin:$(python3 -m site --user-base)/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin${PATH}"' >> ~/.profile

