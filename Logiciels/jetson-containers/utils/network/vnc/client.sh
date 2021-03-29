sudo apt install tigervnc-viewer
xtigervncviewer -SecurityTypes VncAuth -passwd /home/sam/.vnc/passwd :1
sudo xtigervncviewer -SecurityTypes VncAuth -passwd /home/sam/.vnc/passwd :1
sudo xtigervncviewer -SecurityTypes VncAuth -passwd /home/sam/.vnc/passwd :2
gsettings set org.gnome.Vino require-encryption false
sudo xtigervncviewer -SecurityTypes VncAuth -passwd /home/sam/.vnc/passwd :2
dbus-launch gsettings set org.gnome.Vino authentication-methods "['vnc']"
dbus-launch gsettings set org.gnome.Vino vnc-password $(echo -n "12345sam12345"|base64)
sudo xtigervncviewer -SecurityTypes VncAuth -passwd /home/sam/.vnc/passwd :2
dbus-launch gsettings set org.gnome.Vino alternative-port 5910
dbus-launch gsettings set org.gnome.Vino use-alternative-port true
sudo apt update
sudo apt install gvncviewer tigervnc-viewer remmina
rm -fr ~/.vnc
mkdir -p ~/.vnc
ln -s /etc/ssl/certs/ca-certificates.crt ~/.vnc/x509_ca.pem
mkdir -p ~/.pki/CA
ln -s /etc/ssl/certs/ca-certificates.crt ~/.pki/CA/cacert.pem
xtigervncviewer -SecurityTypes VncAuth,TLSVnc -passwd /home/sam/.vnc/passwd 192.168.55.1:1
vncviewer 192.168.55.1:1
