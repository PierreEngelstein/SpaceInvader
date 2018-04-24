import math
import random
import sys
import tkFont

from EntityAlien import EntityAlien
from EntityPlayer import EntityPlayer
from LevelParser import *

try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *


# The main game class, which handles frame creation and main game loop
class Display(object):

    def __init__(self, width, height, tkinterRoot, lvlConf="null"):
        # Frame declaration
        self.root = tkinterRoot
        self.c = Canvas(self.root, width=width, height=height, bg="black")  # the width and height parameters are updated only 2 frames later...
        self.root.title("Space Invader - version 1.1")  # version : Major.Minor
        self.w = width
        self.h = height
        self.border = 10
        self.c.focus_set()
        
        # Debug system
        self.font = tkFont.Font(family="Consolas", size=10, weight="normal")
        self.debugString = StringVar()
        self.debugString.set("")
        self.LabelString = Message(self.c, textvariable=self.debugString, anchor='nw', justify=LEFT, width=200).place(x=0, y=self.h - 50, width=135, height=50)
        
        # Entities default declaration
        self.enemySize = 50
        self.enemyPerWave = 10
        self.NbWaves = 3
        
        # Entities management
        self.currEnemy = 0
        self.flagEnemy = -1
        self.EnemyUpdatingTime = 0
        self.EnemyUpdatingSpeed = 1  # The number of frames between two enemy updates.
        self.enemyGoesRight = 1
        self.EnemyShootingTime = 0
        self.EnemyShootingSpeed = 100  # The number of frames between two enemy shots.
        self.bulletList = []  # The list of all the bullets to be rendered
        self.enemyList = []  # The list of all the enemies to be rendered
        self.shooterCols = []
        self.player = EntityPlayer(250, height - 110, 100, 100, self.c, self)
        
        #Level creation
        if(lvlConf == "null"):
            self.ConfigureLevelBase()
        else:
            self.CreateLevelWithConfiguration(lvlConf = lvlConf)
        
        self.update()
        self.root.mainloop()
    
    
    def CreateLevelBase(self): #Creates the default level
        self.shooterCols = range(0, self.enemyPerWave)
        self.EnemySpaceX = (self.w - 2 * self.border - (self.enemyPerWave + 1) * self.enemySize) / self.enemyPerWave
        for j in range(0, self.NbWaves):
            for i in range(0, self.enemyPerWave):
                if(i == 0): canShoot = 1
                else:canShoot = 0
                EntityAlien(self.border + i * (self.enemySize + self.EnemySpaceX) + self.enemySize / 2, self.border + (self.NbWaves - (j + 1)) * (self.enemySize + 10) + self.enemySize / 2, self.enemySize, self.enemySize, j, i, 5, self.c, self, canShoot)
        return
    
    def CreateLevelWithConfiguration(self, lvlConf): #Creates the level given by the parsed configuration
        self.enemyPerWave = lvlConf.nbCol
        self.NbWaves = int(math.ceil(lvlConf.nbLocations / (self.enemyPerWave * 1.0)))
        self.EnemySpaceX = (self.w - 2 * lvlConf.border - (self.enemyPerWave + 1) * self.enemySize) / self.enemyPerWave
        print ("NbWaves = "), self.NbWaves
        print ("********")
        index = 0
        inindex = 0
        print ("lvlConf.nbLocations : "), lvlConf.nbLocations
        print (lvlConf.alien)
        while index < lvlConf.nbLocations:
            print ("Hello, it's-a-me, Inindex ! : ", inindex)
            i = index % self.enemyPerWave  # Index of the column
            j = index / self.enemyPerWave  # Index of the row
            if(lvlConf.alien[inindex] != -1):
                EntityAlien(self.border + i * (self.enemySize + self.EnemySpaceX) + self.enemySize / 2, self.border + (self.NbWaves - (j + 1)) * (self.enemySize + 10) + self.enemySize / 2, self.enemySize, self.enemySize, i, j, lvlConf.speed, self.c, self, 0, lvlConf.alien[inindex], lvlConf.alien[inindex + 2])
                inindex += 3
            else :
                inindex += 1
            index += 1
        # We put the canShoot property of the aliens
        TFList = [False] * self.enemyPerWave  # Array to know if we put a shooter to an enemy
        id = 0
        flag = 0
        while(flag == 0):
            k = self.enemyList[id].col
            if TFList[k] == False:
                TFList[k] = True
                self.enemyList[id].turnToShooter()
            if TFList == [True] * self.enemyPerWave:
                flag = 1
            if k == len(self.enemyList) - 1:
                flag = 1
            id += 1
        print(TFList)
        # We create the list of columns that can shoot
        for i in range (0, len(TFList)):
            if(TFList[i] == True):
                self.shooterCols.append(i)
        print(self.shooterCols)
        return
    
    def EntityRenderAndUpdate(self):
        # Player updating and rendering
        self.player.next()
        self.player.render(self.c)
        a = 0
        # Bullet updating and rendering
        while(a < len(self.bulletList)):
            if(self.bulletList[a].life == -1):
                self.bulletList.pop(a)
                break
            else:                
                self.bulletList[a].next()
                self.bulletList[a].render(self.c)
                a += 1
        # Enemy updating and rendering (could be in the same loop as Bullet rendering but it's cleaner this way)
        b = 0
        while(b < len(self.enemyList)):
            if(self.enemyList[b].life <= 0):
                self.enemyList[b].c.delete(self.enemyList[b].form)
                # Re-assignation (or not if the whole column is dead) of the shooting role
                col = self.enemyList[b].col
                self.enemyList.pop(b)
                flag = 0
                id = 0
                while(id < len(self.enemyList)and flag == 0):
                    if(self.enemyList[id].col == col):
                        self.enemyList[id].turnToShooter()
                        flag = 1
                    id += 1
                if (flag == 0):
                    id = 0
                    while(id < len(self.shooterCols)):
                        print("id = " + str(id))
                        if(col == self.shooterCols[id]):
                            break
                        id += 1
                    self.shooterCols.pop(id)
                break
            
            else:
                b += 1
        
        if self.currEnemy >= len(self.enemyList):
            self.currEnemy = 0
            self.flagEnemy = -1
        
        if self.EnemyUpdatingTime > self.EnemyUpdatingSpeed and len(self.enemyList):
            self.enemyList[self.currEnemy].next()
            self.enemyList[self.currEnemy].render(self.c)
            self.EnemyUpdatingTime = 0
            self.currEnemy += 1
        self.EnemyUpdatingTime += 1
        self.debugString.set("Bullets : " + str(a) + "\nEnemies : " + str(b) + "\n" + "Player score : " + str(self.player.score) + "\n")
        self.root.update_idletasks()
        return
    
    def DetectCollisions(self):
        bulletID = 0  # Bullet index
        while(bulletID < len(self.bulletList)):
            enemyID = 0  # Enemy index
            bulletFlag = 0
            if(self.bulletList[bulletID].isFromAlien == -1):  # If the bullet is shot from the player
                while(enemyID < len(self.enemyList) and bulletFlag == 0):
                    if((self.bulletList[bulletID].x0 < self.enemyList[enemyID].x1 and self.bulletList[bulletID].x1 > self.enemyList[enemyID].x0 and self.bulletList[bulletID].y0 < self.enemyList[enemyID].y1 and self.bulletList[bulletID].y1 > self.enemyList[enemyID].y0)):  # If we hit one monster
                        self.enemyList[enemyID].life -= self.bulletList[bulletID].damages
                        self.player.addScore(10)
                        self.bulletList[bulletID].damages = 0
                        self.bulletList[bulletID].c.delete(self.bulletList[bulletID].form)
                        self.bulletList.pop(bulletID)
                        bulletFlag = 1
                    enemyID += 1
            else:
                if((self.bulletList[bulletID].x0 < self.player.x1 and self.bulletList[bulletID].x1 > self.player.x0 and self.bulletList[bulletID].y0 < self.player.y1 and self.bulletList[bulletID].y1 > self.player.y0)):
                    sys.exit(0)  # Later on it will be a death screen...
            bulletID += 1
        
        return
    
    def EnemyShooting(self):
        if self.EnemyShootingTime >= self.EnemyShootingSpeed and len(self.shooterCols) >= 1:
            id = random.randint(0, len(self.shooterCols) - 1)
            self.currShootingCol = self.shooterCols[id]
            flag = 0
            idid = 0
            while(flag == 0):
                if self.enemyList[idid].col == self.currShootingCol:
                    self.enemyList[idid].shootBullet()
                    flag = 1
                idid += 1
                if idid == len(self.enemyList): flag = 1
            self.EnemyShootingTime = 0
        
        self.EnemyShootingTime += 1
        return

    def KeyBinding(self):
        self.c.bind("<Button-1>", self.player.shootBullet)
        return
    
    def update(self): # Main game loop
        self.EntityRenderAndUpdate()
        self.DetectCollisions()
        self.EnemyShooting()
        self.KeyBinding()
        
        self.c.pack()
        self.root.after(10, self.update)