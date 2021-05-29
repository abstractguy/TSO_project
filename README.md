# TSO_project

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fabstractguy%2FTSO_project&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com) [![License: BSD 2-clause](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## An "intelligent" robotic arm using a camera for pick and place.
A preconfigured development computer (auto-install scripts and documentation included) connects by SSH to a preconfigured Nvidia Jetson Nano (auto-install scripts and documentation included) with an Arducam camera array shield tiling up to 4 cameras (auto-install scripts and documentation included). Only one is attached by a 1 meter MIPI ribbon with a repeater extension to the tip of the uArm. The USB-controlled Jetson becomes the central controlling unit in this topology. The x86_64 (but could be other architectures) flashes the firmware on the ESP32 microcontroller (soldered on the Altium-designed Printed Circuit Board) through another USB port. This firmware (without going into the details or extras just yet) listens to the UART for GCODE which it then executes and effects using 3 Pulse Width Modulation outputs to 3 proprietary servomotors (the only uArm part which has not been (re)defined in this project). 4 analog inputs provide angle feedback to the firmware. The valve is strapped to VCC and the pump is driven with a GPIO by flipping the logical levels. The uARM (the name of the robotic arm used in this project) initializes to a position in the middle of its servomotor angle range. It can be controlled using GCODE from the UART to pick up objects using absolute, relative or polar coordinates (polar coordinates simplify the X and Y axis PIDs and are normalized to grads to represent the whole uArm range by all axes scaled by a +/- 100 range). It can then pick up a single selected class of common objects labeled from the COCO dataset (80 classes) and a bunch of goodies (see software/jetson/fastmot/), using neural network detection feedback from a camera. It then places and drops the object to a predefined location and loops...

## Documentation
Still a work in progress. Early development phase.

## Compile code and documentation to website
To compile and deploy parts of previously commented code as a website on readthedocs or locally, click the link below.
Note: Since the impact of this on my notes was minimal and the code commenting required was time-consuming, not all documentation will be displayed to the website.

[Install documentation as website](https://docs.readthedocs.io/en/stable/development/install.html)

## Mechanics
<img src="documentation/doc/assembly.gif" width="640"/>
The *.STL files can be 3D-printed.
This has not been attempted as I would lack the time to assemble the parts.
It is available though.

## Simulation
The *.STL files can be converted to *.URDF for simulation using a physics engine like Gazebo (or displayed using RVIZ) in ROS Kinetic, all within Docker (see instructions in software/jetson/jetson-containers/README.md).
If you add the Moveit plugins, simulation can run with the uARM in tandem. If you then add openai-gym to the ROS container, you can plug this environment to [FERM](https://github.com/PhilipZRH/ferm), replacing the xArm by the uArm. This was plan C, which has not been completed, as focus shifted towards implementing plans A and B. I have only ran physical and simulation movements separately in ROS and put the plan aside for lack of time and points.

## Electronics
<img src="electronics/Project Outputs for uARM/OSHPARK/top_layer.png" width="640"/>
The minimalistic Printed Circuit Board features an ESP32 as the motor-driving microcontroller.
Altium design files are provided in the electronics/ folder. A standard ESP32-WROOM-32 module is the microcontroller. A CP2109 USB to serial chip is used to program it and transfer data from a Micro-USB connector. An unused SD card slot is available if more external memory is required. A MCP16311T-E/M step-down regulator taps 12 volts from the jack barrel connector to provide the 5 volts servomotors need to function. A fixed output Complementary Metal Oxide Semiconductor Low-Dropout regulator (TC1264) taps 5 volts from the USB connector to provide 3.3 volts for the other circuits. One Light Emitting Diode confirms that regulator provides the 3.3 volts. There is one GPIO-controllable LED and one push button plugged on another GPIO. Another push button is plugged to the EN pin for enabling the ESP32-WROOM-32 module.

## Software
There is PC-compatible (Windows, MACOSX, Linux, Raspbian, other ARM flavors, etc.) software with drivers to program and deploy the environment for commanding everything from the Jetson (or computer). Firmware for the PCB (compatible with a number of architectures) is located in software/arduino-1.8.13/.
The main code was tested on PC and Jetson for easier modular tests while integrating.

## Firmware
The firmware is portable across Arduino boards (it runs on AVR, SAM, SAMD, NRF52, STM32F4, ESP32 and ESP32-S2 microcontrollers). Only pin definitions in software/arduino-1.8.13/portable/sketchbook/libraries/UArmForArduino/src/uArmPins.h need to be redefined. The script in software/jetson/install/flash_firmware_custom.sh automates the flashing process. See software/arduino-1.8.13/portable/sketchbook/libraries/UArmForArduino/README.md for more explanations.

## ArduCAM Camarray or Raspberry Pi camera v2.1 (your choice, but the RPi cam is less expansive and requires less installs)
An automated installation procedure and seemless handling for the driver code, all compatible with V4L2 and Gstreamer frameworks, allowing faster, easier and interchangeable inference using images, videos, a few network streaming protocols, V4L2-supported cameras (MIPI, USB, etc), etc., all accessible using the same interface.

## Custom uARM GCODE-based serial port controller in Python-3.7
A custom controller communicating with the uARM firmware using a GCODE protocol through a USB connection to the serial port provides grad-scaled absolute polar coordinate positioning for easy control. There is bicubic easing, a slowmove extension, calibration, movement recording and replay, etc.

## Multi-threading and multi-process management
For faster and simpler parallel handling of the whole ecosystem, the main entrypoint process loop runs with parallel programs excluding the manager loop: the main camera/inference loop, a PID controller for the X axis, a PID controller for the Y axis and the uARM control process. Camera input is optionally threaded in 4 ways (no threading, video get, video show and both).

## Accelerated inference using TensorRT and Numba, deployable on Nvidia Jetson platforms
A platform featuring YOLOv4-mish-640, KLT optical flow tracking, camera motion compensation, a Kalman filter, data association (...), with instructions for training and evaluation and deployable inference on an Nvidia Jetson (Nano or AGX Xavier) using TensorRT and Numba.

<details><summary><b>CLICK ME</b> - Hardware prerequisites</summary>

##### Prerequisites for the Jetson Nano
    - Micro SD card with at least 16Gb of storage
    - Ubuntu host PC* with SD card slot or USB SD card reader/writer
    - Jetson Nano Dev Kit with micro USB power supply (at least 5V, 2A) or DC power supply (5V 4A)
    - Full HD display with HDMI
    - Keyboard and mouse
    - Ethernet cable connected to the Internet, or USB Wi-Fi adapter
    - Either an Arducam camera array hat, or the Raspberry Pi camera v2.1 (recommended)

* You can use a Windows host PC to flash the microSD card instead, however this tutorial uses Ubuntu as it’s a simpler process. See NVIDIA’s guide for a Windows option.
</details>

<details><summary><b>CLICK ME</b> - Software prerequisites</summary>
- CUDA >= 10
- cuDNN >= 7
- TensorRT >= 7
- OpenCV >= 3.3
- PyCuda
- Numpy >= 1.15
- Scipy >= 1.5
- TensorFlow < 2.0 (for SSD support)
- Numba == 0.48
- cython-bbox
- pyserial
</details>

<details><summary><b>CLICK ME</b> - Hardware instructions for the Jetson Nano Devkit B01 (previous board revision also shown)</summary>

<img src="documentation/doc/nano.png" width="640"/>

- Insert the microSD card into the appropriate slot
- Connect the display and USB keyboard /mouse and Ethernet cable.
- Depending on the power supply you want to use, you may have to add or remove the jumper for power selection:
- If using a jack, the jumper must be set.
- If using USB, the jumper must be off.
- Plug in the power supply. The green LED (D53) close to the micro USB port should turn green, and the display should show the NVIDIA logo before booting begins.
- You will want to install a jumper on J48 to power with the jack barrel
</details>

<details><summary><b>CLICK ME</b> - Installation From Scratch Instructions for Linux (skip down to "Download and install the live *.iso" if installing Linux is needed and get back here just after the install)</summary>

##### Dependencies
    None which aren't covered by this guide.

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
</details>

<details><summary><b>CLICK ME</b> - Download and install the live *.iso of Ubuntu 18.04.5 LTS for x86_64 (from here https://unetbootin.github.io)</summary>

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
</details>

<details><summary><b>CLICK ME!</b> - Flash uArm firmware</summary>
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
</details>

<details><summary><b>CLICK ME!</b> - Jetson Nano or AGX Xavier Devkit install instructions (JetPack-4.4)</summary>
### If using the Nvidia Jetson AGX Xavier Devkit, sign in to install Nvidia's sdkmanager from https://developer.nvidia.com/nvsdk-manager

### Else if using the Nvidia Jetson Nano Devkit, flash the Micro-SD card and then plug the Micro-SD card in the device's slot
```
$ cd software/jetson && bash install/install_jetson_nano_sd_card.sh
```

### Either follow the instructions on the monitor or type this below, after plugging in a mouse, a keyboard, a HDMI screen and the network connector type you have chosen
```
$ screen /dev/ttyACM0
```

#### If it can't SSH into the Jetson, you have skipped the above step; redo it and the install will resume after

##### Create workspace directory on the Jetson (from the x86_64)
```
$ ssh sam@192.168.55.1 'mkdir -p ~/workspace'
```

##### Prepare directories on the Jetson (from the x86_64)
```
$ scp -r ~/workspace/TSO_project/software/jetson sam@192.168.55.1:/home/sam/workspace
```

##### Install Jetson prerequisites (replace <JETSON_PASSWORD> with your Jetson user's password)
```
$ ssh -t sam@192.168.55.1 'cd ~/workspace/jetson && bash install/install_jetson.sh <JETSON_PASSWORD>'
```
</details>

<details><summary><b>CLICK ME</b> - Docker install for Ubuntu 18.04 on Jetson (not necessary)</summary>
Make sure to have [nvidia-docker](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#docker) installed. The image requires an NVIDIA Driver version >= 450. Build and run the docker image:
  ```
  $ cd ~/workspace/jetson
  $ docker build -t project:latest .
  $ docker run --rm --gpus all -it -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY project:latest
  ```
</details>

<details><summary><b>CLICK ME</b> - Inference</summary>

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
</details>

<details><summary><b>CLICK ME</b> - Pre-trained models</summary>

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

### Yolo v3 models
* [csresnext50-panet-spp-original-optimal.cfg](https://raw.githubusercontent.com/AlexeyAB/darknet/master/cfg/csresnext50-panet-spp-original-optimal.cfg) - **65.4% mAP@0.5 (43.2% AP@0.5:0.95) - 32(R) FPS** - 100.5 BFlops - 217 MB: [csresnext50-panet-spp-original-optimal_final.weights](https://drive.google.com/open?id=1_NnfVgj0EDtb_WLNoXV8Mo7WKgwdYZCc)

* [yolov3-spp.cfg](https://raw.githubusercontent.com/AlexeyAB/darknet/master/cfg/yolov3-spp.cfg) - **60.6% mAP@0.5 - 38(R) FPS** - 141.5 BFlops - 240 MB: [yolov3-spp.weights](https://pjreddie.com/media/files/yolov3-spp.weights)

* [csresnext50-panet-spp.cfg](https://raw.githubusercontent.com/AlexeyAB/darknet/master/cfg/csresnext50-panet-spp.cfg) - **60.0% mAP@0.5 - 44 FPS** - 71.3 BFlops - 217 MB: [csresnext50-panet-spp_final.weights](https://drive.google.com/file/d/1aNXdM8qVy11nqTcd2oaVB3mf7ckr258-/view?usp=sharing)

* [yolov3.cfg](https://raw.githubusercontent.com/AlexeyAB/darknet/master/cfg/yolov3.cfg) - **55.3% mAP@0.5 - 66(R) FPS** - 65.9 BFlops - 236 MB: [yolov3.weights](https://pjreddie.com/media/files/yolov3.weights)

* [yolov3-tiny.cfg](https://raw.githubusercontent.com/AlexeyAB/darknet/master/cfg/yolov3-tiny.cfg) - **33.1% mAP@0.5 - 345(R) FPS** - 5.6 BFlops - 33.7 MB: [yolov3-tiny.weights](https://pjreddie.com/media/files/yolov3-tiny.weights)

* [yolov3-tiny-prn.cfg](https://raw.githubusercontent.com/AlexeyAB/darknet/master/cfg/yolov3-tiny-prn.cfg) - **33.1% mAP@0.5 - 370(R) FPS** - 3.5 BFlops - 18.8 MB: [yolov3-tiny-prn.weights](https://drive.google.com/file/d/18yYZWyKbo4XSDVyztmsEcF9B_6bxrhUY/view?usp=sharing)

### Yolo v2 models
* `yolov2.cfg` (194 MB COCO Yolo v2) - requires 4 GB GPU-RAM: https://pjreddie.com/media/files/yolov2.weights
* `yolo-voc.cfg` (194 MB VOC Yolo v2) - requires 4 GB GPU-RAM: http://pjreddie.com/media/files/yolo-voc.weights
* `yolov2-tiny.cfg` (43 MB COCO Yolo v2) - requires 1 GB GPU-RAM: https://pjreddie.com/media/files/yolov2-tiny.weights
* `yolov2-tiny-voc.cfg` (60 MB VOC Yolo v2) - requires 1 GB GPU-RAM: http://pjreddie.com/media/files/yolov2-tiny-voc.weights
* `yolo9000.cfg` (186 MB Yolo9000-model) - requires 4 GB GPU-RAM: http://pjreddie.com/media/files/yolo9000.weights

### Multimedia testing usage
- USB webcam:
  ```
  $ python3 app.py --input_uri /dev/video0 --mot
  ```
- MIPI CSI camera:
  ```
  $ python3 app.py --input_uri csi://0 --mot
  ```
- RTSP stream:
  ```
  $ python3 app.py --input_uri rtsp://<user>:<password>@<ip>:<port>/<path> --mot
  ```
- HTTP stream:
  ```
  $ python3 app.py --input_uri http://<user>:<password>@<ip>:<port>/<path> --mot
  ```
- Image sequence:
  ```
  $ python3 app.py --input_uri img_%06d.jpg --mot
  ```
- Video file:
  ```
  $ python3 app.py --input_uri video.mp4 --mot
  ```
- Use `--gui` to visualize and `--output_uri` to save output
- To disable the GStreamer backend, set `WITH_GSTREAMER = False` [here](https://github.com/GeekAlexis/FastMOT/blob/3a4cad87743c226cf603a70b3f15961b9baf6873/fastmot/videoio.py#L11)
- Note that the first run will be slow due to Numba compilation

### More options can be configured in cfg/mot.json
  - Set `resolution` and `frame_rate` that corresponds to the source data or camera configuration (optional). They are required for image sequence, camera sources, and MOT Challenge evaluation. List all configurations for your USB/CSI camera:
    ```
    $ v4l2-ctl -d /dev/video0 --list-formats-ext
    ```
  - To change detector, modify `detector_type`. This can be either `YOLO` or `SSD`
  - To change classes, set `class_ids` under the correct detector. Default class is `1`, which corresponds to person
  - To swap model, modify `model` under a detector. For SSD, you can choose from `SSDInceptionV2`, `SSDMobileNetV1`, or `SSDMobileNetV2`
  - Note that with SSD, the detector splits a frame into tiles and processes them in batches for the best accuracy. Change `tiling_grid` to `[2, 2]`, `[2, 1]`, or `[1, 1]` if a smaller batch size is preferred
  - If more accuracy is desired and processing power is not an issue, reduce `detector_frame_skip`. Similarly, increase `detector_frame_skip` to speed up tracking at the cost of accuracy. You may also want to change `max_age` such that `max_age × detector_frame_skip ≈ 30`

</details>

<details><summary><b>CLICK ME</b> - Track custom classes</summary>
FastMOT supports multi-class tracking and can be easily extended to custom classes (e.g. vehicle). You need to train both YOLO and a ReID model on your object classes. Check [Darknet](https://github.com/AlexeyAB/darknet) for training YOLO and [fast-reid](https://github.com/JDAI-CV/fast-reid) for training ReID. After training, convert the model to ONNX format and place it in fastmot/models. To convert YOLO to ONNX, use [tensorrt_demos](https://github.com/jkjung-avt/tensorrt_demos/blob/master/yolo/yolo_to_onnx.py) to be compatible with the TensorRT YOLO plugins.
### Add custom YOLOv3/v4
1. Subclass `YOLO` like here: https://github.com/GeekAlexis/FastMOT/blob/4e946b85381ad807d5456f2ad57d1274d0e72f3d/fastmot/models/yolo.py#L94
    ```
    ENGINE_PATH: path to TensorRT engine (converted at runtime)
    MODEL_PATH: path to ONNX model
    NUM_CLASSES: total number of classes
    LETTERBOX: keep aspect ratio when resizing
               For YOLOv4-csp/YOLOv4x-mish, set to True
    NEW_COORDS: new_coords parameter for each yolo layer
                For YOLOv4-csp/YOLOv4x-mish, set to True
    INPUT_SHAPE: input size in the format "(channel, height, width)"
    LAYER_FACTORS: scale factors with respect to the input size for each yolo layer
                   For YOLOv4/YOLOv4-csp/YOLOv4x-mish, set to [8, 16, 32]
                   For YOLOv3, set to [32, 16, 8]
                   For YOLOv4-tiny/YOLOv3-tiny, set to [32, 16]
    SCALES: scale_x_y parameter for each yolo layer
            For YOLOv4-csp/YOLOv4x-mish, set to [2.0, 2.0, 2.0]
            For YOLOv4, set to [1.2, 1.1, 1.05]
            For YOLOv4-tiny, set to [1.05, 1.05]
            For YOLOv3, set to [1., 1., 1.]
            For YOLOv3-tiny, set to [1., 1.]
    ANCHORS: anchors grouped by each yolo layer
    ```
    Note that anchors may not follow the same order in the Darknet cfg file. You need to mask out the anchors for each yolo layer using the indices in `mask` in Darknet cfg.
    Unlike YOLOv4, the anchors are usually in reverse for YOLOv3 and tiny
2. Change class labels [here](https://github.com/GeekAlexis/FastMOT/blob/master/fastmot/models/label.py) to your object classes
3. Modify cfg/mot.json: set `model` in `yolo_detector` to the added Python class and set `class_ids` you want to detect. You may want to play with `conf_thresh` based on the accuracy of your model
### Add custom ReID
1. Subclass `ReID` like here: https://github.com/GeekAlexis/FastMOT/blob/aa707888e39d59540bb70799c7b97c58851662ee/fastmot/models/reid.py#L51
    ```
    ENGINE_PATH: path to TensorRT engine (converted at runtime)
    MODEL_PATH: path to ONNX model
    INPUT_SHAPE: input size in the format "(channel, height, width)"
    OUTPUT_LAYOUT: feature dimension output by the model (e.g. 512)
    METRIC: distance metric used to match features ('euclidean' or 'cosine')
    ```
2. Modify cfg/mot.json: set `model` in `feature_extractor` to the added Python class. You may want to play with `max_feat_cost` and `max_reid_cost` - float values from `0` to `2`, based on the accuracy of your model
</details>

<details><summary><b>CLICK ME</b> - Last steps</summary>

##### Download VOC dataset for INT8 calibration
Only required if you want to use SSD (not in this case)
```
$ install/download_data.sh
```

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
</details>

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
- software/jetson/jetson-containers/README.md
- software/arduino-1.8.13/portable/sketchbook/libraries/UArmForArduino/README.md
- software/arduino-1.8.13/portable/sketchbook/libraries/Servo/docs/readme.md
- software/arduino-1.8.13/portable/sketchbook/libraries/ESP32Servo/README.md
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

### Convert webpages to markdown for viewing on Github
[[HTML-to-Markdown]](http://heckyesmarkdown.com/)

### STL to GIF
[[STL to GIF]](https://github.com/DAguirreAg/STL-to-gif)

## Reference papers

[[Yolov3 paper]](https://arxiv.org/abs/1804.02767)
[[Yolov4 paper]](https://arxiv.org/abs/2004.10934)
[[SPP paper]](https://arxiv.org/abs/1406.4729)
[[CSPNet paper]](https://arxiv.org/abs/1911.11929)

