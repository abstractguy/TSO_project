/**
  ******************************************************************************
  * @file	uArmSystem.h
  * @author	David.Long	
  * @email	xiaokun.long@ufactory.cc
  * @date	2016-09-28
  * @license GNU
  * copyright(c) 2016 UFactory Team. All right reserved
  ******************************************************************************
  */

#ifndef _UARMSERVICE_H_
#define _UARMSERVICE_H_

#include <Arduino.h>
#include <EEPROM.h>
#include "UFServo.h"
#include "uArmConfig.h"
#include "uArmPin.h"
#include "uArmController.h"
#include "uArmAPI.h"
#include "uArmComm.h"

#define NORMAL_MODE                 0

#define OK                      0
#define ERR1                    1
#define ERR2                    2

#define SS   "[S]"
#define S0  "[S0]"
#define S1  "[S1]"
#define S2  "[S2]"
#define FF   "[F]"
#define F0  "[F0]"
#define F1  "[F1]"

// Calibration Flag & OFFSET EEPROM ADDRESS.
#define CALIBRATION_FLAG                    10
#define CALIBRATION_LINEAR_FLAG             11
#define CALIBRATION_MANUAL_FLAG             12
#define CALIBRATION_STRETCH_FLAG            13

#define SERVO_9G_MAX    460
#define SERVO_9G_MIN    98

#define CONFIRM_FLAG                        0x80

#define SUCCESS                 1
#define FAILED                  -1

class uArmService {
public:
	uArmService();

	void init();
	void run();

	void btDetect();
	void setReportInterval(unsigned int interval);

	void setButtonService(bool on);

private:	
	void systemRun();
	bool play();
	bool record();
	void tickTaskRun();
	void recorderTick();	

private:
	unsigned char mButtonServiceDisable = false;
	unsigned char mSysStatus = NORMAL_MODE;
	unsigned int mRecordAddr = 0;
	unsigned int mReportInterval; // ms. 0 means no report.
	unsigned long mReportStartTime;
	unsigned long mTickRecorderTime;	
};

extern uArmService service;

#endif // _UARMSERVICE_H_

