// File:        c/tests/I2C/I2C_test_1.c
// By:          Samuel Duclos
// For:         My team.
// Description: Simple I2C_test using ADXL345 device for testing.
// Usage:       bash c/tests/I2C/I2C_test_1
// Example:     bash c/tests/I2C/I2C_test_1
// TODO:        Implement for VL6180X Time-of-Flight sensor.

#include <stdio.h>
#include <fcntl.h>
#include <sys/ioctl.h>
#include <linux/i2c.h>
#include <linux/i2c-dev.h>

#define DEV_ID      0x00
#define BUFFER_SIZE 40

int main(void) {
    char buffer_read[BUFFER_SIZE], buffer_write[1] = {0x00};
    int file;

    puts("Starting I2C_test application using ADXL345 sensor!");

    if ((file = open("/dev/i2c-1", O_RDWR)) < 0) {
        fputs("I2C BUS ERROR! Failed to open!", stderr);
        return 1;
    }

    if (ioctl(file, I2C_SLAVE, 0x53) < 0) {
        fputs("I2C CONNECTION ERROR! Failed to connect to sensor!", stderr);
        return 1;
    }

    if (write(file, buffer_write, 1) != 1) {
        fputs("I2C READ ADDRESS WRITE ERROR! Failed to reset sensor's read address!", stderr);
        return 1;
    }

    if (read(file, buffer_read, BUFFER_SIZE) != BUFFER_SIZE) {
        fputs("I2C READ ERROR! Failed to read in buffer!", stderr);
        return 1;
    }

    printf("The Device ID is: 0x%02x\n", buffer_read[DEV_ID]);
    close(file);
    return 0;
}
