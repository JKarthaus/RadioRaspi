#!/bin/bash

# Shutting Down RadioRaspi

service mpcLcdService stop
service illumination stop

./switchOffLCD.py

