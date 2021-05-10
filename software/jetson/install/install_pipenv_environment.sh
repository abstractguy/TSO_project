#!/usr/bin/env bash

# File:      software/install/install_pipenv_environment.sh
# By:        Samuel Duclos
# For:       Myself
# Usage:     cd ~/school/Projets/Final/TSO_project/software/jetson && bash install/install_pipenv_environment.sh

BASE_PATH="${HOME}/school/Projets/Final/TSO_project/software/jetson"
NUMPY_VERSION='<1.19'
SCIPY_VERSION='>=1.5'
NUMBA_VERSION='==0.48'
WRAPT_VERSION='==1.12.1'
PYSERIAL_VERSION='==3.5b0'
TENSORFLOW_VERSION='<2.0'
TORCH_VERSION='==1.8.1+cu111'
TORCHVISION_VERSION='==0.9.1+cu111'
TORCHAUDIO_VERSION='==0.8.1'

# Install as many packages as possible at once so that the package resolver solves as many dependencies as possible for us.
cd ${BASE_PATH} && \
pipenv install "numpy${NUMPY_VERSION}" pandas python-opencv matplotlib pycocotools tqdm onnx cupy lxml pybind11 imagesize jupyterlab ipywidgets widgetsnbextension pycuda "numba${NUMBA_VERSION}" "scipy${SCIPY_VERSION}" scikit-learn imgaug albumentations "tensorflow-gpu${TENSORFLOW_VERSION}" tensorflow-estimator tensorflow-datasets tensorflow-addons keras keras-applications keras-preprocessing tensorboard cvlib onnxruntime scikit-multilearn "wrapt${WRAPT_VERSION}" cython-bbox "pyserial${PYSERIAL_VERSION}"

# Verify TensorFlow install.
python -c "import tensorflow as tf;print(tf.reduce_sum(tf.random.normal([1000, 1000])))"

# Install PyTorch, TorchVision and TorchAudio.
cd ${BASE_PATH} && \
pipenv install "torch${TORCH_VERSION}" "torchvision${TORCHVISION_VERSION}" "torchaudio${TORCHAUDIO_VERSION}" -f https://download.pytorch.org/whl/torch_stable.html

# Install custom pyuarm.
pipenv install -e pyuarm/pyuarm

#pipenv run python3 main.py

