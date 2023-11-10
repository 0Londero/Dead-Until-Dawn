import pyxel
import random 
from random import random 
from random import randint
from Personagem import player
from inimigo import inimigo

class Colision(player, inimigo):
    def __init__(self):
        player.__init__()
        inimigo.__init__()
        
    
    def ColisionUpdate (self):
        if ((self.x + 3 == self.x_Ene - 2) or (self.x + 3 == self.x_Ene - 2.25) or (self.x + 3 == self.x_Ene -2.50) or (self.x + 3 == self.x_Ene -2.75) or (self.x + 3 == self.x_Ene -3.0)):
            if self.playerAlive:
                #jogador morre
                self.playerAlive = False
                #reset score e posição
                self.score = 0
                self.x = 20
                self.y = 90
                self.player_vy = 0
                self.playerAlive = True
                self.x_Ene = 200
                self.y_Ene = 90
                self.w_Ene = 16
                self.h_Ene = 16
                self.EneSpeed = 1