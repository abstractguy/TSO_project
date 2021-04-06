// File:        c/main.c
// By:          Samuel Duclos
// For:         My team.
// Description: uARM and balance control in C for TSO_team.
//              - finish Python (see Python)
//              - translate from Python

#include <sys/types.h>
#include <sys/wait.h>
#include <signal.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define SHELL "/bin/bash"

static void cleanup(int signo) {
    fprintf(stderr, "Termination signal received (%d)! Cleaning up!\n", signo);
    fprintf(stderr, "Killing child!\n");
    kill(pid, SIGINT);
    sleep(3);
}

uint8_t read_weight_from_child(FILE *stream) {
    char weight[10];
    fscanf(stream, "%d", weight);
    if (ferror(stream))
        fputs("Error grabbing weight from stream!", stderr);
    return (uint8_t)atoi(weight);
}

int main(int argc, char *argv[]) {
    FILE *stream = NULL;

    // Hack letting me use system() in background while getting PID back through file.
    const char *command = "/usr/bin/nohup /usr/bin/python3 /home/debian/workspace/StationDePesage/python/uARM_payload.py & /bin/echo $! > /tmp/pid";

    int pipe_to_parent[2], pipe_to_child[2], status;
    pid_t ppid = getpid(), pid, return_value, p;
    char CAN_input;
    bool is_breaking = false;

    if (argc != 2) {
        fprintf(stderr, "Usage: %s <string>\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    /*
    if (pipe(pipe_to_parent) == -1) {
        fputs("PIPE TO PARENT ERROR!", stderr);
        exit(EXIT_FAILURE);
    }

    if (pipe(pipe_to_child) == -1) {
        fputs("PIPE TO CHILD ERROR!", stderr);
        exit(EXIT_FAILURE);
    }
    */

    //return_value = fork();
    //pid = getpid();

    if (!(stream = popen(command, "r")))
        fputs("ERROR: Unable to open stream!", stderr);

    /*
    if (return_value == (pid_t)-1) { // error
        fputs("FORK ERROR!", stderr);
        exit(EXIT_FAILURE);
    } else if (!return_value) { // child
        if (signal(SIGTERM, cleanup) == SIG_ERR) {
            fputs("Error while setting SIGTERM signal handler!", stderr);
            return EXIT_FAILURE;
        }

        if (signal(SIGINT, cleanup) == SIG_ERR) {
            fputs("Error while setting SIGINT signal handler!", stderr);
            return EXIT_FAILURE;
        }

        if (signal(SIGHUP, cleanup) == SIG_ERR) {
            fputs("Error while setting SIGHUP signal handler!", stderr);
            return EXIT_FAILURE;
        }

        close(pipe_to_parent[1]); // Close unused write end.
        close(pipe_to_child[0]); // Close unused read end.
        while (read(pipe_to_parent[0], &buf, 1) > 0) {
            write(STDOUT_FILENO, &buf, 1);
        }

        //execlp(command, ARGS_GO_HERE, NULL);
        execlp(command, NULL);

        // Find a way to run in child file.
        //close(pipe_to_child[1]); // Close remaining.
        //write(STDOUT_FILENO, "\n", 1);
        //close(pipe_to_parent[0]);
        //_exit(EXIT_SUCCESS);

        //return 127; // Reaching this means error.
        _exit(EXIT_FAILURE); // Fun fact: Avoids flushing fully-buffered streams like STDOUT.
    } else { // parent
        close(pipe_to_parent[0]); // Close unused read end.
        close(pipe_to_child[1]); // Close unused write end.
        write(pipe_to_parent[1], argv[1], strlen(argv[1]));

        while (1) {
            is_factory_reset = getchar(); // Simulating factory reset.

            if (is_factory_reset == 'y') {
                while (1) {
                    CAN_input = getchar(); // CAN input goes here.

                    if (CAN_input == 'k') is_breaking = true;
                    else if (CAN_input == 'l') {
                        puts("Parent continues normally, everyone is happy!");
                    } else {
                        fputs("PROTOCOL ERROR!", stderr);
                        is_breaking = true;
                    }

                    puts(status); // CAN output goes there.

                    if (is_breaking) break;
                }
            } else break;
        }

        close(pipe_to_parent[1]); // Reader will see EOF.
        if (waitpid(pid, &status, 0) != pid) {
           status = 1;
        }
        close(pipe_to_child[0]); // Close remaining.

        if (raise(SIGINT)) {
            fputs("Error while raising SIGINT signal!", stderr);
            return EXIT_FAILURE;
        }

        exit(EXIT_SUCCESS);
    }
    */

    weight = read_weight_from_child(stream);

    if (!pclose(stream))
        fputs("ERROR: Unable to close stream!", stderr);

    exit(EXIT_SUCCESS);
}

