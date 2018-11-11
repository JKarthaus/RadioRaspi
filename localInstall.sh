#!/bin/bash

# Pre Install these Python tools

if [ "$EUID" -ne 0 ]
  then echo "Please run the Script via sudo or as root"
  exit
fi

echo "install python tools"
apt-get install python-smbus i2c-tools python-pip python-blinkt

echo "numpy is required for illumination"
pip install numpy

echo "set shutdown Display links"
ln -s /home/volumio/lcd/lcdShutdown.service /etc/systemd/system/halt.target.wants/lcdShutdown.service
ln -s /home/volumio/lcd/lcdShutdown.service /etc/systemd/system/poweroff.target.wants/lcdShutdown.service

echo "install mpcLCD service"
cp /home/volumio/mpcLcdService /etc/init.de
echo "Set mpcLcdService as default start Service"
update-rc.d mpcLcdService defaults


