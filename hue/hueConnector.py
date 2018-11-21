'''
Created on 20.11.2018

@author: joern
'''

import logging
import subprocess
import json
import glob

# create logger
logger = logging.getLogger('hueConnector')

def parseActualSong ():
    logger.info("check Actual Playing Song")
    p = subprocess.Popen(["volumio", "status"], stdout=subprocess.PIPE)
    parsed_json = json.loads(p.communicate()[0])
    
    if parsed_json['status'] == "play" :
        return parsed_json['uri']
    else :
        return "NONE"

def parseHuePlaylists(songURI):
    logger.info("Parsing playlists beginning with hue* and Song " + songURI)
    print(glob.glob("/home/joern/git/RadioRaspi/hue/hue_*"))
    
    
if __name__ == '__main__':
    actualSong = parseActualSong()
    if actualSong != "NONE":
        parseHuePlaylists(actualSong)
    
    pass