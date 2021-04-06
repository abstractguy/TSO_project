// File:        c/drivers/VL6180X.h
// By:          Samuel Duclos
// For:         My team.
// Description: Header file for Time-of-Flight sensor VL6180X.

#ifndef VL6180X_H
    #define VL6180X_H
    #include "i2cdev.h"

    // Internal constants:
    #define VL6180X_DEFAULT_I2C_ADDR = 0x29
    #define VL6180X_REG_IDENTIFICATION_MODEL_ID = 0x000
    #define VL6180X_REG_SYSTEM_INTERRUPT_CONFIG = 0x014
    #define VL6180X_REG_SYSTEM_INTERRUPT_CLEAR = 0x015
    #define VL6180X_REG_SYSTEM_FRESH_OUT_OF_RESET = 0x016
    #define VL6180X_REG_SYSRANGE_START = 0x018
    #define VL6180X_REG_SYSALS_START = 0x038
    #define VL6180X_REG_SYSALS_ANALOGUE_GAIN = 0x03F
    #define VL6180X_REG_SYSALS_INTEGRATION_PERIOD_HI = 0x040
    #define VL6180X_REG_SYSALS_INTEGRATION_PERIOD_LO = 0x041
    #define VL6180X_REG_RESULT_ALS_VAL = 0x050
    #define VL6180X_REG_RESULT_RANGE_VAL = 0x062
    #define VL6180X_REG_RESULT_RANGE_STATUS = 0x04D
    #define VL6180X_REG_RESULT_INTERRUPT_STATUS_GPIO = 0x04F

    // User-facing constants:
    #define ALS_GAIN_1 = 0x06
    #define ALS_GAIN_1_25 = 0x05
    #define ALS_GAIN_1_67 = 0x04
    #define ALS_GAIN_2_5 = 0x03
    #define ALS_GAIN_5 = 0x02
    #define ALS_GAIN_10 = 0x01
    #define ALS_GAIN_20 = 0x00
    #define ALS_GAIN_40 = 0x07

    #define ERROR_NONE = 0
    #define ERROR_SYSERR_1 = 1
    #define ERROR_SYSERR_5 = 5
    #define ERROR_ECEFAIL = 6
    #define ERROR_NOCONVERGE = 7
    #define ERROR_RANGEIGNORE = 8
    #define ERROR_SNR = 11
    #define ERROR_RAWUFLOW = 12
    #define ERROR_RAWOFLOW = 13
    #define ERROR_RANGEUFLOW = 14
    #define ERROR_RANGEOFLOW = 15

    typedef struct I2C_Bus i2c_bus;
    typedef struct I2C_Device i2c_device;

    void init(i2c_bus i2c, uint16_t, uint16_t);
    uint16_t range(void);
    float read_lux(uint8_t);
    uint8_t range_status(void);
    void load_settings(void);
    uint8_t write_8(i2c_device, uint16_t, uint8_t);
    void write_16(i2c_device, uint16_t, uint8_t);
    uint8_t read_8(uint16_t);
    uint16_t read_16(uint16_t);
#endif
