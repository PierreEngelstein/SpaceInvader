#A simple level parser.
import os.path, sys


class LevelParser(object):
    def __init__(self, fileToRead):
        self.ftr = fileToRead
        if(not os.path.exists(fileToRead)):
            print("Error : input file does not exists. Please give an existing file !")
            sys.exit(0)
        extension = os.path.splitext(fileToRead)[1]
        if(extension != ".spi"):
            print("Error : Can't read " + extension + " files. Please give a '.spi' file.")
            sys.exit(0)
        self.f = open(fileToRead, 'r')
        self.message = self.f.read()
        print(self.message)
    
    def parseFile(self):
        index = 0
        #Header
        self.nbCol = int(self.message[0], 16) + 1 # [1; 16]
        self.speed = int(self.message[1], 16)
        self.border = int(self.message[2], 16)
        if int(self.message[3], 16) > 7:
            return 1
        l = (int(self.message[3], 16)/4)
        i = ((int(self.message[3], 16)/2 - 2*l))
        e = int(self.message[3], 16) - (4*l + 2*i)
        self.lifeSize = int((l+1) * 2) #Encoded with two or four hex
        self.imgSize =  int(i+1) # Encoded with one or two hex
        self.expSize = int((e+1)*2) # Encoded with two or four hex
        print (self.lifeSize, self.imgSize, self.expSize)
        self.alienArrayInterp = []
        index = 4
        nbLocations = 0
        #Ship
        while (self.message[index] + self.message[index + 1] != "F1") :
            nbLocations += 1
            if self.message[index] + self.message[index + 1] == "F3":
                self.alienArrayInterp.append(-1)
                index += 2
            else:
                inindex = 0
                for j in range (0, 3):
                    value = ''
                    if j == 0:
                        currSize = self.lifeSize
                    if j == 1:
                        currSize = self.imgSize
                    if j == 2:
                        currSize = self.expSize
                    for i in range (0, currSize):
                        value = value + self.message[index + inindex]
                        inindex += 1
                        
                    value = int(value, 16)
                    self.alienArrayInterp.append(value)
                
                index += inindex
        lvlConf = LevelConfig(nbCol = self.nbCol, speed = self.speed, border = self.border, alienList = self.alienArrayInterp, nbLocations = nbLocations)
        return lvlConf
            
class LevelConfig(object):

    def __init__(self, nbCol, speed, border, alienList, nbLocations):
        self.nbCol = nbCol
        self.speed = speed
        self.border = border
        self.alien = alienList
        self.nbLocations = nbLocations
        