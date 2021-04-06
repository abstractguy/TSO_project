// File:        c/drivers/UART/uart.h
// By:          Samuel Duclos
// For:         My team.
// Description: UART driver for Linux.
// Parameters:
//     bus           The bus number /dev/ttyO{bus}
//     baudrate      must be one of the standard speeds in the UART spec. 115200 and 57600 are most common.
//     timeout       timeout is in seconds and must be >=0.1
//     canonical_en  0 for non-canonical mode (raw data), non-zero for canonical mode where only one line ending in '\n' is read at a time.
//     stop_bits     number of stop bits, 1 or 2, usually 1 for most sensors
//     parity_en     0 to disable parity, nonzero to enable. usually disabled for most sensors.

#ifndef UART_H
    #define UART_H

    #ifdef __cplusplus
        extern "C" {
    #endif

    #include <stdint.h>
    #include <stdio.h>
    #include <termios.h>
    #include <errno.h>
    #include <time.h>
    #include <sys/time.h>
    #include <fcntl.h>
    #include <unistd.h>
    #include <string.h>
    #include <sys/ioctl.h>
    #include <math.h>

    #define MAX_BUS 16
    #define STRING_BUF 64
    #define MAX_READ_LEN 128 // Most bytes to read at once. This is the size of the Sitara UART FIFO buffer.

    int uart_init(int bus, int baudrate, float timeout, int canonical_en, int stop_bits, int parity_en);
    int uart_close(int bus);
    int uart_get_fd(int bus);
    int uart_flush(int bus);
    int uart_write(int bus, uint8_t* data, size_t bytes);
    int uart_read_bytes(int bus, uint8_t* buf, size_t bytes);
    int uart_read_line(int bus, uint8_t* buf, size_t max_bytes);
    int uart_bytes_available(int bus);

    #ifdef __cplusplus
        }
    #endif
#endif
