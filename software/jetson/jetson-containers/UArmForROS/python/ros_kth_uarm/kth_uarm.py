#! /usr/bin/env python
'''

# File Name : kth_uarm.py
# Authors : Joshua Haustein
# Version : V1.00
# Date : 18 Oct, 2016
# Date : 20 Oct, 2016
# Description : This module contains a wrapper class of the UArm Python interface developed for the
                KTH course DD2425 Robotics and Autonomous Systems.

'''

import pyuarm
import math
import yaml
import logging
import time
import numpy


class KTHUarm(object):
    """ This class is a wrapper for the original pyuarm class.
        It provides a reimplementation of the inverse kinematics of the uarm
        to ease arm-camera coordination. Note that an instance of this class needs to
        be calibrated before usage. The calibration can be performed by either calling
        the calibrate function or by providing a calibration from a previous run."""

    LOWER_LIMITS = [0.0, -4.9, -4.83, -65.0]
    UPPER_LIMITS = [180.0, 130.0, 123.8, 40.0]
    J2_J1_MIN_LIMIT_OFFSET= 18.5
    J2_J1_MAX_LIMIT_OFFSET = 153.0
    NUM_JOINTS = 4
    JOINT_NAMES = ['j0', 'j1', 'j2', 'j3']
    CALIBRATION_CONFIG = [45.0, 130.0, -4.83, 0.0]
    DEFAULT_EXECUTION_SLEEP_TIME = 0.1
    MAXIMAL_NUM_INTERPOLATION_STEPS = 80.0
    NO_INTERPOLATION = 'None'
    LINEAR_INTERPOLATION = 'Linear'
    CUBIC_INTERPOLATION = 'Cubic'
    # LINKS
    L1 = 10.645
    L2 = 2.117
    L3 = 14.825
    L4 = 16.02
    L5 = 3.3
    L6 = 5.9

    def __init__(self, calibration_file_name=None):
        """ Create a new KTHUarm instance.
            @param calibration_file_name - If provided, the arm calibration is read from this file.
        """
        self._calibrated = False
        self._logger = logging.getLogger(__name__)
        self._uarm = pyuarm.get_uarm()
        self._offsets = numpy.array([])
        self._pump_status = False
        if calibration_file_name is not None:
            self.load_calibration(calibration_file_name)
        if self._calibrated:
            self.attach_all_servos()

    ############################### PRIVATE FUNCTIONS ##############################
    def _to_raw_arm_configuration(self, values):
        # maps the given values to the raw servo angles (without offsets)
        return map(lambda x, y: x + y, values, self._offsets)

    def _check_connection(self):
        # Throws an exception if not connected
        if self._uarm is None:
            raise RuntimeError('There is no uarm attached.')

    def _check_calibration(self):
        self._check_connection()
        # Throws an exception if not calibrated
        if not self._calibrated:
            raise RuntimeError('The uarm is not properly calibrated. Please execute the calibration first!')

    def _cubic_interpolation(self, start_value, distance, t):
        return start_value + 3.0 * distance * t * t - 2.0 * distance * t * t * t

    def _linear_interpolation(self, start_value, distance, t):
        return start_value + t * distance

    def _interpolate(self, start_values, target_values, num_steps, interpolation_type='Linear'):
        interpolation_func = None
        if interpolation_type == 'Linear':
            interpolation_func = self._linear_interpolation
        elif interpolation_type == 'Cubic':
            interpolation_func = self._cubic_interpolation
        elif interpolation_type == 'None' or interpolation_type == None:
            return None
        else:
            self._logger.error('Unkown interpolation type: ' + str(interpolation_type))
            raise ValueError('Invalid interpolation type ' + interpolation_type)
        distances = map(lambda x,y: x - y, target_values, start_values)
        t_step = 1.0 / num_steps
        values = []
        for i in range(int(num_steps) + 1):
            t = i * t_step
            # we interpolate a point using cubic interpolation
            interpolated_config = map(interpolation_func,
                                      start_values,
                                      distances,
                                      self.NUM_JOINTS * [t])
            values.append(interpolated_config)
        return values

    def _move_servos(self, config):
        self._check_connection()
        [j0, j1, j2, j3] = self._to_raw_arm_configuration(config)
        self._uarm.write_servo_angle(pyuarm.SERVO_BOTTOM, j0, with_offset=False)
        self._uarm.write_servo_angle(pyuarm.SERVO_LEFT, j1, with_offset=False)
        self._uarm.write_servo_angle(pyuarm.SERVO_RIGHT, j2, with_offset=False)
        self._uarm.write_servo_angle(pyuarm.SERVO_HAND, j3, with_offset=False)

    ################################################################################
    def attach_all_servos(self):
        """ Attaches all servos. Attached servos should not be moved by hand! The servos need to be attached
            in order for the arm to move. """
        self._check_connection()
        self._uarm.attach_all_servos()

    def calibrate(self, file_name=None):
        """ Calibrates the arm. Note that this requires you to manually move the arm.
            @param file_name - if provided, the calibration is stored in the specified file.
        """
        self._check_connection()
        self._uarm.detach_all_servos()
        achar = 'n'
        while not achar == 'y':
            achar = raw_input('Please move the arm into the calibration configuration. Once this is done, type y:')
        joint_values = self._uarm.read_servo_angle(with_offset=False)
        self._uarm.attach_all_servos()
        offsets = map(lambda x, y: x - y, joint_values, self.CALIBRATION_CONFIG)
        self._offsets = numpy.array(offsets)
        self._calibrated = True
        if file_name is not None:
            offsets_as_dict = {}
            for i in range(self.NUM_JOINTS):
                offsets_as_dict[self.JOINT_NAMES[i]] = offsets[i]
            try:
                afile = open(file_name, 'w')
                yaml.dump(offsets_as_dict, afile)
                afile.close()
            except IOError as err:
                self._logger.error('Could not save calibration in file ' + file_name)
                self._logger.error(str(err))

    def detach_all_servos(self):
        """ Detaches all servos. This allows moving the servos to any desired configuration by hand. """
        self._check_connection()
        self._uarm.detach_all_servos()

    def forward_kinematics(self, j0=0.0, j1=0.0, j2=0.0, j3=0.0, config=None):
        """ Returns a the position (x,y,z) and theta for the given configuration.
            Either:
            @param j0 - angle of joint 0 (in degrees)
            @param j1 - angle of joint 1 (in degrees)
            @param j2 - angle of joint 2 (in degrees)
            @param j3 - angle of joint 3 (in degrees)
            Or:
            @param config - iterable of joint angles [j0, j1, j2, j3] (in degrees)
            In case config is specified, the arguments j0, j1, j2, j3 are ignored.
            @return (x,y,z) as numpy array and theta, i.e. (x, y, z), theta
        """
        if config is not None:
            [j0, j1, j2, j3] = config
        # if not self.in_joint_limits(j0, j1, j2, j3):
            # return None
        y_prime = self.L2 + self.L3 * math.cos(j1 * math.pi / 180.0) + self.L4 * math.cos(j2 * math.pi /
                                                                                          180.0) + self.L5
        x = y_prime * math.cos(j0 * math.pi / 180.0)
        y = y_prime * math.sin(j0 * math.pi / 180.0)
        z = self.L1 + self.L3 * math.sin(j1 * math.pi / 180.0) - self.L4 * math.sin(j2 * math.pi / 180.0) - self.L6
        theta = j0 - j3
        return numpy.array([x,y,z]), theta

    def get_configuration(self):
        """ Returns the current configuration of the arm.
            Note that the arm needs to be calibrated for this!
            @return numpy array (j0, j1, j2, j3)
        """
        self._check_calibration()
        values = self._uarm.read_servo_angle(with_offset=False)
        return numpy.array(map(lambda x, y: x - y, values, self._offsets))

    def get_position(self):
        """ Returns the current end-effector position and orientation.
            @return numpy array (x,y,z)
        """
        current_config = self.get_configuration()
        position, theta = self.forward_kinematics(config=current_config)
        return position

    def get_pose(self):
        """ Returns the current pose of the end-effector.
            @return numpy array (x,y,z), float theta
        """
        current_config = self.get_configuration()
        return self.forward_kinematics(config=current_config)

    def has_uarm(self):
        """ Returns whether this instance is connected to a uarm. """
        return self._uarm is not None

    def inverse_kinematics(self, x, y, z, theta, check_limits=True):
        """ Returns the configuration [j0, j1, j2, j3] such that the end-effector reaches the position
            x,y,z.
            @param x - cartesian position in cm
            @param y - cartesian position in cm
            @param z - cartesian position in cm
            @param theta - orientation of eef in degrees (if None, it is ignored -> j3 = 0.0)
            @param check_limits - if true, a solution is only returned if it is within limits
            @return numpy array of the configuration achieving the desired position or None,
                    if position is not reachable (and check_limits == True).
        """
        # The rotation of the first joint is directly given by the orientation of the arm.
        theta_0 = math.atan2(y, x)
        # The other two angles can be computed by reducing the problem to a plane (2D)
        # Compute how far the eef is away from the origin
        # There are two ways of doing this, choose the numerically stabler option
        if abs(math.cos(theta_0)) < abs(math.sin(theta_0)):
            arm_stretch = y / math.sin(theta_0)
        else:
            arm_stretch = x / math.cos(theta_0)
        # Let's now compute the position of the screw next to eef in a 2D plane in respect to joint j1
        y_prime = arm_stretch - self.L2 - self.L5
        z_prime = z - self.L1 + self.L6
        # make a sanity check here, y_prime has to be positive
        if y_prime <= 0.0:
            self._logger.info('Can not compute IK, y_prime invalid: ' + str(y_prime))
            return None
        # Given these coordinates in a plane (with respect to joint j1), we can compute
        # theta_1, theta_2 using geometric relations (applying the law of cosines)
        # For this, consider the triangle spanned by link 3 (L3), link 4 (L4)
        # and the line (r) connecting the screw on the eef with the origin of joint 1
        # This triangle is rotated around the axis of joint 1 by theta_prime:
        theta_prime = math.atan2(z_prime, y_prime)
        r_2 = y_prime * y_prime + z_prime * z_prime  # this is r * r, which is > 0
        # The angle alpha between r and L3 is given by the law of cosines:
        acos_arg = (self.L3 * self.L3 + r_2 - self.L4 * self.L4) / (2.0 * self.L3 * math.sqrt(r_2))
        if abs(acos_arg) > 1.0:
            # if this is the case, we do not have a valid triangle, i.e. the position is out of reach
            self._logger.info('Can not compute IK, acos_arg invalid: ' + str(acos_arg))
            return None
        alpha = math.acos(acos_arg)
        # With this we get theta_1:
        theta_1 = theta_prime + alpha
        # Now, we can easily compute theta_2, by choosing it such that we reach the demanded z
        # i.e. it has to be L3 * sin(theta_1) - L4 * sin(theta_2) = z_prime:
        asin_arg = (self.L3 * math.sin(theta_1) - z_prime) / self.L4
        # in case the argument for the asin is of greater magnitude than 1.0, we can not reach the point
        if abs(asin_arg) > 1.0:
            self._logger.info('Can not compute IK, asin_arg invalid: ' + str(asin_arg))
            return None
        theta_2 = math.asin(asin_arg)
        # Compute theta 3 according to desired eef orientation (j3 rotates in the opposite direction of j0)
        theta_3 = 0.0
        if theta is not None:
            theta_3 = theta_0 - theta * math.pi / 180.0
        # Finally, transform all thetas into degrees and return them as numpy array
        config = numpy.array([theta_0 * 180.0 / math.pi,
                              theta_1 * 180.0 / math.pi,
                              theta_2 * 180.0 / math.pi,
                              theta_3 * 180.0 / math.pi])
        if self.in_joint_limits(*config) or not check_limits:
            return config
        else:
            self._logger.info('Computed IK solution is not within joint limits: ' + str(config))
            return None

    def in_joint_limits(self, j0, j1, j2, j3):
        """ Returns True iff the given joint values are within the respective limits.
            Note that this function is based on approximations of the arm kinematics.
            There may be valid configurations that this function identifies as invalid.
            On the other hand, it may identify a configuration as valid although it results in self
            collisions.
            @param j0 - angle of joint 0 (in degrees)
            @param j1 - angle of joint 1 (in degrees)
            @param j2 - angle of joint 2 (in degrees)
            @param j3 - angle of joint 3 (in degrees)
            @return True or False depending on whether the given values are witin the limits
        """
        # first check j0
        if j0 < self.LOWER_LIMITS[0] or j0 > self.UPPER_LIMITS[0]:
            return False
        # next check j1:
        if j1 < self.LOWER_LIMITS[1] or j1 > self.UPPER_LIMITS[1]:
            return False
        # next check j2:
        # this is where it gets tricky! the limits of j2 depend on the current value of j1
        if j2 < max(self.LOWER_LIMITS[2], self.J2_J1_MIN_LIMIT_OFFSET - j1) or \
           j2 > min(self.UPPER_LIMITS[2], self.J2_J1_MAX_LIMIT_OFFSET - j1):
            return False
        if j3 < self.LOWER_LIMITS[3] or j3 > self.UPPER_LIMITS[3]:
            return False
        return True

    def is_calibrated(self):
        """ Returns whether this uarm is calibrated. """
        return self._calibrated

    def is_sucking(self):
        """ Returns whether the pump is turned on or not.
            @param bool - True if pump is on, else False
        """
        return self._pump_status

    def load_calibration(self, file_name):
        """ Loads the arm calibration from the given file.
            @param file_name - path to the file
            @return - False, if the calibration from file failed, else True
        """
        try:
            afile = open(file_name, 'r')
            file_content = yaml.load(afile)
            if type(file_content) is not dict:
                self.logger.error('The given file %s does not contain a dictionary of joint offsets' % file_name)
                return False
            elif len(file_content) < self.NUM_JOINTS:
                self._logger.error('The configuration file ' + file_name + ' needs to contain ' + str(self.NUM_JOINTS)
                              + ' joint offsets, but it contains only ' + str(len(file_content)))
                return False
            else:
                self._offsets = numpy.array(self.NUM_JOINTS * [0.0])
                for i in range(self.NUM_JOINTS):
                    if self.JOINT_NAMES[i] in file_content:
                        self._offsets[i] = file_content[self.JOINT_NAMES[i]]
                    else:
                        self._logger.error('The configuration file ' + file_name + ' is missing an offset '
                                      + ' for joint ' + self.JOINT_NAMES[i])
                        return False
                self._calibrated = True
                return self._calibrated
        except IOError as err:
            self._logger.error('Could not read configuration file ' + file_name)
            self._logger.error(str(err))
        return False

    def move_cartesian(self, x=None, y=None, z=None, theta=None, interpolation_type=None, duration=None,
                       check_limits=True):
        """ Moves the arm to the specified x,y,z end-effector position at orientation theta.
            Note that the arm needs to be calibrated for this!
            @param x - absolute x position (in cm), current x if None
            @param y - absolute y position (in cm), current y if None
            @param z - absolute z position (in cm), current z if None
            @param theta - absolute orientation (in degrees), ignored if None
            @param interpolation_type - Type of interpolation to use:
                                        None, Linear, Cubic (either string or None)
            @param duration - desired duration of movement in seconds
                              (if None, default value is used; only active if interpolation_type is not None)
            @param check_limits - if true, joint limit checks are performed
            @return True/False - True iff execution was attempted.
        """
        self._check_calibration()
        current_pos, current_theta = self.get_pose()
        if x is None:
            x = current_pos[0]
        if y is None:
            y = current_pos[1]
        if z is None:
            z = current_pos[2]
        goal_config = self.inverse_kinematics(x, y, z, theta, check_limits)
        if goal_config is None:
            self._logger.warn('The given position is not reachable, aborting move request.')
            return False
        return self.move(*goal_config, interpolation_type=interpolation_type,
                         duration=duration, check_limits=check_limits)

    def move_cartesian_relative(self, dx=0.0, dy=0.0, dz=0.0, dtheta=0.0, interpolation_type=None,
                                duration=None, check_limits=True):
        """ Moves the arm's end-effector relative to the current position.
            Note that the arm needs to be calibrated for this!
            @param dx - delta in x
            @param dy - delta in y
            @param dz - delta in z
            @param dtheta - delta in theta (if None, theta is ignored and only the position is considered)
            @param interpolation_type - Type of interpolation to use:
                                        None, Linear, Cubic (either string or None)
            @param duration - desired duration of movement in seconds
                              (if None, default value is used; only active if interpolation_type is not None)
            @param check_limits - if true, joint limit checks are performed
            @return True/False - True iff execution was attempted
        """
        self._check_calibration()
        current_pos, current_theta = self.get_pose()
        target_theta = current_theta + dtheta if dtheta is not None else None
        return self.move_cartesian(current_pos[0] + dx,
                                   current_pos[1] + dy,
                                   current_pos[2] + dz,
                                   target_theta,
                                   interpolation_type=interpolation_type,
                                   duration=duration,
                                   check_limits=check_limits)

    def move(self, j0, j1, j2, j3, interpolation_type=None, duration=None, check_limits=True):
        """ Moves the arm to the specified arm configuration.
            All joint angles are expected to be in degrees.
            Note that the arm needs to be calibrated for this!
            @param j0 - desired angle of joint 0
            @param j1 - desired angle of joint 1
            @param j2 - desired angle of joint 2
            @param j3 - desired angle of joint 3
            @param interpolation_type - Type of interpolation to use:
                                        None, Linear, Cubic (either string or None)
            @param duration - desired duration of movement in seconds
                              (if None, default value is used; only active if interpolation_type is not None)
            @param check_limits - if true, joint limit checks are performed
            @return True/False - True iff execution was attempted
        """
        self._check_calibration()
        if check_limits:
            if not self.in_joint_limits(j0, j1, j2, j3):
                return False
        # Do interpolation in the same way as they do it in the firmware
        start_values = self.get_configuration()
        target_values = [j0, j1, j2, j3]
        distances = map(lambda x, y: abs(x - y), target_values, start_values)
        # One interpolation step / degree of maximal changing joint or minimal num of steps
        num_steps = min(self.MAXIMAL_NUM_INTERPOLATION_STEPS, max(*distances))
        interpolation_steps = self._interpolate(start_values, target_values, num_steps, interpolation_type)
        # in case an interpolation method was chosen, interpolate:
        if interpolation_steps is not None:
            if duration is None:
                sleep_time = self.DEFAULT_EXECUTION_SLEEP_TIME
            else:
                sleep_time = duration / num_steps

            for i in range(len(interpolation_steps)):
                self._move_servos(interpolation_steps[i])
                time.sleep(sleep_time)
        else:
            # else just move the servos to the target
            self._move_servos(target_values)

        return True

    def move_relative(self, dj0=0.0, dj1=0.0, dj2=0.0, dj3=0.0, interpolation_type=None,
                      duration=None, check_limits=True):
        """ Moves the arm relative to the current configuration.
            Note that the arm needs to be calibrated for this!
            @param dj0 - delta in joint 0 angle
            @param dj1 - delta in joint 1 angle
            @param dj2 - delta in joint 2 angle
            @param dj3 - delta in joint 3 angle
            @param interpolation_type - Type of interpolation to use:
                                        None, Linear, Cubic (either string or None)
            @param duration - desired duration of movement in seconds
                              (if None, default value is used; only active if interpolation_type is not None)
            @param check_limits - if true, joint limit checks are performed
            @return True/False - True iff execution was attempted
        """
        self._check_calibration()
        current_config = self.get_configuration()
        return self.move(current_config[0] + dj0,
                         current_config[1] + dj1,
                         current_config[2] + dj2,
                         current_config[3] + dj3,
                         interpolation_type=interpolation_type,
                         duration=duration,
                         check_limits=check_limits)

    def pump(self, pump_status):
        """ Activates/Deactivates the pump.
            @param pump_state - True = pump on, False = pump off
        """
        self._check_connection()
        self._uarm.pump_control(pump_status)
        self._pump_status = pump_status


def recordJointValues(arm, timeout):
    joint_values = []
    start_time = time.time()
    while time.time() < start_time + timeout:
        joint_values.append(arm.get_configuration())
        time.sleep(0.02)
    return joint_values

if __name__ == '__main__':
    logging.basicConfig()
    import IPython
    uarm = KTHUarm('test_calibration.yaml')
    IPython.embed()
