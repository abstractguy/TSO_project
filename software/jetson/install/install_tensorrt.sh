#!/usr/bin/env bash

# File:      software/jetson/install/install_tensorrt.sh
# By:        Samuel Duclos
# For:       Myself
# Usage:     cd ~/school/Projets/Final/TSO_project/software/jetson && bash install/install_tensorrt.sh

BASE_PATH="${HOME}/school/Projets/Final/TSO_project/software/jetson"

export PATH="/usr/src/tensorrt/bin:$PATH"
export PYTHONPATH=/usr/lib/python3.7/dist-packages:$PYTHONPATH

# Install TensorRT. Requires that libcudnn7 is installed above.
sudo apt-get install -y --no-install-recommends libnvinfer6=6.0.1-1+cuda10.1 \
    libnvinfer-dev=6.0.1-1+cuda10.1 \
    libnvinfer-plugin6=6.0.1-1+cuda10.1

# Install TensorRT through PIPY.
cd ${BASE_PATH} && \
pipenv install --upgrade setuptools pip && \
pipenv install nvidia-pyindex pybind11 && \
pipenv install --upgrade nvidia-tensorrt && \
pipenv run python3 -c 'import tensorrt; print(tensorrt.__version__); assert tensorrt.Builder(tensorrt.Logger())'

