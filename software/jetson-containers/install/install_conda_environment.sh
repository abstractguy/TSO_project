#!/usr/bin/env bash

# File:      install/install_conda_environment.sh
# By:        Samuel Duclos
# For:       Myself
# Usage:     bash ~/workspace/${CONDA_ENV_NAME}/${CONDA_ENV_NAME}/install/install_conda_environment.sh

CONDA_ENV_NAME="school"
PYTHON_VERSION="3.7"
PYTORCH_VERSION="1.7"
TORCHVISION_VERSION="0.8"

conda update --yes --name base --channel defaults conda && \
conda create --yes --name ${CONDA_ENV_NAME} --channel pytorch --channel conda-forge numpy==1.19.5 pandas opencv matplotlib pycocotools tqdm onnx cupy lxml pybind11 imagesize jupyterlab ipywidgets widgetsnbextension scipy scikit-learn imgaug albumentations tensorflow-gpu tensorflow-estimator tensorflow-datasets keras keras-applications keras-preprocessing pytorch=${PYTORCH_VERSION} torchvision=${TORCHVISION_VERSION} tensorboard cudatoolkit pip python=${PYTHON_VERSION} && \
conda init bash && \
source activate ${CONDA_ENV_NAME} && \
if [[ "$(echo $PS1 | cut -d' ' -f1 | tr -d '()')" == "${CONDA_ENV_NAME}" ]]
then
    conda install --yes --channel esri --channel conda-forge tensorflow-addons && \
    yes | python -m pip install --upgrade cvlib onnxruntime scikit-multilearn
else
    echo "Could not source activate ${CONDA_ENV_NAME}..."
fi

