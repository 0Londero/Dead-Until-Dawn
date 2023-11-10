#importando as bibliotecas necessárias
import pyxel
import random
#aleatoriedade
from random import randint
from random import random 


# Cria a classe do ambiente e inicializa a pontuação
class ambiente:
    def __init__(self):
        self.score = 0
    
    # Atualiza a pontuação do ambiente
    def atualizapontuacao (self):
        if pyxel.frame_count % 10000:
            self.score += 1
            
            
    
    
    def drawcenario (self):
        offset = pyxel.frame_count % 200
        for loop in range (2):
            pyxel.bltm (loop*200 - offset, 0, 0, 0, 0, 200, 120, colkey= pyxel.COLOR_BLACK)
        s = "Score {: >4} ". format (self.score)
        pyxel.text (5 , 4, s, 1)
        pyxel.text (4, 4, s, 7)