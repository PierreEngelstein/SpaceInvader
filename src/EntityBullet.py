class EntityBullet(object):
    
    def __init__(self, x, y, width, height, speed, dmg, canvas):
        self.posx = x
        self.posy = y
        self.width = width
        self.height = height
        self.speed = speed
        self.damages = dmg
        self.c = canvas
        self.form = canvas.create_oval(self.posx - self.width/2, self.posy - self.height/2, self.posx + self.width/2, self.posy + self.height/2, fill="white")
        self.life = 1
    
    def next(self):
        self.dy = -1*self.speed
        self.posy += self.dy
        return
    
    def render(self, canvas):
        if(self.posy < 10): #OR if it touches an enemy
            canvas.delete(self.form)
            self.life = -1
        canvas.move(self.form, 0, self.dy)
        return
        