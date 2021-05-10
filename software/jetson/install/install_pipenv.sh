#!/usr/bin/env bash

# File:      software/install/install_pipenv.sh
# By:        Samuel Duclos
# For:       Myself
# Usage:     cd ~/school/Projets/Final/TSO_project/software/jetson && bash install/install_pipenv.sh
# Notes:     Ensure CUDATOOLKIT is installed!

BASE_PATH="${HOME}/school/Projets/Final/TSO_project/software/jetson"
PYTHON_VERSION='3.6'


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
pip3 install --user pipenv && \
echo "$(python3 -m site --user-base)/bin:${PATH}" >> ~/.profile

