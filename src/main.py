#Flaaaaag Invader project
#Adrien Chotard, Pierre Engelstein

import sys
sys.dont_write_bytecode = True

try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *

from LevelParser import *
from gui_mainMenu import gui_mainMenu
from gui_endMenuLost import gui_endMenuLost

root = Tk()

root.resizable(False, False)

c = Canvas(root, width=1200, height=700, bg='#565656')
# gui_endMenuLost(width = 800, height = 600, canvas = c, root = root)

mainMenu = gui_mainMenu(width = 1200, height = 700, canvas = c, root = root)

# lvlParse = LevelParser("resources/levels/level2.spi")
# lvlConf = lvlParse.parseFile()
# if(lvlConf == 1):
#     print ("Zbrah")
# else:
#     zbrah = 1
#     if zbrah == 1 :
#         display = Display(width=1200, height=700, tkinterRoot=root, lvlConf = lvlConf)
#     else :
#         display = Display(width=1200, height=700, tkinterRoot=root)
