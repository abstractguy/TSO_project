/**
  ******************************************************************************
  * @file	uArmAPI.cpp
  * @author	David.Long	
  * @email	xiaokun.long@ufactory.cc
  * @date	2016-11-28
  * @modified	Samuel Duclos (nomfullcreatif@gmail.com)
  ******************************************************************************
  */

#include "uArmAPI.h" 

static unsigned char _moveTo(double x, double y, double z);

void initHardware() {
	pinMode(PUMP_EN, OUTPUT);
	pinMode(GRIPPER, OUTPUT);
	pinMode(VALVE_EN, OUTPUT);
}

/*!
   \brief init components
 */
void uArmInit() {
	initHardware();
	controller.init();	
}

/*!
   \brief move to pos(x, y, z)
   \param x, y, z in mm
   \return IN_RANGE if everything is OK
   \return OUT_OF_RANGE_NO_SOLUTION if cannot reach
   \return OUT_OF_RANGE will move to the closest pos
   \return NO_NEED_TO_MOVE if it is already there
 */
unsigned char moveTo(double x, double y, double z) {
	unsigned char result = IN_RANGE;
	//debugPrint("moveTo: x=%f, y=%f, z=%f, speed=%f", x, y, z, 255);
	result = _moveTo(x, y, z);
	return result;
}

/*!
   \brief attach servo(0~3)
   \param servoNumber: SERVO_ROT_NUM, SERVO_LEFT_NUM, SERVO_RIGHT_NUM, SERVO_HAND_ROT_NUM
   \return true or false
 */
bool attachServo(unsigned char servoNumber) {
	if (servoNumber < SERVO_COUNT) {
		controller.attachServo(servoNumber);
		return true;
	}

	return false;
}

/*!
   \brief detach servo(0~3)
   \param servoNumber: SERVO_ROT_NUM, SERVO_LEFT_NUM, SERVO_RIGHT_NUM, SERVO_HAND_ROT_NUM
   \return true or false
 */
bool detachServo(unsigned char servoNumber) {
	if (servoNumber < SERVO_COUNT) {
		controller.detachServo(servoNumber);
		return true;
	}

	return false;	
}

/*!
   \brief set servo angle
   \param servoNumber(0~3)
   \param angle (0~180)
   \return OK if everything is OK
   \return ERR_SERVO_INDEX_EXCEED_LIMIT if servoNumber not in range(0~3)
   \return ERR_ANGLE_OUT_OF_RANGE if angle not in range(0~180)
 */
unsigned char setServoAngle(unsigned char servoNumber, double angle) {
	if (servoNumber >= SERVO_COUNT) return ERR_SERVO_INDEX_EXCEED_LIMIT;
	if (angle > 180 || angle < 0) return ERR_ANGLE_OUT_OF_RANGE;
	controller.writeServoAngle(servoNumber, angle);
	return OK;
}

/*!
   \brief get servo angle
   \param servoNumber(0~3)
   \return value of angle
   \return -1 if servoNumber not in range(0~3)
 */
double getServoAngle(unsigned char servoNumber) {
	if (servoNumber >= SERVO_COUNT)
		return -1;	

	return controller.readServoAngle(servoNumber);
}

/*!
   \brief pump working
 */
void pumpOn() {
    digitalWrite(PUMP_EN, HIGH); 
    digitalWrite(VALVE_EN, LOW);
}

/*!
   \brief pump stop
 */
void pumpOff() {
    digitalWrite(PUMP_EN, LOW); 
    digitalWrite(VALVE_EN, HIGH);
}

/*!
   \brief get current pos
   \output x, y, z(mm)
 */
void getCurrentXYZ(double& x, double& y, double& z) {
    controller.updateAllServoAngle();
    controller.getCurrentXYZ(x, y, z);	
}

/*!
   \brief get servo angles from pos(x, y, z)
   \param x, y, z(mm)
   \output angles of servo(0~180)
   \return IN_RANGE if everything is OK
   \return OUT_OF_RANGE_NO_SOLUTION if cannot reach
   \return OUT_OF_RANGE can move to the closest pos   
 */
unsigned char xyzToAngle(double x, double y, double z, double& angleRot, double& angleLeft, double& angleRight) {
	return controller.xyzToAngle(x, y, z, angleRot, angleLeft, angleRight);
}

static unsigned char _moveTo(double x, double y, double z) {
	double targetRot = 0, targetLeft = 0, targetRight = 0;
	unsigned char status = 0;
	status = controller.xyzToAngle(x, y, z, targetRot, targetLeft, targetRight);
	if (status == OUT_OF_RANGE_NO_SOLUTION) return OUT_OF_RANGE_NO_SOLUTION;
	controller.writeServoAngle(targetRot, targetLeft, targetRight);
	return IN_RANGE;
}

