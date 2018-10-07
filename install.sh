#!/bin/bash

echo "copy lcd directory python Scripts to Radio Raspi"

scp -r lcd volumio@radioRaspi:~


echo "copy Service Script to Radio Raspi"

scp mpcLcdService volumio@radioRaspi:~
