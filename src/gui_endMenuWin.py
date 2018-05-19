import sys

import PIL.Image

from LevelParser import *
from gui_button import gui_button

try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *

class gui_endMenuWin(object):
    
    def __init__(self, width, height, canvas, root):
        self.c = canvas
        self.c.focus_set()
        self.root = root
        self.update()
        self.root.mainloop()
        return
    
    def update(self):
        self.c.pack()
        self.root.after(10, self.update)
        return

    
    def deleteAll(self):
        self.c.delete(self.currButton)    
        
    