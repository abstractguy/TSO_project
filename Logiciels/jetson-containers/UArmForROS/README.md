# KTH uArm package
This is the official KTH-RAS uarm ROS package, based on the original ufactory software, designed by Joey Song ( joey@ufactory.cc / astainsong@gmail.com) and **heavily** improved upon by Joshua Haustein (haustein@kth.se). It is the favored way of interaction with the uarm in the RAS course.

## 1. Installation
---
### 1.1 Pre-Requirements
Connect uArm and get USB permission to access uArm
```bash
$ cd /etc/udev/rules.d
```
Create a file `ttyUSB.rules` and put the following line: `KERNEL=="ttyUSB*", MODE="0666"`. Save the file and **reconnect** the uArm USB to make it effective. (if you already have the permission to access USB, you can skip this step).

For using this package, the [pyUarm](https://github.com/uArm-Developer/pyuarm) library **MUST** be installed at first.

```bash
$ pip install pyuarm
```

Connect the uArm to the computer and upgrade your uArmProtocol Firmware

```bash
$ uarm-miniterm
$ firmware force
```

### 1.2 Package Download and Install
Install the ROS package in the src folder of your [catkin workspace](http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment).

```bash
$ cd ~/catkin_ws/src
$ git clone https://github.com/KTH-RAS/UArmForROS.git
$ cd ~/catkin_ws
$ catkin_make
```

## 2. Source Files
---

Before you use any packages in uarmForROS, source all setup.bash files which allow you to access uarm package

 ```bash

# Configure your ROS environment variables automatically every time you open a shell
echo "source /opt/ros/indigo/setup.bash" >> ~/.bashrc

# Source setup.bash
echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

## 3. Package Modules
---
### 3.1 Node
- `kth_uarm_core.py` is the main node. Run this node before anything else.

    **Step 1**: Connect uArm

    Set up ROS enviroment at first
    ```bash
    roscore
    ```
    Open another shall to connect uArm before use.
    ```bash
    rosrun uarm kth_uarm_core.py  // this will find the uarm automatically
    ```

    **Step 2**: Calibrate

    The first time you use the node, you will be prompted to calibrate the arm:
    ```
    Please calibrate the uArm. Check the wiki for instructions!
    Please move the arm into the calibration configuration. Once this is done, type y:
    ```
    The calibration configuration can be set as in the official ufactory documentation:

    <img src="https://uarmdocs.readthedocs.io/img/cli/calibration_position1.gif" width="450">
    
    The same procedure seen from the back:
    
    <img src="https://uarmdocs.readthedocs.io/img/cli/calibration_position2.gif" width="450">
    
    Once in the final position, type y and press enter.

### 3.2 Services

The KTH uArm package includes the following set of services:

- /uarm/attach_servos
    ```
      Service type: `uarm/AttachDetach`.
      Data: bool attach
            ---
            bool attach
    ```
    Set the boolean to true to attach the servos, false to detach. While detached, you can move the uArm manually.

- `/uarm/move_to` - Send a cartesian command to the uArm.
    ```
    Service type: `uarm/MoveTo`
    Data: int32 ABSOLUTE_MOVEMENT=0
          int32 RELATIVE_MOVEMENT=1
          int32 NO_INTERPOLATION=0
          int32 CUBIC_INTERPOLATION=1
          int32 LINEAR_INTERPOLATION=2
          geometry_msgs/Point position
            float64 x
            float64 y
            float64 z
          float32 eef_orientation
          int32 move_mode
          duration movement_duration
          bool ignore_orientation
          int32 interpolation_type
          bool check_limits
          ---
          geometry_msgs/Point position
            float64 x
            float64 y
            float64 z
          duration elapsed
          bool error
    ```
    This service allows you to move the end-effector in cartesian space. You will be able to choose an interpolation mode, and if you want to move in absolute coordinates, or relative to your currently measured pose. Note that choosing `NO_INTERPOLATION` will command the servos directly to the final configuration, resulting in a brusque movement.
    The service also allows you to set the desired orientation of the end-effector. If this is of no use to you, you can ser the `ignore_orientation` flag to true.

    The service returns the final position of the end-effector, and wheter an error occurred.

-   `/uarm/pump` - control the pump.
      ```
      Message_type: `uarm/Pump`.
      Data: bool pump_status
            ---
            bool pump_status
      ```
      Call this service to turn the pump on or off (`pump_status` respectively set to true or false).

-    `/uarm/move_to_joints` - Send the arm to a configuration in joint space.
       ```
       Message_type: uarm/MoveToJoints
       Data: int32 ABSOLUTE_MOVEMENT=0
             int32 RELATIVE_MOVEMENT=1
             int32 NO_INTERPOLATION=0
             int32 CUBIC_INTERPOLATION=1
             int32 LINEAR_INTERPOLATION=2
             float32 j0
             float32 j1
             float32 j2
             float32 j3
             int32 move_mode
             duration movement_duration
             int32 interpolation_type
             bool check_limits
             ---
             float32 j0
             float32 j1
             float32 j2
             float32 j3
             duration elapsed
             bool error
       ```
       This service operates similarly to the move_to service, but for a desired joint configuration.

### 3.3 Topics

-      /uarm/joint_state
       ```
       Message_type: sensor_msgs/JointState
       ```
       The current arm configuration is publish in a ROS standard way at a user-defined frequency.

### 3.4 Node parameters

When launching ```kth_uarm_core.py``` from a launch file, you can set the following parameters:

- joint_state_topic_name: topic where the uArm joint state is published.
  ```
   Default: /uarm/joint_state
  ```
- uarm_calibration_file: directory of the calibration file for the uArm. If not found the node will prompt the user for a new calibration.
  ```
   Default: test_calibration.yaml
  ```
- uarm_frame_name: name of the uArm base frame in the TF tree
  ```
   Default: uarm
  ```
- eef_frame_name: name of the end-effector frame in the TF tree
  ```
   Default: eef
  ```
- state_publishing_frequency: frequency at which the joint state is published. **WARNING**: Do not set this much higher than 10, as the uArm will be unable to query the servos at high frequencies.
  ```
   Default: 10
  ```

An example of how this can be achieved is offered in ```launch/kth_uarm.launch```. Under ```config/kth_uarm_core_config.yaml``` you will find a simple configuration file that is loaded by the ```kth_uarm``` launch file with the required parameters.

## 4.0 Troubleshooting
-----
### 4.1 Reported position/joint angles are far off.
If the reported end-effector position or the reported joint angles are far off, i.e. more than 5-7 degrees off, than you might have to recalibrate the firmware. Mount your arm on the legs it was shipped with and make sure it has sufficient space to move in all directions - it will move each joint from the lower to the upper limit. 

To start the calibration run:
```bash
$ uarm-calibrate
```
and follow the instructions on the screen. The arm will first move around for a while. Once it is done, a prompt will appear asking you to move the arm in a calibration configuration. This is the same configuration as shown in 3.1. Once you moved the arm in this configuration, confirm and the calibration is finished.

**If this did not solve your issue, do not do this again! Contact us instead.**

### 4.2 uArm often refuses to move.
This may be due to violation of joint limits. We do not recommend to move the arm with ```check_limits=False```. Instead you can check whether the joint limits of your arm are different from ours. Open the file 
https://github.com/KTH-RAS/UArmForROS/blob/master/python/ros_kth_uarm/kth_uarm.py
and compare the values assigned to LOWER_LIMITS and UPPER_LIMITS to the limits of your arm. You can see the limits of your arm by detaching the servos and manually moving the servos to their limits. In case your servo can safely be moved outside of the limits in the file, you may change them in your local copy. **Note, however, that changing the limits incorrectly may damage the arm!**
