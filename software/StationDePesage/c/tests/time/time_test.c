// File:          c/tests/time/time_test_1.c
// By:            Samuel Duclos
// For:           My team.
// Description:   Simple time_test.
// Usage example: bash c/tests/time/time_test_1

#include <stdio.h>
#include <inttypes.h>
#include <rc/time.h>

#define LOOPS 10000

int main(int argc, char *argv[]) {
    uint64_t a, b, nanos;
    int i;

    printf("\ntesting rc time functions\n");

    // Time nanos_since_epoch.
    a = nanos_since_epoch();
    for(i = 0; i < LOOPS; i++) b = nanos_since_epoch();
    nanos = (b - a) / LOOPS;
    printf("average time to call nanos_since_epoch: %" PRIu64 "ns\n", nanos);

    // Time nanos_since_boot.
    a = nanos_since_boot();
    for(i = 0; i < LOOPS; i++) b = nanos_since_boot();
    nanos = (b - a) / LOOPS;
    printf("average time to call nanos_since_boot: %" PRIu64 "ns\n", nanos);

    // time nanos_thread_time
    a = nanos_thread_time();
    for (i = 0; i < LOOPS; i++) b = nanos_thread_time();
    nanos = (b - a) / LOOPS;
    printf("average time to call nanos_thread_time: %" PRIu64 "ns\n", nanos);
    return 0;
}