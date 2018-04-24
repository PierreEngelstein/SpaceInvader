import PIL.Image

try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *
from EntityBullet import EntityBullet

class EntityAlien(object):

    def __init__(self, x, y, width, height, row, col, speed, canvas, parent, canShoot, life = 30, EXP = 50):
        self.posx = x
        self.posy = y
        self.dx = 0
        self.dy = 0
        self.width = width
        self.height = height
        self.c = canvas
        self.parent = parent
        self.direction = 1
        self.speed = speed
        self.life = life
        self.row = row
        self.col = col
        self.canShoot = canShoot
#         self.form = canvas.create_rectangle(self.posx - self.width/2, self.posy - self.height/2, self.posx + self.width/2, self.posy + self.height/2, fill= 'white')
        image = PIL.Image.open("SpaceInvader_Enemy1.png")
        image = image.resize((width, height))
        image.save("SpaceInvader_Enemy1.png", "png")
        self.pic = PhotoImage(file = "SpaceInvader_Enemy1.png")
        self.form = canvas.create_image(self.posx, self.posy, image = self.pic)
        self.parent.enemyList.append(self)
        self.updateBBOX()
        
    def next(self):
#         print ("posy (before) : ", self.posy)
        self.dx = self.parent.enemyGoesRight*self.speed
        self.dy = 0
        if self.parent.flagEnemy >= self.parent.currEnemy:
            self.dx *= 2
        self.posx += self.dx
        
        if self.direction != self.parent.enemyGoesRight:
            self.direction = self.parent.enemyGoesRight
            self.dy = 25
            
        if (self.posx >= (self.parent.w - (self.parent.border + 1) - self.width/2)) or (self.posx <= ((self.parent.border + 1) + self.width/2)):
            self.parent.enemyGoesRight = - self.parent.enemyGoesRight
            self.parent.flagEnemy = self.parent.currEnemy
            self.parent.currEnemy = -1
        self.posy += self.dy
        self.updateBBOX()
#         print ("posy (after) : ", self.posy)
        return

    def render(self, canvas):
        if(self.life <= 0):
            canvas.delete(self.form)
        canvas.move(self.form, self.dx, self.dy)
        return
    
    def turnToShooter(self):
        self.canShoot = 1
        
    def updateBBOX(self):
        self.x0 = self.posx - self.width/2
        self.y0 = self.posy - self.height/2
        self.x1 = self.posx + self.width/2
        self.y1 = self.posy + self.height/2
    def shootBullet(self):
        bullet = EntityBullet(x = self.posx, y = self.posy, width = 10, height = 10, speed = 10, dmg = 10, ifa = 1, canvas = self.parent.c)
        self.parent.bulletList.append(bullet)
