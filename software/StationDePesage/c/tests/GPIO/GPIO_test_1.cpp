// File:        c/tests/GPIO/GPIO_test_1.cpp
// By:          Samuel Duclos
// For:         My team.
// Description: GPIO control on Linux in C++.
// Usage:       bash c/tests/GPIO/GPIO_test_1

#include <iostream>
#include <unistd.h>
#include "GPIO.h"

using namespace TSO_project;
using namespace std;

int main(void) {
    GPIO outGPIO(60), inGPIO(46);

    // Flash LED 10 times for 10 seconds.
    outGPIO.setDirection(OUTPUT);
    for (int i = 0; i < 10; i++) {
        outGPIO.setValue(HIGH);
        usleep(500000); //micro-second sleep 0.5 seconds
        outGPIO.setValue(LOW);
        usleep(500000);
    }

    inGPIO.setDirection(INPUT);
    cout << "The value of the input is: "<< inGPIO.getValue() << endl;

    // Fast write to GPIO 1 million times.
    outGPIO.streamOpen();

    for (int i = 0; i < 1000000; i++) {
        outGPIO.streamWrite(HIGH);
        outGPIO.streamWrite(LOW);
    }

    outGPIO.streamClose();

    return 0;
}
