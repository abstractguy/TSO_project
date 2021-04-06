// File:          c/tests/CAN/CAN_test_1.c
// By:            Samuel Duclos
// For:           My team.
// Description:   Simple CAN_test_1.
// Usage example: bash c/tests/CAN/CAN_test_1

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

int main(int argc, char *argv[]) {
    int s, nbytes;
    struct sockaddr_can addr;
    struct can_frame frame;
    struct ifreq ifr;
    const char *ifname = "vcan0";

    if ((s = socket(PF_CAN, SOCK_RAW, CAN_RAW)) < 0) {
        fputs("Error while opening socket", stderr);
        return -1;
    }

    strcpy(ifr.ifr_name, ifname);
    ioctl(s, SIOCGIFINDEX, &ifr);
    addr.can_family  = AF_CAN;
    addr.can_ifindex = ifr.ifr_ifindex;
    printf("%s at index %d\n", ifname, ifr.ifr_ifindex);

    if (bind(s, (struct sockaddr *)&addr, sizeof(addr)) < 0) {
        fputs("Error in socket bind", stderr);
        return -2;
    }

    frame.can_id  = 0x003; // Arbitration ID for weighing station is 0x003.
    frame.can_dlc = 2;     // TSO_protocol says 2 bytes for everyone.
    frame.data[0] = 0x48;  // Code for black puck is ready: run whole payload.
    frame.data[1] = 0x00;  // Simulating empty weights.
    nbytes = write(s, &frame, sizeof(struct can_frame));
    printf("Wrote %d bytes\n", nbytes);

    return 0;
}
