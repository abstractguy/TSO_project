/*
 * Table of Content
   Function 1 - 4 :    move to a certain point (f)
   Fucntion d : detach servos
   Function o : pump on
   Function f : pump off
   Function g : read current coordinate
   Function 5 : Read Servo offset
 */

int value;        // value is the data recevied

void setup() {
        Wire.begin();      // join i2c bus (address optional for master)
        Serial.begin(9600); // start serial port at 9600 bps
}

void loop() {/*
 * Table of Content
   Function 1 - 4 :    move to a certain point (f)
   Fucntion d : detach servos
   Function o : pump on
   Function f : pump off
   Function g : read current coordinate
   Function 5 : Read Servo offset
 */

int value;        // value is the data recevied

#include "uArm.h"

#define USE_SERIAL_CMD	1	// 1: use serial for control	0: just use arduino to control(release ROM and RAM space)

unsigned long tickStartTime = millis(); // get timestamp;
static void Init();

void setup()
{
	Serial.begin(115200);
	Init(); // Don't remove

	debugPrint("debug start"); // uncomment DEBUG in uArmConfig.h to use debug function
	
	// TODO
	moveTo(0, 150, 150);
	Serial.println("@1");	// report ready
}

void loop()
{
	run(); // Don't remove

        if (Serial.available() > 0)
        {
                char readSerial = Serial.read();
                Serial.println(readSerial);
                //----------------------------------  function 1  ------------------------------------
                // function below is for move uArm from current position to absolute coordinate
                // x = 13, y = -13, z = 3
                if (readSerial == '1') {
                        uarm.move_to(13,-13,3);
                        delay(1000);
                }
                //----------------------------------  function 2  ------------------------------------
                // function below is for move uArm from current position to absolute coordinate
                // x = -13, y = -13, z = 3
                if (readSerial == '2') {
                        uarm.move_to(-13,-13,3);
                        delay(1000);
                }
                //----------------------------------  function 3  ------------------------------------
                // function below is for move uArm from current position to relative coordinate
                // (dot) dx = 4, dy = -3, dz = 2 in 5 seconds
                if (readSerial == '3') {
                        uarm.move_to(5,0,0,RELATIVE,2);
                        delay(1000);
                }
                //----------------------------------  function 4  ------------------------------------
                // function below is for move uArm from current position to relative coordinate
                // (dot) dx = -4, dy = 3, dz = -2 in 5 seconds
                if (readSerial == '4') {
                        uarm.move_to(-4,3,-2,RELATIVE,5);
                        delay(1000);
                }
                //----------------------------------  function d  ------------------------------------
                // Detach Servo
                if (readSerial == 'd') {
                    uarm.set_servo_status(false, SERVO_ROT_NUM);
                    uarm.set_servo_status(false, SERVO_LEFT_NUM);
                    uarm.set_servo_status(false, SERVO_RIGHT_NUM);
                    uarm.set_servo_status(false, SERVO_HAND_ROT_NUM);
                }
                //----------------------------------  function a  ------------------------------------
                // Detach Servo
                if (readSerial == 'a') {
                    uarm.set_servo_status(true, SERVO_ROT_NUM);
                    uarm.set_servo_status(true, SERVO_LEFT_NUM);
                    uarm.set_servo_status(true, SERVO_RIGHT_NUM);
                    uarm.set_servo_status(true, SERVO_HAND_ROT_NUM);
                }
                //----------------------------------  function o  ------------------------------------
                // Pump on
                if (readSerial == 'o') {
                        uarm.pump_on();
                }
                //----------------------------------  function f  ------------------------------------
                // Pump off
                if (readSerial == 'f') {
                        uarm.pump_off();
                }
                //----------------------------------  function g  ------------------------------------
                // function below is for print current x,y,z absolute location
                if (readSerial == 'g') {
                        uarm.get_current_xyz();
                        Serial.print("The current location is ");
                        Serial.print(uarm.get_current_x());
                        Serial.print(" , ");
                        Serial.print(uarm.get_current_y());
                        Serial.print(" , ");
                        Serial.print(uarm.get_current_z());
                        Serial.println();
                        delay(1000);
                }
                //----------------------------------  function 5  ------------------------------------
                // function below is for read servo offset
                if (readSerial == '5') {
                        Serial.print("SERVO_ROT_NUM offset:");
                        Serial.println(uarm.read_servo_offset(SERVO_ROT_NUM));
                        Serial.print("SERVO_LEFT_NUM offset:");
                        Serial.println(uarm.read_servo_offset(SERVO_LEFT_NUM));
                        Serial.print("SERVO_RIGHT_NUM offset:");
                        Serial.println(uarm.read_servo_offset(SERVO_RIGHT_NUM));
                        Serial.print("SERVO_HAND_ROT_NUM offset:");
                        Serial.println(uarm.read_servo_offset(SERVO_HAND_ROT_NUM));
                }
        } // close read available
}

// time out every TICK_INTERVAL(50 ms default)
void tickTimeOut()
{
	
}

////////////////////////////////////////////////////////////
// DO NOT EDIT
static void Init()
{
	uArmInit();	// Don't remove
	service.init();

	#if USE_SERIAL_CMD == 1
	serialCmdInit();
	

	#endif
}

void run()
{
	#if USE_SERIAL_CMD == 1
	handleSerialCmd();
	#endif

	manage_inactivity(); // Don't remove
}

void tickTaskRun()
{
	tickTimeOut();

    buttonPlay.tick();
    buttonMenu.tick();
#ifdef MKII
    ledRed.tick();
    service.btDetect();
#endif    
}

void manage_inactivity(void)
{
#if USE_SERIAL_CMD == 1
	getSerialCmd();	// for serial communication
#endif
	service.run();	// for led, button, bt etc.

	// because there is no other hardware timer available in UNO, so use a soft timer
	// it's necessary for button,led, bt
	// so Don't remove it if you need them
	if(millis() - tickStartTime >= TICK_INTERVAL)
	{
		tickStartTime = millis();
		tickTaskRun();
	}   
}
        if (Serial.available() > 0)
        {
                char readSerial = Serial.read();
                Serial.println(readSerial);
                //----------------------------------  function 1  ------------------------------------
                // function below is for move uArm from current position to absolute coordinate
                // x = 13, y = -13, z = 3
                if (readSerial == '1') {
                        uarm.move_to(13,-13,3);
                        delay(1000);
                }
                //----------------------------------  function 2  ------------------------------------
                // function below is for move uArm from current position to absolute coordinate
                // x = -13, y = -13, z = 3
                if (readSerial == '2') {
                        uarm.move_to(-13,-13,3);
                        delay(1000);
                }
                //----------------------------------  function 3  ------------------------------------
                // function below is for move uArm from current position to relative coordinate
                // (dot) dx = 4, dy = -3, dz = 2 in 5 seconds
                if (readSerial == '3') {
                        uarm.move_to(5,0,0,RELATIVE,2);
                        delay(1000);
                }
                //----------------------------------  function 4  ------------------------------------
                // function below is for move uArm from current position to relative coordinate
                // (dot) dx = -4, dy = 3, dz = -2 in 5 seconds
                if (readSerial == '4') {
                        uarm.move_to(-4,3,-2,RELATIVE,5);
                        delay(1000);
                }
                //----------------------------------  function d  ------------------------------------
                // Detach Servo
                if (readSerial == 'd') {
                    uarm.set_servo_status(false, SERVO_ROT_NUM);
                    uarm.set_servo_status(false, SERVO_LEFT_NUM);
                    uarm.set_servo_status(false, SERVO_RIGHT_NUM);
                    uarm.set_servo_status(false, SERVO_HAND_ROT_NUM);
                }
                //----------------------------------  function a  ------------------------------------
                // Detach Servo
                if (readSerial == 'a') {
                    uarm.set_servo_status(true, SERVO_ROT_NUM);
                    uarm.set_servo_status(true, SERVO_LEFT_NUM);
                    uarm.set_servo_status(true, SERVO_RIGHT_NUM);
                    uarm.set_servo_status(true, SERVO_HAND_ROT_NUM);
                }
                //----------------------------------  function o  ------------------------------------
                // Pump on
                if (readSerial == 'o') {
                        uarm.pump_on();
                }
                //----------------------------------  function f  ------------------------------------
                // Pump off
                if (readSerial == 'f') {
                        uarm.pump_off();
                }
                //----------------------------------  function g  ------------------------------------
                // function below is for print current x,y,z absolute location
                if (readSerial == 'g') {
                        uarm.get_current_xyz();
                        Serial.print("The current location is ");
                        Serial.print(uarm.get_current_x());
                        Serial.print(" , ");
                        Serial.print(uarm.get_current_y());
                        Serial.print(" , ");
                        Serial.print(uarm.get_current_z());
                        Serial.println();
                        delay(1000);
                }
                //----------------------------------  function 5  ------------------------------------
                // function below is for read servo offset
                if (readSerial == '5') {
                        Serial.print("SERVO_ROT_NUM offset:");
                        Serial.println(uarm.read_servo_offset(SERVO_ROT_NUM));
                        Serial.print("SERVO_LEFT_NUM offset:");
                        Serial.println(uarm.read_servo_offset(SERVO_LEFT_NUM));
                        Serial.print("SERVO_RIGHT_NUM offset:");
                        Serial.println(uarm.read_servo_offset(SERVO_RIGHT_NUM));
                        Serial.print("SERVO_HAND_ROT_NUM offset:");
                        Serial.println(uarm.read_servo_offset(SERVO_HAND_ROT_NUM));
                }
        } // close read available
}
