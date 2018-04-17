try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *
import math

from EntityAlien import EntityAlien
from EntityPlayer import EntityPlayer
from LevelParser import *
import tkFont

#The main game class, which handles frame creation and main game loop
class Display(object):
    def __init__(self, width, height, tkinterRoot, lvlConf = "null"):
        self.count = 0 #A counter for clock purpose
        self.root = tkinterRoot
        self.w = width
        self.h = height
        self.border = 10
        self.enemySize = 50
        self.enemyPerWave = 10
        self.NbWaves = 3
        self.c = Canvas(self.root, width=width, height=height, bg = "gray") #the width and height parameters are updated only 2 frames later...
        self.c.focus_set()
        self.root.title("Space Invader - version 1.04.05") #version : Version.Month.Day
        self.bulletList = [] #The list of all the bullets to be rendered
        self.enemyList = [] #The list of all the enemies to be rendered
        self.enemyGoesRight = 1
        self.currEnemy = 0
        self.flagEnemy = -1
        self.EnemyUpdatingTime = 0
        self.font = tkFont.Font(family = "Consolas", size = 10, weight = "normal")
        self.player = EntityPlayer(250, height-25, 50, 50, self.c, self)
        self.debugString = StringVar()
        self.debugString.set("")
        self.LabelString =  Message(self.c, textvariable = self.debugString, anchor = 'nw', justify = LEFT, width = 200).place(x = 0, y  = 0, width = 135, height = 50)
        self.updatingSpeed = 1 #The number of frames between two enemy updates.
        if lvlConf == "null":
            self.EnemySpaceX = (self.w - 2*self.border - (self.enemyPerWave+1)*self.enemySize) / self.enemyPerWave
            for j in range(0, self.NbWaves):
                for i in range(0, self.enemyPerWave):
                    EntityAlien(self.border + i*(self.enemySize + self.EnemySpaceX) + self.enemySize/2, self.border + (self.NbWaves - (j+1))*(self.enemySize + 10) + self.enemySize/2, self.enemySize, self.enemySize, 5, self.c, self)
        else :
            self.enemyPerWave = lvlConf.nbCol
            self.NbWaves = int(math.ceil(lvlConf.nbLocations/(self.enemyPerWave * 1.0)))
            self.EnemySpaceX = (self.w - 2*lvlConf.border - (self.enemyPerWave+1)*self.enemySize) / self.enemyPerWave
            print ("NbWaves = "), self.NbWaves
            print ("********")
            index = 0
            inindex = 0
            print ("lvlConf.nbLocations : "), lvlConf.nbLocations
            print (lvlConf.alien)
            while index < lvlConf.nbLocations:
                print ("Hello, it's-a-me, Inindex ! : ", inindex)
                i = index % self.enemyPerWave
                j = index / self.enemyPerWave
                if(lvlConf.alien[inindex] != -1):
                    EntityAlien(self.border + i*(self.enemySize + self.EnemySpaceX) + self.enemySize/2, self.border + (self.NbWaves - (j+1))*(self.enemySize + 10) + self.enemySize/2, self.enemySize, self.enemySize, lvlConf.speed, self.c, self, lvlConf.alien[inindex], lvlConf.alien[inindex+2])
                    inindex += 3
                else :
                    inindex += 1
                index += 1
              
        self.update()
        self.root.mainloop()
#########################################################################
#Main game loop
    def update(self):
        #Player updating and rendering
        self.player.next()
        self.player.render(self.c)
        a = 0
        #Bullet updating and rendering
        while(a < len(self.bulletList)):
            if(self.bulletList[a].life == -1):
                self.bulletList.pop(a)
                break
            else:                
                self.bulletList[a].next()
                self.bulletList[a].render(self.c)
                a+=1
        #Enemy updating and rendering (could be in the same loop as Bullet rendering but it's cleaner this way)
        b = 0
        while(b < len(self.enemyList)):
            if(self.enemyList[b].life <= 0):
                self.enemyList[b].c.delete(self.enemyList[b].form)
                self.enemyList.pop(b)
                break
            else:
                b+=1
                
        
        if self.currEnemy >= len(self.enemyList):
            self.currEnemy = 0
            self.flagEnemy = -1
        
        if self.EnemyUpdatingTime > self.updatingSpeed and len(self.enemyList):
            self.enemyList[self.currEnemy].next()
            self.enemyList[self.currEnemy].render(self.c)
            self.EnemyUpdatingTime = 0
            self.currEnemy += 1
        self.EnemyUpdatingTime += 1
        
        self.debugString.set("Bullets : " + str(a) + "\nEnemies : " + str(b) + "\n" + "Player score : " + str(self.player.score) + "\n")

        self.root.update_idletasks()
        
        #Collision detection
        bulletID=0 #Bullet index
        while(bulletID < len(self.bulletList)):
            enemyID=0 #Enemy index
            bulletFlag = 0
            while(enemyID < len(self.enemyList) and bulletFlag == 0):
                #collision boxes of the bullet and of the enemy
                bx0 = self.bulletList[bulletID].posx - self.bulletList[bulletID].width/2
                by0 = self.bulletList[bulletID].posy - self.bulletList[bulletID].height/2
                bx1 = self.bulletList[bulletID].posx + self.bulletList[bulletID].width/2
                by1 = self.bulletList[bulletID].posy + self.bulletList[bulletID].height/2
                ex0 = self.enemyList[enemyID].posx - self.enemyList[enemyID].width/2
                ey0 = self.enemyList[enemyID].posy - self.enemyList[enemyID].height/2
                ex1 = self.enemyList[enemyID].posx + self.enemyList[enemyID].width/2
                ey1 = self.enemyList[enemyID].posy + self.enemyList[enemyID].height/2
                if((bx0 < ex1 and bx1 > ex0 and by0 < ey1 and by1 > ey0)): #If we hit one monster
                    self.enemyList[enemyID].life -= self.bulletList[bulletID].damages
                    self.player.addScore(10)
#                     print ("damaging ", self.bulletList[bulletID].damages)
                    self.bulletList[bulletID].damages = 0
                    self.bulletList[bulletID].c.delete(self.bulletList[bulletID].form)
                    self.bulletList.pop(bulletID)
                    bulletFlag = 1

#                     print ("collided bullet ", bulletID, " and enemy ", enemyID)
                enemyID += 1
            bulletID += 1
        #Keyboard & mouse bindings
        
        self.c.bind("<Button-1>", self.player.shootBullet)
        
        self.c.pack()
        self.count = (self.count + 1)%120
        self.root.after(10, self.update)