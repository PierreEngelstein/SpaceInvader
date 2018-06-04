#
# This file is subject to the terms and conditions defined in
# file 'LICENSE.txt', which is part of this source code package.
#

#A simple level parser.
import os.path, sys
from LevelParser import *

class GameParser(object):
    def __init__(self, fileToRead):
        self.ftr = fileToRead
        self.currentLevel = 0
        if(not os.path.exists(fileToRead)):
            print("Error : input file does not exists. Please give an existing file !")
            sys.exit(0)
        extension = os.path.splitext(fileToRead)[1]
        if(extension != ".game"):
            print("Error : Can't read " + extension + " files. Please give a '.game' file.")
            sys.exit(0)
        self.f = open(fileToRead, 'r')
        self.message = self.f.read()
        self.levelListConf = []
    
    def parseFile(self):
        with open(self.ftr) as fp:  
           line = fp.readline()
           while line:
               print("Loading level " + line.strip())
               lvlParse = LevelParser(line.strip())
               lvlConf = lvlParse.parseFile()
               line = fp.readline()
               self.levelListConf.append(lvlConf)
        return self.levelListConf
            
class GameConfig(object):

    def __init__(self, levelName, nbCol, speed, border, alienList, nbLocations):
        self.levelName = levelName
        self.nbCol = nbCol
        self.speed = speed
        self.border = border
        self.alien = alienList
        self.nbLocations = nbLocations

gp = GameParser("resources/levels/game1.game")
gp.parseFile()