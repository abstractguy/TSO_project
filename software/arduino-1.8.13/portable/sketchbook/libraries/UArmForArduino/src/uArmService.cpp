/**
  ******************************************************************************
  * @file	uArmService.cpp
  * @author	David.Long	
  * @email	xiaokun.long@ufactory.cc
  * @date	2016-09-28
  * @license GNU
  * copyright(c) 2016 UFactory Team. All right reserved
  ******************************************************************************
  */

#include "uArm.h" 
#include "uArmComm.h"

uArmService service;

uArmService::uArmService() {
	mRecordAddr = 0;
	mReportInterval = 0; 
	mButtonServiceDisable = true;
	mReportStartTime = millis();
	mTickRecorderTime = millis();
}

void uArmService::setReportInterval(unsigned int interval) {
	mReportInterval = interval;
}

void uArmService::init() {}

void uArmService::systemRun() {
	if (mReportInterval > 0) {
		if (millis() - mReportStartTime >= mReportInterval) {
			mReportStartTime = millis();
			reportPos();
		}
	}
}

void uArmService::run() {
	systemRun();

	if (millis() - mTickRecorderTime >= 50)
		mTickRecorderTime = millis();
}

