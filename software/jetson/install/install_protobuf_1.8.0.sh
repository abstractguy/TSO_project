#!/usr/bin/env bash

# File:     yolo_inference/install/install_protobuf_1.8.0.sh
# By:       Samuel Duclos
# For:      DRDC
# Reference: https://github.com/jkjung-avt/jetson_nano.git

JETSON_PASSWORD=$1

set -e

folder=${HOME}/src
mkdir -p $folder

echo "** Install requirements"
echo $JETSON_PASSWORD | sudo -S apt-get install -y autoconf libtool

echo "** Download protobuf-3.8.0 sources"
cd $folder
if [ ! -f protobuf-python-3.8.0.zip ]; then
    wget https://github.com/protocolbuffers/protobuf/releases/download/v3.8.0/protobuf-python-3.8.0.zip
fi

if [ ! -f protoc-3.8.0-linux-aarch_64.zip ]; then
    wget https://github.com/protocolbuffers/protobuf/releases/download/v3.8.0/protoc-3.8.0-linux-aarch_64.zip
fi

echo "** Install protoc"
unzip protobuf-python-3.8.0.zip
unzip protoc-3.8.0-linux-aarch_64.zip -d protoc-3.8.0
echo $JETSON_PASSWORD | sudo -S cp protoc-3.8.0/bin/protoc /usr/local/bin/protoc

echo "** Build and install protobuf-3.8.0 libraries"
export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=cpp
cd protobuf-3.8.0/
bash autogen.sh
bash configure --prefix=/usr/local
make -j$(nproc)
make check
echo $JETSON_PASSWORD | sudo -S make install
echo $JETSON_PASSWORD | sudo -S ldconfig

# Remove previous installation of python3 protobuf module.
echo "** Update python3 protobuf module"
echo $JETSON_PASSWORD | sudo -S apt-get install -y python3-pip
echo $JETSON_PASSWORD | sudo -S pip3 uninstall -y protobuf
echo $JETSON_PASSWORD | sudo -S pip3 install Cython
cd python/
python3 setup.py build --cpp_implementation
python3 setup.py test --cpp_implementation
echo $JETSON_PASSWORD | sudo -S python3 setup.py install --cpp_implementation

echo "** Build protobuf-3.8.0 successfully"

