#!/usr/bin/env sh

#curl -sSL http://get.gazebosim.org | sh
#docker build -f Dockerfile.ros.kinetic -t jetson/ros:kinetic .
#bash launch_container_gazebo.sh

XSOCK=/tmp/.X11-unix
XAUTH=/tmp/.docker.xauth
touch $XAUTH
xauth nlist $DISPLAY | sed -e 's/^..../ffff/' | xauth -f $XAUTH nmerge -

xhost +local:root
sudo xhost +si:localuser:root

docker run -d \
           --privileged \
           --runtime=nvidia --rm -it \
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
           --name gazebo-kinetic \
           jetson/ros:kinetic \
    bash -c 'curl -o double_pendulum.sdf http://models.gazebosim.org/double_pendulum_with_base/model-1_4.sdf && \
             gz model --model-name double_pendulum --spawn-file double_pendulum.sdf && \
             gzserver'

export GAZEBO_MASTER_IP=$(docker inspect --format '{{ .NetworkSettings.IPAddress }}' gazebo-kinetic)
export GAZEBO_MASTER_URI=$GAZEBO_MASTER_IP:11345

gzclient --verbose &
GZCLIENT_PID=$!

# After exit.
function cleanup {
    sudo kill $GZCLIENT_PID && \
    docker stop gazebo-kinetic && \
    docker rm gazebo-kinetic
}

trap SIGKILL cleanup
trap SIGTERM cleanup
trap SIGINT cleanup

