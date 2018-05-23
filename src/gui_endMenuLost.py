<<<<<<< Updated upstream
import sys

import PIL.Image

=======
import PIL.Image
import sys

>>>>>>> Stashed changes
from LevelParser import *
from gui_button import gui_button

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
        if goodshots == 0:
            accuracy = 0
        else:
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
        self.currButton = gui_button(x = width/2, y = 550, width = 150, height = 50, text = "Quit",        canvas = self.c, action = self.action_quit,     next = "null" ,          selected = False)
        self.currButton = gui_button(x = width/2, y = 500, width = 150, height = 50, text = "Main Menu",   canvas = self.c, action = self.action_mainMenu, next = self.currButton , selected = True)
        self.update()
        self.root.mainloop()
        return
    
    def update(self):
        self.currButton.draw()
        self.c.bind("<Return>", self.currButton.action)
        self.c.bind("<Down>", self.switchDown)
        self.c.bind("<Up>", self.switchUp)
        self.c.pack()
        self.root.after(10, self.update)
        return

    def switchDown(self, event):
        if (self.currButton.next == 'null'):
            return
        self.currButton.selected = False
        self.currButton.draw()
        self.currButton = self.currButton.next
        self.currButton.selected = True
        
    def switchUp(self, event):
        if (self.currButton.prev == 'null'):
            return
        self.currButton.selected = False
        self.currButton.draw()
        self.currButton = self.currButton.prev
        self.currButton.selected = True
    
    def deleteAll(self):
        self.c.delete(self.currButton)    
    def action_quit(self, event):
        print("Exiting the game")
        sys.exit(0)
    def action_mainMenu(self, event):
        print("AH")
        self.c.destroy()
        self.c = Canvas(self.root, width=1200, height=700, bg='#565656')
        from gui_mainMenu import gui_mainMenu
        mainMenu = gui_mainMenu(width = 1200, height = 700, canvas = self.c, root = self.root)
    