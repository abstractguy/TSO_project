// time.h

#ifndef TIME_H
    #define TIME_H

    #ifdef  __cplusplus
        extern "C" {
    #endif

    #include <stdint.h>
    #include <time.h>
    #include <sys/time.h>

    typedef struct timespec timespec;
    typedef struct timeval timeval;

    void nanosleep(uint64_t ns);
    void usleep(unsigned int us);
    uint64_t nanos_since_epoch(void);
    uint64_t nanos_since_boot(void);
    uint64_t nanos_thread_time(void);
    uint64_t timespec_to_micros(timespec ts);
    uint64_t timespec_to_millis(timespec ts);
    uint64_t timeval_to_micros(timeval tv);
    uint64_t timeval_to_millis(timeval tv);
    timespec timespec_diff(timespec A, timespec B);
    void timespec_add(timespec* start, double seconds);

    #ifdef __cplusplus
        }
    #endif
#endif // TIME_H
