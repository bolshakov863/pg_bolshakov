from pygame.constants import *
from all_colors import *
import pygame
from random import choice
pygame.init()

size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Моя игра")
BACKGROUND = (255, 255, 255)
screen.fill(BACKGROUND)
x = 0
y = 0
rect_size = 200
colors = [RED,BLACK]
#rect1 = pygame.Rect(x, y, rect_size, rect_size)
#rect1.center = (screen.get_width() // 2, screen.get_height() // 2)
#rect2 = pygame.Rect(x, y, rect_size // 2, rect_size // 2)
#rect2.center = (screen.get_width() // 2, screen.get_height() // 2)
#pygame.draw.rect(screen, BLACK, rect1)
#pygame.draw.rect(screen,RED, rect2)
for i in range(1,2):
    rect1 = pygame.Rect(x, y, rect_size, rect_size)
    rect1.center = (screen.get_width() // 2, screen.get_height() // 2)
    rect2 = pygame.Rect(x, y, rect_size // 2, rect_size // 2)
    rect2.center = (screen.get_width() // 2, screen.get_height() // 2)
    pygame.draw.rect(screen, BLACK, rect1)
    pygame.draw.rect(screen, RED, rect2)
FPS = 60
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()