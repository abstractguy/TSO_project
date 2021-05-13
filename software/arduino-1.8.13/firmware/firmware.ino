#include "uArm.h"

static void Init();

void setup() {
  Serial.begin(115200);
  Init();

  debugPrint("debug start"); // Uncomment DEBUG in uArmConfig.h to use debug function.

  moveTo(0, 150, 150);
  Serial.println("@1"); // Report ready.
}

void loop() {
  handleSerialCmd();
  getSerialCmd();
}

static void Init() {
  uArmInit();
  serialCmdInit();
}
