#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 20.11.2018

@author: joern
'''

import logging
import subprocess
import json
import glob
import os
import time
import signal
from phue import Bridge
from time import sleep


class GracefulKiller:
  kill_now = False
  def __init__(self):
    signal.signal(signal.SIGINT, self.exit_gracefully)
    signal.signal(signal.SIGTERM, self.exit_gracefully)

  def exit_gracefully(self,signum, frame):
    self.kill_now = True



# create logger
logger = logging.getLogger('hueConnector')
bridge = Bridge("192.168.2.119")
# If the app is not registered and the button is not pressed, press the button and call connect()
# (this only needs to be run a single time)
bridge.connect()
# Get the bridge state (This returns the full dictionary that you can explore)
bridge.get_api()


def parseActualSong ():
    logger.info("check Actual Playing Song")
    p = subprocess.Popen(["volumio", "status"], stdout=subprocess.PIPE)
    parsed_json = json.loads(p.communicate()[0])
    
    if parsed_json['status'] == "play" :
        return parsed_json['title']
    else :
        return "NONE"


def parseHuePlaylistsForScene(songURI):
    logger.info("Parsing playlists beginning with hue* and Song " + songURI)
    for filename in glob.glob("/home/volumio/hue/playlist/hue_*"):
        with open(filename) as playlist_file:
            logger.info("Checking Filename:" + filename)
            parsed_json = json.load(playlist_file)
            for items in parsed_json:
                if items["title"] == songURI :
                    scene = os.path.basename(filename)
                    scene = os.path.splitext(scene)[0]
                    scene = "rr_" + scene[4:]
                    return scene
    return "NONE"            


def checkGroupExists(groupName):
    for groups in bridge.groups:
        logger.debug("Found Group:" + groups.name)
        if groups.name == groupName:
            return True
    logger.error("Group : " + groupName + " not found at hue Bridge")
    return False


def checkSceneExists(sceneName):
    for scenes in bridge.scenes:
        logger.debug("Found Scene:" + scenes.name)
        if scenes.name == sceneName:
            return True
    return False


def switchGroupOff(group):
    if checkGroupExists(group):
        bridge.set_group(group, 'on', False)

def switchGroupOn(group):
    if checkGroupExists(group):
        bridge.set_group(group, 'on', True)
        

def selectHueScene(newScene,group):
    logger.info("Try to switch on Scene : "+ newScene + " on Group: " + group)    

    #if checkGroupExists(group) and checkSceneExists(newScene):
    bridge.run_scene(group,newScene)
    logger.info("Starting Scene :" + newScene + " to Group: " + group)



                
if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)

    killer = GracefulKiller()
    logger.info("hueConnector up and running")

    switchGroupOn("radioRaspi")

    time.sleep(10)
    
    while True :
     
        if killer.kill_now:
            logger.info("Service Shutdown requestet -> switch off hue group")
            switchGroupOff("radioRaspi")
            break   
        
        actualSong = parseActualSong()
        
        if actualSong == "NONE":
            selectHueScene("rr_pause","radioRaspi")
        else:
            parsedScene = parseHuePlaylistsForScene(actualSong) 

            if parsedScene == "NONE":
                selectHueScene("rr_play","radioRaspi")
            else: 
               selectHueScene(parsedScene,"radioRaspi")
            
        time.sleep(3)
    
    pass