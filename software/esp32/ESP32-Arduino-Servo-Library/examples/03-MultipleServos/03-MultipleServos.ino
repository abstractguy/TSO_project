/*
 * Original sourse: https://github.com/RoboticsBrno/ESP32-Arduino-Servo-Library
 * 
 * This is Arduino code to control Servo motor with ESP32 boards.
 The position of servo is controlled more thean one servo motor
 * Watch video instruction for this code: https://youtu.be/KUqR3ZLX5Ks
   
 * Written/updated by Ahmad Shamshiri for Robojax Video channel www.Robojax.com
 * Date: Dec 17, 2019, in Ajax, Ontario, Canada
 * Permission granted to share this code given that this
 * note is kept with the code.
 * Disclaimer: this code is "AS IS" and for educational purpose only.
 * this code has been downloaded from http://robojax.com/learn/arduino/
 
 * Get this code and other Arduino codes from Robojax.com
Learn Arduino step by step in structured course with all material, wiring diagram and library
all in once place. Purchase My course on Udemy.com http://robojax.com/L/?id=62

****************************
Get early access to my videos via Patreon and have  your name mentioned at end of very 
videos I publish on YouTube here: http://robojax.com/L/?id=63 (watch until end of this video to list of my Patrons)
****************************

or make donation using PayPal http://robojax.com/L/?id=64

 *  * This code is "AS IS" without warranty or liability. Free to be used as long as you keep this note intact.* 
 * This code has been download from Robojax.com
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
 */
#include <Servo_ESP32.h>

const int servoCount = 4;// how many servo 
static const int servosPins[servoCount] = {12, 14, 27, 26}; // define pins here

Servo_ESP32 servos[servoCount];//do not change

/*
* this funciton is to move all servos to the same angle. Watch video for instruction https://youtu.be/KUqR3ZLX5Ks
*/
void setServos(int degrees) {
    for(int i = 0; i < servoCount; ++i) {
        servos[i].write((degrees + (35 * i)) % 180);
    }
}

void setup() {
    Serial.begin(115200);
	Serial.print("Robojax ESP32 Multiple servo");

    for(int i = 0; i < servoCount; ++i) {
        if(!servos[i].attach(servosPins[i])) {
            Serial.print("Servo ");
            Serial.print(i);
            Serial.println("attach error");
        }
    }
}

void loop() {
	//Robojax.com multiple Servo using ESP32
    for(int posDegrees = 0; posDegrees <= 180; posDegrees++) {
        setServos(posDegrees);
        Serial.println(posDegrees);
        delay(20);
    }


    for(int posDegrees = 180; posDegrees >= 0; posDegrees--) {
        setServos(posDegrees);
        Serial.println(posDegrees);
        delay(20);
    }
}
