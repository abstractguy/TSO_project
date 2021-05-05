#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File:        software/jetson/utils/manager.py
# By:          Samuel Duclos
# For:         Myself
# Description: This file implements a multiprocessing manager for PID motor control with object detection.

from multiprocessing import Value, Process, Manager
from utils.loop import loop
from utils.pid import PIDController
from utils.uarm import UArm
from pyuarm.protocol import SERVO_BOTTOM, SERVO_LEFT, SERVO_RIGHT, SERVO_HAND

IS_ARDUCAM = False

if IS_ARDUCAM:
    from utils import arducam_config_parser
    from utils import ArducamSDK
    from utils.ImageConvert import *

import cv2, json, logging, numpy as np, os, pyuarm, signal, sys, threading, time

logging.basicConfig()
LOGLEVEL = logging.getLogger().getEffectiveLevel()


global uarm, cfg, handle, running, Width, Height, save_flag, color_mode, save_raw
running = True
save_flag = False
save_raw = False
cfg = {}
handle = {}

def configBoard(config):
    global handle
    ArducamSDK.Py_ArduCam_setboardConfig(handle, config.params[0], \
        config.params[1], config.params[2], config.params[3], \
            config.params[4:config.params_length])

pass

def camera_initFromFile(fileName):
    global cfg, handle, Width, Height, color_mode, save_raw

    #config = json.load(open(fileName, "r"))
    config = arducam_config_parser.LoadConfigFile(fileName)

    camera_parameter = config.camera_param.getdict()
    Width = camera_parameter["WIDTH"]
    Height = camera_parameter["HEIGHT"]

    BitWidth = camera_parameter["BIT_WIDTH"]
    ByteLength = 1

    if BitWidth > 8 and BitWidth <= 16:
        ByteLength = 2
        save_raw = True

    FmtMode = camera_parameter["FORMAT"][0]
    color_mode = camera_parameter["FORMAT"][1]
    print("color mode", color_mode)

    I2CMode = camera_parameter["I2C_MODE"]
    I2cAddr = camera_parameter["I2C_ADDR"]
    TransLvl = camera_parameter["TRANS_LVL"]
    cfg = {
        "u32CameraType": 0x00,
        "u32Width": Width,
        "u32Height": Height,
        "usbType": 0,
        "u8PixelBytes": ByteLength,
        "u16Vid": 0,
        "u32Size": 0,
        "u8PixelBits": BitWidth,
        "u32I2cAddr": I2cAddr,
        "emI2cMode": I2CMode,
        "emImageFmtMode": FmtMode,
        "u32TransLvl": TransLvl
    }

    #ret, handle, rtn_cfg = ArducamSDK.Py_ArduCam_open(cfg, 0)
    ret, handle, rtn_cfg = ArducamSDK.Py_ArduCam_autoopen(cfg)

    if ret == 0:       
        #ArducamSDK.Py_ArduCam_writeReg_8_8(handle, 0x46, 3, 0x00)
        usb_version = rtn_cfg['usbType']
        configs = config.configs
        configs_length = config.configs_length

        for i in range(configs_length):
            type = configs[i].type

            if ((type >> 16) & 0xFF) != 0 and ((type >> 16) & 0xFF) != usb_version:
                continue

            if type & 0xFFFF == arducam_config_parser.CONFIG_TYPE_REG:
                ArducamSDK.Py_ArduCam_writeSensorReg(handle, configs[i].params[0], configs[i].params[1])

            elif type & 0xFFFF == arducam_config_parser.CONFIG_TYPE_DELAY:
                time.sleep(float(configs[i].params[0]) / 1000)

            elif type & 0xFFFF == arducam_config_parser.CONFIG_TYPE_VRCMD:
                configBoard(configs[i])

        ArducamSDK.Py_ArduCam_registerCtrls(handle, config.controls, config.controls_length)
        ArducamSDK.Py_ArduCam_setCtrl(handle, "setFramerate", 5)

        rtn_val, datas = ArducamSDK.Py_ArduCam_readUserData(handle, 0x400 - 16, 16)
        print("Serial: %c%c%c%c-%c%c%c%c-%c%c%c%c" % (
                  datas[0], datas[1], datas[2], datas[3],
                  datas[4], datas[5], datas[6], datas[7],
                  datas[8], datas[9], datas[10], datas[11]
              ))

        return True

    else:
        print("open fail, rtn_val = ", ret)
        return False

pass

def captureImage_thread():
    global handle, running

    rtn_val = ArducamSDK.Py_ArduCam_beginCaptureImage(handle)

    if rtn_val != 0:
        print("Error beginning capture, rtn_val = ", rtn_val)

        running = False

        return

    else:
        print("Capture began, rtn_val = ", rtn_val)

    while running:
        #print('capture')

        rtn_val = ArducamSDK.Py_ArduCam_captureImage(handle)

        if rtn_val > 255:
            print("Error capture image, rtn_val = ", rtn_val)

            if rtn_val == ArducamSDK.USB_CAMERA_USB_TASK_ERROR:
                break

        time.sleep(0.005)

    running = False
    ArducamSDK.Py_ArduCam_endCaptureImage(handle)

def readImage_thread():
    global handle, running, Width, Height, save_flag, cfg, color_mode, save_raw
    global COLOR_BayerGB2BGR, COLOR_BayerRG2BGR, COLOR_BayerGR2BGR, COLOR_BayerBG2BGR

    count = 0
    totalFrame = 0

    time0 = time.time()
    time1 = time.time()

    data = {}

    cv2.namedWindow("ArduCam Camarray", 1)

    if not os.path.exists("images"):
        os.makedirs("images")

    while running:
        display_time = time.time()

        if ArducamSDK.Py_ArduCam_availableImage(handle) > 0:		
            rtn_val, data, rtn_cfg = ArducamSDK.Py_ArduCam_readImage(handle)
            datasize = rtn_cfg['u32Size']

            if rtn_val != 0 or datasize == 0:
                ArducamSDK.Py_ArduCam_del(handle)

                print("Read data fail!")

                continue

            image = convert_image(data, rtn_cfg, color_mode)

            time1 = time.time()

            if time1 - time0 >= 1:
                print("%s %d %s\n" % ("fps:", count, "/s"))

                count = 0
                time0 = time1

            count += 1

            if save_flag:
                cv2.imwrite("images/image%d.jpg" % totalFrame, image)

                if save_raw:
                    with open("images/image%d.raw" % totalFrame, 'wb') as f:
                        f.write(data)

                totalFrame += 1

            image = cv2.resize(image, (640, 480), interpolation=cv2.INTER_LINEAR)

            cv2.imshow("ArduCam Demo", image)
            cv2.waitKey(10)

            ArducamSDK.Py_ArduCam_del(handle)

            #print("------------------------display time:", (time.time() - display_time))

        else:
            time.sleep(0.001)

def showHelp():
    print(" usage: sudo python ArduCam_Py_Demo.py <path/config-file-name>	\
        \n\n example: sudo python ArduCam_Py_Demo.py ../../../python_config/AR0134_960p_Color.json	\
        \n\n While the program is running, you can press the following buttons in the terminal:	\
        \n\n 's' + Enter:Save the image to the images folder.	\
        \n\n 'c' + Enter:Stop saving images.	\
        \n\n 'q' + Enter:Stop running the program.	\
        \n\n")

def stream(args):
    showHelp()

    try:
        if camera_initFromFile(args.config_file_name):
            ArducamSDK.Py_ArduCam_setMode(handle, ArducamSDK.CONTINUOUS_MODE)
            ct = threading.Thread(target=captureImage_thread)
            rt = threading.Thread(target=readImage_thread)
            ct.start()
            rt.start()
        
            while running:
                input_kb = str(sys.stdin.readline()).strip("\n")

                if input_kb == 'q' or input_kb == 'Q':
                    running = False
                if input_kb == 's' or input_kb == 'S':
                    save_flag = True
                if input_kb == 'c' or input_kb == 'C':
                    save_flag = False

            ct.join()
            rt.join()

            #pause
            #ArducamSDK.Py_ArduCam_writeReg_8_8(handle, 0x46, 3, 0x40)

            rtn_val = ArducamSDK.Py_ArduCam_close(handle)

            if rtn_val == 0:
                print("device close success!")
            else:
                print("device close fail!")

            #os.system("pause")

    except KeyboardInterrupt:
        print('User terminated stream process.')

    except Exception as e:
        print(e)

    finally:
        # Release resources.
        print('Done.')


def set_servos(pan, tilt, flip_vertically=False, flip_horizontally=False):
    """Servomotor loop for motor control."""
    global uarm

    try:
        while True:
            pan_angle = (-1 if flip_vertically else 1) * pan.value
            tilt_angle = (-1 if flip_horizontally else 1) * tilt.value

            uarm.set_servo_angle(SERVO_BOTTOM, pan_angle) # Verify this is the correct servo!!!
            uarm.set_servo_angle(SERVO_LEFT, tilt_angle) # Verify this is the correct servo!!!

    except KeyboardInterrupt:
        print('User terminated servo process.')

    except Exception as e:
        print(e)

    finally:
        # Release resources.
        print('Done.')

def pid_process(output, p, i, d, box_coord, origin_coord, action):
    """PID loop for single motor control."""
    try:
        # Create a PID and initialize it.
        p = PIDController(p.value, i.value, d.value)
        p.reset()

        # Loop indefinitely.
        while True:
            error = origin_coord - box_coord.value
            output.value = p.update(error)
            logging.info(f'{action} error {error} angle: {output.value}')

    except KeyboardInterrupt:
        print('User terminated PID process.')

    except Exception as e:
        print(e)

    finally: # Release resources.
        print('Done.')

#('person',)
#('orange', 'apple', 'sports ball')
def process_manager(args):
    """Main process manager."""
    global uarm

    image_shape = args.image_shape
    (height, width) = image_shape

    try:
        uarm = UArm(uarm_speed=args.uarm_speed, 
                    uart_delay=args.uart_delay, 
                    servo_attach_delay=args.servo_attach_delay, 
                    set_position_delay=args.set_position_delay, 
                    servo_detach_delay=args.servo_detach_delay, 
                    pump_delay=args.pump_delay)

        with Manager() as manager:
            # Set initial bounding box (x, y)-coordinates to center of frame.
            center_x = manager.Value('i', 0)
            center_y = manager.Value('i', 0)

            object_x = manager.Value('i', 0)
            object_y = manager.Value('i', 0)

            center_x.value = height // 2
            center_y.value = width // 2

            # Pan and tilt angles updated by independent PID processes.
            pan = manager.Value('i', 0)
            tilt = manager.Value('i', 0)

            # PID gains for panning.
            pan_p = manager.Value('f', 1)
            # 0 time integral gain until inferencing is faster than ~50ms.
            pan_i = manager.Value('f', 0)
            pan_d = manager.Value('f', 0)
        
            # PID gains for tilting.
            tilt_p = manager.Value('f', 1)
            # 0 time integral gain until inferencing is faster than ~50ms.
            tilt_i = manager.Value('f', 0)
            tilt_d = manager.Value('f', 0)

            detect_process = Process(target=loop, args=(args, object_x, object_y, center_x, center_y))
            pan_process = Process(target=pid_process, args=(pan, pan_p, pan_i, pan_d, center_x, center_x.value, 'pan'))
            tilt_process = Process(target=pid_process, args=(tilt, tilt_p, tilt_i, tilt_d, center_y, center_y.value, 'tilt'))
            servo_process = Process(target=set_servos, args=(pan, tilt, args.flip_vertically, args.flip_horizontally))

            detect_process.start()
            pan_process.start()
            tilt_process.start()
            servo_process.start()

            detect_process.join()
            pan_process.join()
            tilt_process.join()
            servo_process.join()

    except KeyboardInterrupt:
        print('User terminated manager process.')

    except Exception as e:
        print(e)

    finally: # Release resources.
        print('Done.')

