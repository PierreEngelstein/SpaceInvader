#The level generator for the space invader
from Tkinter import *

root = Tk()
root.resizable(False, False)
root.title("Space Invader Level Generator")

# frame = Frame(root, width = "800", height = "600", bg = "white")
# frame.pack()
# label = Label(frame, text="Name", width="100", height="40", borderwidth=2, relief="groove")
# label.grid(row = 0, column = 0, rowspan =2, sticky = W+E+N+S) 
# 
# label1 = Label(frame, text="Name", width="30", height="30", borderwidth=2, relief="groove")
# label1.grid(row = 0, column = 1)
# 
# label2 = Label(frame, text="Name", width="30", height="10", borderwidth=2, relief="groove")
# label2.grid(row = 1, column = 1)

leftPanel = Frame(root, width = 800, height = 600).grid(row = 0, column = 0, rowspan =2) 
rU = Frame(root, width = 50, height = 50).grid(row = 0, column = 1)
rD = Frame(root, width = 50, height = 50).grid(row = 1, column = 1)

root.mainloop()

