## Machine Learning Containers for Jetson and JetPack for uARM control.

#### Somewhat modified by Samuel Duclos.

#### Refer to INSTALL_DOCKER.md for prerequisites.

##### Emulate on an x86_64 before trying out on ARM64:

```bash
DOCKER_URL=''
DOCKER_USER='arm64v8'
DOCKER_USER="${DOCKER_URL}${DOCKER_USER}"
DOCKER_IMAGE='ubuntu'
DOCKER_TAG='16.04'
```

##### Install QEMU the Docker way and verify.
```bash
uname -m
sudo apt-get install qemu binfmt-support qemu-user-static
docker run --rm --privileged multiarch/qemu-user-static --reset -p yes
docker pull ${DOCKER_USER}/${DOCKER_IMAGE}:${DOCKER_TAG}
docker run -it --rm --privileged --network=host --runtime nvidia -e DISPLAY=$DISPLAY -v /tmp/.X11-unix/:/tmp/.X11-unix -v $(pwd):/app ${DOCKER_USER}/${DOCKER_IMAGE}:${DOCKER_TAG} uname -m
```

##### Build and run.
```bash
sudo docker build -f Dockerfile.ros.kinetic -t jetson/ros:kinetic .
sudo chmod +x launch_container.sh
sudo ./launch_container.sh
```

##### Party!
```bash
roscore &
```

##### Modify this comment later.
```bash
uarm-miniterm
```

##### Modify this comment later.
```bash
firmware force
```

##### Modify this comment later.
```bash
rosrun uarm kth_uarm_core.py
```

#### See jetson-containers/UArmForROS/README.md for the rest.

#### The rest of this README.md is from the original jetson-containers.

###############################################################################

Hosted on [NVIDIA GPU Cloud](https://ngc.nvidia.com/catalog/containers?orderBy=modifiedDESC&query=L4T&quickFilter=containers&filters=) (NGC) are the following Docker container images for machine learning on Jetson:

* [`l4t-ml`](https://ngc.nvidia.com/catalog/containers/nvidia:l4t-ml)
* [`l4t-pytorch`](https://ngc.nvidia.com/catalog/containers/nvidia:l4t-pytorch)
* [`l4t-tensorflow`](https://ngc.nvidia.com/catalog/containers/nvidia:l4t-tensorflow)

Dockerfiles are also provided for the following containers, which can be built for JetPack 4.4 or newer:

* ROS Melodic (`ros:melodic-ros-base-l4t-r32.4.4`)
* ROS Noetic (`ros:noetic-ros-base-l4t-r32.4.4`)
* ROS2 Eloquent (`ros:eloquent-ros-base-l4t-r32.4.4`)
* ROS2 Foxy (`ros:foxy-ros-base-l4t-r32.4.4`)

Below are the instructions to build and test the containers using the included Dockerfiles.

## Docker Default Runtime

To enable access to the CUDA compiler (nvcc) during `docker build` operations, add `"default-runtime": "nvidia"` to your `/etc/docker/daemon.json` configuration file before attempting to build the containers:

``` json
{
    "runtimes": {
        "nvidia": {
            "path": "nvidia-container-runtime",
            "runtimeArgs": []
        }
    },

    "default-runtime": "nvidia"
}
```

You will then want to restart the Docker service or reboot your system before proceeding.

## Building the Containers

To rebuild the containers from a Jetson device running [JetPack 4.4](https://developer.nvidia.com/embedded/jetpack) or newer, first clone this repo:

``` bash
$ git clone https://github.com/dusty-nv/jetson-containers
$ cd jetson-containers
```

### ML Containers

To build the ML containers (`l4t-pytorch`, `l4t-tensorflow`, `l4t-ml`), use [`scripts/docker_build_ml.sh`](scripts/docker_build_ml.sh) - along with an optional argument of which container(s) to build: 

``` bash
$ ./scripts/docker_build_ml.sh all        # build all: l4t-pytorch, l4t-tensorflow, and l4t-ml
$ ./scripts/docker_build_ml.sh pytorch    # build only l4t-pytorch
$ ./scripts/docker_build_ml.sh tensorflow # build only l4t-tensorflow
```

> You have to build `l4t-pytorch` and `l4t-tensorflow` to build `l4t-ml`, because it uses those base containers in the multi-stage build.

Note that the TensorFlow and PyTorch pip wheel installers for aarch64 are automatically downloaded in the Dockerfiles from the [Jetson Zoo](https://elinux.org/Jetson_Zoo).

### ROS Containers

To build the ROS containers, use [`scripts/docker_build_ros.sh`](scripts/docker_build_ros.sh) with the name of the ROS distro to build:

``` bash
$ ./scripts/docker_build_ros.sh all       # build all: melodic, noetic, eloquent, foxy
$ ./scripts/docker_build_ros.sh melodic   # build only melodic
$ ./scripts/docker_build_ros.sh noetic    # build only noetic
$ ./scripts/docker_build_ros.sh eloquent  # build only eloquent
$ ./scripts/docker_build_ros.sh foxy      # build only foxy
```

Note that ROS Noetic and ROS2 Foxy are built from source for Ubuntu 18.04, while ROS Melodic and ROS2 Eloquent are installed from Debian packages into the containers.

## Testing the Containers

To run a series of automated tests on the packages installed in the containers, run the following from your `jetson-containers` directory:

``` bash
$ ./scripts/docker_test_ml.sh all        # test all: l4t-pytorch, l4t-tensorflow, and l4t-ml
$ ./scripts/docker_test_ml.sh pytorch    # test only l4t-pytorch
$ ./scripts/docker_test_ml.sh tensorflow # test only l4t-tensorflow
```

To test ROS:

``` bash
$ ./scripts/docker_test_ros.sh all       # test if the build of ROS all was successful: 'melodic', 'noetic', 'eloquent', 'foxy'
$ ./scripts/docker_test_ros.sh melodic   # test if the build of 'ROS melodic' was successful
$ ./scripts/docker_test_ros.sh noetic    # test if the build of 'ROS noetic' was successful
$ ./scripts/docker_test_ros.sh eloquent  # test if the build of 'ROS eloquent' was successful
$ ./scripts/docker_test_ros.sh foxy      # test if the build of 'ROS foxy' was successful
```

