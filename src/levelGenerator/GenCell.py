#
# This file is subject to the terms and conditions defined in
# file 'LICENSE.txt', which is part of this source code package.
#

class GenCell:
    def __init__(self, rank, canvas):
        self.rank = rank
        self.isSelected = False
        self.isAlive = False
        self.c = canvas
        self.HP = 0
        self.XP = 0
        self.idIMG = rank%2
#        print(str(int(str(rankX*10%255 *256 + rankY*10%255 + 1), 16)))
       
    def setxy(self, x, y, size):
        self.posx0 = x
        self.posy0 = y
        self.width = size
        self.height = size
        self.render()
      
    def setSelection(self):
        self.isSelected = not(self.isSelected)
        self.render()
            
    def render(self):
        try:
            self.c.delete(self.form)
        except:
            color = ''
        if not self.isSelected:
            if self.isAlive:
                color = 'dark blue'
            else:
                color = 'dark red'
        elif self.isAlive:
            color = "#4444FF"
        else:
            color = '#FF4444'
        self.form = self.c.create_rectangle(self.posx0, self.posy0, self.posx0 + self.width, self.posy0 + self.height, fill=color)