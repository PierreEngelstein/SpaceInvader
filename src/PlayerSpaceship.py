
class PlayerSpaceship(object):
    


    def __init__(self, x, y, width, height):
        self.posx = x
        self.posy = y
        self.width = width
        self.height = height
        
    def render(self, Canvas):
        Canvas.create_rectangle(self.posx, self.posy, self.posx + self.width, self.posy + self.height)
        return
    
    def move(self):
        self.posx += 10
        self.posy += 10
        return
    
    def goUp(self):
        self.posy -= 1
        print("BIJOUR, JE VAIS EN HAUT")
        return
    
    def goDown(self):
        self.posy += 1
        return
    
    def goLeft(self):
        self.posx -= 1
        return
    
    def goRight(self):
        self.posx += 1
        return
############################
        