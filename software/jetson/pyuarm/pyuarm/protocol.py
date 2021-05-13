# parameters

## SERVO NUMBER INDEX
SERVO_BOTTOM = 0
SERVO_LEFT = 1
SERVO_RIGHT = 2
SERVO_HAND = 3

## OFFSET EEPROM ADDRESS
LINEAR_INTERCEPT_START_ADDRESS = 70
LINEAR_SLOPE_START_ADDRESS = 50
OFFSET_START_ADDRESS = 30
OFFSET_STRETCH_START_ADDRESS = 20

SERIAL_NUMBER_ADDRESS = 100

## PROTOCOL MESSAGE
READY                   = "@1"
OK                      = "OK"
SET_POSITION            = "G0 X{} Y{} Z{} F{}"
GET_FIRMWARE_VERSION    = "P203"
GET_HARDWARE_VERSION    = "P202"
SET_ANGLE               = "G202 N{} V{}"
STOP_MOVING             = "G203"
SET_PUMP                = "M231 V{}"
GET_PUMP                = "P231"
SET_GRIPPER             = "M232 V{}"
GET_GRIPPER             = "P232"
ATTACH_SERVO            = "M201 N{}"
DETACH_SERVO            = "M202 N{}"
GET_COOR                = "P220"
GET_ANGLE               = "P200"
GET_IS_MOVE             = "M200"
GET_ANALOG              = "P241 N{}"

