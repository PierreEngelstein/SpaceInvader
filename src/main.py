#
# This file is subject to the terms and conditions defined in
# file 'LICENSE.txt', which is part of this source code package.
#

import sys
# sys.dont_write_bytecode = True

try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *

from LevelParser import *
from gui_mainMenu import gui_mainMenu
from gui_endMenuLost import gui_endMenuLost

root = Tk()

root.resizable(False, False)

c = Canvas(root, width=1200, height=700, bg='#565656')

mainMenu = gui_mainMenu(width = 1200, height = 700, canvas = c, root = root)
