'''
Created on 20.11.2018

@author: joern
'''

import logging
import subprocess
import json
import glob
import os

# create logger
logger = logging.getLogger('hueConnector')

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


def selectHueScene(scene):
    logger.info("Switch to Scene : ")    

            
if __name__ == '__main__':
    actualSong = parseActualSong()
    if actualSong != "NONE":
        print parseHuePlaylistsForScene(actualSong)
    
    pass