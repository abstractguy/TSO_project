#ifndef _UARM_H_
	#define _UARM_H_

	#include <Arduino.h>

	#ifdef ARDUINO_ESP32_DEV
		#include <ESP32Servo.h>
	#else
		#include <Servo.h>
	#endif

	#include "uArmConfig.h"
	#include "uArmTypes.h"
	#include "uArmPin.h"
	#include "uArmController.h"
	#include "uArmDebug.h"
	#include "uArmComm.h"
	#include "uArmAPI.h"
#endif // _UARM_H_

