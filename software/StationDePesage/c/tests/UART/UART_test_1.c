// File:        c/tests/UART/UART_test_1.c
// By:          Samuel Duclos
// For:         My team.
// Description: Simple UART_test_1.
// Usage:       bash c/tests/UART/UART_test_1 <STRING>
// Example:     bash c/tests/UART/UART_test_1 "This is a test..."
// Arguments:   <STRING>: test string

#include <stdio.h>
#include <string.h>
#include <termios.h>
#include <fcntl.h>
#include <unistd.h>
#include "../drivers/UART/uart.h"

#define TTY "/dev/ttyACM0"

int main(int argc, char *argv[]) {
    struct termios options;
    int file, count;

    if (argc != 2) {
        fputs("INVALID ARGUMENT ERROR! Pass arguments correctly (see comments)...", stderr);
        return -2;
    }

    if ((file = open(TTY, O_RDWR | O_NOCTTY | O_NDELAY)) < 0) {
        fputs("UART ERROR! Failed to open the device...", stderr);
        return -1;
    }

    tcgetattr(file, &options);
    options.c_cflag = B115200 | CS8 | CREAD | CLOCAL;
    options.c_iflag = IGNPAR | ICRNL;
    tcflush(file, TCIFLUSH);
    tcsetattr(file, TCSANOW, &options);

    if ((count = write(file, argv[1], strlen(argv[1]) + 1)) < 0) {
        fputs("UART: Failed to write to the output.", stderr);
        return -1;
    }

    close(file);
    return 0;
}
