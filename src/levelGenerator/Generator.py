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
    import tkinter.font
elif platform.system() == "Linux":
    import tkfont
    
from GenCell import GenCell
    
class Generator:
    def __init__(self, master, width, height):
        if platform.system() == "Windows":
            font = tkinter.font.Font(family = "Consolas", size = 10, weight = "normal") 
        elif platform.system() == "Linux":
            font = tkfont.Font(family = "Consolas", size = 10, weight = "normal")
        self.c = Canvas(master, width=width, height=height, bg = "gray") #the width and height parameters are updated only 2 frames later...
        master.minsize(width=width, height=height)
        master.maxsize(width=width, height=height)
        ttk.Separator(master,orient=VERTICAL).place(x=(5*width)/8, y=0, height=height)
        ttk.Separator(master,orient=HORIZONTAL).place(x=(5*width)/8, y=(5*height)/8, width=(3*width)/8)
        Label(master, text = "Number of columns :").place(x = (5*width)/8 + 5, y = 10, width = font.measure("Number of columns :"), height = 20)
        Label(master, text = "Number of lines :").place(x = (5*width)/8 + 5  , y = 80, width = font.measure("Number of lines :"), height = 20) 
        inputCol = Entry(master)
        self.nbCol = 5
        inputCol.insert(0, self.nbCol)
        inputCol.place(x = (5*width)/8 + 5, y = 30)
        inputRow = Entry(master)
        self.nbRow = 12
        inputRow.insert(0, self.nbRow)
        inputRow.place(x = (5*width)/8 + 5, y = 100)
        self.cellList = []
        self.b = 10
        self.currCell;
        #NE PAS OUBLIER DE L'UPDATE SI CHANGEMENT DU NBRE DE COLONNES/LIGNES
        self.cellSize = min((5*width/8 - 2*self.b)/(self.nbCol*1.1), (height - 2*self.b)/(self.nbRow*1.1), 75)
        
        for i in range(0, self.nbRow):
            for j in range(0, self.nbCol):
                self.cellList.append(GenCell(x = self.b + j*((5*width)/8 - self.cellSize - 2*self.b)/(self.nbCol - 1), y = self.b + i*(height - self.cellSize - 2*self.b)/(self.nbRow - 1), size = self.cellSize, rankX = j, rankY = i, canvas = self.c, isSelected = false))
                
        self.currCell = self.cellList[0]
        self.currCell.isSelected = True
        self.c.pack()
root = Tk()

root.resizable(False, False)
root.title("Space Invader Level Generator")
gen = Generator(master = root, width  = 800, height = 600)
root.mainloop()
