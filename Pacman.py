import pygame
import os

LARGURA = 600
ALTURA = 400
TITULO_DO_JOGO = "PACMAN"
PRETO = (0, 0, 0)


class Game:
    def __init__(self):
        # CRIANDO A TELA DO JOGO
        pygame.init()
        pygame.mixer.init()  # PARA USAR A ABA DE MUISCAS
        self.tela = pygame.display.set_mode((600, 400))  # CRIA A TELA DO JOGO
        pygame.display.set_caption(TITULO_DO_JOGO)
        self.relogio = pygame.time.Clock()  # DEFINE A TAXA DE FPS
        self.esta_rodando = True

    def novo_jogo(self):
        # INSTANCIA AS CLASSES DAS SPRITES DO JOGO
        self.todas_as_sprites = pygame.sprite.Group()  # CHAMA AS SPRITES
        self.rodar()

    def rodar(self):
        self.jogando = True
        while self.jogando:
            self.relogio.tick(30)  # RODA A 30 FRAMES POR SEGUNDO
            self.eventos()
            self.atualizar_sprites()  # VE SE TEVE ALGUM EVENTO, COLISÃO
            self.desenhar_sprites()  # ATUALIZA AS SPRITES

    def eventos(self):
        # DEFINE OS EVENTOS DO JOGO
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.jogando:
                    self.jogando = False

            self.esta_rodando = False

    def atualizar_sprites(self):
        # ATUALIZA AS SPRITES
        self.todas_as_sprites.update()

    def desenhar_sprites(self):
        self.tela.fill(PRETO)  # LIMAPNDO A TELA
        self.todas_as_sprites.draw(self.tela)  # DESENHANDO AS SPRITES
        pygame.display.flip()  # ATUALIZA A TELA POR FRAME

    def carregar_arquivos(self):
        # CARREGAR OS ARQUIVOS DE AUDIO E IMAGENS
        diretorio_imagens = os.path.join(os.getcwd(), 'imagens')

    def mostrar_tela_start(self):
        pass

    def mostrar_tela_game_over(self):
        pass


g = Game()
g.mostrar_tela_start()

while g.esta_rodando:
    g.novo_jogo()
    g.mostrar_tela_game_over()










