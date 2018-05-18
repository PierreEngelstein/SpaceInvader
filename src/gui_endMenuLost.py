from gui_button import gui_button
import sys
from LevelParser import *
import PIL.Image
try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *

class gui_endMenuLost(object):
    
    def __init__(self, width, height, canvas, root, kills = 1, shots = 256, goodshots = 254, timer = 36415, score = 0):
        self.c = canvas
        self.c.focus_set()
        self.root = root
        accuracy = 1.0*goodshots / shots
        hours = timer/3600
        minutes = (timer%3600)/60
        seconds = timer%60
        self.c.create_text(width/5, 100, fill = "white", anchor = "nw", text = "Game Over !", font=("Courier new", 40))
        self.c.create_text(width/5, 200, fill = "white", anchor = "nw", text = "Nb of kills : " + str(kills), font=("Courier new", 15))
        self.c.create_text(width/5, 250, fill = "white", anchor = "nw", text = "Nb of shots (hit / total): " + str(goodshots) + " / " + str(shots), font=("Courier new", 15))
        self.c.create_text(width/5, 300, fill = "white", anchor = "nw", text = "Accuracy : " + str(round(accuracy * 100, 2)) + " %", font=("Courier new", 15))
        self.c.create_text(width/5, 350, fill = "white", anchor = "nw", text = "Timer : " + str(hours) + "h " + str(minutes) + "min " + str(seconds) + "s", font=("Courier new", 15))
        self.c.create_text(width/5, 400, fill = "white", anchor = "nw", text = "Final Score : " + str(score), font=("Courier new", 30))
        self.update()
        self.root.mainloop()
        return
    
    def update(self):
        self.c.pack()
        self.root.after(10, self.update)
        return

    
    def deleteAll(self):
        self.c.delete(self.currButton)    
        
    