/**
  ******************************************************************************
  * @file	uArmPin.h
  * @author	David.Long	
  * @email	xiaokun.long@ufactory.cc
  * @date	2016-10-17
  * @modified	Samuel Duclos (nomfullcreatif@gmail.com)
  ******************************************************************************
  */

#ifndef _UARMPIN_H_
#define _UARMPIN_H_

#include "uArmConfig.h"

#elif defined(METAL)
	#define PUMP_EN                 6    // HIGH = Valve OPEN
	#define VALVE_EN                5    // HIGH = Pump ON
	#define GRIPPER                 9    // LOW = Catch
	#define GRIPPER_FEEDBACK        A6
#endif // _UARMPIN_H_

