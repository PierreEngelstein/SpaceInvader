try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *

class gui_button(object):
    def __init__(self, x, y, width, height, text, canvas, next, action, selected = False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.c = canvas
        self.selected = selected
        self.next = next
        self.prev = "null"
        self.txt = text
        self.action = action
        self.text = Message(self.c, text = text, justify=LEFT, width=200, background = "gray").place(x=self.x - self.width / 2, y=self.y - self.height/2, width=self.width, height=self.height)
        if(self.next != "null"):
            self.next.prev = self
    
    def draw(self):
        self.c.delete(self.text)
        if(self.selected == True):
            self.text = Message(self.c, text = self.txt, justify=LEFT, width=200, background = "yellow").place(x=self.x - self.width / 2, y=self.y - self.height/2, width=self.width, height=self.height)
        if(self.selected == False):
            self.text = Message(self.c, text = self.txt, justify=LEFT, width=200, background = "gray").place(x=self.x - self.width / 2, y=self.y - self.height/2, width=self.width, height=self.height)
        return
    
    def action(self):
        if(self.selected):
            return self.action()