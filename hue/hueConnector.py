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
from phue import Bridge


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
    for filename in glob.glob("playlist/hue_*"):
        with open(filename) as playlist_file:
            logger.info("Checking Filename:" + filename)
            parsed_json = json.load(playlist_file)
            for items in parsed_json:
                if items["title"] == songURI :
                    scene = os.path.basename(filename)
                    scene = os.path.splitext(scene)[0]
                    scene = scene[4:]
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
        

def selectHueScene(newScene,group):
    logger.info("Try to switch on Scene : "+ newScene + " on Group: " + group)    

    if checkGroupExists(group) and checkSceneExists(newScene):
        bridge.run_scene(group,newScene)
        logger.info("Starting Scene :" + newScene + " to Group: " + group)



                
if __name__ == '__main__':

    logging.basicConfig(level=logging.DEBUG)
    actualSong = parseActualSong()
    #if actualSong != "NONE":
    #    print parseHuePlaylistsForScene(actualSong)
    #selectHueScene("Rock","Wohnzimmer")
    switchGroupOff("Wohnzimmer")
    pass