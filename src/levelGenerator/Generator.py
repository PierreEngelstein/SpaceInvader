#The level generator for the space invader
from Tkinter import *
import ttk
import tkFont

class Generator:
    def __init__(self, master, width, height):
        font = tkFont.Font(family = "Consolas", size = 10, weight = "normal") 
        master.minsize(width=width, height=height)
        master.maxsize(width=width, height=height)
        ttk.Separator(master,orient=VERTICAL).place(x=(5*width)/8, y=0, height=height)
        ttk.Separator(master,orient=HORIZONTAL).place(x=(5*width)/8, y=(5*height)/8, width=(3*width)/8)
        Label(master, text = "Number of columns :").place(x = (5*width)/8 + 5, y = 10, width = font.measure("Number of columns :"), height = 20)
        Label(master, text = "Number of lines :").place(x = (5*width)/8 + 5  , y = 80, width = font.measure("Number of lines :"), height = 20) 
        inputCol = Entry(master)
        inputCol.insert(0, "20")
        inputCol.place(x = (5*width)/8 + 5, y = 30)
        inputRow = Entry(master)
        inputRow.insert(0, "20")
        inputRow.place(x = (5*width)/8 + 5, y = 100)

root = Tk()

root.resizable(False, False)
root.title("Space Invader Level Generator")
gen = Generator(master = root, width  = 800, height = 600)
root.mainloop()
