try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *

class gui_button(object):
    def __init__(self, x, y, width, height, text, canvas, next, action, selected = False, txtSize = 20):
        self.x = x - width/2
        self.y = y
        self.width = width
        self.height = height
        self.textSize = txtSize
        self.c = canvas
        self.action = action
        self.selected = selected
        self.next = next
        self.prev = "null"
        self.txt = text
        self.text = self.c.create_text(self.x, self.y, fill = "white", anchor = "nw", text = self.txt, font=("Courier new", self.textSize))
        if(self.next != "null"):
            self.next.prev = self
    
    def draw(self):
        self.c.delete(self.text)
        if(self.selected == True):
            self.text = self.c.create_text(self.x, self.y, fill = "blue", anchor = "nw", text = self.txt, font=("Courier new", self.textSize))
        if(self.selected == False):
            self.text = self.c.create_text(self.x, self.y, fill = "white", anchor = "nw", text = self.txt, font=("Courier new", self.textSize))
        return
    
    def action(self):
        if(self.selected):
            return self.action()