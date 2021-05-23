#include "uArm.h"

#define USE_SERIAL_CMD 1 // 1: use serial for control	0: just use arduino to control(release ROM and RAM space)

unsigned long tickStartTime = millis(); // Get timestamp.
static void Init();

void setup() {
	Serial.begin(115200);
	Init(); // Don't remove.
	debugPrint("debug start"); // Uncomment DEBUG in uArmConfig.h to use debug function.
	moveTo(0, 150, 150);
	Serial.println("@1");	// Report ready.
}

void loop() {run();}

// Time out every TICK_INTERVAL (50 ms default).
void tickTimeOut() {}

static void Init() {
	uArmInit();
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

	buttonPlay.tick();
	buttonMenu.tick();

	#ifdef MKII
		ledRed.tick();
		service.btDetect();
	#endif    
}

void manage_inactivity(void) {
	#if USE_SERIAL_CMD == 1
		getSerialCmd();	// For serial communication.
	#endif

	service.run(); // For led, button, bt etc.

	// Because there is no other hardware timer available in UNO, so use a soft timer for button, led, bt.
	if(millis() - tickStartTime >= TICK_INTERVAL) {
		tickStartTime = millis();
		tickTaskRun();
	}   
}

