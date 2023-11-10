import pyxel
#Importa todas as classes relacionadas com o jogo
from Personagem import player
from inimigo import inimigo
from ambiente import ambiente
from obstaculos import Colision

INICIO = 0
JOGAR = 1 

class DeadUntilDawn:
    def __init__(self):
        #Resolução e nome da janela
        pyxel.init( 200,120, title = "Dead Until Dawn")
        #Carrega as sprites
        pyxel.load ("art.pyxres")
        pyxel.playm (0,loop=True)
        self.telainicio = INICIO
        #Recebimento por herança as funçoes construtoras das classes
        ambiente.__init__(self)
        player.__init__(self)
        inimigo.__init__(self)
        player.exception(self)
        pyxel.run(self.update, self.draw)
    


    def update(self):
        #Escape sai do jogo
        if pyxel.btn (pyxel.KEY_ESCAPE):
            pyxel.quit()
        
        if self.telainicio == INICIO:
            self.update_tela()
 
        elif self.telainicio == JOGAR:
            self.update_jogar()
    
    
    def update_tela(self):
        #Atualiza a tela, utilizando o espaço para iniciar o jogo
        if pyxel.btnp (pyxel.KEY_SPACE):
            self.telainicio = JOGAR
        
    
    def update_jogar(self):
        Colision.ColisionUpdate(self) 
        player.updateplayer(self)
        inimigo.updateEnemy(self)
        
    def draw(self):
        pyxel.cls(0)
        ambiente.drawcenario(self)
        if self.telainicio == INICIO:
            self.drawInicio() 
        elif self.telainicio == JOGAR:
            self.drawJogar()
        inimigo.drawInimigo(self)
        player.drawPlayer(self)
    
    
    def drawInicio (self):
        pyxel.text (48,50, "Dead Until Dawn", pyxel.frame_count % 16)
        pyxel.text (75,60, " Aperte Espaco para comecar ", 13)
        
    def drawJogar (self):
        ambiente.atualizapontuacao (self)
        inimigo.drawInimigo (self)
        player.drawPlayer (self)
        
try:
    print ('Aperte CTRL + C para iniciar o jogo!')
    inp=input()
except KeyboardInterrupt:
    print ('keyboardInterrupt!')

DeadUntilDawn()
