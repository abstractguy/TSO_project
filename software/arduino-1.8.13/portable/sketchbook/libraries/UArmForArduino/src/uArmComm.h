/**
  ******************************************************************************
  * @file	  uArmComm.h
  * @author	David.Long	
  * @email	xiaokun.long@ufactory.cc
  * @date	  2016-10-08
  * @license GNU
  * copyright(c) 2016 UFactory Team. All right reserved
  ******************************************************************************
  */

#ifndef _UARMCOMM_H_
#define _UARMCOMM_H_

#include <Arduino.h>
#include "uArm.h"

#define COM_LEN_MAX   48

#define OUT_OF_RANGE      10
#define NO_SUCH_CMD       20
#define PARAMETER_ERROR   21
#define ADDRESS_ERROR     22

enum CommState {IDLE, START, CMD, END, STATE_COUNT};

#define REPORT_POS        3

void reportPos();
void serialCmdInit();
void getSerialCmd();
void handleSerialCmd();

#endif // _UARMCOMM_H_

