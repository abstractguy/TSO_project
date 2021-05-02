#!/usr/bin/env bash

BASEDIR=$(dirname "$0")
DIR=$BASEDIR/../fastmot/models

set -e

sudo apt install curl

#./utils/cloud/download_from_google_drive.sh 1MLC2lKnQvAQgBKZP1EXB6UdmqujY9qVd ${DIR}/osnet_x0_25_msmt17.onnx
#./utils/cloud/download_from_google_drive.sh 1-Cqk2P72P4feYLJGtJFPcCxN5JttzTfX ${DIR}/ssd_inception_v2_coco.pb
#./utils/cloud/download_from_google_drive.sh 1IfSveiXaub-L6PO9mqne5pk2EByzb25z ${DIR}/ssd_mobilenet_v1_coco.pb
#./utils/cloud/download_from_google_drive.sh 1ste0fQevAjF4UqD3JsCtu1rUAwCTmETN ${DIR}/ssd_mobilenet_v2_coco.pb
./utils/cloud/download_from_google_drive.sh 1-kXZpA6y8pNbDMMD7N--IWIjwqqnAIGZ ${DIR}/yolov4_crowdhuman.onnx
