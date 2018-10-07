#!/bin/bash

# Pre Install these Python tools

echo "install python tools"
sudo apt-get install python-smbus i2c-tools

echo "set shutdown Display links"
sudo ln -s /home/volumio/lcd/lcdShutdown.service /etc/systemd/system/halt.target.wants/lcdShutdown.service
sudo ln -s /home/volumio/lcd/lcdShutdown.service /etc/systemd/system/poweroff.target.wants/lcdShutdown.service

echo "install mpcLCD service"
sudo copy mpcLcdService /etc/init.de
sudo update-rc.d mpcLcdService defaults


