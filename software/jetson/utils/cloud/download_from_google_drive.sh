#!/usr/bin/env bash

# File:        software/jetson/utils/cloud/download_from_google_drive.sh
# By:          Samuel Duclos
# For:         Myself
# Usage:       bash utils/cloud/download_from_google_drive.sh <FILE_ID> <FILE_NAME>
# Example:     bash utils/cloud/download_from_google_drive.sh 10m_3MlpQwRtZetQxtksm9jqHrPTHZ6vo yolov3-tiny.pt
# Description: Google Drive Downloader.

# FILE_ID can be extracted from the shared link.
FILE_ID=$1

# FILE_NAME is what it is.
FILE_NAME=$2

echo "Downloading ${FILE_NAME}..."
curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=${FILE_ID}" > /dev/null
curl -Lb ./cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/ {print $NF}' ./cookie`&id=${FILE_ID}" -o ${FILE_NAME}
rm cookie
echo "Downloaded ${FILE_NAME}..."


