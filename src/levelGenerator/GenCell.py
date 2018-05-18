class GenCell:
    def __init__(self, x, y, size, rankX, rankY, canvas, isSelected):
        
        self.posx0 = x
        self.posy0 = y
        self.width = size
        self.height = size
        self.rankX = rankX
        self.rankY = rankY
        self.isSelected = isSelected
        print(str(int(str(rankX*10%255 *256 + rankY*10%255 + 1), 16)))
        self.form = canvas.create_rectangle(self.posx0, self.posy0, self.posx0 + self.width, self.posy0 + self.height, fill='Blue')
        
    def update(self):
        if self.isSelected:
            self.form.destroy()
            self.form = canvas