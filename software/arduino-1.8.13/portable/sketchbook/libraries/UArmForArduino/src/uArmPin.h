/**
  ******************************************************************************
  * @file	uArmPin.h
  * @author	David.Long	
  * @email	xiaokun.long@ufactory.cc
  * @date	2016-10-17
  ******************************************************************************
  */

#ifndef _UARMPIN_H_
#define _UARMPIN_H_

#include "uArmConfig.h"

#elif defined(ARDUINO_ESP32_DEV)

	// Possible PWM GPIO pins on the ESP32: 0 (used by on-board button), 2, 4, 5 (used by on-board LED), 12-19, 21-23, 25-27 and 32-33.
	#define SERVO_ROT_PIN           25
	#define SERVO_LEFT_PIN          27
	#define SERVO_RIGHT_PIN         26
	#define SERVO_HAND_ROT_PIN      22

	// Possible ADC pins on the ESP32: 0, 2, 4, 12-15, 32-39; 34-39 are recommended for analog input.
	#define SERVO_ROT_ANALOG_PIN 		34
	#define SERVO_LEFT_ANALOG_PIN 		32
	#define SERVO_RIGHT_ANALOG_PIN 		33
	#define SERVO_HAND_ROT_ANALOG_PIN 	35

	#define PUMP_EN                 SERVO_HAND_ROT_PIN	// HIGH = Valve OPEN
	#define VALVE_EN                NIL			// HIGH = Pump ON, so plugged to VCC
	#define GRIPPER                 NIL			// LOW = Catch
	#define GRIPPER_FEEDBACK        NIL

	// This is the default ADC max value on the ESP32 (12 bit ADC width).
	// This width can be set (in low-level oode) from 9-12 bits, for a range of values between 512 and 4096 extremums.
	#define ADC_MAX 4096
#else
	#define SERVO_ROT_PIN           11
	#define SERVO_LEFT_PIN          13
	#define SERVO_RIGHT_PIN         12
	#define SERVO_HAND_ROT_PIN      10

	#define SERVO_ROT_ANALOG_PIN 		2
	#define SERVO_LEFT_ANALOG_PIN 		0
	#define SERVO_RIGHT_ANALOG_PIN 		1
	#define SERVO_HAND_ROT_ANALOG_PIN 	3

	#define PUMP_EN                 6    // HIGH = Valve OPEN
	#define VALVE_EN                5    // HIGH = Pump ON
	#define GRIPPER                 9    // LOW = Catch
	#define GRIPPER_FEEDBACK        A6
#endif

#endif // _UARMPIN_H_

