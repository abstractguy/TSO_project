sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list' && \
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654 && \
sudo apt update && \
sudo apt install -y ros-melodic-desktop-full && \
echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc && \
source ~/.bashrc && \
source /opt/ros/melodic/setup.bash && \
sudo apt-get install -y build-essential \
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
                        python-pip \
                        python-skimage \
                        python-rosdep \
                        python-rosinstall \
                        python-rosinstall-generator \
                        python-wstool \
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
                        ros-melodic-urdf && \
yes | conda create -n gymenv python=2.7 pip=19.3.1 numpy=1.16.2 matplotlib=2.2.3 protobuf=3.5.2 scikit-image=0.14.2 cudatoolkit=9.0 && \
conda activate gymenv && \
yes | pip2 install gym h5py keras pyuarm pyyaml pyserial rospkg catkin_pkg defusedxml netifaces tensorflow-gpu --user && \
curl -sSL http://get.gazebosim.org | sh && \
git clone https://github.com/erlerobot/gym-gazebo && \
cd gym-gazebo && \
sudo pip install -e . && \
cd gym_gazebo/envs/installation && \
bash setup_melodic.bash && \
cd ../../../.. #&& \
#git clone https://github.com/abstractguy/gym_gazebo_kinetic.git && \
#cd gym_gazebo_kinetic && \
#pip install -e . && \
#cd gym_gazebo/envs/installation && \
#bash setup_melodic.bash && \
echo 'KERNEL=="ttyUSB*", MODE="0666"' > /etc/udev/rules.d/ttyUSB.rules && \
LINE_TO_ADD=$(lsusb | grep Arduino | cut -d" " -f6 | xargs -I{} echo "UARM_HWID_KEYWORD = \"USB VID:PID={}\"") sed -i "s|^UARM_HWID_KEYWORD.*$|$LINE_TO_ADD|g" /usr/local/lib/python2.7/dist-packages/pyuarm/tools/list_uarms.py && \
python2 -c 'import pyuarm.tools.firmware; pyuarm.tools.firmware' && \
mkdir -p ~/catkin_ws/src && \
cd ~/catkin_ws/src && \
git clone https://github.com/abstractguy/UArmForROS.git && \
cd ~/catkin_ws && \
catkin_make && \
echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
