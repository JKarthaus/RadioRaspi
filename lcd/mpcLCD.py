#!/usr/bin/python

import lcddriver
import time
import os
import signal

class GracefulKiller:
  kill_now = False
  def __init__(self):
    signal.signal(signal.SIGINT, self.exit_gracefully)
    signal.signal(signal.SIGTERM, self.exit_gracefully)

  def exit_gracefully(self,signum, frame):
    self.kill_now = True




def parse_mpc():
    #raw = os.popen('simmpc.sh').read()
    raw = os.popen('mpc').read()
    
    playing=False
    paused=False
    
     
    if raw.find("playing") > 0 :
        playing = True
    
    if raw.find("paused") > 0 :
        paused =True
    
    if not playing and not paused :
        return "Radio","Raspi"
    
    if playing :
        interpret = raw.splitlines()[0].split("-")[0]
        title = raw.splitlines()[0].split("-")[1]
    
    if paused :
        interpret = "Pausiert"
        title = raw.splitlines()[0].split("-")[1]
    
    return title,interpret
    

def writeToLCD(row1,row2): 
    lcd.lcd_clear()
    lcd.lcd_display_string(row1, 1)
    lcd.lcd_display_string(row2, 2)

        
if __name__ == "__main__": 
    
    lcd = lcddriver.lcd()
    killer = GracefulKiller()
   
    print "MPC - parser up and running"

    while True :
     
        if killer.kill_now:
            print "Service Shutdown requestet..."
            break   
        
        titel,interpret = parse_mpc()
        writeToLCD(titel,interpret)
        # print parse_mpc()
        time.sleep(3)