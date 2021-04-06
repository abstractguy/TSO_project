// File:        c/drivers/GPIO.h
// By:          Samuel Duclos
// For:         My team.
// Description: GPIO control on Linux in C++.

#ifndef GPIO_H_
#define GPIO_H_

#include <string>
#include <fstream>

using std::string;
using std::ofstream;

#define GPIO_PATH "/sys/class/gpio/"

namespace TSO_project {

typedef int (*CallbackType)(int);
enum GPIO_DIRECTION {INPUT, OUTPUT};
enum GPIO_VALUE {LOW=0, HIGH=1};
enum GPIO_EDGE {NONE, RISING, FALLING, BOTH};

class GPIO {
    private:
        int number, debounceTime;
        string name, path;

    public:
        GPIO(int);
        virtual int getNumber(void) {return number;}

        virtual int setDirection(GPIO_DIRECTION);
        virtual GPIO_DIRECTION getDirection(void);
        virtual int setValue(GPIO_VALUE);
        virtual int toggleOutput(void);
        virtual GPIO_VALUE getValue(void);
        virtual int setActiveLow(bool isLow=true); // low=1, high=0
        virtual int setActiveHigh();
        virtual void setDebounceTime(int time) {this->debounceTime = time;}

        // Faster write by keeping the stream alive (~x20).
        virtual int streamOpen(void);
        virtual int streamWrite(GPIO_VALUE);
        virtual int streamClose(void);

        virtual int toggleOutput(int time); // Threaded invert output every X ms.
        virtual int toggleOutput(int numberOfTimes, int time);
        virtual void changeToggleTime(int time) {this->togglePeriod = time;}
        virtual void toggleCancel(void) {this->threadRunning = false;}

        // Detect threaded and non-threaded input edges;
        virtual int setEdgeType(GPIO_EDGE);
        virtual GPIO_EDGE getEdgeType(void);
        virtual int waitForEdge(void);
        virtual int waitForEdge(CallbackType callback);
        virtual void waitForEdgeCancel(void) {this->threadRunning = false;}

        virtual ~GPIO(void);

    private:
        int write(string path, string filename, string value);
        int write(string path, string filename, int value);
        string read(string path, string filename);
        //int exportGPIO();
        //int unexportGPIO();
        ofstream stream;
        pthread_t thread;
        CallbackType callbackFunction;
        bool threadRunning;
        int togglePeriod;  //default 100ms
        int toggleNumber;  //default -1 (infinite)
        friend void* threadedPoll(void *value);
        friend void* threadedToggle(void *value);
};

void *threadedPoll(void *);
void *threadedToggle(void *);
}

#endif
