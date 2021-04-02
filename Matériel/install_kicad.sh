#!/usr/bin/env bash

# Install KiCAD.
sudo add-apt-repository --yes ppa:kicad/kicad-5.1-releases
sudo apt update

# Full install.
sudo apt -y install --install-recommends kicad

# If you want demo projects
sudo apt -y install kicad-demos

# If you prefer a minimal install...
#sudo apt install --no-install-recommends kicad

