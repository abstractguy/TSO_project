/**
  ******************************************************************************
  * @file	uArmController.h
  * @author	David.Long	
  * @email	xiaokun.long@ufactory.cc
  * @date	2016-09-28
  * @license GNU
  * copyright(c) 2016 UFactory Team. All right reserved
  ******************************************************************************
  */

#ifndef _UARMCONTROLLER_H_
#define _UARMCONTROLLER_H_

#include <Arduino.h>

#ifdef ARDUINO_ESP32_DEV
	#include <ESP32Servo.h>
#else
	#include <Servo.h>
#endif

#include "uArmConfig.h"
#include "uArmPin.h"
#include "uArmTypes.h"

#define DEFAULT_ANGLE			60

#define MATH_PI 			3.141592653589793238463
#define MATH_TRANS  		57.2958    
#define MATH_L1 			107.45	
#define MATH_L2 			21.17	
#define MATH_LOWER_ARM 		148.25	
#define MATH_UPPER_ARM 		160.2 	
#define MATH_FRONT_HEADER 	25.00 // The distance between wrist to the front point we use.
#define MATH_UPPER_LOWER 	MATH_UPPER_ARM/MATH_LOWER_ARM
#define MAX_Z				260 // Max height.
#define MIN_Z				(-120)

#define LOWER_ARM_MAX_ANGLE      120
#define LOWER_ARM_MIN_ANGLE      5
#define UPPER_ARM_MAX_ANGLE      120
#define UPPER_ARM_MIN_ANGLE      5
#define LOWER_UPPER_MAX_ANGLE    150
#define LOWER_UPPER_MIN_ANGLE    30

#define LINEAR_INTERCEPT_START_ADDRESS      70
#define LINEAR_SLOPE_START_ADDRESS          50
#define MANUAL_OFFSET_ADDRESS               30
#define OFFSET_STRETCH_START_ADDRESS        20
#define SERIAL_NUMBER_ADDRESS               100

/*
Servo 0 INTERCEPT: -30.45, SLOPE: 0.35, MANUAL: -18.76
Servo 1 INTERCEPT: -28.37, SLOPE: 0.34, MANUAL: 10.0
Servo 2 INTERCEPT: -29.6, SLOPE: 0.35, MANUAL: -20.0
Servo 3 INTERCEPT: -42.67, SLOPE: 0.47, MANUAL: 0.0
*/
#define SERVO_0_INTERCEPT -30.45
#define SERVO_0_SLOPE 0.35
#define SERVO_0_MANUAL  -18.76
#define SERVO_1_INTERCEPT -28.37
#define SERVO_1_SLOPE 0.34
#define SERVO_1_MANUAL 10.0
#define SERVO_2_INTERCEPT -29.6
#define SERVO_2_SLOPE 0.35
#define SERVO_2_MANUAL -20.0
#define SERVO_3_INTERCEPT -42.67
#define SERVO_3_SLOPE 0.47
#define SERVO_3_MANUAL 0.0

#define SERVO_9G_MAX    460
#define SERVO_9G_MIN    98

#define DATA_LENGTH  0x40
#define LEFT_SERVO_ADDRESS   0x0000
#define RIGHT_SERVO_ADDRESS  0x02D0
#define ROT_SERVO_ADDRESS    0x05A0

class uArmController {
public:
	uArmController();

	void init();

	void attachAllServo();
	void attachServo(byte servoNum);
	void detachServo(byte servoNum);
	void detachAllServo();

	double getReverseServoAngle(byte servoNum, double servoAngle);
	void writeServoAngle(double servoRotAngle, double servoLeftAngle, double servoRightAngle);
	void writeServoAngle(byte servoNum, double servoAngle, boolean writeWithOffset = true);
	double readServoAngle(byte servoNum, boolean withOffset = true);
	double readServoAngles(double& servoRotAngle, double& servoLeftAngle, double& servoRightAngle, boolean withOffset = true);	
	void updateAllServoAngle(boolean withOffset = true);

	double getServoAngles(double& servoRotAngle, double& servoLeftAngle, double& servoRightAngle);
	double getServeAngle(byte servoNum);

	unsigned char getCurrentXYZ(double& x, double& y, double& z);
	unsigned char getXYZFromAngle(double& x, double& y, double& z, double rot, double left, double right);

	unsigned char setServoSpeed(unsigned char speed);
	unsigned char setServoSpeed(byte servoNum, unsigned char speed);
	unsigned int getServoAnalogData(byte servoNum);
	unsigned char xyzToAngle(double x, double y, double z, double& angleRot, double& angleLeft, double& angleRight, boolean allowApproximate = true);
	unsigned char limitRange(double& angleRot, double& angleLeft, double& angleRight);
	double analogToAngle(byte servoNum, int inputAnalog);

protected:
	Servo mServo[SERVO_COUNT];

	unsigned char mServoSpeed = 255;
	double mCurAngle[SERVO_COUNT] = {90, 90, 0, 90};

	// Offset of assembling.
	double mServoAngleOffset[SERVO_COUNT];
	
	const byte SERVO_CONTROL_PIN[SERVO_COUNT] = {SERVO_ROT_PIN, SERVO_LEFT_PIN, SERVO_RIGHT_PIN, SERVO_HAND_ROT_PIN};
	const byte SERVO_ANALOG_PIN[SERVO_COUNT] = {SERVO_ROT_ANALOG_PIN, SERVO_LEFT_ANALOG_PIN, SERVO_RIGHT_ANALOG_PIN, SERVO_HAND_ROT_ANALOG_PIN};
};

extern uArmController controller;

#endif // _UARMCONTROLLER_H_

