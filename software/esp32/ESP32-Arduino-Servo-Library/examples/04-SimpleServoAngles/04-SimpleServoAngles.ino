/*
 * Original sourse: https://github.com/RoboticsBrno/ESP32-Arduino-Servo-Library
 * 
 * This is Arduino code to control Servo motor with ESP32 boards.

Watch videos
 Mutitle Servo https://youtu.be/KUqR3ZLX5Ks
 Single Servo https://youtu.be/cDbd0ASkMog
 Servo with potentiometer (variable resistor) https://youtu.be/iigDMFCZkJw
 
   
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

/*
 * Description:
 * Example for setting the minimal and maximal angle.
 */ 

static const int servoPin = 14;//printed G14 on the board


Servo_ESP32 servo1;

void setup() {
    Serial.begin(115200);
    servo1.attach(
        servoPin, 
        Servo_ESP32::CHANNEL_NOT_ATTACHED, 
        45,
        120
    );
}

void loop() {
    for(int posDegrees = 0; posDegrees <= 180; posDegrees++) {
        servo1.write(posDegrees);
        Serial.println(posDegrees);
        delay(20);
    }

    for(int posDegrees = 180; posDegrees >= 0; posDegrees--) {
        servo1.write(posDegrees);
        Serial.println(posDegrees);
        delay(20);
    }
}