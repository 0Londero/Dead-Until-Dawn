#importando as bibliotecas necessárias
import pyxel
import random 
#aleatoriedade
from random import randint
from random import random


#cria-se a classe do jogador 
class player:
    def __init__(self):
        #Indica a posição no mapa
        self.x = 20
        self.y = 90
        self.w = 16
        self.h = 16
        #Status do jogador
        self.player_vy = 0
        self.playerAlive = True


    def updateplayer (self):
        #Movimentação do personagem
        if pyxel.btn (pyxel.KEY_LEFT): # Seta para esquerda
            self.x = max(self.x - 2,0)
        
        if pyxel.btn (pyxel.KEY_RIGHT): # Seta para direita
            self.x = min(self.x + 2,190)
            
        if pyxel.btn (pyxel.KEY_SPACE): # Pulo do jogador no espaço
            if self.y > 67:
                # Soma ou movimento para cima aonde adiona a variável vy
                self.y += self.player_vy
                self.player_vy = min(self.player_vy - 1,1)
                
                
        # Ápice do pulo no qual começa a descida 
        if self.y != 90 and self.y <91:
            self.y += self.player_vy
            self.player_vy = min(self.player_vy + 1,1)
        
    # Desenha o personagem na tela
    def drawPlayer(self):
        u = (pyxel.frame_count // 4 % 2) * 8
        pyxel.blt (x= self.x  , y= self.y, img= 0 , u=u , v= 0 , w=8 , h=8 , colkey= pyxel.COLOR_BLACK)
    
    def exception(self):
        try:
            assert (self.y == 90) # Jogador correndo por conta da posição inicial 
        except AssertionError:
            print ("Exceção Assertion, Jogador está pulando")
        else:
            print ("Em movimento")