import pyxel
import random
from random import random
from random import randint
from ambiente import ambiente

class inimigo(): 
    def __init__(self):
        #Localização do Inimigo
        self.x_Ene = 200
        self.y_Ene = 90
        self.w_Ene = 16
        self.h_Ene = 15
        self.EneSpeed = 1
        # Rando para a movimentação
        self.offset = int(random()*60)
        
        
    def updateEnemy(self):
        #Movimentação do Inimigo
        if (pyxel.frame_count + self.offset) % 30 < 30:
            self.x_Ene -= self.EneSpeed
        while self.x_Ene < 0:
            self.x_Ene = 200
            self.y_Ene = 90
            self.EneSpeed += 0.25 # A cada momento que o inimigo sai da tela acrescenta 0.25 de velocidade
    
    
    def drawInimigo (self):
        u = (pyxel.frame_count // 4 % 2) * 8
        pyxel.blt (self.x_Ene, self.y_Ene, img = 1, u=0, v= 0, w=self.w_Ene, h= self.h_Ene, colkey= pyxel.COLOR_BLACK)