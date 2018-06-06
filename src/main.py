#
# This file is subject to the terms and conditions defined in
# file 'LICENSE.txt', which is part of this source code package.
#

import sys
#Create the directories that the game requires
import os
import shutil
if not os.path.exists("resources/img/imgResized/"):
    os.makedirs("resources/img/imgResized/")

try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *

from LevelParser import *
from gui_mainMenu import gui_mainMenu

root = Tk()

root.resizable(False, False)

c = Canvas(root, width=1200, height=700, bg='#565656')

mainMenu = gui_mainMenu(width = 1200, height = 700, canvas = c, root = root)

print("Removing useless directories...")
shutil.rmtree("resources/img/imgResized/")
