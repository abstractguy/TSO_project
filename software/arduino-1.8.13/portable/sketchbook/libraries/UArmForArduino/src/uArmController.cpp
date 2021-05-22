/**
  ******************************************************************************
  * @file	uArmController.cpp
  * @author	David.Long	
  * @email	xiaokun.long@ufactory.cc
  * @date	2016-09-28
  * @modified	Samuel Duclos
  * @license GNU
  * copyright(c) 2016 UFactory Team. All right reserved
  ******************************************************************************
  */

#include <assert.h>
#include "uArmController.h"
#include "uArmAPI.h"

uArmController controller;

uArmController::uArmController() {mServoSpeed = 255;}

void uArmController::init() {
	mServoAngleOffset[0] = SERVO_0_MANUAL;
	mServoAngleOffset[1] = SERVO_1_MANUAL;
	mServoAngleOffset[2] = SERVO_2_MANUAL;
	mServoAngleOffset[3] = SERVO_3_MANUAL;

	#ifdef ARDUINO_ESP32_DEV
		ESP32PWM::allocateTimer(0);		// Allocate one timer.
		ESP32PWM::allocateTimer(1);		// Allocate one timer.
		ESP32PWM::allocateTimer(2);		// Allocate one timer.
		ESP32PWM::allocateTimer(3);		// Allocate one timer.

		mServo[0].setPeriodHertz(50);		// Standard 50hz servo.
		mServo[1].setPeriodHertz(50);		// Standard 50hz servo.
		mServo[2].setPeriodHertz(50);		// Standard 50hz servo.
		mServo[3].setPeriodHertz(50);		// Standard 50hz servo.

		// TODO: merge <ESP32Servo.h> with <Servo.h>.
		mServo[SERVO_ROT_NUM].attach(SERVO_ROT_NUM, 500, 2500);
		mServo[SERVO_LEFT_NUM].attach(SERVO_LEFT_NUM, 500, 2500);
		mServo[SERVO_RIGHT_NUM].attach(SERVO_RIGHT_NUM, 500, 2500);
		mServo[SERVO_HAND_ROT_NUM].attach(SERVO_HAND_ROT_NUM, 600, 2400);
	#else
		mServo[SERVO_ROT_NUM].setPulseWidthRange(500, 2500);
		mServo[SERVO_LEFT_NUM].setPulseWidthRange(500, 2500);
		mServo[SERVO_RIGHT_NUM].setPulseWidthRange(500, 2500);
		mServo[SERVO_HAND_ROT_NUM].setPulseWidthRange(600, 2400);
	#endif

	attachAllServo();  

	mCurAngle[0] = readServoAngle(SERVO_ROT_NUM, true);
	mCurAngle[1] = readServoAngle(SERVO_LEFT_NUM, true);
	mCurAngle[2] = readServoAngle(SERVO_RIGHT_NUM, true);
	mCurAngle[3] = readServoAngle(SERVO_HAND_ROT_NUM, true);
}

void uArmController::attachAllServo() {
	for (int i = SERVO_ROT_NUM; i < SERVO_COUNT; i++) mServo[i].attach(SERVO_CONTROL_PIN[i]);
}

void uArmController::attachServo(byte servoNum) {
	mServo[servoNum].attach(SERVO_CONTROL_PIN[servoNum]);
}

void uArmController::detachServo(byte servoNum) {
	mServo[servoNum].detach();
}

void uArmController::detachAllServo() {
	for (int i = SERVO_ROT_NUM; i < SERVO_COUNT; i++) detachServo(i);
}

void uArmController::writeServoAngle(double servoRotAngle, double servoLeftAngle, double servoRightAngle) {
	writeServoAngle(SERVO_ROT_NUM, servoRotAngle);
	writeServoAngle(SERVO_LEFT_NUM, servoLeftAngle);
	writeServoAngle(SERVO_RIGHT_NUM, servoRightAngle);
}

double uArmController::getReverseServoAngle(byte servoNum, double servoAngle) {return servoAngle;}

void uArmController::writeServoAngle(byte servoNum, double servoAngle, boolean writeWithOffset) {
	servoAngle = constrain(servoAngle, 0.00, 180.00);

	mCurAngle[servoNum] = servoAngle;
	servoAngle = writeWithOffset ? (servoAngle + mServoAngleOffset[servoNum]) : servoAngle;

	mServo[servoNum].write(servoAngle, mServoSpeed);
}

double uArmController::readServoAngle(byte servoNum, boolean withOffset) {
	double angle;

	if (servoNum == SERVO_HAND_ROT_NUM) angle = map(getServoAnalogData(SERVO_HAND_ROT_ANALOG_PIN), SERVO_9G_MIN, SERVO_9G_MAX, 0, 180);
	else angle = analogToAngle(servoNum, getServoAnalogData(servoNum));

	if (withOffset) angle -= mServoAngleOffset[servoNum];

	angle = constrain(angle, 0.00, 180.00);

	return angle;
}

double uArmController::readServoAngles(double& servoRotAngle, double& servoLeftAngle, double& servoRightAngle, boolean withOffset) {
	servoRotAngle = readServoAngle(SERVO_ROT_NUM, withOffset);
	servoLeftAngle = readServoAngle(SERVO_LEFT_NUM, withOffset);
	servoRightAngle = readServoAngle(SERVO_RIGHT_NUM, withOffset);
}

double uArmController::getServoAngles(double& servoRotAngle, double& servoLeftAngle, double& servoRightAngle) {
	servoRotAngle = mCurAngle[SERVO_ROT_NUM];
	servoLeftAngle = mCurAngle[SERVO_LEFT_NUM];
	servoRightAngle = mCurAngle[SERVO_RIGHT_NUM];
}

double uArmController::getServeAngle(byte servoNum) {
	return mCurAngle[servoNum];
}

void uArmController::updateAllServoAngle(boolean withOffset) {
	for (unsigned char servoNum = SERVO_ROT_NUM; servoNum < SERVO_COUNT; servoNum++) {
		mCurAngle[servoNum] = readServoAngle(servoNum, withOffset); 	
	}
}

unsigned char uArmController::getCurrentXYZ(double& x, double& y, double& z) {
	double stretch = MATH_LOWER_ARM * cos(mCurAngle[SERVO_LEFT_NUM] / MATH_TRANS) + MATH_UPPER_ARM * cos(mCurAngle[SERVO_RIGHT_NUM] / MATH_TRANS) + MATH_L2 + MATH_FRONT_HEADER;
	double height = MATH_LOWER_ARM * sin(mCurAngle[SERVO_LEFT_NUM] / MATH_TRANS) - MATH_UPPER_ARM * sin(mCurAngle[SERVO_RIGHT_NUM] / MATH_TRANS) + MATH_L1;

	x = stretch * cos(mCurAngle[SERVO_ROT_NUM] / MATH_TRANS);
	y = stretch * sin(mCurAngle[SERVO_ROT_NUM] / MATH_TRANS);
	z = height;

	return IN_RANGE;
}

unsigned char uArmController::getXYZFromAngle(double& x, double& y, double& z, double rot, double left, double right) {
	double stretch = MATH_LOWER_ARM * cos(left / MATH_TRANS) + MATH_UPPER_ARM * cos(right / MATH_TRANS) + MATH_L2 + MATH_FRONT_HEADER;
	double height = MATH_LOWER_ARM * sin(left / MATH_TRANS) - MATH_UPPER_ARM * sin(right / MATH_TRANS) + MATH_L1;

	x = stretch * cos(rot / MATH_TRANS);
	y = stretch * sin(rot / MATH_TRANS);
	z = height;

	return IN_RANGE;    
}

unsigned char uArmController::xyzToAngle(double x, double y, double z, double& angleRot, double& angleLeft, double& angleRight, boolean allowApproximate) {
	double xIn = 0.0;
	double zIn = 0.0;
	double rightAll = 0.0;
	double sqrtZX = 0.0;
	double phi = 0.0;

	x = constrain(x, -3276, 3276);
	y = constrain(y, -3276, 3276);
	z = constrain(z, -3276, 3276);

	x = (double)((int)(x * 10) / 10.0);
	y = (double)((int)(y * 10) / 10.0);
	z = (double)((int)(z * 10) / 10.0);

	if (z > MAX_Z || z < MIN_Z) return OUT_OF_RANGE_NO_SOLUTION;

	zIn = (z - MATH_L1) / MATH_LOWER_ARM;

	if (!allowApproximate) { // If need the move to closest point we have to jump over the return function.
		if (y < 0) return OUT_OF_RANGE_NO_SOLUTION; // Check the range of x.
	}

	// Calculate value of theta 1: the rotation angle.
	if (x == 0) angleRot = 90;
	else {
		if (x > 0) angleRot = atan(y / x) * MATH_TRANS; // Angle tranfer 0-180 CCW.
		if (x < 0) angleRot = 180 + atan(y / x) * MATH_TRANS; // Angle tranfer  0-180 CCW.
	}

	// Calculate value of theta 3.
	if (angleRot != 90) // xIn is the stretch.
		xIn = (x / cos(angleRot / MATH_TRANS) - MATH_L2 - MATH_FRONT_HEADER) / MATH_LOWER_ARM;
	else xIn = (y - MATH_L2 - MATH_FRONT_HEADER) / MATH_LOWER_ARM;

	phi = atan(zIn / xIn) * MATH_TRANS; // phi is the angle of line (from joint 2 to joint 4) with the horizon.

	sqrtZX = sqrt(zIn * zIn + xIn * xIn);

	rightAll = (sqrtZX * sqrtZX + MATH_UPPER_LOWER * MATH_UPPER_LOWER  - 1) / (2 * MATH_UPPER_LOWER  * sqrtZX); // Cosine law.
	angleRight = acos(rightAll) * MATH_TRANS; // Cosine law.

	// Calculate value of theta 2.
	rightAll = (sqrtZX * sqrtZX + 1 - MATH_UPPER_LOWER * MATH_UPPER_LOWER ) / (2 * sqrtZX); // Cosine law.
	angleLeft = acos(rightAll) * MATH_TRANS; // Cosine law.

	angleLeft = angleLeft + phi;
	angleRight = angleRight - phi;

	// Determine if the angle can be reached.
	return limitRange(angleRot, angleLeft, angleRight);
}

unsigned char uArmController::limitRange(double& angleRot, double& angleLeft, double& angleRight) {
	unsigned char result = IN_RANGE;

	// Determine if the angle can be reached.
	if (isnan(angleRot) || isnan(angleLeft) || isnan(angleRight)) result = OUT_OF_RANGE_NO_SOLUTION;
	else if (((angleLeft + mServoAngleOffset[SERVO_LEFT_NUM]) < LOWER_ARM_MIN_ANGLE) || ((angleLeft + mServoAngleOffset[SERVO_LEFT_NUM]) > LOWER_ARM_MAX_ANGLE)) // Check the right in range.
		result = OUT_OF_RANGE;
	else if (((angleRight + mServoAngleOffset[SERVO_RIGHT_NUM]) < UPPER_ARM_MIN_ANGLE) || ((angleRight + mServoAngleOffset[SERVO_RIGHT_NUM]) > UPPER_ARM_MAX_ANGLE)) // Check the left in range.
		result = OUT_OF_RANGE;
	else if (((180 - angleLeft - angleRight) > LOWER_UPPER_MAX_ANGLE) || ((180 - angleLeft - angleRight) < LOWER_UPPER_MIN_ANGLE)) // Check the angle of upper arm and lowe arm in range.
		result = OUT_OF_RANGE;

	angleRot = constrain(angleRot, 0.00, 180.00);
	angleLeft = constrain(angleLeft, 0.00, 180.00);
	angleRight = constrain(angleRight, 0.00, 180.00);

	return result;
}

double uArmController::analogToAngle(byte servoNum, int inputAnalog) {
	double intercept = 0.0f;
	double slope = 0.0f;

	switch (servoNum) {
		case 0:
			intercept = SERVO_0_INTERCEPT;
			slope = SERVO_0_SLOPE;
			break;

		case 1:
			intercept = SERVO_1_INTERCEPT;
			slope = SERVO_1_SLOPE;
			break;

		case 2:
			intercept = SERVO_2_INTERCEPT;
			slope = SERVO_2_SLOPE;
			break;

		case 3:
			intercept = SERVO_3_INTERCEPT;
			slope = SERVO_3_SLOPE;
			break;

		default:
			assert(0);
			break;
	}

	double angle = intercept + slope * inputAnalog;  

	return angle;
}

unsigned int uArmController::getServoAnalogData(byte servoNum) {
	return getAnalogPinValue(SERVO_ANALOG_PIN[servoNum]);
}

unsigned char uArmController::setServoSpeed(byte servoNum, unsigned char speed) {
	mServoSpeed = speed;
}

unsigned char uArmController::setServoSpeed(unsigned char speed) {
	setServoSpeed(SERVO_ROT_NUM, speed);
	setServoSpeed(SERVO_LEFT_NUM, speed);
	setServoSpeed(SERVO_RIGHT_NUM, speed);
	//setServoSpeed(SERVO_HAND_ROT_NUM, true);
}

