#
# This file is subject to the terms and conditions defined in
# file 'LICENSE.txt', which is part of this source code package.
#

#The level generator for the space invader
from _tkinter import create
import PIL.Image
try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *
import platform
import ttk

from GenCell import GenCell


if platform.system() == "Windows":
    import tkinter.font as FONT
elif platform.system() == "Linux":
    try:
        # for Python2
        import tkFont as FONT
    except ImportError:
        # for Python3
       import tkinter.font as FONT
    

  
class Generator:
    def __init__(self, master, width, height):
        if platform.system() == "Windows":
            self.font = FONT.Font(family = "Consolas", size = 10, weight = "normal") 
        elif platform.system() == "Linux":
            self.font = FONT.Font(family = "Consolas", size = 10, weight = "normal")
        self.c = Canvas(master, width=width, height=height, bg = "gray") #the width and height parameters are updated only 2 frames later...
        self.c.focus_set()
        self.width = width
        self.height = height
        self.root = master

        master.minsize(width=width, height=height)
        master.maxsize(width=width, height=height)
        ttk.Separator(master,orient=VERTICAL).place(x=(5*width)/8, y=0, height=height)
        ttk.Separator(master,orient=HORIZONTAL).place(x=(5*width)/8, y=(5*height)/8, width=(3*width)/8)
        
        
        self.b = 10 #Border
        
        
        self.c.create_text((5*width)/8 + 5, 10, fill = "black", anchor = "nw", text = "Number of columns : ", font = self.font)
        
        self.nbCol = 10
        self.inputCol = self.c.create_text((5*width)/8 + 5, 30, fill = "black", anchor = "nw", text = str(self.nbCol), font = self.font)
        
        self.buttonIncCol = Button(self.root, text = "Increase columns", command = self.increaseCol)
        self.buttonIncCol.place(x = (5*width)/8 + 5, y = 50)
        
        self.buttonDecCol = Button(self.root, text = "Decrease columns", command = self.decreaseCol)
        self.buttonDecCol.place(x = (5*width)/8 + 5, y = 70)
        
        
        self.c.create_text((5*width)/8 + 5, 100, fill = "black", anchor = "nw", text = "Number of rows : ", font = self.font)
        
        self.nbRow = 10
        self.inputRow = self.c.create_text((5*width)/8 + 5, 120, fill = "black", anchor = "nw", text = str(self.nbRow), font = self.font)
        
        self.buttonIncRow = Button(self.root, text = "Increase rows", command = self.increaseRow)
        self.buttonIncRow.place(x = (5*width)/8 + 5, y = 140)
        
        self.buttonDecRow = Button(self.root, text = "Decrease rows", command = self.decreaseRow)
        self.buttonDecRow.place(x = (5*width)/8 + 5, y = 160)
        
        self.cellList = []
        self.currCell = 'null';
        #NE PAS OUBLIER DE L'UPDATE SI CHANGEMENT DU NBRE DE COLONNES/LIGNES
        
        self.initialization()
    
   
        
    def initialization(self):
        for i in range(0, self.nbRow):
            for j in range(0, self.nbCol):
                self.cellList.append(GenCell(rank = i * self.nbCol + j, canvas = self.c))
        
        self.resizeCellGrid()
        self.currCell = self.cellList[0]
        self.currCell.setSelection()
        self.loadImgArray("null")
        self.showInfos()
        self.update()
        
    def loadImgArray(self, event):
        self.ImgArray = []
        i = 0
        try:
            while True:
                image = PIL.Image.open("../resources/img/SpaceInvader_Enemy" + str(i+1) + ".png")
                i += 1
                image = image.resize((100, 100))
                image.save("../resources/img/imgResized/SpaceInvader_Enemy" + str(i) + ".png", "png")
                self.pic = PhotoImage(file = "../resources/img/imgResized/SpaceInvader_Enemy" + str(i) + ".png")
                self.ImgArray.append(self.pic)
        except:
            print("End ! " + str(i) + " images found !")
        
    def decreaseCol(self):
        for temp in range(0, len(self.cellList)-self.nbRow):
            if temp%(self.nbCol-1) == 0 and temp != 0:
                self.c.delete(self.cellList[temp].form)
                self.cellList.pop(temp)
                self.cellList[temp].rank = temp
                print(self.cellList[temp].rank)
            else :
                self.cellList[temp].rank = temp
                print(self.cellList[temp].rank)
                
        
        self.c.itemconfig(self.inputCol, text = self.nbCol - 1)
        self.resizeCellGrid()
    
    def decreaseRow(self):
        self.c.itemconfig(self.inputRow, text = self.nbRow - 1)
        self.resizeCellGrid()
        
    def increaseCol(self):
        for i in range(0, int(self.nbRow)):
            self.c.insert
        
        
        self.c.itemconfig(self.inputCol, text = self.nbCol + 1)
        self.resizeCellGrid()
        
    def increaseRow(self):
        self.c.itemconfig(self.inputRow, text = self.nbRow + 1)
        self.resizeCellGrid()
    
    def resizeCellGrid(self):
        
        self.nbRow = int(self.c.itemcget(self.inputRow, "text"))
        self.nbCol = int(self.c.itemcget(self.inputCol, "text"))
        self.cellSize = min((5*self.width/8 - 2*self.b)/(self.nbCol*1.1), (self.height - 2*self.b)/(self.nbRow*1.1), 75)
        temp = 0
        while temp < len(self.cellList):
            self.cellList[int(temp/self.nbCol)*self.nbCol+(temp%self.nbCol)].setxy(x = self.b + (temp%self.nbCol)*((5*self.width)/8 - self.cellSize - 2*self.b)/(self.nbCol - 1), y = self.b + int(temp/self.nbCol)*(self.height - self.cellSize - 2*self.b)/(self.nbRow - 1), size = self.cellSize)
            temp += 1
        
    def updateImg(self):
        a = a
        
    def update(self):
        #self.isModified();
        self.c.bind("<Down>", self.switchDown)
        self.c.bind("<Up>", self.switchUp)
        self.c.bind("<Left>", self.switchLeft)
        self.c.bind("<Right>", self.switchRight)
        self.c.bind("<Return>", self.LiveOrDie)
        self.c.bind("<F5>", self.loadImgArray)
        self.c.bind("<Q>", exit)
        self.c.pack()
        self.root.after(10, self.update)
        return


    #Functions binded to the arrows, which allow toe browse of the cell grid
    def switchDown(self, event):
        a = self.currCell.rank + self.nbCol
        if a < len(self.cellList):
            self.currCell.setSelection()
            self.currCell = self.cellList[a]
            self.currCell.setSelection()
            self.showInfos()
            
    def switchUp(self, event):
        a = self.currCell.rank - self.nbCol
        if a >= 0:
            self.currCell.setSelection()
            self.currCell = self.cellList[a]
            self.currCell.setSelection()
            self.showInfos()
            
    def switchLeft(self, event):
        if self.currCell.rank%self.nbCol != 0:
            self.currCell.setSelection()
            self.currCell = self.cellList[self.currCell.rank-1]
            self.currCell.setSelection()
            self.showInfos()
            
    def switchRight(self, event):
        if (self.currCell.rank+1)%self.nbCol != 0:
            self.currCell.setSelection()
            self.currCell = self.cellList[self.currCell.rank+1]
            self.currCell.setSelection()
            self.showInfos()
            
    def LiveOrDie(self, event):
        self.currCell.isAlive = not(self.currCell.isAlive)
        self.currCell.render()
        self.showInfos()
        
    def showInfos(self):
        try:
            self.c.delete(self.renderHP)
            self.c.delete(self.renderXP)
            self.c.delete(self.imgSkin)
            self.formHP.destroy()
            self.formXP.destroy()
            self.c.delete(self.formIMG)
        except:
            a = 1;
        if self.currCell.isAlive:
            self.renderHP = self.c.create_text((5*self.width)/8 + 5, (5*self.height)/8 + 10, fill = "black", anchor = "nw", text = "HP :", font = self.font)
            self.formHP = Entry(self.root)
            self.formHP.place(x = (5*self.width)/8 + 35, y = (5*self.height)/8 + 10)
            self.renderXP = self.c.create_text((5*self.width)/8 + 5, (5*self.height)/8 + 30, fill = "black", anchor = "nw", text = "XP :", font = self.font)
            self.formXP = Entry(self.root)
            self.formXP.place(x = (5*self.width)/8 + 35, y = (5*self.height)/8 + 30)
            self.imgSkin = self.c.create_image((5*self.width)/8 + 55, (5*self.height)/8 + 100, image = self.ImgArray[self.currCell.idIMG])
        
root = Tk()
root.resizable(False, False)
root.title("Space Invader Level Generator")
gen = Generator(master = root, width  = 800, height = 600)
root.mainloop()  
