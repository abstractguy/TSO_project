/**
  ******************************************************************************
  * @file	uArmController.h
  * @author	David.Long	
  * @email	xiaokun.long@ufactory.cc
  * @date	2016-09-28
  * @license	GNU
  * @modified	Samuel Duclos (nomfullcreatif@gmail.com)
  * copyright(c) 2016 UFactory Team. All right reserved
  ******************************************************************************
  */

#ifndef _UARMCONTROLLER_H_
#define _UARMCONTROLLER_H_

#include <Arduino.h>
#include <EEPROM.h>
#include "UFServo.h"
#include "uArmConfig.h"
#include "uArmPin.h"
#include "uArmTypes.h"

#define DEFAULT_ANGLE			60

#if defined(METAL)
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
#endif

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

#define SERVO_9G_MAX    460
#define SERVO_9G_MIN    98

#define DATA_LENGTH  0x40
#define LEFT_SERVO_ADDRESS   0x0000
#define RIGHT_SERVO_ADDRESS  0x02D0
#define ROT_SERVO_ADDRESS    0x05A0

#define SERVO_ROT_PIN           11
#define SERVO_LEFT_PIN          13
#define SERVO_RIGHT_PIN         12
#define SERVO_HAND_ROT_PIN      10

#define SERVO_ROT_ANALOG_PIN 		2
#define SERVO_LEFT_ANALOG_PIN 		0
#define SERVO_RIGHT_ANALOG_PIN 		1
#define SERVO_HAND_ROT_ANALOG_PIN 	3

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
	void writeServoAngle(byte servoNum, double servoAngle);
	double readServoAngle(byte servoNum);
	double readServoAngles(double& servoRotAngle, double& servoLeftAngle, double& servoRightAngle);	
	void updateAllServoAngle();

	double getServoAngles(double& servoRotAngle, double& servoLeftAngle, double& servoRightAngle);

	unsigned char getCurrentXYZ(double& x, double& y, double& z);

	unsigned int getServoAnalogData(byte servoNum);
	unsigned char xyzToAngle(double x, double y, double z, double& angleRot, double& angleLeft, double& angleRight, boolean allowApproximate = true);
	unsigned char limitRange(double& angleRot, double& angleLeft, double& angleRight);

	/*!
	   \brief get pin value
	   \param pin of arduino
	   \return HIGH or LOW
	 */
	int getDigitalPinValue(unsigned int pin);

	/*!
	   \brief set pin value
	   \param pin of arduino
	   \param value: HIGH or LOW
	 */
	void setDigitalPinValue(unsigned int pin, unsigned char value);

	/*!
		\brief get analog value of pin
		\param pin of arduino
		\return value of analog data
	 */
	int getAnalogPinValue(unsigned int pin);

protected:
	Servo mServo[SERVO_COUNT];

	double mCurAngle[SERVO_COUNT] = {90, 90, 0, 90};

	// Offset of assembling.
	const byte SERVO_CONTROL_PIN[SERVO_COUNT] = {SERVO_ROT_PIN, SERVO_LEFT_PIN, SERVO_RIGHT_PIN, SERVO_HAND_ROT_PIN};
	const byte SERVO_ANALOG_PIN[SERVO_COUNT] = {SERVO_ROT_ANALOG_PIN, SERVO_LEFT_ANALOG_PIN, SERVO_RIGHT_ANALOG_PIN, SERVO_HAND_ROT_ANALOG_PIN};

private:
	void sort(unsigned int array[], unsigned int len);
};

extern uArmController controller;

#endif // _UARMCONTROLLER_H_

