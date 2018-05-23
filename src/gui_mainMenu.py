import sys

import PIL.Image

from Display import Display
from LevelParser import *
from gui_button import gui_button


try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *

class gui_mainMenu(object):
    
    def __init__(self, width, height, canvas, root):
        self.c = canvas
        self.c.focus_set()
        self.root = root
        #Logo
        logo = PIL.Image.open("resources/img/title_concept.png")
        logo = logo.resize((512, 512))
        logo.save("resources/img/imgResized/title_concept.png", "png")
        self.Logo = PhotoImage(file = "resources/img/imgResized/title_concept.png")
        self.logoImage = self.c.create_image(width/2, 3*height/14, image = self.Logo)
        #Buttons
        self.currButton = gui_button(x = width/2, y = 440, width = 150, height = 50, text = "Quit",        canvas = self.c, action = self.action_quit,    next = "null" , selected = False)
        self.currButton = gui_button(x = width/2, y = 370, width = 150, height = 50, text = "Options",     canvas = self.c, action = self.action_options, next = self.currButton, selected = False) 
        self.currButton = gui_button(x = width/2, y = 300, width = 150, height = 50, text = "Launch game", canvas = self.c, action = self.action_launchGame, next = self.currButton, selected = True)
        #Indicator
        image = PIL.Image.open("resources/img/SpaceInvader_Enemy1.png")
        image = image.resize((33, 33))
        image.save("resources/img/imgResized/SpaceInvader_Enemy1.png", "png")
        self.pic = PhotoImage(file = "resources/img/imgResized/SpaceInvader_Enemy1.png")
        self.alienIndicator = self.c.create_image(self.currButton.x - 30, self.currButton.y + 12, image = self.pic)
        
        self.update()
        self.root.mainloop()
        return
    
    def update(self):
        self.currButton.draw()
        self.c.delete(self.alienIndicator)
        self.alienIndicator = self.c.create_image(self.currButton.x - 30, self.currButton.y + 12, image = self.pic)
        self.c.bind("<Return>", self.currButton.action)
        self.c.bind("<Down>", self.switchDown)
        self.c.bind("<Up>", self.switchUp)
        self.c.pack()
        self.root.after(10, self.update)
        return

    def action_quit(self, event):
        sys.exit(0)
    def action_options(self, event):
        print("JE NE SUIS PAS OPTIONNEL !!!")
    def action_launchGame(self, event):
        print("THIS IS A FOCKING GAME")
        self.c.destroy()
        lvlParse = LevelParser("resources/levels/level2.spi")
        lvlConf = lvlParse.parseFile()
        if(lvlConf == 1):
            print ("Zbrah")
        else:
            zbrah = 1
            if zbrah == 1 :
                display = Display(width=1200, height=700, tkinterRoot=self.root, lvlConf = lvlConf)
            else :
                display = Display(width=1200, height=700, tkinterRoot=self.root)
        
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
        
    