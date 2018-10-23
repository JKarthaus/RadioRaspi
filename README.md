# RadioRaspi

![RadioRaspi](http://www.joern-karthaus.de/blog/img/radio/radio7.jpg)

This Respository contains some Pyhton Code that I have build on Top of my **RadioRaspi** 
Project.

I have a more detailed Build Story on my Blog in *German* Language.

http://www.joern-karthaus.de/blog/radioRaspi.html

I use this Components inside the RadioRaspi

* **CPU** Raspberry Pi V3
* **DAC (Soundcard)** https://www.hifiberry.com/products/digiplus
* **Storage** 2 1/2 Inch USB3 Harddisk
* **Display** 2 ROW LCD https://tutorials-raspberrypi.de//hd44780-lcd-display-per-i2c-mit-dem-raspberry-pi-ansteuern/
* **Illumination** Powered by blinkt https://shop.pimoroni.de/products/blinkt

##mpcLcdParser Service
The **mpdLcdParserService** parses mpc Output to extract the actual playing **Title** and **Album**
And Display this Information at the LCD Display.

##background Service
The **backgroundservice** controls the **Blinkt** Modul

