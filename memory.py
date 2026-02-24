import pygame
import sys


pygame.init()

LARGURA, ALTURA = 400, 400
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Treino de Memória 3x3")


BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CINZA_CLARO = (213, 213, 213)

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    tela.fill(CINZA_CLARO)


    TAMANHO_QUADRADO = 100
    ESPACO = 10
    for linha in range(3):
        for coluna in range(3):
            x = coluna * (TAMANHO_QUADRADO + ESPACO) + 40
            y = linha * (TAMANHO_QUADRADO + ESPACO) + 40

            if coluna == 1:
                espessura = 0
            else:
                espessura = 2

            pygame.draw.rect(tela, PRETO, (x, y, TAMANHO_QUADRADO, TAMANHO_QUADRADO), espessura)

    pygame.display.flip()
    
