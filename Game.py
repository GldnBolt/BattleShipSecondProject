import pygame

BLUE = (0,0,255)
BLACK = (0,0,0)

TamGrid = 100

pygame.init()

size = (600,600)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Grid")

clock = pygame.time.Clock()
gameOver = False

while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
    screen.fill(BLACK)
    for i in range(1, size[0], TamGrid + 1):
         for j in range(1, size[1], TamGrid + 1):
             pygame.draw.rect(screen, BLUE, [i, j, TamGrid, TamGrid], 0)
    pygame.display.flip()
    clock.tick(1)
pygame.quit()
