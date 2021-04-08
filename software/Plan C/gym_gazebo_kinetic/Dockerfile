#sudo docker system prune -a --volumes
#sudo bash build.sh kinetic-perception

#ARG NAME=ros_ws
ARG NAME=catkin_ws

ARG UID=1000
ARG GID=1000

FROM ros:kinetic-robot-xenial

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y bash-completion \
                       build-essential \
                       cmake \
                       git \
                       sudo \
                       wget && \
    rm -rf /var/lib/apt/lists/*

#RUN addgroup --gid ${GID} ros
#RUN adduser --gecos "ROS User" --disabled-password --uid ${UID} --gid ${GID} ros
RUN addgroup --gid 1000 ros
RUN adduser --gecos "ROS User" --disabled-password --uid 1000 --gid 1000 ros
RUN usermod -a -G dialout ros
ADD config/99_aptget /etc/sudoers.d/99_aptget
RUN chmod 0440 /etc/sudoers.d/99_aptget && \
    chown root:root /etc/sudoers.d/99_aptget
#    mkdir -p config && \
#    echo "ros ALL=(ALL) NOPASSWD: ALL" > config/99_aptget

ENV USER ros
USER ros
ENV HOME /home/${USER}

## Update packages and install dependencies.
#RUN sudo /bin/sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
#RUN /bin/bash -c "sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654 && \
#                  curl -sSL 'http://keyserver.ubuntu.com/pks/lookup?op=get&search=0xC1CF6E31E6BADE8868B172B4F42ED6FBAB17C654' | sudo apt-key add - && \
#                  sudo apt-get update && \
#                  sudo apt-get install ros-kinetic-desktop-full"

#RUN /bin/bash -c 'echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc && \
#                  source /opt/ros/kinetic/setup.bash'

RUN sudo /bin/sh -c "apt-get update && \
                     apt-get install -y build-essential \
                                        cmake \
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
                                        pyqt4-dev-tools \
                                        python-pip \
                                        python-skimage \
                                        python-rosdep \
                                        python-rosinstall \
                                        python-rosinstall-generator \
                                        python-wstool \
                                        python3-defusedxml \
                                        python3-pip \
                                        python3-pyqt4 \
                                        python3-skimage \
                                        python3-vcstool \
                                        pyqt4-dev-tools \
                                        pyqt5-dev-tools \
                                        qt4-qmake \
                                        ros-kinetic-ar-track-alvar-msgs \
                                        ros-kinetic-control-msgs \
                                        ros-kinetic-control-toolbox \
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
                                        ros-kinetic-rviz \
                                        ros-kinetic-std-srvs \
                                        ros-kinetic-tf2-sensor-msgs \
                                        ros-kinetic-trajectory-msgs \
                                        ros-kinetic-urdf && \
                     rm -rf /var/lib/apt/lists/*"

#RUN sudo -H /bin/bash -c "yes | pip install --upgrade pip==19.3.1 && \
#                          yes | pip install gym \
#                                            h5py \
#                                            keras \
#                                            pyuarm \
#                                            pyyaml \
#                                            pyserial \
#                                            rospkg \
#                                            catkin_pkg \
#                                            defusedxml \
#                                            netifaces \
#                                            numpy==1.16.2 \
#                                            matplotlib==2.2.3 \
#                                            protobuf==3.5.2 \
#                                            scikit-image==0.14.2 \
#                                            tensorflow-gpu \
#                                    --user"

RUN sudo -H /bin/bash -c "yes | pip install --upgrade pip==19.3.1 && \
                          yes | pip install gym \
                                            h5py \
                                            keras \
                                            pyuarm \
                                            pyyaml \
                                            pyserial \
                                            rospkg \
                                            catkin_pkg \
                                            defusedxml \
                                            netifaces \
                                            numpy==1.16.2 \
                                            matplotlib==2.2.3 \
                                            protobuf==3.5.2 \
                                            scikit-image==0.14.2 \
                                    --user"

# Install Gazebo 7 .
#RUN curl -sSL http://get.gazebosim.org | sh
RUN sudo sh -c 'echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-stable $(lsb_release -cs) main" > /etc/apt/sources.list.d/gazebo-stable.list'
RUN wget http://packages.osrfoundation.org/gazebo.key -O - | sudo apt-key add -
RUN sudo sh -c "apt-get update && \
                apt-get install -y gazebo7 \
                                   libignition-math2-dev \
                                   ros-kinetic-gazebo-ros-pkgs \
                                   ros-kinetic-gazebo-ros-control && \
                                   #ros-kinetic-ur-gazebo \
                                   #ros-kinetic-ur5-moveit-config \
                                   #ros-kinetic-ur-kinematics \
                                   #moveit_simple_controller_manager \
                rm -rf /var/lib/apt/lists/*"

ENV NAME='catkin_ws'
RUN mkdir -p ${HOME}/${NAME}/src
WORKDIR ${HOME}/${NAME}/src

RUN /bin/bash -c "source /opt/ros/${ROS_DISTRO}/setup.bash; catkin_init_workspace"
WORKDIR ${HOME}/${NAME}
RUN /bin/bash -c "source /opt/ros/${ROS_DISTRO}/setup.bash; catkin_make"

RUN /bin/bash -c "git clone https://github.com/erlerobot/gym-gazebo && \
                  cd gym-gazebo && \
                  pip install -e . --user && \
                  cd gym_gazebo/envs/installation && \
                  bash setup_kinetic.bash"

RUN /bin/bash -c "cd ${HOME}/${NAME}/src && \
                  git clone https://github.com/abstractguy/UArmForROS.git"

RUN /bin/bash -c "cd ${HOME}/${NAME}; source /opt/ros/${ROS_DISTRO}/setup.bash; catkin_make"

#RUN sudo -H /bin/bash -c "rosdep init && \
#                          rosdep update"

# Set missing environment variable needed to run Qt applications.
ENV QT_X11_NO_MITSHM 1

# Source bash.
#RUN source ${HOME}/${NAME}/devel/setup.bash

COPY config/update_bashrc /sbin/update_bashrc
RUN sudo chmod +x /sbin/update_bashrc; sudo chown ros /sbin/update_bashrc; sync; /bin/bash -c /sbin/update_bashrc; sudo rm /sbin/update_bashrc

COPY config/entrypoint.sh /ros_entrypoint.sh
RUN sudo chmod +x /ros_entrypoint.sh; sudo chown ros /ros_entrypoint.sh

RUN sudo sh -c "apt-get clean && \
                rm -rf /var/lib/apt/lists/*"

ENTRYPOINT ["/ros_entrypoint.sh"]
CMD ["source devel/setup.bash && /bin/bash"]
