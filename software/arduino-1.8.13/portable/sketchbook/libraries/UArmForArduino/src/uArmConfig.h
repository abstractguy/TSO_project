/**
  ******************************************************************************
  * @file	uArmConfig.h
  * @author	David.Long
  * @email	xiaokun.long@ufactory.cc
  * @date	2016-09-28
  * @modified	Samuel Duclos
  * @license GNU
  * copyright(c) 2016 UFactory Team. All right reserved
  ******************************************************************************
  */

#ifndef _UARMCONFIG_H_
#define _UARMCONFIG_H_

#include <Arduino.h>

//#define DEBUG                 // uncomment if you want to print debug info

#define HW_VER  "2.1"
#define SW_VER  "2.2.3"

#ifdef ARDUINO_ESP32_DEV
	#define DEVICE_NAME "ESP32Metal"
#else
	#define DEVICE_NAME "Metal"
#endif

#define TICK_INTERVAL    50    // ms

#endif // _UARMCONFIG_H_

