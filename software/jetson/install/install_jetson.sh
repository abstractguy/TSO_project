#!/usr/bin/env bash

# File:        software/jetson/install/install_jetson.sh
# By:          Samuel Duclos
# For:         Myself
# Usage:       cd ~/workspace/software/jetson && bash install/install_jetson.sh <JETSON_PASSWORD>
# Description: Install FastMOT Jetson packages.
# Reference:   https://github.com/GeekAlexis/FastMOT.git

JETSON_PASSWORD=$1

DIR=$HOME

## Jetpack 4.4+ (OpenCV, CUDA, TensorRT) is required
#JP_VERSION=44
#TF_VERSION=1.15.2
#NV_VERSION=20.4

# Jetpack 4.5 (4.4+) (OpenCV, CUDA, TensorRT) is required
JP_VERSION=45
TF_VERSION=1.15.4
NV_VERSION=20.12
set -e

# set up environment variables
echo 'export PATH=/usr/local/cuda/bin${PATH:+:${PATH}}' >> ~/.bashrc 
echo 'export LD_LIBRARY_PATH=/usr/local/cuda/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}' >> ~/.bashrc 
source ~/.bashrc

bash ${PWD}/install/update_cmake.sh $JETSON_PASSWORD
bash ${PWD}/install/install_protobuf_1.8.0.sh $JETSON_PASSWORD

# Install pip, numpy, pycuda, tensorflow, cython-bbox
echo $JETSON_PASSWORD | sudo -S ln -fs /usr/include/locale.h /usr/include/xlocale.h
echo $JETSON_PASSWORD | sudo -S apt-get update
echo $JETSON_PASSWORD | sudo -S apt-get install python3-pip libhdf5-serial-dev hdf5-tools libcanberra-gtk-module
echo $JETSON_PASSWORD | sudo -SH pip3 install cython
echo $JETSON_PASSWORD | sudo -SH pip3 install numpy cython-bbox
echo $JETSON_PASSWORD | sudo -SH pip3 install --global-option=build_ext --global-option="-I/usr/local/cuda/include" --global-option="-L/usr/local/cuda/lib64" pycuda
echo $JETSON_PASSWORD | sudo -SH pip3 install --no-cache-dir --extra-index-url https://developer.download.nvidia.com/compute/redist/jp/v$JP_VERSION tensorflow==$TF_VERSION+nv$NV_VERSION

# install scipy
yes | echo $JETSON_PASSWORD | sudo -S apt-get install libatlas-base-dev gfortran
echo $JETSON_PASSWORD | sudo -SH pip3 install scipy==1.5.0

# install llvm (This may take a while)
cd $DIR
wget http://releases.llvm.org/7.0.1/llvm-7.0.1.src.tar.xz
tar -xvf llvm-7.0.1.src.tar.xz
cd llvm-7.0.1.src
mkdir llvm_build_dir
cd llvm_build_dir/
cmake ../ -DCMAKE_BUILD_TYPE=Release -DLLVM_TARGETS_TO_BUILD="ARM;X86;AArch64"
make -j4
echo $JETSON_PASSWORD | sudo -S make install
cd bin/
echo "export LLVM_CONFIG=\""`pwd`"/llvm-config\"" >> ~/.bashrc
echo "alias llvm='"`pwd`"/llvm-lit'" >> ~/.bashrc
source ~/.bashrc
echo $JETSON_PASSWORD | sudo -SH pip3 install llvmlite==0.31.0

# Install numba==0.48.
echo $JETSON_PASSWORD | sudo -SH pip3 install numba==0.48

# Install onnx==1.4.1.
pip3 install onnx==1.4.1

# Install onnxruntime-gpu==1.7.0.
wget https://nvidia.box.com/shared/static/ukszbm1iklzymrt54mgxbzjfzunq7i9t.whl -O onnxruntime_gpu-1.7.0-cp36-cp36m-linux_aarch64.whl

# Install pip wheel.
pip3 install onnxruntime_gpu-1.7.0-cp36-cp36m-linux_aarch64.whl

