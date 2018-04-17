import PIL.Image

try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *
from EntityBullet import EntityBullet

#The player class
class EntityPlayer(object):
    def __init__(self, x, y, width, height, Canvas, parent):
        self.posx = x
        self.posy = y
        self.width = width
        self.height = height
        self.dx = 0
        self.dy = 0
        self.bulletDmg=10
        self.c = Canvas
        self.parent = parent
        self.life=1
        self.score = 0
        image = PIL.Image.open("image.png")
        image = image.resize((width, height))
        image.save("image.png", "png")
        self.pic = PhotoImage(file = "image_resized.png")
        self.images = Canvas.create_image(self.posx, self.posy, image = self.pic)

    def next(self):
        self.setLocation((self.c.winfo_pointerx() - self.c.winfo_rootx()), (self.c.winfo_pointery() - self.c.winfo_rooty()))
        return

    def render(self, Canvas):
        Canvas.move(self.images, self.dx, self.dy)
        return
#########################################################################        
    def setLocation(self, x, y):
        if(x < self.width/2): x = (self.width/2) + 1
        if(x > self.parent.c.winfo_width() - self.width/2): x = self.parent.c.winfo_width() - self.width/2 - 1
        self.dx = x - self.posx
        self.posx = x
        return
   
    def shootBullet(self, event):
        bullet = EntityBullet(x = self.posx, y = self.posy - 20, width = 10, height = 10, speed = 10, dmg = 10, canvas = self.parent.c)
        self.parent.bulletList.append(bullet)
        return
    def addScore(self, score):
        self.score += score
        return