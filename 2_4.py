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
rect = pygame.Rect(0, 100, 200, 150)
speed = 5
FPS = 60
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    rect.x += speed
    if rect.x > screen.get_width():
        rect.x = -rect.width







    screen.fill(BACKGROUND)
    pygame.draw.rect(screen, BLUE, rect)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
