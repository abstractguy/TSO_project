#!/usr/bin/env bash

# File:          install/install_conda.sh
# By:            Samuel Duclos
# For            Myself
# Description:   Install conda.
# Example usage: bash ~/school/Projets/Final/TSO_Project/Logiciels/jetson-containers/install/install_conda.sh

sudo apt update && \
sudo apt install -y wget bzip2 ca-certificates libglib2.0-0 libxext6 libsm6 libxrender1 git mercurial subversion && \
sudo apt clean && \
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
sudo /bin/bash ~/miniconda.sh -b -p /opt/conda && \
rm ~/miniconda.sh && \
WHOAMI="${USER}" && \
sudo chown -R $WHOAMI /opt/conda && \
/opt/conda/bin/conda init && \
/opt/conda/bin/conda clean -tipsy && \
/opt/conda/bin/conda clean -afy && \
source ~/.bashrc

