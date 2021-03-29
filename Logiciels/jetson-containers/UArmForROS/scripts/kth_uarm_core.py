#!/usr/bin/env python

'''

# File Name : kth_uarm_core.py
# Authors : Diogo Almeida, Joshua Haustein; based on uarm_core.py by Joey Song
# Version : V1.00
# Date : 20 Oct, 2016
# Modified Date : 20 Oct, 2016
# Description : This module contains a ROS node that provides access to the KTH uarm python wrapper.
# Copyright(C) 2016 uArm Team. All right reserved.

'''
# All libraries needed to import
# Import system library
import sys
import time
import rospy
import logging
import tf
import math
import threading

# Import kth uarm python library
import ros_kth_uarm.kth_uarm as kth_uarm

# Import messages type
from std_msgs.msg import String
from std_msgs.msg import UInt8
from std_msgs.msg import Int32
import geometry_msgs
from sensor_msgs.msg import JointState
from uarm.srv import MoveTo, MoveToResponse
from uarm.srv import MoveToJoints, MoveToJointsResponse
from uarm.srv import Pump, PumpResponse
from uarm.srv import AttachDetach, AttachDetachResponse


class ROSKTHUarmBridge(object):

    def __init__(self, calibration_file_name, base_frame_name='uarm', eef_frame_name='eef',
                 joint_state_topic_name='/uarm/joint_states'):
        self._calibration_file_name = calibration_file_name
        self._uarm_lock = threading.RLock()
        self._uarm = None
        self.try_connect_uarm()
        self._base_frame_name = base_frame_name
        self._eef_frame_name = eef_frame_name
        self._joint_state_seq_num = 0
        self._tf_broadcaster = tf.TransformBroadcaster()
        self._joint_state_publisher = rospy.Publisher(joint_state_topic_name, JointState, queue_size=5)

    # def handle_get_positions(self, request):
    #     """Process a GetPositions request."""
    #     rospy.loginfo("A GetPositions request has been received. Processing...")
    #     response = GetPositionsResponse()
    #     with self._uarm_lock:
    #         eef_position = self._uarm.get_position()
    #         response.position.x = eef_position[0]
    #         response.position.y = eef_position[1]
    #         response.position.z = eef_position[2]
    #
    #         config = self._uarm.get_configuration()
    #         response.angles = list(config)
    #     return response

    def handle_move_to(self, request):
        """Process a MoveTo service request."""
        with self._uarm_lock:
            begin_time = rospy.Time.now()
            target_position = request.position
            move_mode = request.move_mode
            duration = request.movement_duration
            ignore_orientation = request.ignore_orientation
            interpolation_type_int = request.interpolation_type
            check_limits = request.check_limits

            if move_mode != request.ABSOLUTE_MOVEMENT and move_mode != request.RELATIVE_MOVEMENT:
                rospy.logerr("MoveTo request contains an invalid move mode. Aborting.")
                return self.create_move_to_error(begin_time)

            interpolation_type = None
            if interpolation_type_int == request.NO_INTERPOLATION:
                interpolation_type = 'None'
            elif interpolation_type_int == request.CUBIC_INTERPOLATION:
                interpolation_type = 'Cubic'
            elif interpolation_type_int == request.LINEAR_INTERPOLATION:
                interpolation_type = 'Linear'
            else:
                rospy.logerr("MoveTo request contains an invalid ease type. Aborting")
                return self.create_move_to_error(begin_time)

            if duration.to_sec() <= 0.0 and interpolation_type != 'None':
                rospy.logerr("MoveTo request contains an invalid duration (must be >= 0.0). Aborting.")
                return self.create_move_to_error(begin_time)

            rospy.loginfo("A proper MoveTo request has been received. Processing...")

            theta = None
            if not ignore_orientation:
                theta = request.eef_orientation
            # Based on the request either do a relative movement or absolute movement
            success = False
            if move_mode == request.RELATIVE_MOVEMENT:
                success = self._uarm.move_cartesian_relative(dx=target_position.x,
                                                             dy=target_position.y,
                                                             dz=target_position.z,
                                                             dtheta=theta,
                                                             interpolation_type=interpolation_type,
                                                             duration=duration.to_sec(),
                                                             check_limits=check_limits)
            else:
                success = self._uarm.move_cartesian(x=target_position.x, y=target_position.y,
                                                    z=target_position.z, theta=theta,
                                                    interpolation_type=interpolation_type, duration=duration.to_sec(),
                                                    check_limits=check_limits)

            response = MoveToResponse()
            move_time = rospy.Time.now()
            eef_position = self._uarm.get_position()
            response.position.x = eef_position[0]
            response.position.y = eef_position[1]
            response.position.z = eef_position[2]
            response.elapsed = move_time - begin_time
            response.error = not success
            return response

    def handle_move_to_joints(self, request):
        """Process a MoveToJoints service request."""
        with self._uarm_lock:
            begin_time = rospy.Time.now()
            target_configuration = [request.j0, request.j1, request.j2, request.j3]
            move_mode = request.move_mode
            duration = request.movement_duration
            interpolation_type_int = request.interpolation_type
            check_limits = request.check_limits

            if move_mode != request.ABSOLUTE_MOVEMENT and move_mode != request.RELATIVE_MOVEMENT:
                rospy.logerr("MoveToJoints request contains an invalid move mode. Aborting.")
                return self.create_move_to_joints_error(begin_time)

            interpolation_type = None
            if interpolation_type_int == request.NO_INTERPOLATION:
                interpolation_type = 'None'
            elif interpolation_type_int == request.CUBIC_INTERPOLATION:
                interpolation_type = 'Cubic'
            elif interpolation_type_int == request.LINEAR_INTERPOLATION:
                interpolation_type = 'Linear'
            else:
                rospy.logerr("MoveToJoints request contains an invalid ease type. Aborting")
                return self.create_move_to_joints_error(begin_time)

            if duration.to_sec() <= 0.0 and interpolation_type != 'None':
                rospy.logerr("MoveToJoints request contains an invalid duration (must be >= 0.0). Aborting.")
                return self.create_move_to_joints_error(begin_time)

            rospy.loginfo("A proper MoveToJoints request has been received. Processing...")

            # Based on the request either do a relative movement or absolute movement
            success = False
            if move_mode == request.RELATIVE_MOVEMENT:
                success = self._uarm.move_relative(*target_configuration,
                                                   interpolation_type=interpolation_type,
                                                   duration=duration.to_sec(),
                                                   check_limits=check_limits)
            else:
                success = self._uarm.move(*target_configuration,
                                          interpolation_type=interpolation_type,
                                          duration=duration.to_sec(),
                                          check_limits=check_limits)

            response = MoveToJointsResponse()
            [response.j0, response.j1, response.j2, response.j3] = self._uarm.get_configuration()
            move_time = rospy.Time.now()
            response.elapsed = move_time - begin_time
            response.error = not success
            return response

    def handle_pump(self, request):
        with self._uarm_lock:
            self._uarm.pump(request.pump_status)
            response = PumpResponse()
            response.pump_status = self._uarm.is_sucking()
            return response

    def handle_attach_detach(self, request):
        with self._uarm_lock:
            response = AttachDetachResponse()
            if request.attach:
                self._uarm.attach_all_servos()
                response.attach = True
            else:
                self._uarm.detach_all_servos()
                response.attach = False
            return response

    def create_move_to_error(self, init_time):
        """Return a MoveToResponse filled with information and positive error flag."""
        response = MoveToResponse()
        position, response.theta = self._uarm.get_pose()
        response.position.x = position[0]
        response.position.y = position[1]
        response.position.z = position[2]
        current_time = rospy.Time.now()
        response.elapsed = current_time - init_time
        response.error = True
        return response

    def create_move_to_joints_error(self, init_time):
        """Return a MoveToJointsResponse filled with information and positive error flag."""
        response = MoveToJointsResponse()
        [response.j0, response.j1, response.j2, response.j3] = self._uarm.get_configuration()
        current_time = rospy.Time.now()
        response.elapsed = current_time - init_time
        response.error = True
        return response

    def publish_state(self):
        """ Publishes the current joint angles and end-effector TF """
        with self._uarm_lock:
            # Publish joint states:
            joint_state_msg = JointState()
            joint_state_msg.header.frame_id = self._base_frame_name
            joint_state_msg.header.stamp = rospy.Time.now()
            joint_state_msg.header.seq = self._joint_state_seq_num
            self._joint_state_seq_num = self._joint_state_seq_num + 1
            joint_state_msg.name = ['j0', 'j1', 'j2', 'j3']
            config = self._uarm.get_configuration()
            joint_state_msg.position = list(config)
            self._joint_state_publisher.publish(joint_state_msg)

            # Publish TF of end-effector
            position, theta = self._uarm.get_pose()
            theta_rad = math.pi / 180.0 * theta
            self._tf_broadcaster.sendTransform(map(lambda x: x / 100.0, position),
                                               tf.transformations.quaternion_about_axis(theta_rad, (0,0,1)),
                                               rospy.Time.now(),
                                               self._eef_frame_name,
                                               self._base_frame_name)

    def try_connect_uarm(self):
        """ Attempts to connect the uarm
            @return True if successful, False otherwise
        """
        with self._uarm_lock:
            if self._uarm is not None:
                return True
            try:
                self._uarm = kth_uarm.KTHUarm(self._calibration_file_name)
                return True
            except RuntimeError as e:
                rospy.logwarn('Could not connect uArm. Please make sure there is uArm connected to this machine')
            return False

    def is_calibrated(self):
        """ Returns whether the uarm is calibrated and the ROS API can be used. """
        with self._uarm_lock:
            return self._uarm.is_calibrated()

    def calibrate(self):
        with self._uarm_lock:
            rospy.logwarn('Please calibrate the uArm. Check the wiki for instructions!')
            self._uarm.calibrate(self._calibration_file_name)
            if self.is_calibrated():
                rospy.logwarn('Calibration successful.')
            else:
                rospy.logerr('Calibration failed.')


if __name__ == '__main__':
    # initialize node and get parameters
    rospy.init_node('uarm_bridge', anonymous=True)
    joint_state_topic_name = rospy.get_param('joint_state_topic_name', '/uarm/joint_state')
    calibration_file_name = rospy.get_param('uarm_calibration_file', 'test_calibration.yaml')
    uarm_frame_name = rospy.get_param('uarm_frame_name', 'uarm')
    eef_frame_name = rospy.get_param('eef_frame_name', 'eef')
    publishing_frequency = rospy.get_param('state_publishing_frequency', 10)
    # create bridge class
    uarm_bridge = ROSKTHUarmBridge(calibration_file_name=calibration_file_name,
                                  joint_state_topic_name=joint_state_topic_name,
                                  base_frame_name=uarm_frame_name,
                                  eef_frame_name=eef_frame_name)
    # Make sure the uarm is connected
    while not uarm_bridge.try_connect_uarm() and not rospy.is_shutdown():
        rospy.sleep(2.0)
    # Make sure the uarm is calibrated. If not allow the user to do so
    while not rospy.is_shutdown() and not uarm_bridge.is_calibrated():
        # IPython.embed()
        uarm_bridge.calibrate()

    # If we reached this point, the uarm is connected and calibrated. So advertise the ROS Api
    rospy.Service("uarm/move_to", MoveTo, uarm_bridge.handle_move_to)
    rospy.Service("uarm/move_to_joints", MoveToJoints, uarm_bridge.handle_move_to_joints)
    rospy.Service("uarm/pump", Pump, uarm_bridge.handle_pump)
    rospy.Service("uarm/attach_servos", AttachDetach, uarm_bridge.handle_attach_detach)

    rospy.loginfo("KTH uArm core initialized successfully!")
    
    publisher_rate = rospy.Rate(publishing_frequency)
    while not rospy.is_shutdown():
        uarm_bridge.publish_state()
        publisher_rate.sleep()
    sys.exit(0)
