// File:          c/drivers/CAN/CAN.c
// By:            Samuel Duclos
// For:           My team.
// Description:   Minimal SocketCAN driver for Linux.

#include "CAN.h"

void CAN_init_driver(const char *ifname) {
    //const char *ifname = "vcan0";
    struct sockaddr_can addr;
    struct ifreq ifr;

    int s, nbytes;

    if ((s = socket(PF_CAN, SOCK_RAW, CAN_RAW)) < 0) {
        fputs("SOCKET OPEN ERROR!", stderr);
    }

    strcpy(ifr.ifr_name, ifname);
    ioctl(s, SIOCGIFINDEX, &ifr);
    memset(&addr, 0, sizeof(addr));

    addr.can_family  = AF_CAN;
    addr.can_ifindex = ifr.ifr_ifindex;

    printf("%s at index %d\n", ifname, ifr.ifr_ifindex);

    if (bind(s, (struct sockaddr *)&addr, sizeof(addr)) < 0) {
        fputs("SOCKET BIND ERROR!", stderr);
    }
}

void CAN_send(uint16_t can_id, uint8_t can_dlc, uint8_t *data) {
    struct can_frame frame;
    frame.can_id  = can_id; //0x003; // Arbitration ID for weighing station is 0x003.
    frame.can_dlc = can_dlc; //2;     // TSO_protocol says 2 bytes for everyone.

    //frame.data[0] = //0x48;  // Code for black puck is ready: run whole payload.
    //frame.data[1] = //0x00;  // Simulating empty weights.
    frame.data = data;

    if (write(s, &frame, sizeof(struct can_frame)) != sizeof(struct can_frame)) {
        fputs("CAN WRITE ERROR!", stderr);
    }
}

uint8_t *CAN_receive(void) {
    int nbytes;
    struct can_frame frame;
    nbytes = read(s, &frame, sizeof(struct can_frame));

    if (nbytes < 0) {
        fputs("CAN READ ERROR!", stderr);
    }

    printf("0x%03X [%d] ", frame.can_id, frame.can_dlc);

    for (uint8_t i = 0; i < frame.can_dlc; i++) {
        printf("%02X ", frame.data[i]);
    }

    printf("\r\n");

    return frame.data;
}

void CAN_close(int s) {
    if (close(s) < 0) {
        fputs("SOCKET CLOSE ERROR!", stderr);
    }
}

