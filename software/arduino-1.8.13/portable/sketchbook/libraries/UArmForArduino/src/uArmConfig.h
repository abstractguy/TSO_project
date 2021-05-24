/**
  ******************************************************************************
  * @file	uArmConfig.h
  * @author	David.Long
  * @email	xiaokun.long@ufactory.cc
  * @date	2016-09-28
  * @license GNU
  * copyright(c) 2016 UFactory Team. All right reserved
  * @modified	Samuel Duclos
  ******************************************************************************
  */

#ifndef _UARMCONFIG_H_
#define _UARMCONFIG_H_

#include <Arduino.h>

//#define UARM_FULL		// Use the full version of the library.
//#define DEBUG                 // Uncomment if you want to print debug info.

#define USE_SERIAL_CMD 1 // 1: use serial for control	0: just use arduino to control(release ROM and RAM space)

#define TICK_INTERVAL    50    // ms

#define HW_VER  "2.1"
#define SW_VER  "2.2.3"

#define DISABLE_SERVO_EASING
//#define SAVE_PINS
//#define DISABLE_SERVO_SPEED
//#define DISABLE_SERVO_INTERCEPT
//#define DISABLE_SERVO_SLOPE
//#define DISABLE_SERVO_OFFSET

#ifdef ARDUINO_ESP32_DEV
	#define DEVICE_NAME "ESP32Metal"
	#define DEVICE_ESP32
	#ifndef DISABLE_SERVO_SPEED
		#define DISABLE_SERVO_SPEED
	#endif
#elif defined(ARDUINO_ESP32S2_DEV)
	#define DEVICE_NAME "ESP32Metal"
	#define DEVICE_ESP32
	#ifndef DISABLE_SERVO_SPEED
		#define DISABLE_SERVO_SPEED
	#endif
#else
	#define DEVICE_NAME "Metal"
#endif

#ifdef DISABLE_SERVO_EASING
	#ifndef DISABLE_SERVO_SPEED
		#define DISABLE_SERVO_SPEED
	#endif
#endif

#ifdef SERVO_COUNT
	#undef SERVO_COUNT
#endif

#ifdef SAVE_PINS
	#define SERVO_COUNT 3
#else
	#define SERVO_COUNT 4
#endif

#endif // _UARMCONFIG_H_

