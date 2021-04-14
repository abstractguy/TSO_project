#!/bin/sh

pyinstaller Build.spec --clean
cp -r Resources/* dist/uArmCreatorStudio.app/Contents/Resources/
