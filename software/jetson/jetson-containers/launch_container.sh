#!/usr/bin/env sh

#sudo docker build -f Dockerfile.ros.kinetic -t jetson/ros:kinetic .
#sudo ./launch_container.sh
#roscore &

XSOCK=/tmp/.X11-unix
XAUTH=/tmp/.docker.xauth
touch $XAUTH
xauth nlist $DISPLAY | sed -e 's/^..../ffff/' | xauth -f $XAUTH nmerge -

xhost +local:root
sudo xhost +si:localuser:root

docker run --privileged \
           --runtime=nvidia --rm -it \
           --volume=$HOME/school/Projets/Final/jetson-containers:/app \
           --volume=$XSOCK:$XSOCK:rw \
           --volume=$XAUTH:$XAUTH:rw \
           --volume=$HOME:$HOME \
           --volume=/usr/lib/aarch64-linux-gnu/tegra:/usr/lib/aarch64-linux-gnu/tegra \
           --volume=/usr/lib/aarch64-linux-gnu/tegra-egl:/usr/lib/aarch64-linux-gnu/tegra-egl \
           --volume=/usr/local/cuda:/usr/local/cuda \
           --volume=/dev:/dev \
           --volume $HOME/.gazebo:/root/.gazebo \
           --env="XAUTHORITY=${XAUTH}" \
           --env="DISPLAY=${DISPLAY}" \
           --env=TERM=xterm-256color \
           --env=QT_X11_NO_MITSHM=1 \
           --net=host \
           jetson/ros:kinetic

