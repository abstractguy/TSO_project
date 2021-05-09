#!/usr/bin/env bash

# File:      software/install/install_conda_environment.sh
# By:        Samuel Duclos
# For:       Myself
# Usage:     cd ~/school/Projets/Final/TSO_project/software && bash install/install_conda_environment.sh

CONDA_ENV_NAME="school"
PYTHON_VERSION="3.6"
#NUMPY_VERSION="1.19.5"
NUMPY_VERSION="1.18.5"
SCIPY_VERSION="1.5"
NUMBA_VERSION="0.48"
TENSORFLOW_VERSION="1.15"
PYTORCH_VERSION="1.7"
TORCHVISION_VERSION="0.8"

conda update --yes --name base --channel defaults conda && \
conda create --yes --name ${CONDA_ENV_NAME} --channel pytorch --channel conda-forge --channel esri numpy=${NUMPY_VERSION} pandas opencv matplotlib pycocotools tqdm onnx cupy lxml pybind11 imagesize jupyterlab ipywidgets widgetsnbextension pycuda numba=${NUMBA_VERSION} scipy=${SCIPY_VERSION} scikit-learn imgaug albumentations tensorflow-gpu=${TENSORFLOW_VERSION} tensorflow-estimator tensorflow-datasets tensorflow-addons keras keras-applications keras-preprocessing pytorch=${PYTORCH_VERSION} torchvision=${TORCHVISION_VERSION} tensorboard cudatoolkit pip python=${PYTHON_VERSION} && \
conda init bash && \
source activate ${CONDA_ENV_NAME} && \
if [[ "$(echo $PS1 | cut -d' ' -f1 | tr -d '()')" == "${CONDA_ENV_NAME}" ]]
then
    yes | python -m pip install --upgrade cvlib onnxruntime scikit-multilearn && \
    cd jetson/pyuarm && \
    pip install --upgrade -e pyuarm
else
    echo "Could not source activate ${CONDA_ENV_NAME}..."
fi

