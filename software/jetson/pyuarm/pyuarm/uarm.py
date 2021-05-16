from __future__ import print_function
import serial
from . import version, protocol, util
from .util import printf, ERROR, DEBUG, UArmConnectException, get_default_logger
from .tools.list_uarms import uarm_ports, get_port_property, check_port_plug_in
from . import PY3
import logging, time

class UArm(object):
    firmware_version = None
    hardware_version = None
    __isConnected = False

    X_MIN_RELATIVE = -316
    X_MAX_RELATIVE = 316
    Y_MIN_RELATIVE = -212
    Y_MAX_RELATIVE = 212
    Z_MIN_RELATIVE = -253
    Z_MAX_RELATIVE = 253

    def __init__(self, 
                 port_name=None, 
                 logger=None, 
                 debug=False, 
                 uarm_speed=100, 
                 servo_attach_delay=3, 
                 set_position_delay=3, 
                 servo_detach_delay=3, 
                 pump_delay=3):

        """
        :param port_name: UArm Serial Port name, if no port provide, will try first port we detect
        :param logger: if no logger provide, will create a logger by default
        :raise UArmConnectException

        UArm port is immediately opened on object creation, if no port provide, we will detect all connected uArm serial
        devices. please reference `pyuarm.tools.list_uarms`
        port is a device name: depending on operating system. eg. `/dev/ttyUSB0` on GNU/Linux or `COM3` on Windows.
        logger will display all info/debug/error/warning messages.
        """

        self.serial_id = 0
        self.uarm_speed = uarm_speed
        self.servo_attach_delay = servo_attach_delay
        self.set_position_delay = set_position_delay
        self.servo_detach_delay = servo_detach_delay
        self.pump_delay = pump_delay

        if logger is None:
            util.init_logger(util.get_default_logger(debug))

        else:
            util.init_logger(logger)

        if port_name is None:
            ports = uarm_ports()

            if len(ports) > 0:
                port_name = ports[0]

            else:
                raise UArmConnectException(0, "No uArm ports is found.")

        self.port = get_port_property(port_name)

        self.__serial = serial.Serial(baudrate=115200, timeout=.1)

        self.connect()

        self.set_servo_attach()

        self.get_initial_absolute_position()

        self.initialize()

    def disconnect(self):
        """
        disconnect will release/close the uarm port
        :return:
        """
        printf("Disconnect from port - {0}...".format(self.port.device))
        self.__serial.close()
        self.__isConnected = False
        self.checking_port_flag = False

    def connect(self):
        """
        This function will open the port immediately. Function will wait for the READY Message for 5 secs. Once received
        READY message, Function will send the Version search command.
        :return:
        """
        try:
            self.__serial.port = self.port.device
            printf("Connecting from port - {0}...".format(self.port.device))
            self.__serial.open()
            timeout_start = time.time()
            timeout = 7
            while time.time() < timeout_start + timeout:
                if self.is_ready():
                    break
            if not self.__isConnected:
                raise UArmConnectException(1, "{} message received timeout.".format(protocol.READY))
        except serial.SerialException as e:
            raise UArmConnectException(0, "port: {}, Error: {}".format(self.port.device, e.strerror))
        self.responseLog = []
        self.get_firmware_version()
        self.get_hardware_version()
        if version.is_a_version(self.firmware_version):
            printf("Firmware Version: {0}".format(self.firmware_version))
            if not version.is_supported_version(self.firmware_version):
                raise UArmConnectException(2,"Firmware Version: {}".format(self.firmware_version))
        else:
            raise UArmConnectException(1, "Firmware Version: {}".format(self.firmware_version))

    def is_connected(self):
        """
        is_connected will return the uarm connected status
        :return: connected status
        """
        try:
            if PY3:
                self.__gen_serial_id()
                cmnd = "#{} {}".format(self.serial_id, protocol.GET_FIRMWARE_VERSION)
                cmndString = bytes(cmnd + "\n", encoding='ascii')
                self.__serial.write(cmndString)
                response = str(self.__serial.readline(),encoding='ascii')
            else:
                self.__gen_serial_id()
                cmnd = "#{} {}".format(self.serial_id, protocol.GET_FIRMWARE_VERSION)
                cmndString = bytes(cmnd + "\n")
                self.__serial.write(cmndString)
                response = self.__serial.readline()
        except serial.serialutil.SerialException:
            self.__isConnected = False
        if self.__serial.isOpen() and self.__isConnected:
            return True
        else:
            return False

    def is_ready(self):
        if PY3:
            ready_msg = bytes(protocol.READY, encoding='ascii')
        else:
            ready_msg = protocol.READY
        if self.__serial.readline().startswith(ready_msg):
            printf("Connected...")
            self.__isConnected = True
            return True
        else:
            return False

    def __gen_serial_id(self):
        if self.serial_id == 999:
            self.serial_id = 0
        else:
            self.serial_id += 1

    def __gen_response_value(self, response):
        if response.startswith(protocol.OK.lower()):
            return response.rstrip().split(' ')[1:]
        else:
            return False

    def __send_and_receive(self, cmnd, timeout=None):
        """
        This command will send a command and receive the uArm response. There must always be a response!
        Responses should be recieved immediately after sending the command, after which the robot will proceed to
        perform the action.
        :param cmnd: a String command, to send to the robot
        :return: The robots response
        """

        if not self.is_connected():
            printf("Communication| Tried to send a command while robot was not connected!")
            return ""

        # Prepare and send the command to the robot.
        self.__gen_serial_id()
        cmnd = "#{} {}".format(self.serial_id,cmnd)
        # printf(cmnd, type=ERROR)
        if PY3:
            cmndString = bytes(cmnd + "\n", encoding='ascii')
        else:
            cmndString = bytes(cmnd + "\n")

        try:
            self.__serial.write(cmndString)

        except serial.serialutil.SerialException as e:
            printf("while sending command {}. Disconnecting Serial! \nError: {}".format(cmndString, str(e)),type=ERROR)
            self.__isConnected = False
            return ""

        try:
            if PY3:
                response = str(self.__serial.readline(),encoding='ascii')
            else:
                response = self.__serial.readline()
            if response.startswith("${}".format(self.serial_id)):
                if "E20" in response or "E21" in response:
                    printf("Communication| ERROR: send {}, received error from robot: {}".format(cmndString, response), type=ERROR)
                    return ""
                response = response.replace('\n', '')
                response = response.replace('${} '.format(self.serial_id),'')
                printf("Communication| [{}] {}{}".format(cmnd, " " * (30 - len(cmnd)), response), type=DEBUG)
            else:
                printf("Communication| ERROR: received error from robot: {}".format(response),type=ERROR)
                return ""
            return response.lower()
        except serial.serialutil.SerialException as e:
            printf("while sending command {}. Disconnecting Serial! \nError: {}".format(cmnd,str(e)), type=ERROR)
            self.__isConnected = False
            return ""

    def __parse_cmd(self, message, arguments):
        response_dict = {n: 0 for n in arguments}  # Fill the dictionary with zero's

        # Do error checking, in case communication didn't work
        if message is False:
            printf("UArm.__parse_cmd(): Since an error occurred in communication, returning 0's for all arguments!")
            return response_dict

        # Get the arguments and place them into the array
        for i, arg in enumerate(arguments):
            if i < len(arguments) - 1:
                response_dict[arg] = message[message.find(arg) + 1: message.find(arguments[i + 1])]
            else:
                response_dict[arg] = message[message.find(arg) + 1:]

            response_dict[arg] = float(response_dict[arg])

        return response_dict

# -------------------------------------------------------- Commands ----------------------------------------------------

    def get_firmware_version(self):
        """
        Get the firmware version.
        Protocol Cmd: `protocol.GET_FIRMWARE_VERSION`
        :return: firmware version, if failed return False
        """
        cmd = protocol.GET_FIRMWARE_VERSION
        response = self.__send_and_receive(cmd)

        value = self.__gen_response_value(response)
        if value:
            self.firmware_version = value[0][1:]
        else:
            return False

    def get_hardware_version(self):
        """
        Get the Product version.
        Protocol Cmd: `protocol.GET_HARDWARE_VERSION`
        :return: firmware version, if failed return False
        """
        cmd = protocol.GET_HARDWARE_VERSION
        response = self.__send_and_receive(cmd)

        value = self.__gen_response_value(response)
        if value:
            self.hardware_version = value[0][1:]
        else:
            return False

    def set_position(self, x, y, z, speed=300, relative=False):
        """
        Move uArm to the position (x,y,z) unit is mm, speed unit is mm/sec
        :param x:
        :param y:
        :param z:
        :param speed:
        :return:
        """
        x = str(round(x, 2))
        y = str(round(y, 2))
        z = str(round(z, 2))
        s = str(round(speed, 2))

        self.set_servo_attach() # Check if needed here.

        command = protocol.SET_POSITION.format(x, y, z, s)

        response = self.__send_and_receive(command)

        time.sleep(self.set_position_delay)

        self.set_servo_detach() # Check if needed here.

        return response.startswith(protocol.OK.lower())

    def set_relative_position_from_center_in_grad(self, 
                                                  x=0, 
                                                  y=0, 
                                                  z=0, 
                                                  speed=None, 
                                                  height=200.0, 
                                                  width=200.0):

        """Set relative position from center in grad."""

        speed = self.uarm_speed if speed is None else speed

        position = self.initial_position.copy()

        x = max(-100, x) if x < 0 else min(x, 100)
        y = max(-100, y) if y < 0 else min(y, 100)
        z = max(-100, z) if z < 0 else min(z, 100)

        x /= 100.0
        y /= 100.0
        z /= 100.0

        x *= self.X_MAX_RELATIVE
        y *= self.Y_MAX_RELATIVE
        z *= self.Z_MAX_RELATIVE

        position['x'] += x
        position['y'] += y
        position['z'] += z

        print('position:', position)
        self.set_position(**position)

    def drop(self, drop_position=None):
        self.set_position(position=drop_position)
        self.set_pump(ON=False)

    def grab(self, grab_position=None, condition=True):
        self.set_position(position=grab_position)
        if condition:
            self.set_pump(ON=True)
        return condition

    def set_weight_to_somewhere(self, grab_position=None, drop_position=None, sensor=True, detach=False):
        self.grab(grab_position=grab_position, condition=sensor)
        self.drop(drop_position=drop_position)
        self.reset(detach=detach)

    def set_pump(self, ON):
        """
        Control uArm Pump On or OFF
        :param ON: True On, False OFF
        :return: succeed True or Failed False
        """
        cmd = protocol.SET_PUMP.format(1 if ON else 0)
        response = self.__send_and_receive(cmd)
        time.sleep(self.pump_delay)
        self.set_servo_detach() # Check if needed here.
        return response.startswith(protocol.OK.lower())

    def set_servo_attach(self, servo_number=None):
        """
        Set Servo status attach, Servo Attach will lock the servo, You can't move uArm with your hands.
        :param servo_number: If None, will attach all servos, please reference protocol.py SERVO_BOTTOM, SERVO_LEFT, SERVO_RIGHT, SERVO_HAND
        :return: succeed True or Failed False
        """
        if servo_number is not None:
            cmd = protocol.ATTACH_SERVO.format(servo_number)
            response = self.__send_and_receive(cmd)
            if response.startswith(protocol.OK.lower()):
                time.sleep(self.servo_attach_delay) # Check if needed.
                return True
            else:
                return False
        else:
            if self.set_servo_attach(0) and self.set_servo_attach(1) \
                    and self.set_servo_attach(2) and self.set_servo_attach(3):
                time.sleep(self.servo_attach_delay)
                return True
            else:
                return False

    def set_servo_detach(self, servo_number=None):
        """
        Set Servo status detach, Servo Detach will unlock the servo, You can move uArm with your hands. But move function won't be effect until you attach.
        :param servo_number: If None, will detach all servos, please reference protocol.py SERVO_BOTTOM, SERVO_LEFT, SERVO_RIGHT, SERVO_HAND
        :return: succeed True or Failed False
        """
        if servo_number is not None:
            cmd = protocol.DETACH_SERVO.format(servo_number)
            response = self.__send_and_receive(cmd)
            if response.startswith(protocol.OK.lower()):
                time.sleep(self.servo_detach_delay) # Check if needed.
                return True
            else:
                return False
        else:
            if self.set_servo_detach(0) and self.set_servo_detach(1) \
                    and self.set_servo_detach(2) and self.set_servo_detach(3):
                time.sleep(self.servo_detach_delay)
                return True
            else:
                return False

    def get_position(self):
        """
        Get Current uArm position (x,y,z) mm
        :return: Returns an array of the format [x, y, z] of the robots current location
        """
        response = self.__send_and_receive(protocol.GET_COOR)
        value = self.__gen_response_value(response)
        if value:
            parse_cmd = self.__parse_cmd(response, ["x", "y", "z"])
            coordinate = [parse_cmd["x"], parse_cmd["y"], parse_cmd["z"]]
            return coordinate
        else:
            return False

    def get_initial_absolute_position(self):
        """Get initial absolute position."""
        initial_position = self.get_position()
        self.initial_position = {
            'x': initial_position[0], 
            'y': initial_position[1], 
            'z': initial_position[2], 
            'speed': self.uarm_speed, 
            'relative': False
        }

    def initialize(self):
        """Homes back to the initial position after disabling pump."""
        self.set_pump(ON=False)
        self.set_position(**self.initial_position)
        print('Initial position:', self.initial_position)

    def reset(self, detach=False):
        self.initialize()

        if detach:
            self.set_servo_detach()
            self.disconnect()

        print('uARM closed...')

