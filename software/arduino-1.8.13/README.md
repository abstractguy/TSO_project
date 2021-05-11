# uarm_arduino

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fabstractguy%2FTSO_project%2Fsoftware%2Farduino-1.8.13&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

##### Arduino IDE compiles portable which runs on Windows, Linux and MacOS is included here. Just run the installer located in the arduino-1.8.13 folder.

#### The main code is in firmware/firmware.ino.

#### The libraries are in portable/sketchbook/libraries/UArmForArduino.

#### The rest are research artifacts which will gradually clean themselves up with time.




## Install ESP-IDF on Windows

#### An installation utility named ESP-IDF Tools Installer is available on Windows.

[Download version 2.3](https://dl.espressif.com/dl/esp-idf-tools-setup-2.3.exe "Permalink to ")


#### The installer includes the compilers, OpenOCD , cmake, and Ninja build tool . The installer can also download and run installers for Python 3.7 and Git for Windows if they are not already installed on the computer.

Official Documentation
[Official Documentation](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/windows-setup.html#get-started-windows-tools-installer "Permalink to ")

## Install on macOS and Linux

#### By default, the tools should be installed in the ~/esp folder

#### Open a Terminal and run these commands to download the repository

```Bash
mkdir ~/esp
cd ~/esp
git clone --recursive https://github.com/espressif/esp-idf.git
```

#### then start the installation

```Bash
cd ~/esp/esp-idf
./install.sh
```

#### Once the installation is complete, it is necessary to declare the paths in the environment variables

```Bash
. $HOME/esp/esp-idf/export.sh
```

## Common mistakes

```Bash
-bash: idf.py: command not found
```

#### The path to the ESP-IDF directory has not been correctly declared

#### Run the following command depending on the environment

#### PowerShell Windows macOS or Linux terminal

```Powershell
.$HOME/esp/esp-idf/export.ps1
```
	
```Bash
. $HOME/esp/esp-idf/export.sh
```




[HOWTO](https://diyprojects.io/programming-esp32-board-arduino-ide-macos-windows-linux-arm-raspberrypi-orangepi/amp/ "Permalink to ")

[HTML-to-Markdown](http://heckyesmarkdown.com/ "Permalink to ")

