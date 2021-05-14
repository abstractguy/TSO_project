# TSO_project

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fabstractguy%2FTSO_project&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

# TSO_project
## An "Intelligent" robotic arm using a camera for pick and place.
The uARM (the name of the robotic arm used in this project) initializes to a position in the middle of its servomotor angle range, then picks up a single selected class of common objects labeled from the COCO dataset (80 classes) and a bunch of goodies (see software/jetson/fastmot/), using feedback from a camera. It then places and drops the object to a predefined location.
Still a work in progress. Mid development phase.

## Documentation
The documentation provides instructions to compile and deploy parts of previously commented code as a website on readthedocs or locally.
Still a work in progress. Early development phase.

## Mechanics
The *.STL files can be 3D-printed.

## Simulation
The *.STL files can be converted to *.URDF for simulation using a physics engine (see software/jetson/jetson-containers/).

## Electronics
The minimalistic Printed Circuit Board features an ESP32 as the motor-driving microcontroller.

## Software
There is PC-compatible (Windows, MACOSX and Linux) software to program and deploy the environment, firmware for the PCB in software/arduino-1.8.13/, theres is software, drivers, etc. for commanding everything from the Jetson (or computer).

## Accelerated inference using TensorRT, deployable on Nvidia Jetson platforms
A platform featuring YOLOv4-mish-640, with instructions for training and evaluation and deployable inference on an Nvidia Jetson (Nano or AGX Xavier) using TensorRT.

## Installation Instructions for Linux

##### Dependencies
    None which aren't covered by this guide.

## Install from scratch (skip down to "Download and install the live *.iso" if installing Linux is needed)
##### Update apt repository package references (ensure system will be up to date)
```
$ sudo apt update
```

##### Install git
```
$ sudo apt install -y git
```

##### Create base workspace directory
```
$ mkdir -p ~/workspace
```

##### Go to base workspace directory
```
$ cd ~/workspace
```

##### Download repository code
```
$ git clone https://github.com/abstractguy/TSO_project.git
```

##### Go to TSO_project's path
```
$ cd TSO_project/software/jetson
```

#### Download and install the live *.iso of Ubuntu 18.04.5 LTS for x86_64 (from here https://unetbootin.github.io)

##### If running Linux already:
```
$ sudo -H bash install/install_unetbootin.sh
```

### Update and reboot (redo skipped first steps if you're starting on a newly installed system)

## Start with a fresh install of Ubuntu 18.04.5 LTS with automatic updates and proprietary drivers activated

##### Install Nvidia components for JetPack 4.4.1
```
$ sudo -H bash ~/workspace/TSO_project/software/jetson/install/install_jetpack_prerequisites.sh
```

### After the prescribed reboot, review software/jetson/jetson-containers/INSTALL_DOCKER.md and go through the entire procedure (skip the first section on installing Nvidia drivers)

## Old install method (recommended)

##### Install miniconda3
```
$ cd && bash ~/workspace/TSO_project/software/jetson/install/install_conda.sh
```

##### Install conda environment
```
$ cd && bash ~/workspace/TSO_project/software/jetson/install/install_conda_environment.sh
```

## New install method (not recommended, experimental)

##### Do everything in this script manually or if feeling adventurous, automagically (not tested)
```
$ cd ~/workspace/TSO_project/software/jetson && bash install/install_x86_environment_part_1.sh
```

##### New install method: Reboot

##### New install method (not recommended): Do everything in this script manually or if feeling adventurous, automagically (not tested)
```
$ cd ~/workspace/TSO_project/software/jetson && bash install/install_x86_environment_part_2.sh
```

### If you're using Jetson Nano devkit, you will want to install a jumper on J48 to power with the jack barrel

## Install Nvidia JetPack 4.4.1 dependencies after installing TSO_project on Ubuntu 18.04.5 LTS on a x86_64

### Sign in to install Nvidia's sdkmanager from https://developer.nvidia.com/nvsdk-manager

### Follow the instructions and when it can't SSH into the Jetson, plug a screen, keyboard and mouse to the Nvidia Jetson Nano (or AGX Xavier) devkit to configure the rest; the install will resume after

##### Prepare directories on the Jetson (tested using an Nvidia Jetson AGX Xavier) (from x86_64)
```
$ ssh sam@192.168.55.1 'mkdir -p ~/workspace'
$ scp -r ~/workspace/TSO_project/software sam@192.168.55.1:/home/sam/workspace
```

##### Install Jetson prerequisites
```
$ ssh -t sam@192.168.55.1 'bash ~/workspace/software/jetson/utils/install_jetson.sh'
```

##### If you have the Jetson Nano devkit and the dual ArduCAM camera array HAT style with OV9281 sensors (1MP Global Shutter Camera), install the camera drivers
```
$ ssh -t sam@192.168.55.1 'cd ~/workspace/software/jetson && sudo chmod +x ArduCAM/install.sh && ./ArduCAM/install.sh'
```

##### Make the TensorRT YOLO plugins
```
$ ssh -t sam@192.168.55.1 'cd ~/workspace/software/jetson/fastmot/utils/plugins && make'
```

##### Install the custom uARM serial port GCODE spammer
```
$ ssh -t sam@192.168.55.1 'cd ~/workspace/software/jetson && pip3 install -e pyuarm'
```

##### On your TV, open a terminal and run everything
```
$ cd ~/workspace/software/jetson && sudo python3 main.py --inference-type fastmot --input_uri /dev/video0 --mot --gui
```

## Inference
Uses vanilla COCO-pretrained weights to make predictions on images, but you can [train your own YOLOv4-mish](https://github.com/AlexeyAB/darknet). 
The table below displays the inference times when using images scaled to 640x640 as inputs. The taken YOLOv4-mish measurements show the inference time of this implementation on Nvidia Jetson AGX Xavier.

| Backbone                | GPU        | FPS (max smoothed) | mAP@0.5 |
| ----------------------- |:----------:|:------------------:|:-------:|
| Yolov4-608              | AGX Xavier | 32                 | 60      |
| Yolov4-mish-640         | AGX Xavier | XX                 | XX      |
| Yolov4-mish-SAM-640     | AGX Xavier | XX                 | XX      |

## FPS Results
Inference FPS of yolov4 with tkDNN, average of 1200 images with the same dimension as the input size, on 
  * RTX 2080Ti (CUDA 10.2, TensorRT 7.0.0, Cudnn 7.6.5);
  * Xavier AGX, Jetpack 4.3 (CUDA 10.0, CUDNN 7.6.3, tensorrt 6.0.1 );
  * Xavier NX, Jetpack 4.4  (CUDA 10.2, CUDNN 8.0.0, tensorrt 7.1.0 ). 
  * Tx2, Jetpack 4.2 (CUDA 10.0, CUDNN 7.3.1, tensorrt 5.0.6 );
  * Jetson Nano, Jetpack 4.4  (CUDA 10.2, CUDNN 8.0.0, tensorrt 7.1.0 ). 

| Platform   | Network    	| FP32, B=1 | FP32, B=4	| FP16, B=1 |	FP16, B=4 |	INT8, B=1 |	INT8, B=4 | 
| :------:   | :-----:    	| :-----:   | :-----:   | :-----:   |	:-----:   |	:-----:   |	:-----:   | 
| RTX 2080Ti | yolo4 320  	| 118.59	  | 237.31	  | 207.81	  | 443.32	  | 262.37	  | 530.93    | 
| RTX 2080Ti | yolo4 416  	| 104.81	  | 162.86	  | 169.06	  | 293.78	  | 206.93	  | 353.26    | 
| RTX 2080Ti | yolo4 512  	| 92.98	    | 132.43	  | 140.36	  | 215.17	  | 165.35	  | 254.96    | 
| RTX 2080Ti | yolo4 608  	| 63.77	    | 81.53	    | 111.39	  | 152.89	  | 127.79	  | 184.72    | 
| AGX Xavier | yolo4 320  	|	26.78	    | 32.05	    | 57.14	    | 79.05	    | 73.15	    | 97.56     |
| AGX Xavier | yolo4 416  	|	19.96	    | 21.52	    | 41.01	    | 49.00	    | 50.81	    | 60.61     |
| AGX Xavier | yolo4 512  	|	16.58	    | 16.98	    | 31.12	    | 33.84	    | 37.82	    | 41.28     |
| AGX Xavier | yolo4 608  	|	9.45 	    | 10.13	    | 21.92	    | 23.36	    | 27.05	    | 28.93     |
| Xavier NX  | yolo4 320  	|	14.56	    | 16.25	    | 30.14	    | 41.15	    | 42.13	    | 53.42     |
| Xavier NX  | yolo4 416  	|	10.02	    | 10.60	    | 22.43	    | 25.59	    | 29.08	    | 32.94     |
| Xavier NX  | yolo4 512  	|	8.10	    | 8.32	    | 15.78	    | 17.13	    | 20.51	    | 22.46     |
| Xavier NX  | yolo4 608  	|	5.26	    | 5.18	    | 11.54	    | 12.06	    | 15.09	    | 15.82     |
| Tx2        | yolo4 320		| 11.18	    | 12.07	    | 15.32	    | 16.31     | -         | -         |
| Tx2        | yolo4 416		| 7.30	    | 7.58	    | 9.45	    | 9.90      | -         | -         |
| Tx2        | yolo4 512		| 5.96	    | 5.95	    | 7.22	    | 7.23      | -         | -         |
| Tx2        | yolo4 608		| 3.63	    | 3.65	    | 4.67	    | 4.70      | -         | -         |
| Nano       | yolo4 320		| 4.23	    | 4.55	    | 6.14	    | 6.53      | -         | -         |
| Nano       | yolo4 416		| 2.88	    | 3.00	    | 3.90	    | 4.04      | -         | -         |
| Nano       | yolo4 512		| 2.32	    | 2.34	    | 3.02	    | 3.04      | -         | -         |
| Nano       | yolo4 608		| 1.40	    | 1.41	    | 1.92	    | 1.93      | -         | -         |
| Nano       | yolo4-mish 640		| -	    | -	    | -	    | -      | -         | -         |
| Nano       | yolo4-mish-sam 640		| -	    | -	    | -	    | -      | -         | -         |

## MAP Results
Results for COCO val 2017 (5k images), on RTX 2080Ti, with conf threshold=0.001

|                               | CodaLab       | CodaLab   | CodaLab       | CodaLab     | tkDNN map     | tkDNN map |
| ----------------------------- | :-----------: | :-------: | :-----------: | :---------: | :-----------: | :-------: |
|                               | **tkDNN**     | **tkDNN** | **darknet**   | **darknet** | **tkDNN**     | **tkDNN** |
|                               | MAP(0.5:0.95) | AP50      | MAP(0.5:0.95) | AP50        | MAP(0.5:0.95) | AP50      |
| Yolov3 (416x416)              | 0.381         | 0.675     | 0.380         | 0.675       | 0.372         | 0.663     |
| yolov4 (416x416)              | 0.468         | 0.705     | 0.471         | 0.710       | 0.459         | 0.695     |
| yolov4-mish (416x416)         | \-            | \-        | \-            | \-          | \-            | \-        |
| yolov4-mish-sam (416x416)     | \-            | \-        | \-            | \-          | \-            | \-        |
| yolov3tiny (416x416)          | 0.096         | 0.202     | 0.096         | 0.201       | 0.093         | 0.198     |
| yolov4tiny (416x416)          | 0.202         | 0.400     | 0.201         | 0.400       | 0.197         | 0.395     |
| Cnet-dla34 (512x512)          | 0.366         | 0.543     | \-            | \-          | 0.361         | 0.535     |
| mv2SSD (512x512)              | 0.226         | 0.381     | \-            | \-          | 0.223         | 0.378     |


FPS on RTX 2070 (R) and Tesla V100 (V):

* [yolov4x-mish.cfg](https://raw.githubusercontent.com/AlexeyAB/darknet/master/cfg/yolov4x-mish.cfg) - 640x640 - **67.9% mAP@0.5 (49.4% AP@0.5:0.95) - 23(R) FPS / 50(V) FPS** - 221 BFlops (110 FMA) - 381 MB: [yolov4x-mish.weights](https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v4_pre/yolov4x-mish.weights) 
   * pre-trained weights for training: https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v4_pre/yolov4x-mish.conv.166


##### Login on TV screen, convert yolov4-mish-640 from PyTorch *.pt to TensorRT *.trt and run inference
```
$ source ~/workspace/software/jetson/load_programs.sh
$ source ~/workspace/software/jetson/test.sh
```

<p align="center"><img src="software/jetson/doc/valid_test.jpg" width="480"\></p>
<p align="center"><img src="software/jetson/doc/valid_tested.png" width="512"\></p>

## Training and fine-tuning of this neural network is beyond the scope of this project, but please refer to [AlexeyAB's Darknet](https://github.com/AlexeyAB/darknet)

#### The tr
<p align="center"><img src="software/jetson/doc/results.png" width="512"\></p>

#### Visualize with tensorboard.
```
$ tensorboard --logdir=runs
```
<p align="center"><img src="software/jetson/doc/tensorboard_example.png" width="512"\></p>

## Other README.md in other directories
- software/arduino-1.8.13/portable/sketchbook/libraries/UArmForArduino/README.md
- software/arduino-1.8.13/README.md
- software/jetson/fastmot/README.md
- software/jetson/README.md
- arduino-1.8.13/portable/sketchbook/libraries/arduino-esp32/README.md
- arduino-1.8.13/portable/sketchbook/libraries/ESP32-Arduino-Servo-Library/README.md
- arduino-1.8.13/portable/sketchbook/libraries/UArmForArduino/README.md
- arduino-1.8.13/portable/sketchbook/libraries/UArmForArduino_original/README.md
- arduino-1.8.13/README.md
- jetson/jetson-containers/UArmForROS/README.md
- jetson/jetson-containers/README.md
- jetson/README.md
- and others... (in development)

## Credit

### GeekAlexis/FastMOT
[[FastMOT inference]](https://github.com/GeekAlexis/FastMOT)

### AlexeyAB/darknet
[[Training YOLOv4-mish and stats]](https://github.com/AlexeyAB/darknet)

### jktjung-avt/tensorrt_demos
[[Conversion functions]](https://github.com/jkjung-avt/tensorrt_demos)

### ceccocats/tkDNN
[[Performance graphics]](https://github.com/ceccocats/tkDNN)

### Camera Demonstration
[[Camera Demonstration]](https://www.arducam.com/docs/camera-for-jetson-nano/mipi-camera-modules-for-jetson-nano/camera-demonstration/#0--1hardware-connection-)

## Reference papers

[[Yolov3 paper]](https://arxiv.org/abs/1804.02767)
[[Yolov4 paper]](https://arxiv.org/abs/2004.10934)
[[SPP paper]](https://arxiv.org/abs/1406.4729)
[[CSPNet paper]](https://arxiv.org/abs/1911.11929)

