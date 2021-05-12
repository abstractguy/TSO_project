
#include "uArm.h"

#define USE_SERIAL_CMD	1	// 1: use serial for control	0: just use arduino to control(release ROM and RAM space).

unsigned long tickStartTime = millis(); // Get timestamp.
static void Init();

void setup() {
  Serial.begin(115200);
	Init(); // Don't remove

	debugPrint("debug start"); // Uncomment DEBUG in uArmConfig.h to use debug function.
	
	// TODO
	moveTo(0, 150, 150);
	Serial.println("@1");	// Report ready.
}

void loop() {
	run(); // Don't remove.
}

// Time out every TICK_INTERVAL (50 ms default).
void tickTimeOut() {}

////////////////////////////////////////////////////////////
// DO NOT EDIT
static void Init() {
	uArmInit();	// Don't remove
	service.init();

	#if USE_SERIAL_CMD == 1
  	serialCmdInit();
	#endif
}

void run() {
	#if USE_SERIAL_CMD == 1
  	handleSerialCmd();
	#endif

	manage_inactivity(); // Don't remove
}

void tickTaskRun() {
	tickTimeOut();
}

void manage_inactivity(void) {
  #if USE_SERIAL_CMD == 1
	  getSerialCmd();	// for serial communication
  #endif

	service.run();	// for led, button, bt etc.

	// Because there is no other hardware timer available in UNO, so use a soft timer
	// it's necessary for button, led, bt
	// so Don't remove it if you need them.
	if (millis() - tickStartTime >= TICK_INTERVAL) {
		tickStartTime = millis();
		tickTaskRun();
	}   
}
