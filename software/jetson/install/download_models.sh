#!/usr/bin/env bash

# File:        software/jetson/install/download_models.sh
# By:          Samuel Duclos
# For:         Myself
# Usage:       cd software/jetson && bash install/download_models.sh
# Example:     cd software/jetson && bash install/download_models.sh
# Description: Download neural network weights from Google Drive.

BASEDIR=$(dirname "$0")
DIR=$BASEDIR/../fastmot/models

set -e

sudo apt update
sudo apt install curl wget

./utils/cloud/download_from_google_drive.sh 1MLC2lKnQvAQgBKZP1EXB6UdmqujY9qVd ${DIR}/osnet_x0_25_msmt17.onnx
#./utils/cloud/download_from_google_drive.sh 1-Cqk2P72P4feYLJGtJFPcCxN5JttzTfX ${DIR}/ssd_inception_v2_coco.pb
#./utils/cloud/download_from_google_drive.sh 1IfSveiXaub-L6PO9mqne5pk2EByzb25z ${DIR}/ssd_mobilenet_v1_coco.pb
#./utils/cloud/download_from_google_drive.sh 1ste0fQevAjF4UqD3JsCtu1rUAwCTmETN ${DIR}/ssd_mobilenet_v2_coco.pb
#./utils/cloud/download_from_google_drive.sh 1-kXZpA6y8pNbDMMD7N--IWIjwqqnAIGZ ${DIR}/yolov4_crowdhuman.onnx
#./utils/cloud/download_from_google_drive.sh 1cewMfusmPjYWbrnuJRuKhPMwRe_b9PaT ${DIR}/yolov4-608.weights
#curl https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v4_pre/yolov4x-mish.weights --output ${DIR}/yolov4x-mish-640.weights
wget --no-clobber --output-document=${DIR}/yolov4x-mish-640.weights https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v4_pre/yolov4x-mish-640.weights

