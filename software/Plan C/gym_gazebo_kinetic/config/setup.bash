#NAME=ros_ws
NAME=catkin_ws

echo "" >> ~/.bashrc
echo "## ROS" >> ~/.bashrc
echo "source /opt/ros/$ROS_DISTRO/setup.bash" >> ~/.bashrc

# Choose one of these:
echo "source ~/${NAME}/devel/setup.bash" >> ~/.bashrc # ROS.
echo "source /home/ros/${NAME}/install/setup.bash" >> ~/.bashrc # ROS2.
