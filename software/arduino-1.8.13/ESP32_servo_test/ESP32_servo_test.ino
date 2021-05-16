// ESP32_servo_test.ino

// Include the ESP32 Arduino Servo Library instead of the original Arduino Servo Library.
#include <ESP32Servo.h>

// Create servo object to control servos.
Servo servo0;
Servo servo1;
Servo servo2;
Servo servo3;

// Possible PWM GPIO pins on the ESP32: 0 (used by on-board button), 2, 4, 5 (used by on-board LED), 12-19, 21-23, 25-27 and 32-33.
int servoPin0 = 22;	// GPIO pin used to connect the servo control (digital out).
int servoPin1 = 25;	// GPIO pin used to connect the servo control (digital out).
int servoPin2 = 26;	// GPIO pin used to connect the servo control (digital out).
int servoPin3 = 27;	// GPIO pin used to connect the servo control (digital out).

// Possible ADC pins on the ESP32: 0, 2, 4, 12-15, 32-39; 34-39 are recommended for analog input.
int potPin0 = 32;	// GPIO pin used to connect the servo feedback (analog in).
int potPin1 = 33;	// GPIO pin used to connect the servo feedback (analog in).
int potPin2 = 34;	// GPIO pin used to connect the servo feedback (analog in).
int potPin3 = 34;	// GPIO pin used to connect the servo feedback (analog in).
int ADC_Max = 4096;	// This is the default ADC max value on the ESP32 (12 bit ADC width).
			// This width can be set (in low-level oode) from 9-12 bits, for a range of values between 512 and 4096 extremums.

// Variable to read the value from the analog pin.
int val0;
int val1;
int val2;
int val3;

void setup() {
	ESP32PWM::allocateTimer(0);		// Allocate one timer (there are 3 other timers, named 1, 2 and 3).
	servo0.setPeriodHertz(50);		// Standard 50hz servo.
	servo1.setPeriodHertz(50);		// Standard 50hz servo.
	servo2.setPeriodHertz(50);		// Standard 50hz servo.
	servo3.setPeriodHertz(50);		// Standard 50hz servo.
}

void loop() {
	servo0.attach(servoPin0, 500, 2500);	// Attaches the servo on pin 22 to the servo object.
	val0 = analogRead(potPin0);		// Read the value of the ADC (value between 0 and 1023).
	val0 = map(val0, 0, ADC_Max, 0, 180);	// Scale the to use with the servos (with a value between 0 and 180).
	servo0.write(val0);			// Set the servo position according to the scaled value.
	delay(200);				// Wait for the servo to get there.
	servo0.detach()				// Detach servo to save current.

	servo1.attach(servoPin1, 500, 2500);	// Attaches the servo on pin 25 to the servo object.
	val1 = analogRead(potPin1);		// Read the value of the ADC (value between 0 and 1023).
	val1 = map(val1, 0, ADC_Max, 0, 180);	// Scale the to use with the servos (with a value between 0 and 180).
	servo1.write(val1);			// Set the servo position according to the scaled value.
	delay(200);				// Wait for the servo to get there.
	servo1.detach()				// Detach servo to save current.

	servo2.attach(servoPin2, 500, 2500);	// Attaches the servo on pin 26 to the servo object.
	val2 = analogRead(potPin2);		// Read the value of the ADC (value between 0 and 1023).
	val2 = map(val2, 0, ADC_Max, 0, 180);	// Scale the to use with the servos (with a value between 0 and 180).
	servo2.write(val2);			// Set the servo position according to the scaled value.
	delay(200);				// Wait for the servo to get there.
	servo2.detach()				// Detach servo to save current.

	servo3.attach(servoPin3, 500, 2500);	// Attaches the servo on pin 27 to the servo object.
	val3 = analogRead(potPin3);		// Read the value of the ADC (value between 0 and 1023).
	val3 = map(val3, 0, ADC_Max, 0, 180);	// Scale the to use with the servos (with a value between 0 and 180).
	servo3.write(val3);			// Set the servo position according to the scaled value.
	delay(200);				// Wait for the servo to get there.
	servo3.detach()				// Detach servo to save current.
}

