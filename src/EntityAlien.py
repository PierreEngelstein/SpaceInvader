class EntityAlien(object):

    def __init__(self, x, y, width, height, speed, canvas, parent, life = 30, EXP = 50):
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
        self.form = canvas.create_rectangle(self.posx - self.width/2, self.posy - self.height/2, self.posx + self.width/2, self.posy + self.height/2, fill= 'white')
        self.parent.enemyList.append(self)
        
    def next(self):
        print ("posy (before) : ", self.posy)
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
        print ("posy (after) : ", self.posy)
        return

    def render(self, canvas):
        if(self.life <= 0):
            canvas.delete(self.form)
        canvas.move(self.form, self.dx, self.dy)
        return
