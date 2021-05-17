/**
  ******************************************************************************
  * @file	uArmController.cpp
  * @author	David.Long	
  * @email	xiaokun.long@ufactory.cc
  * @date	2016-09-28
  * @license GNU
  * copyright(c) 2016 UFactory Team. All right reserved
  ******************************************************************************
  */

#include "uArmController.h"

static void _sort(unsigned int array[], unsigned int len);

uArmController controller;

uArmController::uArmController() {}

void uArmController::init() {
	delay(50);

	mServo[SERVO_ROT_NUM].setPulseWidthRange(500, 2500);
	mServo[SERVO_LEFT_NUM].setPulseWidthRange(500, 2500);
	mServo[SERVO_RIGHT_NUM].setPulseWidthRange(500, 2500);
	mServo[SERVO_HAND_ROT_NUM].setPulseWidthRange(600, 2400);

	attachAllServo();  

	//writeServoAngle(SERVO_ROT_NUM, 90);
	//writeServoAngle(SERVO_LEFT_NUM, 90);
	//writeServoAngle(SERVO_RIGHT_NUM, 0);
	//writeServoAngle(SERVO_HAND_ROT_NUM, 90);
	mCurAngle[0] = readServoAngle(SERVO_ROT_NUM);
	mCurAngle[1] = readServoAngle(SERVO_LEFT_NUM);
	mCurAngle[2] = readServoAngle(SERVO_RIGHT_NUM);
	mCurAngle[3] = readServoAngle(SERVO_HAND_ROT_NUM);
}

void uArmController::attachAllServo() {
	for (int i = SERVO_ROT_NUM; i < SERVO_COUNT; i++) {
		mServo[i].attach(SERVO_CONTROL_PIN[i]);
	}
}

void uArmController::attachServo(byte servoNum) {
    mServo[servoNum].attach(SERVO_CONTROL_PIN[servoNum]);
}

void uArmController::detachServo(byte servoNum) {
	mServo[servoNum].detach();
}

void uArmController::detachAllServo() {
	for (int i = SERVO_ROT_NUM; i < SERVO_COUNT; i++) {
		detachServo(i);
	}
}

void uArmController::writeServoAngle(double servoRotAngle, double servoLeftAngle, double servoRightAngle) {
	writeServoAngle(SERVO_ROT_NUM, servoRotAngle);
	writeServoAngle(SERVO_LEFT_NUM, servoLeftAngle);
	writeServoAngle(SERVO_RIGHT_NUM, servoRightAngle);
}

double uArmController::getReverseServoAngle(byte servoNum, double servoAngle) {return servoAngle;}

void uArmController::writeServoAngle(byte servoNum, double servoAngle) {
	servoAngle = constrain(servoAngle, 0.00, 180.00);
	mServo[servoNum].write(servoAngle);
}

double uArmController::readServoAngle(byte servoNum) {
	double angle = (servoNum == SERVO_HAND_ROT_NUM) ? map(getServoAnalogData(SERVO_HAND_ROT_ANALOG_PIN), SERVO_9G_MIN, SERVO_9G_MAX, 0, 180) : getServoAnalogData(servoNum);
	angle = constrain(angle, 0.00, 180.00);
	return angle;
}

double uArmController::readServoAngles(double& servoRotAngle, double& servoLeftAngle, double& servoRightAngle) {
	servoRotAngle = readServoAngle(SERVO_ROT_NUM);
	servoLeftAngle = readServoAngle(SERVO_LEFT_NUM);
	servoRightAngle = readServoAngle(SERVO_RIGHT_NUM);
}

double uArmController::getServoAngles(double& servoRotAngle, double& servoLeftAngle, double& servoRightAngle) {
	servoRotAngle = mCurAngle[SERVO_ROT_NUM];
	servoLeftAngle = mCurAngle[SERVO_LEFT_NUM];
	servoRightAngle = mCurAngle[SERVO_RIGHT_NUM];
}

void uArmController::updateAllServoAngle() {
	for (unsigned char servoNum = SERVO_ROT_NUM; servoNum < SERVO_COUNT; servoNum++) {
		mCurAngle[servoNum] = readServoAngle(servoNum); 	
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
		if (x > 0) angleRot = atan(y / x) * MATH_TRANS; // Angle transfer 0-180 CCW.
		if (x < 0) angleRot = 180 + atan(y / x) * MATH_TRANS; // Angle transfer 0-180 CCW.
	}

	// Calculate value of theta 3
	if (angleRot != 90) xIn = (x / cos(angleRot / MATH_TRANS) - MATH_L2 - MATH_FRONT_HEADER) / MATH_LOWER_ARM; // xIn is the stretch
	else xIn = (y - MATH_L2 - MATH_FRONT_HEADER) / MATH_LOWER_ARM;

	phi = atan(zIn / xIn) * MATH_TRANS; // phi is the angle of line (from joint 2 to joint 4) with the horizon.

	sqrtZX = sqrt(zIn * zIn + xIn * xIn);

	rightAll = (sqrtZX * sqrtZX + MATH_UPPER_LOWER * MATH_UPPER_LOWER - 1) / (2 * MATH_UPPER_LOWER * sqrtZX); // Cosine law.
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
	else if ((angleLeft < LOWER_ARM_MIN_ANGLE) || (angleLeft > LOWER_ARM_MAX_ANGLE)) // Check the right in range.
		result = OUT_OF_RANGE;
	else if ((angleRight < UPPER_ARM_MIN_ANGLE) || (angleRight > UPPER_ARM_MAX_ANGLE)) // Check the left in range.
		result = OUT_OF_RANGE;
	else if (((180 - angleLeft - angleRight) > LOWER_UPPER_MAX_ANGLE) || ((180 - angleLeft - angleRight) < LOWER_UPPER_MIN_ANGLE)) // Check the angle of upper arm and lower arm in range.
		result = OUT_OF_RANGE;

	angleRot = constrain(angleRot, 0.00, 180.00);
	angleLeft = constrain(angleLeft, 0.00, 180.00);
	angleRight = constrain(angleRight, 0.00, 180.00);

	angleRot -= 90;
	angleLeft -= 90;
	angleRight -= 90;

	return result;
}

unsigned int uArmController::getServoAnalogData(byte servoNum) {
	return getAnalogPinValue(SERVO_ANALOG_PIN[servoNum]);
}

static void _sort(unsigned int array[], unsigned int len) {
	unsigned int temp = 0;
	unsigned char i = 0, j = 0;

	for (i = 0; i < len; i++) {
		for (j = 0; i + j < (len - 1); j++) {
			if (array[j] > array[j + 1]) {
				temp = array[j];
				array[j] = array[j + 1];
				array[j + 1] = temp;
			}
		}
	}	
}

/*!
   \brief get analog value of pin
   \param pin of arduino
   \return value of analog data
 */
int uArmController::getAnalogPinValue(unsigned int pin) {
	unsigned int dat[8], result;
	for (int i = 0; i < 8; i++) dat[i] = analogRead(pin);
	_sort(dat, 8);
	result = (dat[2] + dat[3] + dat[4] + dat[5]) / 4;
	return result;    
}

