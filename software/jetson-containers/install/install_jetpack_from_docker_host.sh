#!/usr/bin/env bash

# File:          install/install_jetpack_from_docker_host.sh
# Included by:   Samuel Duclos
# For            Myself
# Usage:         cd $HOME/school/Projets/Final/TSO_Project/Logiciels/jetson-containers && bash install/install_jetpack_from_docker_host.sh

#NVIDIA_USERNAME="nomfullcreatif@gmail.com"

#echo -n "Please enter your Nvidia account's password:"
#read -s NVIDIA_PASSWORD
#echo ""

#echo -n "Please enter your host computer's password:"
#read -s HOST_PASSWORD
#echo ""

docker login

#echo "Please enter your Nvidia account email:"
#NVIDIA_ACCOUNT=$(read)
#echo "Please enter your Nvidia account password:"
#NVIDIA_PASSWORD=$(read)
#wget --user=${NVIDIA_ACCOUNT} --password=${NVIDIA_PASSWORD} https://developer.nvidia.com/nvidia-sdk-manager-docker-image
echo "Please login to Nvidia and download the sdkmanager here:"
echo "    https://developer.nvidia.com/nvidia-sdk-manager-docker-image"
echo "Then place the file in this directory and press [enter] when done..."
read

JETPACK_VERSION=4.4.1

SDKMANAGER_FILE=$(ls | grep sdkmanager | cut -d'-' -f2 | cut -d'_' -f1)
SDKMANAGER_VERSION=$(echo ${SDKMANAGER_FILE} | rev | cut -d'.' -f2- | rev)
SDKMANAGER_BUILD=$(echo ${SDKMANAGER_FILE} | rev | cut -d'.' -f1 | rev)

docker load -i ./sdkmanager-${SDKMANAGER_VERSION}.${SDKMANAGER_BUILD}_docker.tar.gz && \
docker tag sdkmanager:${SDKMANAGER_VERSION}.${SDKMANAGER_BUILD} sdkmanager:latest && \
docker run --network=host \
           -it \
           --privileged \
           -v /dev/bus/usb:/dev/bus/usb/ \
           --name JetPack_Xavier_Devkit \
           sdkmanager --cli install \
                      --logintype devzone \
                      --product Jetson \
                      --target P2888-0004 \
                      --targetos Linux \
                      --version ${JETPACK_VERSION} \
                      --select 'Jetson OS' && \
docker commit --author "Samuel Duclos <nomfullcreatif@gmail.com>" \
              --message "Just wanted to say hi." \
              JetPack_Xavier_Devkit \
              jetpack_xavier_devkit:${JETPACK_VERSION}_flash && \
docker run --network=host \
           -it \
           --rm \
           --privileged \
           -v /dev/bus/usb:/dev/bus/usb/ \
           jetpack_xavier_devkit:${JETPACK_VERSION}_flash

#docker run --network=host \
#           -it \
#           --privileged \
#           -v /dev/bus/usb:/dev/bus/usb/ \
#           --name JetPack_Xavier_Devkit \
#           sdkmanager --cli install \
#                      --logintype devzone \
#                      --product Jetson \
#                      --target P2888-0004 \
#                      --targetos Linux \
#                      --version ${JETPACK_VERSION} \
#                      --select 'Jetson OS'
#                      #--select 'Jetson OS' \
#                      #--user "${NVIDIA_USERNAME}" \
#                      #--password "${NVIDIA_PASSWORD}" \
#                      #--sudopassword "${HOST_PASSWORD}" \
#                      #--deselect 'Jetson SDK Components' \
#                      #--flash all \
#                      #--additionalsdk DeepStream \
#                      #--license accept \
#                      #--staylogin true \
#                      #--datacollection disable \
#                      #--exitonfinish
#docker commit --author "Samuel Duclos <nomfullcreatif@gmail.com>" \
#              --message "Just wanted to say hi." \
#              JetPack_Xavier_Devkit \
#              jetpack_xavier_devkit:${JETPACK_VERSION}_flash
#docker run --network=host \
#           -it \
#           --rm \
#           --privileged \
#           -v /dev/bus/usb:/dev/bus/usb/ \
#           jetpack_xavier_devkit:${JETPACK_VERSION}_flash

#docker container rm --volumes JetPack_Xavier_Devkit
#docker run --network=host \
#           -it \
#           --rm \
#           --privileged \
#           -v /dev/bus/usb:/dev/bus/usb/ \
#           jetpack_xavier_devkit:${JETPACK_VERSION}_flash

