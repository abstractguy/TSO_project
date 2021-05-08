# uArm Metal Getting Started Guide #

2016.06   
<center>
![](img/getting_started/01-cover.jpg)
</center>

## Notice
This is a basic guide for uArm beginners.   
If you want to explore more by programming, please visit the [uArm Metal Developer Guide](https://drive.google.com/open?id=0B-L-tCvknXU9YlIyemVwRldZc1U)

# Table of Content
1. [Safety Instructions](#Safety)
2. [uArm Metal Parts List](#Parts)
3. [Assembly Instructions](#Assembly)
4. [Operation Instructions](#Operation)  
   4.1 [Preparation](#Preparation)  
   4.2 [Software Installation](#Software)  
   4.3 [Control uArm via uClient](#uClient)
5. [Community Support](#Community)

## Saftey Instructions <a name="Safety"></a>

- Please don’t put your hands in the highlighted area.
<center>![](img/getting_started/02safety.jpg)</center>

- When uArm is moving, please ensure that nothing that may get hurt or broken is within uArm’s moving range.
<center>![](img/getting_started/03working.jpg)</center>


## uArm Metal Parts List <a name="Parts"></a>

<center>Check if you get all of the following parts</center>  

<center>![](img/getting_started/04-intheboxparts.jpg)</center>  
<br>
1. uArm Metal main body  
2. Power Adapter x1  
3. AC Cable x1  
4. Pump x1 (with 2 screws)   
5. USB Cable x1  
6. Foot brackets x 4(with 8 screws)  
7. Screw Driver x1  


## Assembly Instructions <a name="Assembly"></a>

<center>**Step 1** Install the 4 foot brackets</center>
<center>![](img/getting_started/05foot.jpg)</center>
<center>Please be aware the screws should be inserted from the bottom to top.</center>
<br>
<br>
<center>**Step 2** Install the Pump</center>
<center>![](img/getting_started/06screws.jpg)</center>  
<center>2.1 Insert 2 screws to install the pump</center>
<br>
<br>
<center>![](img/getting_started/07pump-pipe.jpg)</center>
<center>2.2 Attach the Cable and the Pipe</center>

## Operation Instructions <a name="Operation"></a>
### Preparation <a name="Preparation"></a>
1. Power On
<center>![](img/getting_started/08power.jpg)</center>
<center>If the RED light is on, the uArm is powered.</center>
<br>
2. Connect uArm to computer with USB
<center>![](img/getting_started/09USB.jpg)</center>

### Software Installation <a name="Software"></a>
The installation method on Windows, MacOS and Linux are different. Please directly go to the section relevant to you.

1. [Windows](#Windows)  
2. [MacOS](#MacOS)  
3. [Linux](#Linux)

#### Windows <a name="Windows"></a>

##### Step 1 - Download

Please download the following softwares from the [official download page](https://ufactory.cc/en/uarm_metal?tag=download#support):  

- **Driver** - You need to install this driver before you start everything on Windows
- **uClient** - the software that you operate to control the movement of uArm
- **Firmware Helper** - to enable uArm to recognize the operations you made via uClient
    Upgrade your firmware.


##### Step 2 - Intall the Driver  
<br>
<center>![](img/getting_started/10driver-1.png)</center>
<center>**Step 2.1** - unzip the driver file and run _driver.exe_</center>
<br>
<br>
<center>![](img/getting_started/10driver-2.png)</center>
<center>![](img/getting_started/10driver-3.png)</center>  

<center>**Step 2.2** - Follow the instructions to install the driver.</center>


##### Step 3 – Ensure the firmware is the latest version

<center>![](img/getting_started/11firmware-1.png)</center>
<center>**Step 3.1** – unzip the firmware file and run *firmware_helper_exe*</center>
<br>
<center>![](img/getting_started/11firmware-win-check.jpg)</center>
<center>**Step 3.2** – Check the firmware & ensure it is the lastest version</center>

- You will get your uArm port No. and whether your firmware is the latest version at this step.  
- If the firmware is not the latest, enter "Y" to update.  
- After that, Press Enter to Exit.  
<br>

##### Step 4 – Prepare JRE for uClient (for first-time users)

<center>![](img/getting_started/12-uclient1.png)</center>
<center>**Step 4.1** – Click on uClient.exe to launch the APP</center>

<center>![](img/getting_started/12-uclient2.png)</center>
<center>![](img/getting_started/12-uclient3.png)</center>

<center>**Step 4.2** – Download JRE (for first-time users)</center>  
- You will be asked to download JRE (Java Runtime Environment) IF your computer does not
have one.
- Press OK , download JRE, and run the exe
- This download requirement will not pop up again after you finish JRE setup.

<br>
<br>
#### MacOS <a name="MacOS"></a>

##### Step 1 - Open `terminal.app`  
<br>
<center>![](img/getting_started/macinstall-terminal.png)</center>
<center>Search `terminal.app` via Spotlight Search</center>

##### Step 2 - Enter Command to Start Installation

**Step 2.1 Copy & paste the command below to install uArm Enviroment:**

`
    bash -c "$(curl -fsSL http://download.ufactory.cc/tools/macosx/install.sh)"
`

**Notice:**  
If you are installing for the first time, you may be asked to install **Xcode**. Please follow the instruction to install.

<center>![](img/getting_started/mac-01.jpg)</center>  
<br>
<center>![](img/getting_started/mac03.jpeg)</center>
<br>
<br>
<br>
**Step 2.2 When the installation is finished, you will see the words below:**
<center>![](img/getting_started/macinstall04_finish_install.png)</center>
<br>
**Step 2.3 After installation, you could use commands below:**    
- `uarm-firmware` - upgrade your uArm firmware  
- `uarm-listport` - show all connected uArm  
<br>
<center>![](img/getting_started/mac04.jpg)</center>

##### Step 3 - Download uClient
**Please download uClient from our official website.**  
<center>![  ](img/getting_started/mac-changeprivacy.png)</center>
Change the privacy setting on your Mac  
(or you are not able to run uClient)
<br>
<br>
<center>![  ](img/getting_started/mac-uclient_folder.png)  
Run `uarm_client.exe` and have fun!</center>


<br>
#### Linux <a name="Linux"></a>

##### Step 1 Install pip & avrdude
Before installing the uArm Environment, you need to install:
- pip
- avrdude

via your **Package Management Tool** (`apt`, `yum`, etc):

Example:  
`
sudo apt-get install python-pip python-dev build-essential avrdude
`

##### Step 2 Install uArm Environment
Input the command below to install:

```
pip install pyuarm
```

Done!   
You could use following commands in your future usage:
- `uarm-firmware` - upgrade your uArm firmware   
- `uarm-listport` - show all connected uArm  

<br>
### Control uArm via uClient <a name="uClient"></a>
#### Step 1 – Select the right COM and Click *Connect*

<center>![](img/getting_started/12-uclient4.png)</center>

- COM No. for uArm may vary.  
- Click *Rescan* if uClient does not detect the COM for uArm.  
- If there are blue lights flashing, uArm is connected with uClient, and you don’t need to click
*Connect* again.

#### Step 2 – Familiarize with uClient
<center>![](img/getting_started/13-uclient5.png)</center>


**1 － Control uArm movement along X, Y, Z Axis.**  
<br>
**2 － Control the end-effector (Suction Cup/Gripper/Universal Holder)**  


＊ You may rotate the suction cup from 0° to 180° by moving the yellow line. Rotation does not
apply to Gripper or Universal Holder.  

＊ Click *Catch/Release* to pick/release (for suction cup) or grab/release (for gripper).
*Catch/Release* does not apply to Universal Holder

**3 － Leap Motion Control (alternative to mouse control)**  

IF you have a Leap Motion Controller, you may control uArm in this way.
<center>![](img/getting_started/15_leap_motion4.png)</center>
<br>
**To enable Leap Motion Control, please:**  

① Connect Leap Motion Controller to PC, and tick the box in uClient  

② Place the Leap Motion Controller in a way that you are facing the flashing GREEN light
<center>![](img/getting_started/15_leap_motion2.jpg)</center>
<br>
③ Ensure that you have downloaded Leap Motion APP (for PC)

**Leap Motion is activated when the uClient interface displays the following:**  
<center>![](img/getting_started/15_leap_motion3.png)</center>
<center>You may change the minimum Z value of Leap Motion Control.</center>
<br>
**4 － You may reset uArm to the default position.**  

## Community Support <a name="Community"></a>

<center>Welcome to the uArm Community!</center>
<br>
<center>[FAQ]()</center>
<br>
<center>[Customer Service](http://customer.ufactory.cc/)</center>
<br>
<center>[Developer Guide](https://drive.google.com/open?id=0B-L-tCvknXU9YlIyemVwRldZc1U)</center>
<br>
<center>[Official Forum](https://forum.ufactory.cc/)</center>
<br>
<center>[Reddit](https://www.reddit.com/r/uArm ) | [Youtube](https://www.youtube.com/channel/UCyy5ekYtq35jFtPpY3O_tVA ) | [Facebook](https://www.facebook.com/Ufactory2013) | [Twitter](https://twitter.com/UFACTORY_UF ) | [Instagram](https://www.instagram.com/ufactoryofficial/)</center>
