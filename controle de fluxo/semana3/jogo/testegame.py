import pygame

pygame.init()
tela = pygame.display.set_mode((500,500))
pygame.display.set_caption('meu jogo')
while True:
    for event in pygame.event.get():
        pygame.display.update()