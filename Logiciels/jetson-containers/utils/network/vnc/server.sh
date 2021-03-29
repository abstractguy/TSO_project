sudo apt update
sudo apt install tigervnc-standalone-server tigervnc-viewer
dbus-launch gsettings set org.gnome.Vino authentication-methods "['vnc']"
dbus-launch gsettings set org.gnome.Vino vnc-password $(echo -n "12345sam12345"|base64)
dbus-launch gsettings set org.gnome.Vino alternative-port 5910
dbus-launch gsettings set org.gnome.Vino use-alternative-port true
sudo systemctl enable vinostartup.service
cd /usr/lib/systemd/user/graphical-session.target.wants/
sudo ln -s ../vino-server.service ./.
gsettings set org.gnome.Vino prompt-enabled false
gsettings set org.gnome.Vino require-encryption false
gsettings set org.gnome.Vino authentication-methods "['vnc']"
gsettings set org.gnome.Vino vnc-password $(echo -n '12345sam12345' | base64)
# DISABLE DESKTOP EFFECTS!!!
sudo reboot
vncserver -interface 192.168.55.1
xtigervncviewer -SecurityTypes VncAuth -passwd /home/sam/.vnc/passwd :1
vncserver -kill :1
vncserver -localhost no -geometry 800x600 -depth 24

