// File:        c/tests/uARM/uARM_scan_test.c
// By:          Samuel Duclos
// For:         My team.
// Description: uARM scan test (output values on terminal)
// Usage:       bash c/tests/uARM/uARM_scan_test
// Example:     bash c/tests/uARM/uARM_scan_test

#include <stdio.h>

void uarm_scan_for_object(void);

int main(int argc, char *argv[]) {
    uarm_scan_for_object()
    return 0;
}

// Ewww... Update this using new Python version here:
/*
    def scan(self, position=None, sensor=None, sensor_threshold=0.5):
        corner_x = int(position['x'] - self.initial_position['x'])
        corner_y = int(position['y'] - self.initial_position['y'])
        corner_z = int(position['z'] - self.initial_position['z'])
        is_breaking = False

        if not uarm.grab(grab_position=position, sensor=sensor, sensor_threshold=sensor_threshold):
            for k in range(corner_z, self.scan_z_displacement, self.stride_z):
                for j in range(corner_y, self.scan_y_displacement, self.stride_y):
                    for i in range(corner_x, self.scan_x_displacement, self.stride_x):
                        scan_position = {'x': i, 'y': j, 'z': k, 'speed': self.initial_position['speed'], 'relative': False, 'wait': True}
                        if uarm.grab(grab_position=scan_position, sensor=sensor, sensor_threshold=sensor_threshold):
                            is_breaking = True
                            break
                    if is_breaking:
                        break
                if is_breaking:
                    break
*/

void uarm_scan_for_object(void) {
    /*
    for (unsigned char m = 0; m < 128; m++) {
        n = (m % 64) ? (63 - (m % 64)) : (m % 64);
        y = n / 8;
        x = (y % 2) ? (7 - (n % 8)) : (n % 8);
        usleep(500000);
        //if (y == 0) interfaceMalyanM200_deplacement((y % 2) ? (7 - (n % 8)) : (n % 8));
        interfaceMalyanM200_deplacement(x, y, 5, 120, 3000); // 4.
    }
    */
}
