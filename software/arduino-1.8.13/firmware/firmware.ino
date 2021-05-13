#include "uArm.h"

void setup() {
  Serial.begin(115200);

  uArmInit();
  serialCmdInit();

  moveTo(0, 150, 150);

  Serial.println("@1"); // Report ready.
}

void loop() {
  handleSerialCmd();
  getSerialCmd();
}
