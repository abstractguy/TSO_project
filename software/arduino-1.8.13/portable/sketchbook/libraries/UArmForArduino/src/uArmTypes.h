/**
  ******************************************************************************
  * @file	uArmTypes.h
  * @author	David.Long	
  * @email	xiaokun.long@ufactory.cc
  * @date	2016-12-12
  * @modified	Samuel Duclos
  ******************************************************************************
  */

#ifndef _UARMTYPES_H_
#define _UARMTYPES_H_

// Gripper or pump status.
#define STOP            		0
#define WORKING          		1
#define GRABBING        		2

// Return values.
#define OK				0
#define IN_RANGE             		1
#define OUT_OF_RANGE_NO_SOLUTION 	2
#define OUT_OF_RANGE         		3
#define NO_NEED_TO_MOVE			4

#define ERR_SERVO_INDEX_EXCEED_LIMIT	5
#define ERR_ANGLE_OUT_OF_RANGE		6

// Servo define.
#define SERVO_ROT_NUM           	0
#define SERVO_LEFT_NUM          	1
#define SERVO_RIGHT_NUM         	2
#define SERVO_HAND_ROT_NUM      	3

#ifndef SERVO_COUNT
	#define SERVO_COUNT		4
#endif

#endif // _UARMTYPES_H_

