#!/usr/bin/env bash
set -e

# Setup ROS environment.
source "/opt/ros/$ROS_DISTRO/setup.bash"

/sbin/udevadm control --reload-rules && \
udevadm trigger && \
service udev reload && \
service udev restart

exec "$@"

