from Tkinter import *
from PlayerSpaceship import PlayerSpaceship
class Display(object):

    def __init__(self, width, height, tinkerRoot):
        self.root = tinkerRoot
        self.c = Canvas(self.root, width=width, height=height, bg = "red")
        self.root.title("Test")
        self.player = PlayerSpaceship(50, 50, 50, 50)
        
        self.update()
        self.root.mainloop()
########################################################################

#Main game loop
    def update(self):
#TODO : clear screen/clear trace         
        print("hey")
        self.player.move()
        self.render()
        self.c.pack()
        self.root.after(100, self.update)
        
########################################################################

#All the rendering happens here  
    def render(self):
        self.player.render(self.c)