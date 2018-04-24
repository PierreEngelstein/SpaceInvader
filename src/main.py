#Flaaaaag Invader project
#Adrien Chotard, Pierre Engelstein

try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *
from Display import Display
from LevelParser import *

root = Tk()
root.resizable(False, False)
# root.config(cursor="none")
lvlParse = LevelParser("level.txt")
lvlConf = lvlParse.parseFile()
if(lvlConf == 1):
    print ("Zbrah")
else:
    zbrah = 1
    if zbrah == 1 :
        display = Display(width=800, height=600, tkinterRoot=root, lvlConf = lvlConf)
    else :
        display = Display(width=800, height=600, tkinterRoot=root)
