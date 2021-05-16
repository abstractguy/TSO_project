/**
  ******************************************************************************
  * @file	uArmConfig.h
  * @author	David.Long
  * @email	xiaokun.long@ufactory.cc
  * @date	2016-09-28
  * @modified	Samuel Duclos (nomfullcreatif@gmail.com)
  * @license GNU
  * copyright(c) 2016 UFactory Team. All right reserved
  ******************************************************************************
  */

#ifndef _UARMCONFIG_H_
#define _UARMCONFIG_H_

#include <Arduino.h>

#define METAL

#define TICK_INTERVAL    50

//#define DEBUG                 // uncomment if you want to print debug info
#define DebugSerial   Serial    // usr serial0 as debug port

#if defined(METAL)
	#define HW_VER  "2.1"
	#define SW_VER  "2.2.3"
#else
	#error "NO machine model defined(METAL, MKII)"
#endif

#ifdef METAL
    #define DEVICE_NAME "Metal"
#else
    #define DEVICE_NAME "UNKNOWN"
#endif

#endif // _UARMCONFIG_H_

