// File:	software/arduino-1.8.13/firmware/firmware.ino
// By:		Samuel Duclos
// For:		Myself
// Description:	Takes GCODE commands from the UART and does the associated actions.
// Note:	Review "uArmConfig.h" and set what you want.

//#define UARM_FULL

#ifdef UARM_FULL
	#include "uArmFull.h"
#else
	#include "uArm.h"
#endif

unsigned long tickStartTime = millis(); // Get timestamp.
static void Init();

void setup() {
	Serial.begin(115200);
	Init();
	//debugPrint("debug start"); // Uncomment DEBUG in uArmConfig.h to use debug function.
	moveTo(0, 150, 150);
	Serial.println("@1"); // Report ready.
}

void loop() {run();}

// Time out every TICK_INTERVAL (50 ms default).
void tickTimeOut() {}

static void Init() {
	uArmInit();

	#ifdef UARM_FULL
		service.init();
	#endif

	#if USE_SERIAL_CMD == 1
		serialCmdInit();
	#endif
}

void run() {
	#if USE_SERIAL_CMD == 1
		handleSerialCmd();
	#endif

	manage_inactivity();
}

void tickTaskRun() {
	#ifdef UARM_FULL
		tickTimeOut();

		buttonPlay.tick();
		buttonMenu.tick();

		#ifdef MKII
			ledRed.tick();
			service.btDetect();
		#endif
	#endif
}

void manage_inactivity(void) {
	#if USE_SERIAL_CMD == 1
		getSerialCmd();	// For serial communication.
	#endif

	#ifdef UARM_FULL
		service.run(); // For led, button, bt etc.
	#endif

	// Because there is no other hardware timer available in UNO, so use a soft timer for button, led, bt.
	if (millis() - tickStartTime >= TICK_INTERVAL) {
		tickStartTime = millis();
		tickTaskRun();
	}   
}
