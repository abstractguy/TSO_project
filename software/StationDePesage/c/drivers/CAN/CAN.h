// File:          c/drivers/CAN/CAN.h
// By:            Samuel Duclos
// For:           My team.
// Description:   Minimal SocketCAN driver for Linux.

#ifndef CAN_H
    #define CAN_H

    #ifdef  __cplusplus
        extern "C" {
    #endif

    #include <stddef.h>
    #include <stdint.h>
    #include <stdio.h>
    #include <stdlib.h>
    #include <unistd.h>
    #include <string.h>
    #include <net/if.h>
    #include <sys/types.h>
    #include <sys/socket.h>
    #include <sys/ioctl.h>
    #include <linux/can.h>
    #include <linux/can/raw.h>

    void CAN_init(const char *ifname);
    void CAN_send(uint16_t can_id, uint8_t can_dlc, uint8_t *data);
    uint8_t *CAN_receive(void);
    void CAN_close(int s);

    #ifdef __cplusplus
        }
    #endif
#endif
