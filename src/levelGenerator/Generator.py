#The level generator for the space invader
try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *
import ttk
import platform
if platform.system() == "Windows":
    import tkinter.font as FONT
elif platform.system() == "Linux":
    try:
        # for Python2
        import tkFont as FONT
    except ImportError:
        # for Python3
       import tkinter.font as FONT
    
from GenCell import GenCell

  
class Generator:
    def __init__(self, master, width, height):
        if platform.system() == "Windows":
            font = FONT.Font(family = "Consolas", size = 10, weight = "normal") 
        elif platform.system() == "Linux":
            font = FONT.Font(family = "Consolas", size = 10, weight = "normal")
        self.c = Canvas(master, width=width, height=height, bg = "gray") #the width and height parameters are updated only 2 frames later...
        self.c.focus_set()
        self.width = width
        self.height = height
        self.root = master
        
        master.minsize(width=width, height=height)
        master.maxsize(width=width, height=height)
        ttk.Separator(master,orient=VERTICAL).place(x=(5*width)/8, y=0, height=height)
        ttk.Separator(master,orient=HORIZONTAL).place(x=(5*width)/8, y=(5*height)/8, width=(3*width)/8)
        Label(master, text = "Number of columns :").place(x = (5*width)/8 + 5, y = 10, width = font.measure("Number of columns :"), height = 20)
        Label(master, text = "Number of lines :").place(x = (5*width)/8 + 5  , y = 80, width = font.measure("Number of lines :"), height = 20) 
        
        inputCol = Entry(master)
        self.nbCol = 0
        inputCol.insert(0, self.nbCol)
        inputCol.place(x = (5*width)/8 + 5, y = 30)
        
        inputRow = Entry(master)
        self.nbRow = 0
        inputRow.insert(1, self.nbRow)
        inputRow.place(x = (5*width)/8 + 5, y = 100)
        
        self.cellList = []
        self.b = 10 #Border
        self.currCell = 'null';
        #NE PAS OUBLIER DE L'UPDATE SI CHANGEMENT DU NBRE DE COLONNES/LIGNES
        
        self.initialization()
    
   
        
    def initialization(self):
            
        self.resizeCellGrid(5, 5)
        for i in range(0, self.nbRow):
            for j in range(0, self.nbCol):
                self.cellList.append(GenCell(x = self.b + j*((5*self.width)/8 - self.cellSize - 2*self.b)/(self.nbCol - 1), y = self.b + i*(self.height - self.cellSize - 2*self.b)/(self.nbRow - 1), size = self.cellSize, rank = i * self.nbCol + j, canvas = self.c))
                self.cellList[i*self.nbCol+j].render()
        
        self.currCell = self.cellList[0]
        self.currCell.update()
        self.update()
        
        
    def resizeCellGrid(self, newNbRow, newNbCol):
        
        self.nbRow = newNbRow
        self.nbCol = newNbCol
        self.cellSize = min((5*self.width/8 - 2*self.b)/(self.nbCol*1.1), (self.height - 2*self.b)/(self.nbRow*1.1), 75)
        
    def update(self):
        self.c.bind("<Down>", self.switchDown)
        self.c.bind("<Up>", self.switchUp)
        self.c.bind("<Left>", self.switchLeft)
        self.c.bind("<Right>", self.switchRight)
        self.c.bind("<Return>", self.LiveOrDie)
        self.c.pack()
        self.root.after(10, self.update)
        return

    def switchDown(self, event):
        a = self.currCell.rank + self.nbCol
        if a < len(self.cellList):
            self.currCell.update()
            self.currCell = self.cellList[a]
            self.currCell.update()
            
    def switchUp(self, event):
        a = self.currCell.rank - self.nbCol
        if a >= 0:
            self.currCell.update()
            self.currCell = self.cellList[a]
            self.currCell.update()
            
    def switchLeft(self, event):
        if self.currCell.rank%self.nbCol != 0:
            self.currCell.update()
            self.currCell = self.cellList[self.currCell.rank-1]
            self.currCell.update()
            
    def switchRight(self, event):
        if (self.currCell.rank+1)%self.nbCol != 0:
            self.currCell.update()
            self.currCell = self.cellList[self.currCell.rank+1]
            self.currCell.update()
            
    def LiveOrDie(self, event):
        self.currCell.isAlive = not(self.currCell.isAlive)
        self.currCell.render()
root = Tk()
root.resizable(False, False)
root.title("Space Invader Level Generator")
gen = Generator(master = root, width  = 800, height = 600)
root.mainloop()  