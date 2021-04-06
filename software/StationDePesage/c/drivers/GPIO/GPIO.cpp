// File:        c/drivers/GPIO.cpp
// By:          Samuel Duclos
// For:         My team.
// Description: GPIO control on Linux in C++.

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <cstdlib>
#include <cstdio>
#include <fcntl.h>
#include <unistd.h>
#include <sys/epoll.h>
#include <pthread.h>
#include "GPIO.h"

using namespace std;

namespace TSO_project {

GPIO::GPIO(int number) {
    this->number = number;
    this->debounceTime = 0;
    this->togglePeriod = 100;
    this->toggleNumber = -1;
    this->callbackFunction = NULL;
    this->threadRunning = false;

    ostringstream s;
    s << "gpio" << number;
    this->name = string(s.str());
    this->path = GPIO_PATH + this->name + "/";
    // this->exportGPIO();
    usleep(250000); // Give Linux enough time to set up the sysfs structure (250ms).
}

int GPIO::write(string path, string filename, string value) {
    ofstream fs;
    fs.open((path + filename).c_str());

    if (!fs.is_open()){
        perror("GPIO: write failed to open file ");
        return -1;
    }

    fs << value;
    fs.close();
    return 0;
}

string GPIO::read(string path, string filename) {
    ifstream fs;
    fs.open((path + filename).c_str());
    if (!fs.is_open()) perror("GPIO: read failed to open file ");
    string input;
    getline(fs,input);
    fs.close();
    return input;
}

int GPIO::write(string path, string filename, int value) {
    stringstream s;
    s << value;
    return this->write(path,filename,s.str());
}

//int GPIO::exportGPIO() {
//    return this->write(GPIO_PATH, "export", this->number);
//}

//int GPIO::unexportGPIO() {
//    return this->write(GPIO_PATH, "unexport", this->number);
//}

int GPIO::setDirection(GPIO_DIRECTION dir) {
    switch (dir) {
        case INPUT:
            return this->write(this->path, "direction", "in");
            //break;
        case OUTPUT:
            return this->write(this->path, "direction", "out");
            //break;
    }

    return -1;
}

int GPIO::setValue(GPIO_VALUE value) {
    switch(value) {
        case HIGH:
            return this->write(this->path, "value", "1");
            //break;
        case LOW:
            return this->write(this->path, "value", "0");
            //break;
    }
    return -1;
}

int GPIO::setEdgeType(GPIO_EDGE value) {
    switch(value) {
        case NONE:
            return this->write(this->path, "edge", "none");
            //break;
        case RISING:
            return this->write(this->path, "edge", "rising");
            //break;
        case FALLING:
            return this->write(this->path, "edge", "falling");
            //break;
        case BOTH:
            return this->write(this->path, "edge", "both");
            //break;
    }
    return -1;
}

int GPIO::setActiveLow(bool isLow) {
    if (isLow) return this->write(this->path, "active_low", "1");
    else return this->write(this->path, "active_low", "0");
}

int GPIO::setActiveHigh(void) {
    return this->setActiveLow(false);
}

GPIO_VALUE GPIO::getValue(void) {
    string input = this->read(this->path, "value");
    if (input == "0") return LOW;
    else return HIGH;
}

GPIO_DIRECTION GPIO::getDirection(void) {
    string input = this->read(this->path, "direction");
    if (input == "in") return INPUT;
    else return OUTPUT;
}

GPIO_EDGE GPIO::getEdgeType(void) {
    string input = this->read(this->path, "edge");
    if (input == "rising") return RISING;
    else if (input == "falling") return FALLING;
    else if (input == "both") return BOTH;
    else return NONE;
}

int GPIO::streamOpen(void) {
    stream.open((path + "value").c_str());
    return 0;
}

int GPIO::streamWrite(GPIO_VALUE value) {
    stream << value << std::flush;
    return 0;
}

int GPIO::streamClose(void) {
    stream.close();
    return 0;
}

int GPIO::toggleOutput(void) {
    this->setDirection(OUTPUT);
    if ((bool) this->getValue()) this->setValue(LOW);
    else this->setValue(HIGH);
    return 0;
}

int GPIO::toggleOutput(int time) {
    return this->toggleOutput(-1, time);
}

int GPIO::toggleOutput(int numberOfTimes, int time) {
    this->setDirection(OUTPUT);
    this->toggleNumber = numberOfTimes;
    this->togglePeriod = time;
    this->threadRunning = true;

    if (pthread_create(&this->thread, NULL, &threadedToggle, static_cast<void*>(this))) {
        perror("GPIO: Failed to create the toggle thread");
        this->threadRunning = false;
        return -1;
    }

    return 0;
}

// Friend function.
void *threadedToggle(void *value) {
    GPIO *gpio = static_cast<GPIO*>(value);
    bool isHigh = (bool) gpio->getValue();

    while (gpio->threadRunning) {
        if (isHigh)	gpio->setValue(HIGH);
        else gpio->setValue(LOW);
        usleep(gpio->togglePeriod * 500);
        isHigh = !isHigh;
        if(gpio->toggleNumber>0) gpio->toggleNumber--;
        if(gpio->toggleNumber==0) gpio->threadRunning = false;
    }

    return 0;
}

int GPIO::waitForEdge(void) {
    this->setDirection(INPUT);
    int fd, i, epollfd, count=0;
    struct epoll_event ev;
    epollfd = epoll_create(1);

    if (epollfd == -1) {
        perror("GPIO: Failed to create epollfd");
        return -1;
    }

    if ((fd = open((this->path + "value").c_str(), O_RDONLY | O_NONBLOCK)) == -1) {
        perror("GPIO: Failed to open file");
        return -1;
    }

    
    ev.events = EPOLLIN | EPOLLET | EPOLLPRI; // read operation | edge triggered | urgent data
    ev.data.fd = fd;

    if (epoll_ctl(epollfd, EPOLL_CTL_ADD, fd, &ev) == -1) {
        perror("GPIO: Failed to add control interface");
        return -1;
    }

    while (count<=1) {
        i = epoll_wait(epollfd, &ev, 1, -1);
        if (i == -1) {
            perror("GPIO: Poll Wait fail");
            count = 5;
        } else count++;
    }

    close(fd);

    if (count==5) {
        return -1;
    } else {
        return 0;
    }
}

// Friend function.
void* threadedPoll(void *value) {
    GPIO *gpio = static_cast<GPIO*>(value);
    while(gpio->threadRunning) {
        gpio->callbackFunction(gpio->waitForEdge());
        usleep(gpio->debounceTime * 1000);
    }

    return 0;
}

int GPIO::waitForEdge(CallbackType callback) {
    this->threadRunning = true;
    this->callbackFunction = callback;
    if (pthread_create(&this->thread, NULL, &threadedPoll, static_cast<void*>(this))) {
        perror("GPIO: Failed to create the poll thread");
        this->threadRunning = false;
        return -1;
    }
    return 0;
}

GPIO::~GPIO() {
    //this->unexportGPIO();
}

}
