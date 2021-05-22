# TSO_project

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fabstractguy%2FTSO_project&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com) [![License: BSD 2-clause](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## An "Intelligent" robotic arm using a camera for pick and place.
The uARM (the name of the robotic arm used in this project) initializes to a position in the middle of its servomotor angle range, then picks up a single selected class of common objects labeled from the COCO dataset (80 classes) and a bunch of goodies (see software/jetson/fastmot/), using feedback from a camera. It then places and drops the object to a predefined location.
Still a work in progress. Mid development phase.

## Documentation
Still a work in progress. Early development phase.

## Compile code and documentation to website
To compile and deploy parts of previously commented code as a website on readthedocs or locally, click the link below.
Note: Since the impact of this on my notes was minimal, not all documentation will be displayed to the website.

[Install documentation as website](https://docs.readthedocs.io/en/stable/development/install.html "Permalink to ")

## Convert webpages to markdown for viewing on Github

[HTML-to-Markdown](http://heckyesmarkdown.com/ "Permalink to ")

## Mechanics
The *.STL files can be 3D-printed.
This has not been attempted as I would lack the time to assemble the parts.
It is available though.

## Simulation
The *.STL files can be converted to *.URDF for simulation using a physics engine like Gazebo (or displayed using RVIZ) in ROS Kinetic, all within Docker (see instructions in software/jetson/jetson-containers/README.md).
If you add the Moveit plugins, simulation can run with the uARM in tandem.
I have only ran physical and simulation movements separately in ROS and put the plan aside for lack of time and points.

## Electronics
The minimalistic Printed Circuit Board features an ESP32 as the motor-driving microcontroller.
Altium design files are provided in the electronics/ folder.

## Software
There is PC-compatible (Windows, MACOSX, Linux, Raspbian, other ARM flavors, etc.) software to program and deploy the environment, firmware for the PCB is in software/arduino-1.8.13/, theres is software, drivers, etc. for commanding everything from the Jetson (or computer).
The main code was tested on PC and Jetson for easier modular tests while integrating.

## Firmware
The firmware is portable across Arduino boards (it runs AVR, SAM, SAMD, NRF52, STM32F4, ESP32 and ESP32-S2 microcontrollers). Only pin definitions in software/arduino-1.8.13/portable/sketchbook/libraries/UArmForArduino/src/uArmPins.h need to be redefined. The script in software/jetson/install/flash_firmware_custom.sh automates the flashing process (only tested on AVR for now). See software/arduino-1.8.13/portable/sketchbook/libraries/UArmForArduino/README.md for more explanations.

## ArduCAM Camarray
An automated installation procedure and seemless handling for the driver code, all compatible with V4L2 and Gstreamer frameworks, allowing faster, easier and interchangeable inference using images, videos, a few network streaming protocols, V4L2-supported cameras (MIPI, USB, etc), etc., all accessible using the same interface.

## Custom uARM GCODE-based serial port controller in Python-3.7
A custom controller communicating with the uARM firmware using a GCODE protocol through a USB connection to the serial port provides grad-based absolute coordinate with optional scaling with image frame dimensions for easy control. Bicubic easing, movement throttling, calibration, movement recording and replay, etc. are only available while using AVR and SAMD boards.

## Multi-threading and multi-process management
For faster and simpler parallel handling of the whole ecosystem, the main entrypoint process loop runs with parallel programs excluding the manager loop: the main camera/inference loop, a PID controller for the X axis, a PID controller for the Y axis and the uARM control process. Camera input is optionally threaded in 4 ways (no threading, video get, video show and both).

## Accelerated inference using TensorRT and Numba, deployable on Nvidia Jetson platforms
A platform featuring YOLOv4-mish-640, KLT optical flow tracking, camera motion compensation, a Kalman filter, data association (...), with instructions for training and evaluation and deployable inference on an Nvidia Jetson (Nano or AGX Xavier) using TensorRT and Numba.

## Installation Instructions for Linux

##### Dependencies
    None which aren't covered by this guide.

## Install from scratch (skip down to "Download and install the live *.iso" if installing Linux is needed and get back here just after the install)
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

##### Otherwise if running Windows, download and install the live *.iso of Ubuntu 18.04.5 LTS for x86_64 from here: https://unetbootin.github.io

### Update and reboot (redo skipped first steps if you're starting on a newly installed system)


## Start with a fresh install of Ubuntu 18.04.5 LTS with automatic updates and proprietary drivers activated (do not activate secure boot through the USB install method as this can be done later)

##### Enable Hyper-V in the UEFI boot menu for virtual machine support when rebooting

##### Download Windows 10 Enterprise Edition for VirtualBox (https://developer.microsoft.com/en-us/windows/downloads/virtual-machines/)

##### Install VirtualBox 6.1.22 for running Windows 10 programs
```
$ cd ~/workspace/TSO_project/software/jetson && bash install/install_virtualbox.sh
```

##### Install the automatically downloaded extension pack by clicking on it

##### You can now use the Windows 10 Enterprise Edition to run Windows 10 applications from a Linux host, like Altium for PCB developement

##### Install Nvidia components for JetPack 4.4
```
$ sudo -H bash ~/workspace/TSO_project/software/jetson/install/install_jetpack_prerequisites.sh
```

### After the prescribed reboot, review software/jetson/install/INSTALL_DOCKER.md and go through the entire procedure

## Install Python3 development prerequisites

##### Install miniconda3
```
$ cd && bash ~/workspace/TSO_project/software/jetson/install/install_conda.sh
```

##### Install conda environment
```
$ cd ~/workspace/TSO_project/software/jetson && bash install/install_conda_environment.sh
```

### Note: if using the Jetson Nano devkit, you will want to install a jumper on J48 to power with the jack barrel

## Install Nvidia JetPack 4.4 dependencies after installing TSO_project on Ubuntu 18.04.5 LTS on a x86_64

### Sign in to install Nvidia's sdkmanager from https://developer.nvidia.com/nvsdk-manager

### Follow the instructions and when it can't SSH into the Jetson, plug a screen, keyboard and mouse to the Nvidia Jetson Nano (or AGX Xavier) devkit to configure the rest; the install will resume after

##### Create workspace directory on the Jetson (from x86_64)
```
$ ssh sam@192.168.55.1 'mkdir -p ~/workspace'
```

##### Prepare directories on the Jetson (tested using an Nvidia Jetson AGX Xavier) (from x86_64)
```
$ scp -r ~/workspace/TSO_project/software/jetson sam@192.168.55.1:/home/sam/workspace
```

##### Install Jetson prerequisites (replace <JETSON_PASSWORD> with your Jetson user's password)
```
$ ssh -t sam@192.168.55.1 'bash ~/workspace/jetson/install/install_jetson.sh <JETSON_PASSWORD>'
```

##### If you have the Jetson Nano devkit and the dual ArduCAM camera array HAT style with OV9281 sensors (1MP Global Shutter Camera), install the camera drivers
```
$ ssh -t sam@192.168.55.1 'cd ~/workspace/jetson && sudo chmod +x ArduCAM/install.sh && ./ArduCAM/install.sh'
```

##### Make the TensorRT YOLO plugins
```
$ ssh -t sam@192.168.55.1 'cd ~/workspace/jetson/fastmot/utils/plugins && make'
```

##### Install the custom uARM serial port GCODE spammer
```
$ ssh -t sam@192.168.55.1 'cd ~/workspace/jetson && pip3 install -e pyuarm'
```

##### Flash the uARM with the custom firmware
```
$ cd ~/workspace/jetson && bash install/flash_uarm_custom.sh
```

##### Or flash the uARM with the old firmware
```
$ cd ~/workspace/jetson && bash install/flash_uarm.sh
```

##### If flashing the uARM with the old firmware, you must recalibrate (verify the correct tty port!)
##### When awaiting a D7 button press, place the pump directly on the table, the uARM facing the center of its X axis
##### When awaiting a D4 button press, place the pump directly on the table, the uARM aligned by 45 degrees (pi/4 rad) from the clockwise extremum
```
$ sudo /opt/conda/envs/school/bin/python3 -m pyuarm.tools.calibration.calibrate --port /dev/ttyUSB0
```

## Inference

<img src="software/jetson/fastmot/assets/dense_demo.gif" width="400"/> <img src="software/jetson/fastmot/assets/aerial_demo.gif" width="400"/>

## Description
The use of FastMOT as a custom multiple object tracker (here post-processed for single objects) implements:
  - YOLO detector
  - SSD detector
  - Deep SORT + OSNet ReID
  - KLT optical flow tracking
  - Camera motion compensation
  - Support Scaled-YOLOv4 models
  - DIoU-NMS for YOLO (+1% MOTA)
  - Docker container provided on Ubuntu 18.04

Deep learning models are usually the bottleneck in Deep SORT, making Deep SORT unusable for real-time applications. FastMOT significantly speeds up the entire system to run in **real-time** even on Jetson. It also provides enough flexibility to tune the speed-accuracy tradeoff without a lightweight model.

To achieve faster processing, FastMOT only runs the detector and feature extractor every N frames. Optical flow is used to fill in the gaps. YOLOv4 was trained on CrowdHuman (82% mAP@0.5) while SSD's are pretrained COCO models from TensorFlow. OSNet outperforms the original feature extractor in Deep SORT. FastMOT also re-identifies targets that moved out of frame and will keep the same IDs. 

Both detector and feature extractor use the **TensorRT** backend and perform asynchronous inference. In addition, most algorithms, including Kalman filter, optical flow, and data association, are optimized using Numba.

## Performance
### Results on MOT20 train set
| Detector Skip | MOTA | MOTP | IDF1 | IDS | MT | ML |
|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|
| N = 1 | 63.3% | 72.8% | 54.2% | 5821 | 867 | 261 |
| N = 5 | 61.4% | 72.2% | 55.7% | 4517 | 778 | 302 |

### FPS on MOT17 sequences
| Sequence | Density | FPS |
|:-------|:-------:|:-------:|
| MOT17-13 | 5 - 30  | 38 |
| MOT17-04 | 30 - 50  | 22 |
| MOT17-03 | 50 - 80  | 15 |

Performance is evaluated with YOLOv4 using [py-motmetrics](https://github.com/cheind/py-motmetrics). Note that neither YOLOv4 nor OSNet was trained or finetuned on the MOT20 dataset, so train set results should generalize well. FPS results are obtained on Jetson Xavier NX. 

FastMOT has MOTA scores close to **state-of-the-art** trackers from the MOT Challenge. Tracking speed can reach up to **38 FPS** depending on the number of objects. On a desktop CPU/GPU, FPS is expected to be much higher. More lightweight models can be used to achieve better tradeoff.

Uses vanilla COCO-pretrained weights to make predictions on images, but you can [train your own YOLOv4](https://github.com/AlexeyAB/darknet). 
The table below displays the inference times when using images scaled to 608x608 as inputs. The taken YOLOv4 measurements show the inference time of this implementation on Nvidia Jetson AGX Xavier.

| Backbone                | GPU        | FPS (max smoothed) | mAP@0.5 |
| ----------------------- |:----------:|:------------------:|:-------:|
| YOLOv4-608              | AGX Xavier | 34                 | 65.7    |
| YOLOv4-mish-640         | AGX Xavier | 25                 | 67.9    |

* **IoU** (intersect over union) - average intersect over union of objects and detections for a certain threshold = 0.24

* **mAP** (mean average precision) - mean value of `average precisions` for each class, where `average precision` is average value of 11 points on PR-curve for each possible threshold (each probability of detection) for the same class (Precision-Recall in terms of PascalVOC, where Precision=TP/(TP+FP) and Recall=TP/(TP+FN) ), page-11: http://homepages.inf.ed.ac.uk/ckiw/postscript/ijcv_voc09.pdf

**mAP** is default metric of precision in the PascalVOC competition, **this is the same as AP50** metric in the MS COCO competition.
In terms of Wiki, indicators Precision and Recall have a slightly different meaning than in the PascalVOC competition, but **IoU always has the same meaning**.

![precision_recall_iou](https://hsto.org/files/ca8/866/d76/ca8866d76fb840228940dbf442a7f06a.jpg)


## Requirements
- CUDA>=10
- cuDNN>=7
- TensorRT>=7
- OpenCV>=3.3
- PyCuda
- Numpy>=1.15
- Scipy>=1.5
- TensorFlow<2.0 (for SSD support)
- Numba==0.48
- cython-bbox

### Install for Ubuntu 18.04
Make sure to have [nvidia-docker](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#docker) installed. The image requires an NVIDIA Driver version >= 450. Build and run the docker image:
  ```
  $ docker build -t fastmot:latest .
  $ docker run --rm --gpus all -it -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY fastmot:latest
  ```

#### Pre-trained models

There are weights-file for different cfg-files (trained for MS COCO dataset):

FPS on RTX 2070 (R) and Tesla V100 (V):

* [yolov4x-mish.cfg](https://raw.githubusercontent.com/AlexeyAB/darknet/master/cfg/yolov4x-mish.cfg) - 640x640 - **67.9% mAP@0.5 (49.4% AP@0.5:0.95) - 23(R) FPS / 50(V) FPS** - 221 BFlops (110 FMA) - 381 MB: [yolov4x-mish.weights](https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v4_pre/yolov4x-mish.weights) 
  * pre-trained weights for training: https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v4_pre/yolov4x-mish.conv.166

* [yolov4-csp.cfg](https://raw.githubusercontent.com/AlexeyAB/darknet/master/cfg/yolov4-csp.cfg) - 202 MB: [yolov4-csp.weights](https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v4_pre/yolov4-csp.weights) paper [Scaled Yolo v4](https://arxiv.org/abs/2011.08036)

    just change `width=` and `height=` parameters in `yolov4-csp.cfg` file and use the same `yolov4-csp.weights` file for all cases:
  * `width=640 height=640` in cfg: **66.2% mAP@0.5 (47.5% AP@0.5:0.95) - 70(V) FPS** - 120 (60 FMA) BFlops
  * `width=512 height=512` in cfg: **64.8% mAP@0.5 (46.2% AP@0.5:0.95) - 93(V) FPS** - 77 (39 FMA) BFlops
  * pre-trained weights for training: https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v4_pre/yolov4-csp.conv.142

* [yolov4.cfg](https://raw.githubusercontent.com/AlexeyAB/darknet/master/cfg/yolov4.cfg) - 245 MB: [yolov4.weights](https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.weights) (Google-drive mirror [yolov4.weights](https://drive.google.com/open?id=1cewMfusmPjYWbrnuJRuKhPMwRe_b9PaT) ) paper [Yolo v4](https://arxiv.org/abs/2004.10934)
    just change `width=` and `height=` parameters in `yolov4.cfg` file and use the same `yolov4.weights` file for all cases:
  * `width=608 height=608` in cfg: **65.7% mAP@0.5 (43.5% AP@0.5:0.95) - 34(R) FPS / 62(V) FPS** - 128.5 BFlops
  * `width=512 height=512` in cfg: **64.9% mAP@0.5 (43.0% AP@0.5:0.95) - 45(R) FPS / 83(V) FPS** - 91.1 BFlops
  * `width=416 height=416` in cfg: **62.8% mAP@0.5 (41.2% AP@0.5:0.95) - 55(R) FPS / 96(V) FPS** - 60.1 BFlops
  * `width=320 height=320` in cfg:   **60% mAP@0.5 (  38% AP@0.5:0.95) - 63(R) FPS / 123(V) FPS** - 35.5 BFlops

* [yolov4-tiny.cfg](https://raw.githubusercontent.com/AlexeyAB/darknet/master/cfg/yolov4-tiny.cfg) - **40.2% mAP@0.5 - 371(1080Ti) FPS / 330(RTX2070) FPS** - 6.9 BFlops - 23.1 MB: [yolov4-tiny.weights](https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v4_pre/yolov4-tiny.weights)

* [enet-coco.cfg (EfficientNetB0-Yolov3)](https://raw.githubusercontent.com/AlexeyAB/darknet/master/cfg/enet-coco.cfg) - **45.5% mAP@0.5 - 55(R) FPS** - 3.7 BFlops - 18.3 MB: [enetb0-coco_final.weights](https://drive.google.com/file/d/1FlHeQjWEQVJt0ay1PVsiuuMzmtNyv36m/view)

* [yolov3-openimages.cfg](https://raw.githubusercontent.com/AlexeyAB/darknet/master/cfg/yolov3-openimages.cfg) - 247 MB - 18(R) FPS - OpenImages dataset: [yolov3-openimages.weights](https://pjreddie.com/media/files/yolov3-openimages.weights)

<details><summary><b>CLICK ME</b> - Yolo v3 models</summary>

* [csresnext50-panet-spp-original-optimal.cfg](https://raw.githubusercontent.com/AlexeyAB/darknet/master/cfg/csresnext50-panet-spp-original-optimal.cfg) - **65.4% mAP@0.5 (43.2% AP@0.5:0.95) - 32(R) FPS** - 100.5 BFlops - 217 MB: [csresnext50-panet-spp-original-optimal_final.weights](https://drive.google.com/open?id=1_NnfVgj0EDtb_WLNoXV8Mo7WKgwdYZCc)

* [yolov3-spp.cfg](https://raw.githubusercontent.com/AlexeyAB/darknet/master/cfg/yolov3-spp.cfg) - **60.6% mAP@0.5 - 38(R) FPS** - 141.5 BFlops - 240 MB: [yolov3-spp.weights](https://pjreddie.com/media/files/yolov3-spp.weights)

* [csresnext50-panet-spp.cfg](https://raw.githubusercontent.com/AlexeyAB/darknet/master/cfg/csresnext50-panet-spp.cfg) - **60.0% mAP@0.5 - 44 FPS** - 71.3 BFlops - 217 MB: [csresnext50-panet-spp_final.weights](https://drive.google.com/file/d/1aNXdM8qVy11nqTcd2oaVB3mf7ckr258-/view?usp=sharing)

* [yolov3.cfg](https://raw.githubusercontent.com/AlexeyAB/darknet/master/cfg/yolov3.cfg) - **55.3% mAP@0.5 - 66(R) FPS** - 65.9 BFlops - 236 MB: [yolov3.weights](https://pjreddie.com/media/files/yolov3.weights)

* [yolov3-tiny.cfg](https://raw.githubusercontent.com/AlexeyAB/darknet/master/cfg/yolov3-tiny.cfg) - **33.1% mAP@0.5 - 345(R) FPS** - 5.6 BFlops - 33.7 MB: [yolov3-tiny.weights](https://pjreddie.com/media/files/yolov3-tiny.weights)

* [yolov3-tiny-prn.cfg](https://raw.githubusercontent.com/AlexeyAB/darknet/master/cfg/yolov3-tiny-prn.cfg) - **33.1% mAP@0.5 - 370(R) FPS** - 3.5 BFlops - 18.8 MB: [yolov3-tiny-prn.weights](https://drive.google.com/file/d/18yYZWyKbo4XSDVyztmsEcF9B_6bxrhUY/view?usp=sharing)

</details>

<details><summary><b>CLICK ME</b> - Yolo v2 models</summary>

* `yolov2.cfg` (194 MB COCO Yolo v2) - requires 4 GB GPU-RAM: https://pjreddie.com/media/files/yolov2.weights
* `yolo-voc.cfg` (194 MB VOC Yolo v2) - requires 4 GB GPU-RAM: http://pjreddie.com/media/files/yolo-voc.weights
* `yolov2-tiny.cfg` (43 MB COCO Yolo v2) - requires 1 GB GPU-RAM: https://pjreddie.com/media/files/yolov2-tiny.weights
* `yolov2-tiny-voc.cfg` (60 MB VOC Yolo v2) - requires 1 GB GPU-RAM: http://pjreddie.com/media/files/yolov2-tiny-voc.weights
* `yolo9000.cfg` (186 MB Yolo9000-model) - requires 4 GB GPU-RAM: http://pjreddie.com/media/files/yolo9000.weights

</details>


##### Download models
This includes both pretrained OSNet, SSD, and custom YOLOv4 WEIGHTS/ONNX models
```
$ cd ~/workspace/jetson && bash install/download_models.sh
```

##### Convert yolov4x-mish-640 from Darknet *.weights to ONNX *.onnx
```Bash
$ #cd ~/workspace/jetson && python3 utils/convert_DarkNet_to_ONNX.py --darknet-weights ./fastmot/models/yolov4.weights --onnx-weights ./fastmot/models/yolov4.onnx --cfg ./utils/cfg/yolov4.cfg --image-shape 608 608 --names ./utils/cfg/coco.names --batch-size 1 --add-plugins
$ cd ~/workspace/jetson && python3 utils/yolo_to_onnx.py --model fastmot/models/yolov4x-mish-640 --category_num 80
```

##### On your TV, open a terminal and run everything to convert yolov4x-mish-640 from ONNX *.onnx to TensorRT *.trt and run inference
```
$ cd ~/workspace/jetson && sudo python3 main.py --test-type nano
$ cd ~/workspace/jetson && sudo python3 main.py --test-type xavier
$ cd ~/workspace/TSO_project/software/jetson && sudo /opt/conda/envs/school/bin/python3 main.py --test-type x86_64
```

<p align="center"><img src="software/jetson/doc/valid_test.jpg" width="480"\></p>
<p align="center"><img src="software/jetson/doc/valid_tested.png" width="512"\></p>

## Training and fine-tuning of this neural network is beyond the scope of this project, but please refer to [AlexeyAB's Darknet](https://github.com/AlexeyAB/darknet)

#### The training results look like this
<p align="center"><img src="software/jetson/doc/results.png" width="512"\></p>

#### Visualize with tensorboard.
```
$ tensorboard --logdir=runs
```
<p align="center"><img src="software/jetson/doc/tensorboard_example.png" width="512"\></p>

## Other README.md in other directories
- software/arduino-1.8.13/README.md
- software/jetson/README.md
- software/jetson/jetson-containers/README.md
- software/arduino-1.8.13/portable/sketchbook/libraries/UArmForArduino/README.md
- software/arduino-1.8.13/portable/sketchbook/libraries/Servo/README.md
- and others... (in development)

YOLOv4x-mish-640
<img src="documentation/doc/yolov4x-mish-640.onnx.png" width="767" height="24000"/>

YOLOv4-608
<img src="documentation/doc/yolov4.onnx.png" width="697" height="24000"/>

## Credit

### GeekAlexis/FastMOT
[[FastMOT inference]](https://github.com/GeekAlexis/FastMOT)

### AlexeyAB/darknet
[[Training YOLOv4 and stats]](https://github.com/AlexeyAB/darknet)

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

