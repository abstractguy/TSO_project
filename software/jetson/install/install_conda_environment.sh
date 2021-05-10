#!/usr/bin/env bash

# File:      software/install/install_conda_environment.sh
# By:        Samuel Duclos
# For:       Myself
# Usage:     cd ~/school/Projets/Final/TSO_project/software && bash install/install_conda_environment.sh

BASE_PATH="${HOME}/school/Projets/Final/TSO_project/software/jetson"
#CONDA_ENV_NAME='school'
CONDA_ENV_NAME='test'
PYTHON_VERSION='3.6'
CUDATOOLKIT_VERSION='11.0'
NUMPY_VERSION='<1.19'
SCIPY_VERSION='>=1.5'
NUMBA_VERSION='==0.48'
WRAPT_VERSION='==1.12.1'
PYSERIAL_VERSION='==3.5b0'
TENSORFLOW_VERSION='<2.0'
TORCH_VERSION='==1.8.1+cu111'
TORCHVISION_VERSION='==0.9.1+cu111'
TORCHAUDIO_VERSION='==0.8.1'

conda update --yes --name base --channel defaults conda && \
conda create --yes --name ${CONDA_ENV_NAME} --channel conda-forge jupyterlab ipywidgets widgetsnbextension cudatoolkit=${CUDATOOLKIT_VERSION} pip python=${PYTHON_VERSION} && \
conda init bash && \
source activate ${CONDA_ENV_NAME} && \
if [[ "$(echo $PS1 | cut -d' ' -f1 | tr -d '()')" == "${CONDA_ENV_NAME}" ]]
then
    # Install TensorRT through PIPY.
    yes | python -m pip install --upgrade setuptools pip
    yes | python -m pip install nvidia-pyindex pybind11
    yes | python -m pip install --upgrade nvidia-tensorrt
    yes | python -m python -c 'import tensorrt; print(tensorrt.__version__); assert tensorrt.Builder(tensorrt.Logger())'

    # Install as many packages as possible at once so that the package resolver solves as many dependencies as possible for us.
    yes | python -m pip install --upgrade cvlib onnxruntime scikit-multilearn numpy${NUMPY_VERSION} pandas opencv-python matplotlib pycocotools tqdm onnx cupy lxml pybind11 imagesize pycuda numba${NUMBA_VERSION} scipy${SCIPY_VERSION} scikit-learn imgaug albumentations tensorflow-gpu${TENSORFLOW_VERSION} tensorflow-estimator tensorflow-datasets tensorflow-addons keras keras-applications keras-preprocessing tensorboard cvlib onnxruntime scikit-multilearn wrapt${WRAPT_VERSION} cython-bbox pyserial${PYSERIAL_VERSION}

    # Verify TensorFlow install.
    python -c "import tensorflow as tf;print(tf.reduce_sum(tf.random.normal([1000, 1000])))"

    # Install PyTorch, TorchVision and TorchAudio.
    yes | python -m pip install torch${TORCH_VERSION} torchvision${TORCHVISION_VERSION} torchaudio${TORCHAUDIO_VERSION} -f https://download.pytorch.org/whl/torch_stable.html

    # Install custom pyuarm.
    cd jetson/pyuarm && \
    yes | python -m pip install -e pyuarm
else
    echo "Could not source activate ${CONDA_ENV_NAME}..."
fi

