/**
  ******************************************************************************
  * @file	gCommComm.cpp
  * @author	David.Long	
  * @email	xiaokun.long@ufactory.cc
  * @date	2016-10-08
  * @license GNU
  * copyright(c) 2016 UFactory Team. All right reserved
  * @modified	Samuel Duclos (nomfullcreatif@gmail.com)
  ******************************************************************************
  */

#include "uArmComm.h" 
#include "uArmRingBuffer.h"

static CommState commState = IDLE;

static unsigned char cmdReceived[COM_LEN_MAX];
static unsigned char cmdIndex = 0;

static uArmRingBuffer ringBuffer;

#define RESULT_BUFFER_SIZE  50
#define RING_BUFFER_SIZE    48

uint8_t bufData[RING_BUFFER_SIZE];

static void replyError(int serialNum, unsigned int errorCode) {
	if (serialNum > 0) {
		Serial.print("$");
		Serial.print(serialNum);
		Serial.print(" ");
	}

	Serial.print("E");
	Serial.println(errorCode);   
}

static void replyOK(int serialNum) {
	if (serialNum > 0) {
		Serial.print("$");
		Serial.print(serialNum);
		Serial.print(" ");
	}

	Serial.println("OK");   
}

static void replyResult(int serialNum, String result) {
	if (serialNum > 0) {    
		Serial.print("$");
		Serial.print(serialNum);
		Serial.print(" ");
	}

	Serial.print("OK ");
	Serial.println(result);   
}

static void reportResult(int reportCode, String result) {
	Serial.print("@");
	Serial.print(reportCode);
	Serial.print(" ");
	Serial.println(result);   
}

static unsigned char cmdMove(int serialNum, int parameterCount, double value[4]) {
	if (parameterCount != 4) return PARAMETER_ERROR;

	if (moveTo(value[0], value[1], value[2]) != OUT_OF_RANGE_NO_SOLUTION)
		replyOK(serialNum);
	else return OUT_OF_RANGE;

	return 0;
}

static unsigned char cmdSetAttachServo(int serialNum, int parameterCount, double value[4]) {
	if (parameterCount != 1)
		return PARAMETER_ERROR;

	if (attachServo(value[0])) {
		replyOK(serialNum);
		return 0;
	} else return OUT_OF_RANGE;
}

static unsigned char cmdSetDetachServo(int serialNum, int parameterCount, double value[4]) {
	if (parameterCount != 1)
		return PARAMETER_ERROR;

	if (detachServo(value[0])) {
		replyOK(serialNum);
		return 0;
	} else return OUT_OF_RANGE;

	return 0;
}

static unsigned char cmdSetPump(int serialNum, int parameterCount, double value[4]) {
	if (parameterCount != 1)
		return PARAMETER_ERROR;

	if (value[0] == 0) pumpOff(); // Off.
	else pumpOn(); // On.

	replyOK(serialNum);

	return 0;
}

static unsigned char cmdGetHWVersion(int serialNum, int parameterCount, double value[4]) {
	if (parameterCount != 0)
		return PARAMETER_ERROR;    

	char result[RESULT_BUFFER_SIZE];

	msprintf(result, "V%s", HW_VER);

	replyResult(serialNum, result);

	return 0;
}

static unsigned char cmdGetSWVersion(int serialNum, int parameterCount, double value[4]) {
	if (parameterCount != 0)
		return PARAMETER_ERROR;    

	char result[RESULT_BUFFER_SIZE];

	msprintf(result, "V%s", SW_VER);

	replyResult(serialNum, result);

	return 0;
}

static unsigned char cmdGetCurrentXYZ(int serialNum, int parameterCount, double value[4]) {
	if (parameterCount != 0)
		return PARAMETER_ERROR;

	getCurrentXYZ(value[0], value[1], value[2]);

	char result[RESULT_BUFFER_SIZE];
	msprintf(result, "X%f Y%f Z%f", value[0], value[1], value[2]);

	replyResult(serialNum, result);
	return 0;	
}

static void HandleMoveCmd(int cmdCode, int serialNum, int parameterCount, double value[4]) {
	unsigned char result = false;

	switch (cmdCode) {
		case 0:
			result = cmdMove(serialNum, parameterCount, value);
			break;

		default:
			replyError(serialNum, NO_SUCH_CMD);
			return;
	}

	if (result > 0) {
		Serial.print("$");
		Serial.print(serialNum);
		Serial.print(" ");
		Serial.print("E");
		Serial.println(result);
	}
}

static void HandleSettingCmd(int cmdCode, int serialNum, int parameterCount, double value[4]) {
	unsigned char result = false;

	switch (cmdCode) {
		case 201:
			result = cmdSetAttachServo(serialNum, parameterCount, value);
			break;

		case 202:
			result = cmdSetDetachServo(serialNum, parameterCount, value);
			break;

		case 231:
			result = cmdSetPump(serialNum, parameterCount, value);
			break;

		default:
			replyError(serialNum, NO_SUCH_CMD);
			return;
	}

	if (result > 0) {
		Serial.print("$");
		Serial.print(serialNum);
		Serial.print(" ");
		Serial.print("E");
		Serial.println(result);
	}
}

static void HandleQueryCmd(int cmdCode, int serialNum, int parameterCount, double value[4]) {
	unsigned char result = false;

	switch (cmdCode) {
		case 202:
			result = cmdGetHWVersion(serialNum, parameterCount, value);
			break;

		case 203:
			result = cmdGetSWVersion(serialNum, parameterCount, value);
			break;        

		case 220:
			result = cmdGetCurrentXYZ(serialNum, parameterCount, value);
			break;

		default:
			replyError(serialNum, NO_SUCH_CMD);
			return;
	}

	if (result > 0) replyError(serialNum, result);
}

static bool parseCommand(char *message) {
	double value[6];
	int index = 0;
	bool hasSerialNum = false;
	debugPrint("message=%s", message);

	int len = strlen(message);

	char *pch;
	char cmdType;

	// Skip white space.
	while (len > 0) {
		if (isspace(message[len-1])) message[len-1] = '\0';
		else break;
		len--;
	}

	if (len <= 0) return false;

	if (message[0] == '#') hasSerialNum = true;

	pch = strtok(message, " ");
	while (pch != NULL && index < 6) {
		//debugPrint("pch=%s", pch);

		switch (index) {
			case 0:
				if (!hasSerialNum) cmdType = *(pch);
				value[index] = atof(pch+1);
				break;

			case 1:
				if (hasSerialNum) cmdType = *(pch);
				//debugPrint("cmdType=%d", cmdType);
				value[index] = atof(pch+1);
				break;

			default:
				value[index] = atof(pch+1);
				break;
		}

		//debugPrint("value=%f", value[index]);

		pch = strtok(NULL, " ");

		index++;
	}

	int serialNum = 0;
	int cmdCode = 0;
	int parameterCount = 0;
	int valueStartIndex = 0;

	if (hasSerialNum) {
		serialNum = value[0];
		cmdCode = value[1];
		parameterCount = index - 2;
		valueStartIndex = 2;
	} else {
		serialNum = 0;
		cmdCode = value[0];
		parameterCount = index - 1;        
		valueStartIndex = 1;
	}

	switch (cmdType) {
		case 'G':
			HandleMoveCmd(cmdCode, serialNum, parameterCount, value + valueStartIndex);
			break;

		case 'M':
			HandleSettingCmd(cmdCode, serialNum, parameterCount, value + valueStartIndex);
			break;

		case 'P':
			HandleQueryCmd(cmdCode, serialNum, parameterCount, value + valueStartIndex);
			break;
    }
}

static void handleSerialData(char data) {
	static unsigned char cmdCount = 0;

	switch (commState) {
		case IDLE:
			if (data == '#' || data == 'G' || data == 'M' || data == 'P') {
				commState = START;
				cmdIndex = 0;
				if (data != '#') cmdCount = 1; // Get cmd code.
				else cmdCount = 0;
				cmdReceived[cmdIndex++] = data;
			}

			break;

		case START:
			if (cmdIndex >= COM_LEN_MAX) commState = IDLE;
			else if (data == '#') { // Restart.
				cmdIndex = 0;
				cmdCount = 0;
				cmdReceived[cmdIndex++] = data;
			} else if (data == 'G' || data == 'M' || data == 'P') {
				if (cmdCount >= 1) { // Restart.
					cmdIndex = 0;
					cmdReceived[cmdIndex++] = data;
				} else {
					cmdCount++;
					cmdReceived[cmdIndex++] = data;
				}
			} else if (data == '\n') {
				cmdReceived[cmdIndex] = '\0';
				parseCommand((char*)cmdReceived);
				commState = IDLE;
			} else cmdReceived[cmdIndex++] = data;
			break;

		default:
			commState = IDLE;
			break;
	}
}

void serialCmdRun() {
	char data = -1;

	while (Serial.available()) {
		data = Serial.read();

		if (data == -1) return;
		else handleSerialData(data);
	}
}

void getSerialCmd() {
	int data = -1;

	while (Serial.available()) {
		data = Serial.read();

		if (data != -1) ringBuffer.put((uint8_t)data);
	}
}

void handleSerialCmd() {
	uint8_t data = 0;

	while (ringBuffer.get(&data)) {
		handleSerialData(data);
	}
}

void serialCmdInit() {
	ringBuffer.init(bufData, RING_BUFFER_SIZE);
}

