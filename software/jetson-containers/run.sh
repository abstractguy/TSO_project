#!/bin/bash

#NAME=ros_ws
NAME=catkin_ws
TAG=kinetic
USERNAME=ros

mkdir -p source

XSOCK=/tmp/.X11-unix
XAUTH=/tmp/.docker.xauth
touch $XAUTH
xauth nlist $DISPLAY | sed -e 's/^..../ffff/' | xauth -f $XAUTH nmerge -

docker run --net=host \
           -it \
           --volume=$XSOCK:$XSOCK:rw \
           --volume=$XAUTH:$XAUTH:rw \
           --volume="${PWD}/source:/home/ros/${NAME}/src/" \
           --env="XAUTHORITY=${XAUTH}" \
           --env="DISPLAY" \
           -user="${USERNAME}" \
           --
