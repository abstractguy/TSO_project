# Overview of gym-gazebo
An OpenAI gym extension for using Gazebo known as `gym-gazebo`! This work can put gym environment with gazebo, then you would like putting robot into gazebo with code applying gym. You can also visit the official github here [gym-gazebo](https://github.com/erlerobot/gym-gazebo). If you use ROS2, the better way for you is visiting the newest version [gym-gazebo2](https://github.com/AcutronicRobotics/gym-gazebo2).

## Summary
Because the official github which install version to Ubuntu 16.04 has been deprecated, and the package in author's github has many question that has been closed without issues, Here I am porting this to Ubuntu 18.04. Meanwhile, most of this has been tested on Ubuntu 16.04.

The original author's installation is here [original](https://github.com/zhaolongkzz/gym_gazebo_kinetic/blob/kinetic/Introduction.md) and here [INSTALL](https://github.com/zhaolongkzz/gym_gazebo_kinetic/blob/kinetic/INSTALL.md). If you encounter bugs here while I am developing, visit the author's github and/or submit a issue.

## Prerequisites
- ubuntu16.04 (currently working on porting to ubuntu18.04)
- ROS-Kinetic
  &ensp;&ensp;(visit the official web [here](http://wiki.ros.org/kinetic/Installation/Ubuntu).)
- Gazebo 7.14
- openai-gym
  &ensp;&ensp;(visit gym github [here](https://github.com/openai/gym.git).)
- anaconda3
  &ensp;&ensp;(install anaconda, click [here](http://docs.anaconda.com/anaconda/install/linux/).)
- python=2.7
  &ensp;&ensp;(with anaconda env below.)

If you want to train it with GPU here, you should install cuda
- cuda=9.0
- libcudnn7.3


## Installation of conda env

Create an environment to run them.
```bash
yes | conda create -n gymenv python=2.7 pip=19.3.1 numpy=1.16.2 matplotlib=2.2.3 protobuf=3.5.2 scikit-image=0.14.2 cudatoolkit=9.0
conda activate gymenv
yes | pip install rospkg catkin_pkg defusedxml netifaces tensorflow-gpu
yes | sudo pip install gym h5py keras
curl -sSL http://get.gazebosim.org | sh
git clone https://github.com/erlerobot/gym-gazebo
cd gym-gazebo
sudo pip install -e .
cd gym_gazebo/envs/installation
bash setup_melodic.bash
cd ../../../..
git clone https://github.com/abstractguy/gym_gazebo_kinetic.git
cd gym_gazebo_kinetic
pip install -e .
```

## Installation of virtualenv

When using electronics, you may want to use this method instead.
```bash
sudo apt install virtualenv
virtualenv venv --no-pip
source venv/bin/activate
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py pip==19.3.1
```


## Installation of ROS Kinetic (skip if using ROS Melodic)
First installing some ROS dependencies below:
```bash
sudo apt update && \
sudo apt-get -y install cmake \
                        gcc \
                        g++ \
                        qt4-qmake \
                        libqt4-dev \
                        libusb-dev \
                        libftdi-dev \
                        libspnav-dev \
                        libcwiid-dev \
                        libignition-math2-dev \
                        ros-kinetic-ar-track-alvar-msgs \
                        ros-kinetic-control-toolbox \
                        ros-kinetic-control-msgs \
                        ros-kinetic-eigen-conversions \
                        ros-kinetic-geodesy \
                        ros-kinetic-joy \
                        ros-kinetic-kdl-conversions \
                        ros-kinetic-navigation \
                        ros-kinetic-nodelet \
                        ros-kinetic-octomap-msgs \
                        ros-kinetic-octomap-ros \
                        ros-kinetic-pcl-ros \
                        ros-kinetic-pluginlib \
                        ros-kinetic-rqt-joint-trajectory-controller \
                        ros-kinetic-rviz \
                        ros-kinetic-sophus \
                        ros-kinetic-std-srvs \
                        ros-kinetic-tf2-sensor-msgs \
                        ros-kinetic-trajectory-msgs \
                        ros-kinetic-urdf
```


## Installation of ROS Melodic
First installing some ROS dependencies below:
```bash
sudo apt update && \
sudo apt-get -y install cmake \
                        curl \
                        g++ \
                        gcc \
                        libbluetooth-dev \
                        libcwiid-dev \
                        libqt4-dev \
                        libftdi-dev \
                        libignition-math2-dev \
                        libspnav-dev \
                        libusb-dev \
                        python-pip \
                        python-skimage \
                        python3-defusedxml \
                        python3-pyqt4 \
                        python3-vcstool \
                        pyqt4-dev-tools \
                        pyqt5-dev-tools \
                        qt4-qmake \
                        ros-melodic-control-msgs \
                        ros-melodic-control-toolbox \
                        ros-melodic-eigen-conversions \
                        ros-melodic-geodesy \
                        ros-melodic-joy \
                        ros-melodic-kdl-conversions \
                        ros-melodic-navigation \
                        ros-melodic-nodelet \
                        ros-melodic-octomap-msgs \
                        ros-melodic-octomap-ros \
                        ros-melodic-pcl-ros \
                        ros-melodic-pluginlib \
                        ros-melodic-rviz \
                        ros-melodic-sophus \
                        ros-melodic-std-srvs \
                        ros-melodic-tf2-sensor-msgs \
                        ros-melodic-trajectory-msgs \
                        ros-melodic-urdf
```


## Quickstart

### 1.Compile all the packages
**Note**: Anaconda could interfere with ROS dependencies.

I have altered some github package or version in files, use `gazebo_ros_kinetic.repos` in my github [here](https://github.com/abstractguy/gym_gazebo_kinetic/blob/kinetic/gym_gazebo/envs/installation/gazebo_ros_kinetic.repos).
```bash
cd gym_gazebo/envs/installation
bash setup_kinetic.bash
```

Put the model file into your workspace/src folder.
```bash
cd gym_gazebo/envs/installation
bash turtlebot_setup.bash
```

After the first two steps above, you will find five lines being added in your `~/.bashrc`:
```bash
source "${HOME}/school/Project/gym-gazebo/gym_gazebo/envs/installation/gym_ws/devel/setup.bash"
export GAZEBO_MODEL_PATH="${HOME}/school/Project/gym-gazebo/gym_gazebo/envs/installation/../assets/models"
export GYM_GAZEBO_WORLD_MAZE="${HOME}/school/Project/gym-gazebo/gym_gazebo/envs/installation/../assets/worlds/maze.world"
export GYM_GAZEBO_WORLD_CIRCUIT="${HOME}/school/Project/gym-gazebo/gym_gazebo/envs/installation/../assets/worlds/circuit.world"
export GYM_GAZEBO_WORLD_CIRCUIT2="${HOME}/school/Project/gym-gazebo/gym_gazebo/envs/installation/../assets/worlds/circuit2.world"
export GYM_GAZEBO_WORLD_CIRCUIT2C="${HOME}/school/Project/gym-gazebo/gym_gazebo/envs/installation/../assets/worlds/circuit2c.world"
export GYM_GAZEBO_WORLD_ROUND="${HOME}/school/Project/gym-gazebo/gym_gazebo/envs/installation/../assets/worlds/round.world"
```

Open a new terminal and uncomment your conda env in your `.bashrc`. Then use it as below:
```bash
source activate gymenv

cd gym_gazebo/examples/scripts_turtlebot
python circuit2_turtlebot_lidar_qlearn.py
```


### 2.Open gazebo
Open another terminal:
```bash
cd gym-gazebo/gym_gazebo/envs/installation/
source turtlebot_setup.bash
# Here the number is set in your code. Default is 12346.
export GAZEBO_MASTER_URI=http://localhost:12346
gzclient
```

Display a graph showing the current reward history by running the following script:
```bash
cd examples/utilities
python display_plot.py
```

## Picture
<p align="center">
  <img src="https://github.com/abstractguy/gym_gazebo_kinetic/blob/kinetic/imgs/qlearn.png"><br><br>
</p>

<p align="center">
  <img src="https://github.com/abstractguy/gym_gazebo_kinetic/blob/kinetic/imgs/dqn.png"><br><br>
</p>


## LICENCE
[MIT License](https://github.com/abstractguy/gym_gazebo_kinetic/blob/kinetic/LICENSE)


## FAQ

**Q1**: I encounter `ImportError: No module named msg` like below:

```bash
Traceback (most recent call last):
  File "/home/samuel/school/Project/gym_gazebo_kinetic/gym_gazebo/envs/installation/gym_ws/src/hector_gazebo/hector_gazebo_thermal_camera/cfg/GazeboRosThermalCamera.cfg", line 5, in <module>
    from driver_base.msg import SensorLevels
ImportError: No module named msg
```
***

A1: Run driver_base first, like that catkin_make -DCATKIN_WHITELIST_PACKAGES="driver_base".
