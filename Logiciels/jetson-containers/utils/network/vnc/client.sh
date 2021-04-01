# Note: Just a reorganized, untested print of my history.
#       Try line by line. Don't mind redundant or missing stuff until tested.

cd ~
sudo apt update
sudo apt install gvncviewer tigervnc-viewer remmina

gsettings set org.gnome.Vino require-encryption false
dbus-launch gsettings set org.gnome.Vino authentication-methods "['vnc']"
dbus-launch gsettings set org.gnome.Vino vnc-password $(echo -n "12345sam12345"|base64)
dbus-launch gsettings set org.gnome.Vino alternative-port 5910
dbus-launch gsettings set org.gnome.Vino use-alternative-port true

rm -rf ~/.vnc
mkdir -p ~/.vnc
ln -s /etc/ssl/certs/ca-certificates.crt ~/.vnc/x509_ca.pem

mkdir -p ~/.pki/CA
ln -s /etc/ssl/certs/ca-certificates.crt ~/.pki/CA/cacert.pem

ifconfig

xtigervncviewer -SecurityTypes VncAuth,TLSVnc -passwd /home/sam/.vnc/passwd 192.168.55.1:1
xtigervncviewer -SecurityTypes VncAuth,TLSVnc -passwd /home/sam/.vnc/passwd 192.168.55.1:2

vncviewer 192.168.55.1:2
vncviewer 192.168.55.1:1

gvncviewer 192.168.55.1 --display=:1
sudo gvncviewer 192.168.55.1 --display=:1

remmina

