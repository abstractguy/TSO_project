// File:        c/drivers/VL6180X.c
// By:          Samuel Duclos
// For:         My team.
// Description: Driver for Time-of-Flight sensor VL6180X.

#include "VL6180X.h"
#include <stdio.h>

void init(i2c_bus i2c, uint16_t address, uint16_t error) {
    i2c_device device;

    if (address == error)
        address = VL6180X_DEFAULT_I2C_ADDR;

    device = I2CDevice(i2c, address);

    if (read_8(VL6180X_REG_IDENTIFICATION_MODEL_ID) != 0xB4) {
        fprintf("RuntimeError! Could not find VL6180X, is it connected and powered?", stderr);
        load_settings();
        write_8(VL6180X_REG_SYSTEM_FRESH_OUT_OF_RESET, 0x00);
    }
}

// Read the range of an object in front of sensor and return it in mm.
uint16_t range(void) {
    uint8_t range;
    // Wait for device to be ready for range measurement.
    while (!read_8(VL6180X_REG_RESULT_RANGE_STATUS) & 0x01);
    // Start a range measurement.
    write_8(VL6180X_REG_SYSRANGE_START, 0x01);
    // Poll until bit 2 is set.
    while (!read_8(VL6180X_REG_RESULT_INTERRUPT_STATUS_GPIO) & 0x04);
    // Read range in mm.
    range = read_8(VL6180X_REG_RESULT_RANGE_VAL);
    // Clear interrupt.
    write_8(VL6180X_REG_SYSTEM_INTERRUPT_CLEAR, 0x07);
    return range;
}

float read_lux(uint8_t gain) {
    /* Read the lux (light value) from the sensor and return it.
       Must specify the gain value to use for the lux reading:
       - ALS_GAIN_1 = 1x
       - ALS_GAIN_1_25 = 1.25x
       - ALS_GAIN_1_67 = 1.67x
       - ALS_GAIN_2_5 = 2.5x
       - ALS_GAIN_5 = 5x
       - ALS_GAIN_10 = 10x
       - ALS_GAIN_20 = 20x
       - ALS_GAIN_40 = 40x
    */

    uint16_t lux;
    uint8_t reg = read_8(VL6180X_REG_SYSTEM_INTERRUPT_CONFIG);
    reg &= ~0x38;
    reg |= 0x04 << 3; // IRQ on ALS ready.
    write_8(VL6180X_REG_SYSTEM_INTERRUPT_CONFIG, reg);

    // 100 ms integration period.
    write_8(VL6180X_REG_SYSALS_INTEGRATION_PERIOD_HI, 0);
    write_8(VL6180X_REG_SYSALS_INTEGRATION_PERIOD_LO, 100);

    // Analog gain.
    if (gain > ALS_GAIN_40)
        gain = ALS_GAIN_40;

    write_8(VL6180X_REG_SYSALS_ANALOGUE_GAIN, 0x40 | gain);

    // Start ALS.
    write_8(VL6180X_REG_SYSALS_START, 0x1);

    // Poll until "New Sample Ready threshold event" is set.
    while ((read_8(VL6180X_REG_RESULT_INTERRUPT_STATUS_GPIO) >> 3) & 0x07) != 0x04:

    // Read lux.
    lux = read_16(VL6180X_REG_RESULT_ALS_VAL);

    // Clear interrupt.
    write_8(VL6180X_REG_SYSTEM_INTERRUPT_CLEAR, 0x07);
    lux *= 0.32 // Calibrated count/lux.
    if (gain == ALS_GAIN_1) {
    } else if (gain == ALS_GAIN_1_25) {
        lux /= 1.25;
    } else if (gain == ALS_GAIN_1_67) {
        lux /= 1.76;
    } else if (gain == ALS_GAIN_2_5) {
        lux /= 2.5;
    } else if (gain == ALS_GAIN_5) {
        lux /= 5;
    } else if (gain == ALS_GAIN_10) {
        lux /= 10;
    } else if (gain == ALS_GAIN_20) {
        lux /= 20;
    } else if (gain == ALS_GAIN_40) {
        lux /= 20;
    }
    lux *= 100;
    lux /= 100; // Integration time in ms.
    return lux;

uint8_t range_status(void) {
    /* Retrieve the status/error from a previous range read.
       This will return a constant value such as:
    - ERROR_NONE - No error
    - ERROR_SYSERR_1 - System error 1 (see datasheet)
    - ERROR_SYSERR_5 - System error 5 (see datasheet)
    - ERROR_ECEFAIL - ECE failure
    - ERROR_NOCONVERGE - No convergence
    - ERROR_RANGEIGNORE - Outside range ignored
    - ERROR_SNR - Too much noise
    - ERROR_RAWUFLOW - Raw value underflow
    - ERROR_RAWOFLOW - Raw value overflow
    - ERROR_RANGEUFLOW - Range underflow
    - ERROR_RANGEOFLOW - Range overflow
    */
    return read_8(VL6180X_REG_RESULT_RANGE_STATUS) >> 4;
}

void load_settings(void) {
    // Private settings from page 24 of app note.
    write_8(0x0207, 0x01);
    write_8(0x0208, 0x01);
    write_8(0x0096, 0x00);
    write_8(0x0097, 0xFD);
    write_8(0x00E3, 0x00);
    write_8(0x00E4, 0x04);
    write_8(0x00E5, 0x02);
    write_8(0x00E6, 0x01);
    write_8(0x00E7, 0x03);
    write_8(0x00F5, 0x02);
    write_8(0x00D9, 0x05);
    write_8(0x00DB, 0xCE);
    write_8(0x00DC, 0x03);
    write_8(0x00DD, 0xF8);
    write_8(0x009F, 0x00);
    write_8(0x00A3, 0x3C);
    write_8(0x00B7, 0x00);
    write_8(0x00BB, 0x3C);
    write_8(0x00B2, 0x09);
    write_8(0x00CA, 0x09);
    write_8(0x0198, 0x01);
    write_8(0x01B0, 0x17);
    write_8(0x01AD, 0x00);
    write_8(0x00FF, 0x05);
    write_8(0x0100, 0x05);
    write_8(0x0199, 0x05);
    write_8(0x01A6, 0x1B);
    write_8(0x01AC, 0x3E);
    write_8(0x01A7, 0x1F);
    write_8(0x0030, 0x00);

    // Recommended: Public registers - See datasheet for more detail.
    write_8(0x0011, 0x10); // Enables polling for 'New Sample ready'.

    // When measurement completes.
    write_8(0x010A, 0x30); // Set the averaging sample period (compromise between lower noise and increased execution time).
    write_8(0x003F, 0x46); // Sets the light and dark gain (upper nibble). Dark gain should not be changed.
    write_8(0x0031, 0xFF); // sets the # of range measurements after which auto-calibration of system is performed.
    write_8(0x0040, 0x63); // Set ALS integration time to 100ms.
    write_8(0x002E, 0x01); // Perform a single temperature calibration of the ranging sensor.

    // Optional: Public registers - See data sheet for more detail.
    write_8(0x001B, 0x09); // Set default ranging inter-measurement period to 100ms.
    write_8(0x003E, 0x31); // Set default ALS inter-measurement period to 500ms.
    write_8(0x0014, 0x24); // Configures interrupt on 'New Sample Ready threshold event'.
}

uint8_t write_8(i2c_device device, uint16_t address, uint8_t data) {
    // Write 1 byte of data from the specified 16-bit register address.
    uint8_t temp[3];
    i2c_device_open(device);
    temp[0] = (uint8_t)((address >> 8) & 0xFF);
    temp[1] = (uint8_t)(address & 0xFF);
    temp[2] = (uint8_t)data;
    i2c_device_write(temp);
    i2c_close_device(device);
}

void write_16(i2c_device device, uint16_t address, uint8_t data) {
    // Write a 16-bit big endian value to the specified 16-bit register address.
    uint8_t temp[4];
    i2c = i2c_device_open(device);
    temp[0] = (address >> 8) & 0xFF;
    temp[1] = address & 0xFF;
    temp[2] = (data >> 8) & 0xFF;
    temp[3] = data & 0xFF;
    i2c_device_write(temp);
}

uint8_t read_8(uint16_t address) {
    // Read and return a byte from the specified 16-bit register address.
    uint8_t result[1] = {1}, bytes[2];
    i2c = i2c_device_open(device);
    bytes[0] = (address >> 8) & 0xFF;
    bytes[1] = address & 0xFF;
    i2c_device_write(bytes);
    i2c_device_readinto(result);
    i2c_close_device(device);
    return result[0];
}

uint16_t read_16(uint16_t address) {
    // Read and return a 16-bit unsigned big endian value read from the specified 16-bit register address.
    uint8_t result[2], bytes[2];
    i2c = i2c_device_open(device);
    bytes[0] = (address >> 8) & 0xFF;
    bytes[1] = address & 0xFF;
    i2c_device_write(bytes([(address >> 8) & 0xFF, address & 0xFF]));
    i2c_device_readinto(result);
    return (result[0] << 8) | result[1];
}
