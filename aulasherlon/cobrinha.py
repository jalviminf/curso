import pygame
import random
import sys

# Define as direções
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Define as constantes do jogo
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BLOCK_SIZE = 10
SPEED = 20

# Define as cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Inicializa o pygame
pygame.init()

# Cria a janela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jogo da Cobrinha")

# Cria a classe da cobra
class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = GREEN

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = ((cur[0] + (x * BLOCK_SIZE)), (cur[1] + (y * BLOCK_SIZE)))
        if new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, BLACK, r, 1)

# Cria a classe da comida
class Food:
    def __init__(self):
        x = random.randrange(0, SCREEN_WIDTH, BLOCK_SIZE)
        y = random.randrange(0, SCREEN_HEIGHT, BLOCK_SIZE)
        self.position = (x, y)
        self.color = RED

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, BLACK, r, 1)

# Loop principal do jogo
while True:
    clock = pygame.time.Clock()

    # Cria a cobra e a comida
    snake = Snake()
    food = Food()

    # Loop principal do jogo
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.turn(UP)
                elif event.key == pygame.K_DOWN:
                    snake.turn(DOWN)
                elif event.key == pygame.K_LEFT:
                    snake.turn(LEFT)
                elif event.key == pygame.K_RIGHT:
                    snake.turn(RIGHT)

        snake.move()

        if snake.get_head_position() == food.position:
            snake.length += 1
            food = Food()

        screen.fill(WHITE)
        snake.draw(screen)
        food.draw(screen)
        pygame.display.update()
        pygame.time.Clock().tick(SPEED)
