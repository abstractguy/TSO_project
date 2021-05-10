#!/usr/bin/env bash

# File:      software/jetson/install/install_tensorrt.sh
# By:        Samuel Duclos
# For:       Myself
# Usage:     cd ~/school/Projets/Final/TSO_project/software/jetson && bash install/install_tensorrt.sh

BASE_PATH="${HOME}/school/Projets/Final/TSO_project/software/jetson"

# Install TensorRT. Requires that libcudnn8 is installed above.
cd && \
sudo apt-get update && \
sudo apt-get install -y --no-install-recommends libnvinfer7=7.1.3-1+cuda11.0 \
                                                libnvinfer-dev=7.1.3-1+cuda11.0 \
                                                libnvinfer-plugin7=7.1.3-1+cuda11.0

# Install TensorRT through PIPY.
cd ${BASE_PATH} && \
pipenv install --upgrade setuptools pip && \
pipenv install nvidia-pyindex pybind11 && \
pipenv install --upgrade nvidia-tensorrt && \
pipenv run python3 -c 'import tensorrt; print(tensorrt.__version__); assert tensorrt.Builder(tensorrt.Logger())'

