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
        self.bulletDmg=3
        self.c = Canvas
        self.parent = parent
        self.life=1
        self.score = 0
        image = PIL.Image.open("resources/img/image.png")
        image = image.resize((width, height))
        image.save("resources/img/imgResized/image.png", "png")
        self.pic = PhotoImage(file = "resources/img/imgResized/image.png")
        print("Player image size : " + str(image.size))
        self.images = Canvas.create_image(self.posx, self.posy, image = self.pic)
        self.updateBBOX()
        self.bbox = self.c.create_rectangle(self.x0, self.y0, self.x1, self.y1, fill="white", stipple="gray50")

    def next(self):
        self.setLocation((self.c.winfo_pointerx() - self.c.winfo_rootx()), (self.c.winfo_pointery() - self.c.winfo_rooty()))
        self.updateBBOX()
        self.c.delete(self.bbox)
#         self.bbox = self.c.create_rectangle(self.x0, self.y0, self.x1, self.y1, fill="white", stipple="gray50")
        return

    def render(self, Canvas):
        Canvas.move(self.images, self.dx, self.dy)
        return
    def updateBBOX(self):
        self.x0 = self.posx - self.width/2
        self.y0 = self.posy
        self.x1 = self.posx + self.width/2
        self.y1 = self.posy + self.height/2
        
#########################################################################        
    def setLocation(self, x, y):
        if(x < self.width/2): x = (self.width/2) + 1
        if(x > self.parent.c.winfo_width() - self.width/2): x = self.parent.c.winfo_width() - self.width/2 - 1
        self.dx = x - self.posx
        self.posx = x
        return
   
    def shootBullet(self, event):
        bullet = EntityBullet(x = self.posx, y = self.posy - 20, width = 10, height = 10, speed = 10, dmg = 10, ifa = -1, canvas = self.parent.c)
        self.parent.bulletList.append(bullet)
        return
    def addScore(self, score):
        self.score += score
        return