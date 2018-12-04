#!/bin/bash

# Shutting Down RadioRaspi

service mpcLcd stop
service illumination stop

./switchOffLCD.py &


