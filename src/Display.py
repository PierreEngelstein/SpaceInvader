import math
import random
import sys
import time

try:
    # for Python2
    import tkFont as font
except ImportError:
    # for Python3
   import tkinter.font as font

from gui_endMenuLost import gui_endMenuLost
from gui_pauseMenu import gui_pauseMenu
from gui_HUD import gui_HUD
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

    def __init__(self, width, height, tkinterRoot, gameConf, canvas = "null", startTime = 0, precBulleTouched = 0, precBulletTotal = 0, nbKills = 0, score = 0):
        # Frame declaration
        self.root = tkinterRoot
        self.t = time
        if canvas == "null": self.c = Canvas(self.root, width=width, height=height, bg="black")  # the width and height parameters are updated only 2 frames later...
        if canvas != "null":
            self.c = canvas
            self.c.config(width = width, height = height)
        self.root.title("Space Invader - version 1.1")  # version : Major.Minor
        self.w = width
        self.h = height
        self.border = 10
        self.c.focus_set()
        self.hud = gui_HUD(self)
        self.levelName = "EMPTY"
        
        # Entities default declaration
        self.enemySize = 50
        self.enemyPerWave = 10
        self.NbWaves = 3
        
        # Entities management
        self.currEnemy = 0
        self.flagUID = -1
        self.EnemyUpdatingTime = 0
        self.EnemyUpdatingSpeed = 1  # The number of frames between two enemy updates.
        self.enemyGoesRight = 1
        self.EnemyShootingTime = 0
        self.EnemyShootingSpeed = 100  # The number of frames between two enemy shots.
        self.bulletList = []  # The list of all the bullets to be rendered
        self.enemyList = []  # The list of all the enemies to be rendered
        self.shooterCols = []
        self.player = EntityPlayer(250, height - 110, 100, 100, self.c, self, score)
        
        #Score & miscellaneous
        self.numberOfKills = nbKills
        self.shots = precBulletTotal
        self.goodShots = precBulleTouched
        self.paused = False
        self.debug = False
        
        #Level creation
        self.gameConf = gameConf
        if(gameConf == "null"):
            self.CreateLevelBase()
        else:
            self.CreateLevelWithConfiguration(lvlConf = gameConf.levelListConf[gameConf.currentLevel])
            self.levelName = gameConf.levelListConf[gameConf.currentLevel].levelName
        self.startTime = startTime
        self.update()
        self.root.mainloop()
        
    def CreateLevelBase(self): #Creates the default level
        self.shooterCols = range(0, self.enemyPerWave)
        self.EnemySpaceX = (self.w - 2 * self.border - (self.enemyPerWave + 1) * self.enemySize) / self.enemyPerWave
        for j in range(0, self.NbWaves):
            for i in range(0, self.enemyPerWave):
                if(i == 0): canShoot = 1
                else:canShoot = 0
                EntityAlien(self.border + i * (self.enemySize + self.EnemySpaceX) + self.enemySize / 2, self.border + (self.NbWaves - (j + 1)) * (self.enemySize + 10) + self.enemySize / 2, self.enemySize, self.enemySize, j, i, 5, self.c, self, canShoot, UID = i + j*self.enemyPerWave)
        return
    
    def CreateLevelWithConfiguration(self, lvlConf): #Creates the level given by the parsed configuration
        self.enemyPerWave = lvlConf.nbCol
        self.NbWaves = int(math.ceil(lvlConf.nbLocations / (self.enemyPerWave * 1.0)))
        self.EnemySpaceX = (self.w - 2 * lvlConf.border - (self.enemyPerWave + 1) * self.enemySize) / self.enemyPerWave
        print ("NbWaves = "), self.NbWaves
        print ("********")
        id = 0      #Defines the UID of each alien
        index = 0   #Defines the location of the alien
        inindex = 0 #Goes through the values in the lvlConf array, corresponding to an unique alien
        print ("lvlConf.nbLocations : "), lvlConf.nbLocations
        print (lvlConf.alien)
        while index < lvlConf.nbLocations:
            i = index % self.enemyPerWave  # Index of the column
            j = index / self.enemyPerWave  # Index of the row
            if(lvlConf.alien[inindex] != -1):
#                 print (id)
                EntityAlien(self.border + i * (self.enemySize + self.EnemySpaceX) + self.enemySize / 2, self.border + (self.NbWaves - (j + 1)) * (self.enemySize + 10) + self.enemySize / 2, self.enemySize, self.enemySize, j, i, lvlConf.speed, self.c, self, 0, id, lvlConf.alien[inindex], lvlConf.alien[inindex + 1], lvlConf.alien[inindex + 2])
                id += 1
                inindex += 3
            else :
                inindex += 1
            index += 1
        # We put the canShoot property of the aliens
        TFList = [False] * self.enemyPerWave  # Array to know if we put a shooter to an enemy
        id = 0
        flag = 0
#         print("len : ", len(self.enemyList) -1)
        while(flag == 0):
#             print("Hey, i'm id : " + str(id))
            k = self.enemyList[id].col
            if TFList[k] == False:
                TFList[k] = True
                self.enemyList[id].turnToShooter()
            if TFList == [True] * self.enemyPerWave:
                flag = 1
            if id == (len(self.enemyList) - 1):
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
                self.numberOfKills += 1
                self.player.addScore(self.enemyList[b].xp)
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
                        if(col == self.shooterCols[id]):
                            break
                        id += 1
                    self.shooterCols.pop(id)
                break
            
            else:
                b += 1
        
        if self.currEnemy >= len(self.enemyList):
            self.currEnemy = 0
            self.flagUID = -1
        
        if self.EnemyUpdatingTime > self.EnemyUpdatingSpeed and len(self.enemyList):
            self.enemyList[self.currEnemy].next()
            self.enemyList[self.currEnemy].render(self.c)
            self.EnemyUpdatingTime = 0
            self.currEnemy += 1
        if(len(self.enemyList) == 0):
            self.endGame(True, False)
        self.EnemyUpdatingTime += 1
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
                        self.goodShots += 1
                        self.enemyList[enemyID].life -= self.bulletList[bulletID].damages
                        self.bulletList[bulletID].damages = 0
                        self.bulletList[bulletID].c.delete(self.bulletList[bulletID].form)
                        self.bulletList.pop(bulletID)
                        bulletFlag = 1
                    enemyID += 1
            else:
                if((self.bulletList[bulletID].x0 < self.player.x1 and self.bulletList[bulletID].x1 > self.player.x0 and self.bulletList[bulletID].y0 < self.player.y1 and self.bulletList[bulletID].y1 > self.player.y0)):
                    self.endGame(False, True)
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
    
    def Paused(self):
#TODO: create the pause menu
        a=1       
        
    def endGame(self, jumpToNextLevel = False, dead = True):
        if(self.shots == 0):accuracy = 0
        else:accuracy = 1.0*self.goodShots / self.shots
        self.endTime = int(round(self.t.time() * 1000))
        time = int((self.endTime - self.startTime)/1000)
                    
        score = int(max(self.player.score + self.numberOfKills*accuracy - 1*time, 0))
        self.c.delete("all")
        self.c.destroy()
        
        if(self.gameConf != "null" and self.gameConf.currentLevel != (len(self.gameConf.levelListConf) - 1) and jumpToNextLevel == True):
            c = Canvas(self.root, width=1200, height=700, bg="black")
            self.gameConf.currentLevel += 1
            display = Display(width=1200, height=700, tkinterRoot=self.root, gameConf = self.gameConf, startTime = self.startTime, precBulleTouched = self.goodShots, precBulletTotal = self.shots, nbKills = self.numberOfKills, score = self.player.score)
        else:
            c = Canvas(self.root, width=1200, height=700, bg='#565656')
            deathMenu = gui_endMenuLost(width = 1200, height = 700, canvas = c, root = self.root, kills = self.numberOfKills, shots = self.shots, goodshots = self.goodShots, timer = time, score = score, isDead = dead)
    
    def KeyBinding(self):
        self.c.bind("<Button-1>", self.player.shootBullet)
        self.c.bind("<p>", self.pause)
        self.c.bind("<d>", self.hud.setDebugMode)
        return
    
    def update(self): # Main game loop
        if not self.paused or (self.c.winfo_exists() != 0):
            self.EntityRenderAndUpdate()
            self.EnemyShooting()
            self.DetectCollisions()
            self
            self.KeyBinding()
            self.hud.update();
        else:
            self.Paused()
        self.c.pack()
        self.root.after(10, self.update)
    
    def pause(self, event):
        self.paused= not self.paused