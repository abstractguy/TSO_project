#!/usr/bin/env bash

# File:        software/jetson/install/install_jetson_nano_sd_card.sh
# By:          Samuel Duclos
# For:         Myself
# Usage:       cd ~/workspace/software/jetson && bash install/install_jetson_nano_sd_card.sh <JETSON_USER>
# Description: Install JetPack on the Micro-SD card.

JETSON_USER=$(echo "${1:-sam}") && \
read -s -p "Enter password: " LAPTOP_PASSWORD && \
echo $LAPTOP_PASSWORD | sudo -S apt-get update && \
echo $LAPTOP_PASSWORD | sudo -S apt-get -y install screen && \
wget https://developer.nvidia.com/jetson-nano-sd-card-image-44 -O jetson-nano-developer-kit-sd-card-image.zip && \
unzip jetson-nano-developer-kit-sd-card-image.zip && \
read -s -p "Make sure to remove your Micro-SD card then press [enter]." DUMMY && \
echo $LAPTOP_PASSWORD | sudo -S fdisk -l | grep '^Disk /dev/' | cut -d' ' -f2- | cut -d':' -f1 > ./.fdisk_temp_1.txt && \
read -s -p "Make sure to insert your Micro-SD card then press [enter]." DUMMY && \
echo $LAPTOP_PASSWORD | sudo -S fdisk -l | grep '^Disk /dev/' | cut -d' ' -f2- | cut -d':' -f1 > ./.fdisk_temp_2.txt && \
SD_CARD=$(echo $LAPTOP_PASSWORD | sudo -S diff ./.fdisk_temp_1.txt ./.fdisk_temp_2.txt | grep "^>" | cut -d' ' -f2-) && \
echo "\nMicro-SD card is: ${SD_CARD}" && \
echo $LAPTOP_PASSWORD | sudo -S dd if=sd-blob-b01.img of=${SD_CARD} bs=1M oflag=direct status=progress && \
rm -rf sd-blob-b01.img jetson-nano-developer-kit-sd-card-image.zip
echo $LAPTOP_PASSWORD | sudo -S rm ./.fdisk_temp_1.txt ./.fdisk_temp_2.txt
sync
#echo $LAPTOP_PASSWORD | sudo -S screen /dev/ttyACM0

