import pygame
import random

# Definir cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)

# Definir tamanho da tela
largura_tela = 640
altura_tela = 480

# Inicializar Pygame
pygame.init()

# Criar a tela
tela = pygame.display.set_mode([largura_tela, altura_tela])

# Definir título da janela
pygame.display.set_caption("Jogo da Cobrinha")

# Define o relógio
clock = pygame.time.Clock()

# Variáveis da cobrinha
tamanho_cobrinha = 10
velocidade = 15

# Define a fonte do texto
fonte = pygame.font.SysFont(None, 25)


def desenha_cobrinha(lista_cobrinha):
    for i in lista_cobrinha:
        pygame.draw.rect(tela, VERDE, [i[0], i[1], tamanho_cobrinha, tamanho_cobrinha])


def mensagem(msg, cor):
    texto = fonte.render(msg, True, cor)
    tela.blit(texto, [largura_tela / 6, altura_tela / 3])


# Loop principal do jogo
def jogo():
    sair = False
    fim_de_jogo = False

    # Posição inicial da cobrinha
    pos_x = largura_tela / 2
    pos_y = altura_tela / 2

    # Variáveis da cobrinha
    lista_cobrinha = [[pos_x, pos_y]]
    comprimento_cobrinha = 1

    # Define a posição inicial da maçã
    maca_x = round(random.randrange(0, largura_tela - tamanho_cobrinha) / 10.0) * 10.0
    maca_y = round(random.randrange(0, altura_tela - tamanho_cobrinha) / 10.0) * 10.0

    # Loop principal do jogo
    while not sair:
        while fim_de_jogo:
            tela.fill(BRANCO)
            mensagem("Fim de jogo! Pressione Q-Sair ou C-Continuar", VERMELHO)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sair = True
                    fim_de_jogo = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sair = True
                        fim_de_jogo = False
                    if event.key == pygame.K_c:
                        jogo()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    mov_x = -tamanho_cobrinha
                    mov_y = 0
                elif event.key == pygame.K_RIGHT:
                    mov_x = tamanho_cobrinha
                    mov_y = 0
            
