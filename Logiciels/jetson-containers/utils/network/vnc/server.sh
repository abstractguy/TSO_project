# Note: Just a reorganized, untested print of my history.
#       Try line by line. Don't mind redundant or missing stuff until tested.

# DISABLE DESKTOP EFFECTS!!!

cd ~
sudo apt update
sudo apt install tigervnc-standalone-server tigervnc-viewer
#vncserver :1
#tigervncserver -xstartup /usr/bin/xterm
#sudo tigervncserver -xstartup /usr/bin/xterm
#x0vncserver -display :0

sudo echo "[Desktop Entry]" > ~/.config/autostart/vino-server.desktop
sudo echo "Type=Application" >> ~/.config/autostart/vino-server.desktop
sudo echo "Name=Vino VNC server" >> ~/.config/autostart/vino-server.desktop
sudo echo "Exec=/usr/lib/vino/vino-server" >> ~/.config/autostart/vino-server.desktop
sudo echo "NoDisplay=true" >> ~/.config/autostart/vino-server.desktop

dbus-launch gsettings set org.gnome.Vino authentication-methods "['vnc']"
dbus-launch gsettings set org.gnome.Vino vnc-password $(echo -n "12345sam12345"|base64)
dbus-launch gsettings set org.gnome.Vino alternative-port 5910
dbus-launch gsettings set org.gnome.Vino use-alternative-port true

cd /etc/systemd/system/
sudo bash -c 'echo "[Unit]" > vinostartup.service'
sudo bash -c 'echo "Description = description about the service" >> vinostartup.service'
sudo bash -c 'echo "After = network.target" >> vinostartup.service'
sudo bash -c 'echo "[Service]" >> vinostartup.service'
sudo bash -c 'echo "ExecStart = /usr/lib/vino/vino-server" >> vinostartup.service'
sudo bash -c 'echo "[Install]" >> vinostartup.service'
sudo bash -c 'echo "WantedBy = multi-user.target" >> vinostartup.service'
sudo systemctl enable vinostartup.service
sudo systemctl start vinostartup.service

cd /usr/lib/systemd/user/graphical-session.target.wants/
sudo ln -s ../vino-server.service ./.
gsettings set org.gnome.Vino prompt-enabled false
gsettings set org.gnome.Vino require-encryption false
gsettings set org.gnome.Vino authentication-methods "['vnc']"
gsettings set org.gnome.Vino vnc-password $(echo -n '12345sam12345' | base64)
sudo reboot

#vncserver -interface 192.168.55.1
#xtigervncviewer -SecurityTypes VncAuth -passwd /home/sam/.vnc/passwd :1
vncserver -kill :3
vncserver -kill :2
vncserver -kill :1
export DISPLAY=:1
xhost +
sudo xhost +
vncserver -localhost no -geometry 800x600 -depth 24

