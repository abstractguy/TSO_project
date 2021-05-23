//  @modified		Samuel Duclos

#ifndef _UARM_H_
	#define _UARM_H_

	#include <Arduino.h>

	#include "uArmConfig.h"
	#include "uArmTypes.h"
	#include "uArmPin.h"
	#include "uArmController.h"
	#include "uArmDebug.h"
	#include "uArmComm.h"
	#include "uArmAPI.h"

	#ifdef DEVICE_ESP32
		#include <ESP32Servo.h>
	#else
		#include <Servo.h>
	#endif

#endif // _UARM_H_

