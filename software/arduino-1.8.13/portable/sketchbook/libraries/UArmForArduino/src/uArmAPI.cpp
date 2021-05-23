/**
  ******************************************************************************
  * @file	uArmAPI.cpp
  * @author	David.LonG
  * @email	xiaokun.long@ufactory.cc
  * @date	2016-11-28
  * @modified		Samuel Duclos
  ******************************************************************************
  */

#include "uArmAPI.h" 

#ifdef DEBUG 
#define STEP_MAX	30		// Not enough ram for debug, so reduce the size to enable debug.
#else
#define STEP_MAX	60
#endif

#define INTERP_EASE_INOUT_CUBIC 0	// Original cubic ease in/out.
#define INTERP_LINEAR           1
#define INTERP_EASE_INOUT       2	// Quadratic easing methods.
#define INTERP_EASE_IN          3
#define INTERP_EASE_OUT         4

#define STEP_MAX_TIME		20	// ms.

#define PUMP_GRABBING_CURRENT 	55    

static int mCurStep;
static int mTotalSteps;
static unsigned int mTimePerStep;
static unsigned long mStartTime;
static double mPathX[STEP_MAX];
static double mPathY[STEP_MAX];
static double mPathZ[STEP_MAX];

static unsigned char _moveTo(double x, double y, double z, double speed);
static void _sort(unsigned int array[], unsigned int len);
static void _controllerRun();

void initHardware() {
	pinMode(PUMP_EN, OUTPUT);
	#ifndef DEVICE_ESP32
		pinMode(GRIPPER, OUTPUT);
		pinMode(VALVE_EN, OUTPUT);
	#endif
}

/*!
   \brief init components
 */
void uArmInit() {
	initHardware();
	controller.init();

	mCurStep = -1;
	mTotalSteps = -1; 	
}

/*!
   \brief move to pos(x, y, z)
   \param x, y, z in mm
   \param speed: 
   			[0]: move to destination directly
   			[1~99]: change the dutycycle of servo (1~99%)
   			[100~1000]: mm/min, will do interpolation to control the speed and block process util move done
   \return IN_RANGE if everything is OK
   \return OUT_OF_RANGE_NO_SOLUTION if cannot reach
   \return OUT_OF_RANGE will move to the closest pos
   \return NO_NEED_TO_MOVE if it is already there
 */
unsigned char moveTo(double x, double y, double z, double speed) {
	unsigned char result = IN_RANGE;

	#ifdef DISABLE_SERVO_SPEED
		speed = 255;
	#endif

	debugPrint("moveTo: x=%f, y=%f, z=%f, speed=%f", x, y, z, speed);

	// When speed less than 100 mm/min, move to destination directly.
	if (speed < 0) return OUT_OF_RANGE_NO_SOLUTION;
	else if (speed < 100) {
		unsigned char dutyCycle = map(speed, 0, 99, 0, 255);   
		
		controller.setServoSpeed(dutyCycle);

		double angleB, angleL, angleR;
		result = controller.xyzToAngle(x, y, z, angleB, angleL, angleR);
		if (result != OUT_OF_RANGE_NO_SOLUTION) controller.writeServoAngle(angleB, angleL, angleR);

		return result;		
	} else {
		controller.setServoSpeed(255);
		result = _moveTo(x, y, z, speed);

		if (result != OUT_OF_RANGE_NO_SOLUTION) _controllerRun();

		return result;
	}
}

/*!
   \brief move to pos(x, y, z) according to current pos
   \param x, y, z (mm)
   \param speed (mm/min)
   \return IN_RANGE if everything is OK
   \return OUT_OF_RANGE_NO_SOLUTION if cannot reach
   \return OUT_OF_RANGE will move to the closest pos
   \return NO_NEED_TO_MOVE if it is already there
 */
unsigned char relativeMove(double x, double y, double z, double speed) {
	double x1, y1, z1;

	#ifdef DISABLE_SERVO_SPEED
		speed = 255;
	#endif

	// Get current xyz.
	controller.getCurrentXYZ(x1, y1, z1);

	x1 += x;
	y1 += y;
	z1 += z;

	return moveTo(x1, y1, z1, speed);	
}

/*!
   \brief move to pos of polor coordinates(s, r, h)
   \param s: stretch(mm)
   \param r: angle (0~180)
   \param h: height(mm)
   \param speed (mm/min)
   \return IN_RANGE if everything is OK
   \return OUT_OF_RANGE_NO_SOLUTION if cannot reach
   \return OUT_OF_RANGE will move to the closest pos
   \return NO_NEED_TO_MOVE if it is already there
 */
unsigned char moveToPol(double s, double r, double h, double speed) {
	double x, y, z;

	#ifdef DISABLE_SERVO_SPEED
		speed = 255;
	#endif

	polToXYZ(s, r, h, x, y, z);
	return moveTo(x, y, z, speed);		
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
	if (servoNumber >= SERVO_COUNT)
		return ERR_SERVO_INDEX_EXCEED_LIMIT;

	if (angle > 180 || angle < 0)
		return ERR_ANGLE_OUT_OF_RANGE;

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
   \brief gripper work
 */
void gripperCatch() {
	#ifndef DEVICE_ESP32
		digitalWrite(GRIPPER, LOW);
	#endif
}

/*!
   \brief gripper stop
 */
void gripperRelease() {
	#ifndef DEVICE_ESP32
	 	digitalWrite(GRIPPER, HIGH);
	#endif
}

/*!
   \brief get gripper status
   \return STOP if gripper is not working
   \return WORKING if gripper is working but not catched sth
   \return GRABBING if gripper got sth   
 */
unsigned char getGripperStatus() {
	#ifdef DEVICE_ESP32
		return STOP;
	#else
		if (digitalRead(GRIPPER) == HIGH) return STOP;
		else {
			if (getAnalogPinValue(GRIPPER_FEEDBACK) > 600) return WORKING;
			else return GRABBING;
		}
	#endif
}

/*!
   \brief get pump status
   \return STOP if pump is not working
   \return WORKING if pump is working but not catched sth
   \return GRABBING if pump got sth   
 */
unsigned char getPumpStatus() {
	if (digitalRead(PUMP_EN) == HIGH) return 1;
	else return 0;
}

/*!
   \brief pump working
 */
void pumpOn() {
	digitalWrite(PUMP_EN, HIGH);
	#ifndef DEVICE_ESP32
		digitalWrite(VALVE_EN, LOW);
	#endif
}

/*!
   \brief pump stop
 */
void pumpOff() {
	digitalWrite(PUMP_EN, LOW); 
	#ifndef DEVICE_ESP32
		digitalWrite(VALVE_EN, HIGH);
	#endif
}

/*!
   \brief get pin value
   \param pin of arduino
   \return HIGH or LOW
 */
int getDigitalPinValue(unsigned int pin) {
	return digitalRead(pin);
}

/*!
   \brief set pin value
   \param pin of arduino
   \param value: HIGH or LOW
 */
void setDigitalPinValue(unsigned int pin, unsigned char value) {
	if (value) digitalWrite(pin, HIGH);
	else digitalWrite(pin, LOW);
}

/*!
   \brief get analog value of pin
   \param pin of arduino
   \return value of analog data
 */
int getAnalogPinValue(unsigned int pin) {
    unsigned int dat[8];

    for (int i = 0; i < 8; i++) {
        dat[i] = analogRead(pin);
        #ifdef DEVICE_ESP32
            dat[i] = map(dat[i], 0, ADC_MAX, 0, 180);
        #endif
    }

    _sort(dat, 8);

    unsigned int result = (dat[2] + dat[3] + dat[4] + dat[5]) / 4;

    return result;    
}

/*!
   \brief convert polor coordinates to Cartesian coordinate
   \param s(mm), r(0~180), h(mm)
   \output x, y, z(mm)
 */
void polToXYZ(double s, double r, double h, double& x, double& y, double& z) {
    z = h;  
    x = s * cos(r / MATH_TRANS);
    y = s * sin(r / MATH_TRANS);	
}

/*!
   \brief check pos reachable
   \return IN_RANGE if everything is OK
   \return OUT_OF_RANGE_NO_SOLUTION if cannot reach
   \return OUT_OF_RANGE can move to the closest pos
 */
unsigned char validatePos(double x, double y, double z) {
	double angleRot, angleLeft, angleRight;
	return controller.xyzToAngle(x, y, z, angleRot, angleLeft, angleRight, false);
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
   \brief get current pos of polor coordinates
   \output s(mm), r(0~180), h(mm)
 */
void getCurrentPosPol(double& s, double& r, double& h) {
	double angleRot, angleLeft, angleRight;
	double x, y, z;

	controller.updateAllServoAngle();
	controller.getCurrentXYZ(x, y, z);
	controller.getServoAngles(angleRot, angleLeft, angleRight);

	double stretch;
	stretch = sqrt(x * x + y * y);

	s = stretch;
	r = angleRot;
	h = z;
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

/*!
   \brief get  pos(x, y, z) from servo angles  
   \param angles of servo(0~180)
   \output x, y, z(mm)
   \return IN_RANGE if everything is OK
   \return OUT_OF_RANGE_NO_SOLUTION if cannot reach
   \return OUT_OF_RANGE can move to the closest pos   
 */
unsigned char angleToXYZ(double angleRot, double angleLeft, double angleRight, double& x, double& y, double& z) {
	return controller.getXYZFromAngle(x, y, z, angleRot, angleLeft, angleRight);
}

////////////////////////////////////////////////////////////////////////////
// private functions

static void _sort(unsigned int array[], unsigned int len) {
	unsigned int temp = 0;
	unsigned char i = 0, j = 0;

	for(i = 0; i < len; i++) {
		for(j = 0; i+j < (len-1); j++) {
			if(array[j] > array[j+1]) {
				temp = array[j];
				array[j] = array[j+1];
				array[j+1] = temp;
			}
		}
	}	
}

static void _interpolate(double startVal, double endVal, double *interpVals, int steps, byte easeType) {
    startVal = startVal / 10.0;
    endVal = endVal / 10.0;

    double delta = endVal - startVal;
    for (byte i = 1; i <= steps; i++) {
        float t = (float)i / steps;
        //*(interp_vals+f) = 10.0*(start_val + (3 * delta) * (t * t) + (-2 * delta) * (t * t * t));
        *(interpVals + i - 1) = 10.0 * (startVal + t * t * delta * (3 + (-2) * t));
    }
}

static unsigned char _moveTo(double x, double y, double z, double speed) {	
	double angleRot = 0, angleLeft = 0, angleRight = 0;
	double curRot = 0, curLeft = 0, curRight = 0;
	double targetRot = 0;
	double targetLeft = 0;
	double targetRight = 0;
	double curX = 0;
	double curY = 0;
	double curZ = 0;
	int i = 0;
	int totalSteps = 0;
	unsigned int timePerStep;
	unsigned char status = 0;

	status = controller.xyzToAngle(x, y, z, targetRot, targetLeft, targetRight);
	debugPrint("target B=%f, L=%f, R=%f\r\n", curRot, curLeft, curRight);

	if (status == OUT_OF_RANGE_NO_SOLUTION) return OUT_OF_RANGE_NO_SOLUTION;

	#ifdef DISABLE_SERVO_SPEED
		speed = 0;
	#endif

	if (speed == 0) {
		mCurStep = -1;
		controller.writeServoAngle(targetRot, targetLeft, targetRight);
		return IN_RANGE;
	}

	// Get current angles.
	controller.getServoAngles(curRot, curLeft, curRight);
	// Get current xyz.
	controller.getCurrentXYZ(curX, curY, curZ);

	debugPrint("B=%f, L=%f, R=%f\r\n", curRot, curLeft, curRight);

	// Calculate max steps.
	totalSteps = max(abs(targetRot - curRot), abs(targetLeft - curLeft));
	totalSteps = max(totalSteps, abs(targetRight - curRight));

	if (totalSteps <= 0) return NO_NEED_TO_MOVE;

	totalSteps = totalSteps < STEP_MAX ? totalSteps : STEP_MAX;

	// Calculate step time.
	double distance = sqrt((x - curX) * (x - curX) + (y - curY) * (y - curY) + (z - curZ) * (z - curZ));
	speed = constrain(speed, 100, 1000);
	timePerStep = distance / speed * 1000.0 / totalSteps;

	// Keep timePerStep <= STEP_MAX_TIME.
	if (timePerStep > STEP_MAX_TIME) {
		double ratio = double(timePerStep) / STEP_MAX_TIME;

		if (totalSteps * ratio < STEP_MAX) {
			totalSteps *= ratio;
			timePerStep = STEP_MAX_TIME;
		} else {
			totalSteps = STEP_MAX;
			timePerStep = STEP_MAX_TIME;
		}
	}

	totalSteps = totalSteps < STEP_MAX ? totalSteps : STEP_MAX;

	debugPrint("totalSteps= %d\n", totalSteps);

	// Trajectory planning.
	_interpolate(curX, x, mPathX, totalSteps, INTERP_EASE_INOUT_CUBIC);
	_interpolate(curY, y, mPathY, totalSteps, INTERP_EASE_INOUT_CUBIC);
	_interpolate(curZ, z, mPathZ, totalSteps, INTERP_EASE_INOUT_CUBIC);

	for (i = 0; i < totalSteps; i++) {
		status = controller.xyzToAngle(mPathX[i], mPathY[i], mPathZ[i], angleRot, angleLeft, angleRight);

		if (status != IN_RANGE) break;
		else {
			mPathX[i] = angleRot;
			mPathY[i] = angleLeft;
			mPathZ[i] = angleRight;
		}
	}

	if (i < totalSteps) {
		debugPrint("i < totalSteps\r\n");
		_interpolate(curRot, targetRot, mPathX, totalSteps, INTERP_EASE_INOUT_CUBIC);
		_interpolate(curLeft, targetLeft, mPathY, totalSteps, INTERP_EASE_INOUT_CUBIC);
		_interpolate(curRight, targetRight, mPathZ, totalSteps, INTERP_EASE_INOUT_CUBIC);
	}

	mPathX[totalSteps - 1] = targetRot;
	mPathY[totalSteps - 1] = targetLeft;
	mPathZ[totalSteps - 1] = targetRight;

	mTimePerStep = timePerStep;
	mTotalSteps = totalSteps;
	mCurStep = 0;
	mStartTime = millis();

	return IN_RANGE;
}

static void _controllerRun() {
	while (mCurStep >= 0 && mCurStep < mTotalSteps) {
		if ((millis() - mStartTime) >= (mCurStep * mTimePerStep)) {
			// Ignore the point if cannot reach.
			if (controller.limitRange(mPathX[mCurStep], mPathY[mCurStep], mPathZ[mCurStep]) != OUT_OF_RANGE_NO_SOLUTION) {
				debugPrint("curStep:%d, %f, %f, %f", mCurStep, mPathX[mCurStep], mPathY[mCurStep], mPathZ[mCurStep]);

				if (mCurStep == (mTotalSteps - 1)) {
					double angles[3];

					angles[0] = controller.getReverseServoAngle(0, mPathX[mCurStep]);
					angles[1] = controller.getReverseServoAngle(1, mPathY[mCurStep]);
					angles[2] = controller.getReverseServoAngle(2, mPathZ[mCurStep]);
					//debugPrint("curStep:%d, %f, %f, %f", mCurStep, angles[0], angles[1], angles[2]);
					controller.writeServoAngle(angles[0], angles[1], angles[2]);
					//controller.writeServoAngle(mPathX[mCurStep], mPathY[mCurStep], mPathZ[mCurStep]);
				} else controller.writeServoAngle(mPathX[mCurStep], mPathY[mCurStep], mPathZ[mCurStep]);
			}

			mCurStep++;

			if (mCurStep >= mTotalSteps) mCurStep = -1;
		}
	}
}

