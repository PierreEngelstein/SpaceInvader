#
# This file is subject to the terms and conditions defined in
# file 'LICENSE.txt', which is part of this source code package.
#

class EntityBullet(object):
    
    def __init__(self, x, y, width, height, speed, dmg, ifa, canvas):
        self.posx = x
        self.posy = y
        self.width = width
        self.height = height
        self.speed = speed
        self.damages = dmg
        self.c = canvas
        self.isFromAlien = ifa  #-1 => from player ; 1 => from alien
        if ifa == 1 :
            color = 'red'
        else:
            color = 'white'
        self.form = canvas.create_oval(self.posx - self.width/2, self.posy - self.height/2, self.posx + self.width/2, self.posy + self.height/2, fill=color)
        self.life = 1
        self.updateBBOX()
    
    def next(self):
        self.dy = self.isFromAlien*self.speed
        self.posy += self.dy
        self.updateBBOX()
        return
    
    def render(self, canvas):
        if(self.posy < 10 or self.posy > (self.c.winfo_height() - 50)): #OR if it touches an enemy
            canvas.delete(self.form)
            self.life = -1
        canvas.move(self.form, 0, self.dy)
        return
    
    def updateBBOX(self):
        self.x0 = self.posx - self.width/2
        self.y0 = self.posy - self.height/2
        self.x1 = self.posx + self.width/2
        self.y1 = self.posy + self.height/2
        