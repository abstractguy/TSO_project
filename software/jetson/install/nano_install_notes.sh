sudo apt-get update
sudo apt-get -y install screen
wget https://developer.nvidia.com/jetson-nano-sd-card-image-441 -O jetson-nano-4gb-jp441-sd-card-image.zip
unzip jetson-nano-4gb-jp441-sd-card-image.zip
sudo fdisk -l
sudo dd if=sd-blob-b01.img of=/dev/mmcblk0 bs=1M oflag=direct status=progress
#screen /dev/ttyACM0

