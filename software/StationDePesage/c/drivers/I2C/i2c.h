// File:          c/drivers/I2C/i2c.h
// By:            Samuel Duclos
// For:           My team.
// Description:   I2C driver for Linux.

#ifndef I2C_H
    #define I2C_H

    #ifdef  __cplusplus
        extern "C" {
    #endif

    #include <stddef.h>
    #include <stdint.h>
    #include <stdint.h>
    #include <stdlib.h>
    #include <stdio.h>
    #include <fcntl.h>
    #include <unistd.h>
    #include <sys/ioctl.h>
    #include <linux/i2c-dev.h>

    #define I2C_MAX_BUS 5
    #define I2C_BUFFER_SIZE 128
    #define unlikely(x) __builtin_expect (!!(x), 0)
    #define likely(x) __builtin_expect (!!(x), 1)

    int i2c_init(int bus, uint8_t devAddr);
    int i2c_close(int bus);
    int i2c_set_device_address(int bus, uint8_t devAddr);
    int i2c_read_byte(int bus, uint8_t regAddr, uint8_t *data);
    int i2c_read_bytes(int bus, uint8_t regAddr, size_t count,  uint8_t *data);
    int i2c_read_word(int bus, uint8_t regAddr, uint16_t *data);
    int i2c_read_words(int bus, uint8_t regAddr, size_t count, uint16_t* data);
    int i2c_write_byte(int bus, uint8_t regAddr, uint8_t data);
    int i2c_write_bytes(int bus, uint8_t regAddr, size_t count, uint8_t* data);
    int i2c_write_word(int bus, uint8_t regAddr, uint16_t data);
    int i2c_write_words(int bus, uint8_t regAddr, size_t count, uint16_t* data);
    int i2c_send_bytes(int bus, size_t count, uint8_t* data);
    int i2c_send_byte(int bus, uint8_t data);
    int i2c_lock_bus(int bus);
    int i2c_unlock_bus(int bus);
    int i2c_get_lock(int bus);
    int i2c_get_fd(int bus);

    #ifdef AUTOPILOT_EXT
        int i2c_read_data(int bus, uint8_t regAddr, size_t length, uint8_t *data);
    #endif

    typedef struct i2c_state_t {
        uint8_t devAddr;
        int fd;
        int initialized;
        int lock;
    } i2c_state_t;

    #ifdef __cplusplus
        }
    #endif
#endif
