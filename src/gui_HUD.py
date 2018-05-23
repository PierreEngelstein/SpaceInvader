import sys

import PIL.Image
import platform
from LevelParser import *
from gui_button import gui_button

try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *

if platform.system() == "Windows":
    import tkinter.font as FONT
elif platform.system() == "Linux":
    try:
        # for Python2
        import tkFont as FONT
    except ImportError:
        # for Python3
       import tkinter.font as FONT

class gui_HUD(object):
    
    def __init__(self, display):
        self.display = display
        self.c = self.display.c
        
        self.font = FONT.Font(family = "Courier new", size = 20, weight = "normal")
        self.debugFont = FONT.Font(family = "Courier new", size = 12, weight = "normal")
        
        self.time_text  = self.c.create_text(50, self.display.h - 50, fill = "white", anchor = "nw", text = "Current time played ", font=self.font)
        self.score_text = self.c.create_text(self.display.w - 200, self.display.h - 50, fill = "white", anchor = "nw", text = "Player experience : ", font=self.font)
        self.debug_text = self.c.create_text(10, 10, fill = "white", anchor = "nw", text = "", font=self.debugFont)
        self.debugBackground = "null"
        self.debug = False
        return
    
    def update(self):
        time_played = int((int(round(self.display.t.time() * 1000)) - self.display.startTime)/1000)
        hours = time_played/3600
        minutes = (time_played%3600)/60
        seconds = time_played%60
        self.c.itemconfig(self.time_text, text = "Current time played : " + str(hours) + "h " + str(minutes) + "min " + str(seconds) + "s")
        self.c.itemconfig(self.score_text, text = "Player experience : " + str(self.display.player.score))
        
        if(self.debug == True):
            debugStr = "Debug menu\n"
            debugStr += "  Monsters left : " + str(len(self.display.enemyList)) + "\n"
            debugStr += "  Bullets on game : " + str(len(self.display.bulletList)) + "\n"
            debugStr += "  Player position : " + str(self.display.player.posx) + "\n"
            debugStr += "  Current level : " + str(self.display.levelName) + "\n"
            self.c.tag_raise(self.debugBackground)
            self.c.tag_raise(self.debug_text)
            self.c.itemconfig(self.debug_text, text = debugStr)
        else:
            self.c.itemconfig(self.debug_text, text = "")
        self.c.pack()
        return
    
    def setDebugMode(self, event):
        self.debug = not self.debug
        if(self.debug == True):
            self.debugBackground = self.c.create_rectangle(0, 0, self.debugFont.measure("  Current level : " + str(self.display.levelName)) + 20, 100, fill = "#565656", stipple="gray50")
        else:
            self.c.delete(self.debugBackground)