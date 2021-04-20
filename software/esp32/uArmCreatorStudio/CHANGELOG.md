# CHANGELOG

## V1.2.2
- Update - Alex Tan
- Date - 2016-11-16

## Changes
- Fix Translation for Disconnect Camera & Robot
- Fix `New Function` not Working issue


## V1.2.1
- Update - Alex Tan
- Date - 2016-11-15

## Changes
- Compatible GCode Communication Protocol
- Add Protocol Version

## V1.1.8
- Update - Alex Tan
- Date - 2016-11-14

## Changes
- Fix Switch English language didn't change survey link and user manual docs
- Change Execute icon


## V1.1.7
- Update - Alex Tan
- Date - 2016-11-10

## Changes

- Add Camera and Robot Disconnect
- Add OSType (MAC, LINUX, WINDOWS) detect
- Add Language Detect for User manual pdf
- Add Reset Layout action in File Menu
- Add Translation for function description
- Add Survey menu
- Add Setting menu
- Add Bug Report menu action
- Fix Gripper not working
- Filter useless serial port
- Fix Tooltip not display
- Fix Mac What is This Help Button(use Tooltip instead)
- Fix Object Wizard screen size on low resolution


## V1.1.6
- Update - Alex Tan
- Date - 2016-10-31

## Changes

- Fix Home Folder not exists cause issue
- Compatible with firmware V2.1.4
- Fix Mac force quit if open Camera window
- Fix Prompt save issue

## V1.1.5
- Update - Alex Tan
- Date   - 2016-10-19

## Changes

- Fix prompt save issue after user close
- Fix Test loop Command - Alex Thiel
- Fix RecognizeObjectEvent crash issue
- Catch System Exception to logger
- Add error.log to catch all unchecked exception
- Fix Linux Resources Path issue

## V1.1.4
- Update - Alex Tan
- Date   - 2016-10-14

## Changes

- Fix Mac bundle app crash on startup
- Objects and Save Tasks Location move to `user home directory\uArmCreatorStudio`

## V1.1.3
- Update - Alex Tan
- Date   - 2016-10-13

## Changes

- User could save log to file.
- Program crash would save log to file.
- Add Help menu item to File Menu.

## V1.1.2
- Update - Alex Tan
- Date   - 2016-10-10

## Changes

- Support i18n(internationalization)
    - Detect user system locate load different language packs in first time
    - User can switch lanugages from Menu Items
    - Save Language to settings.txt
- Add About Menu Action to File Menu (display UCS version)
- Rename Robot Firmware folder, Add FlashFirmware tool and firmware hex
- Switch Language from Menu item will prompt user to restart program

## Fix

- Fix User Manual.pdf can not open in Mac & Linux
- Disable Native Menu, Fix Mac Menu issue

## To-Do

- Switching Language restart & Save User Task
- UCS version and firmware version compatible mechanism
