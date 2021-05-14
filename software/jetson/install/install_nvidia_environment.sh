#!/usr/bin/env bash

# File:      software/jetson/install/install_nvidia_environment.sh
# By:        Samuel Duclos
# For:       Myself
# Usage:     cd ~/school/Projets/Final/TSO_project/software/jetson && bash install/install_nvidia_environment.sh

# Add NVIDIA package repositories
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-ubuntu1804.pin
sudo mv cuda-ubuntu1804.pin /etc/apt/preferences.d/cuda-repository-pin-600
sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/7fa2af80.pub
sudo add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/ /"
sudo apt-get update

wget http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/nvidia-machine-learning-repo-ubuntu1804_1.0.0-1_amd64.deb

sudo apt install ./nvidia-machine-learning-repo-ubuntu1804_1.0.0-1_amd64.deb
sudo apt-get update

wget https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/libnvinfer7_7.1.3-1+cuda11.0_amd64.deb
sudo apt install ./libnvinfer7_7.1.3-1+cuda11.0_amd64.deb
sudo apt-get update

# Install development and runtime libraries (~4GB)
sudo apt-get install --no-install-recommends cuda-11-0 \
                                             libcudnn8=8.0.4.30-1+cuda11.0  \
                                             libcudnn8-dev=8.0.4.30-1+cuda11.0

sudo apt-get install -y build-essential binutils gdb && \
sudo apt-get install -y freeglut3 freeglut3-dev libxi-dev libxmu-dev && \
sudo apt install -y nvidia-cuda-toolkit && \
nvcc --version && \
echo 'export PATH="/usr/local/cuda/bin:${PATH}"' >> ~/.bashrc && \
echo 'export LD_LIBRARY_PATH="/usr/local/cuda/lib64:${LD_LIBRARY_PATH}"' >> ~/.bashrc
#sudo apt-get install python-dev python-setuptools -y
sudo apt-get install libboost-python-dev libboost-thread-dev -y

# Reboot. Check that GPUs are visible using the command: nvidia-smi
echo 'Please reboot, then run "bash install/install_pipenv.sh"'

