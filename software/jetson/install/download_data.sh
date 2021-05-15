#!/usr/bin/env bash

# File:        software/jetson/install/download_data.sh
# By:          Samuel Duclos
# For:         Myself
# Usage:       cd software/jetson && bash install/download_data.sh
# Example:     cd software/jetson && bash install/download_data.sh
# Description: Download dataset to calibrate INT8 inference.

DIR=$HOME

set -e

PASCAL_VOC2007_DATASET=$DIR/VOCtrainval_06-Nov-2007.tar
wget -O $PASCAL_VOC2007_DATASET http://host.robots.ox.ac.uk/pascal/VOC/voc2007/VOCtrainval_06-Nov-2007.tar
tar -xf $PASCAL_VOC2007_DATASET -C $DIR
rm $PASCAL_VOC2007_DATASET

