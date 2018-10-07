#!/bin/bash

echo "copy lcd directory python Scripts to Radio Raspi"
scp -r lcd volumio@radioRaspi:~

echo "copy blinkt directory python Scripts to Radio Raspi"
scp -r blinkt volumio@radioRaspi:~


echo "copy Service Script to Radio Raspi"
scp mpcLcdService volumio@radioRaspi:~
scp localInstall.sh volumio@radioRaspi:~
