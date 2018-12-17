#!/usr/bin/env python

import colorsys
import math
import time

from sys import exit
import signal

class GracefulKiller:
  kill_now = False
  def __init__(self):
    signal.signal(signal.SIGINT, self.exit_gracefully)
    signal.signal(signal.SIGTERM, self.exit_gracefully)

  def exit_gracefully(self,signum, frame):
    self.kill_now = True

import blinkt

blinkt.set_clear_on_exit()

hue_range = 120
hue_start = 0
max_brightness = 0.2
killer = GracefulKiller()

def show_graph(v, r, g, b):
    v *= blinkt.NUM_PIXELS
    for x in range(blinkt.NUM_PIXELS):
        hue = ((hue_start + ((x / float(blinkt.NUM_PIXELS)) * hue_range)) % 360) / 360.0
        r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(hue, 1.0, 1.0)]
        if v < 0:
            brightness = 0
        else:
            brightness = min(v, 1.0) * max_brightness

        blinkt.set_pixel(x, r, g, b, brightness)
        v -= 1

    blinkt.show()


blinkt.set_brightness(0.1)

while True:
    
    if killer.kill_now:
        blinkt.clear
        break

    t = time.time() * 2
    v = (math.sin(t) + 1) / 2  # Get a value between 0 and 1
    show_graph(v, 255, 0, 255)
    time.sleep(0.01)
