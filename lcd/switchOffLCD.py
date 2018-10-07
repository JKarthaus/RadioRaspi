#!/usr/bin/python

import lcddriver
 
 
if __name__ == "__main__": 
    lcd = lcddriver.lcd()
    lcd.lcd_clear()
 
    lcd.lcd_display_string("Radio Raspi", 1)
    lcd.lcd_display_string("Bitte ausschalten", 2)

    print "Radio Raspi is waiting to switch off"
