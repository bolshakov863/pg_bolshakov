import random
import pygame
from all_colors import *
pygame.init()
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
BACKGROUND = (255, 255, 255)
screen.fill(BACKGROUND)
color_index = random.randint(0,18)
if color_index == 18:
   color = (random.randint(0, 225), random.randint(0,255), random.randint(0,255))
else:
    color = COLORS[color_index]

width = 100
height = 75
rects = []
rects.append(pygame.Rect(0, 0, width, height))
rects.append(pygame.Rect(0, 0, width, height))
rects[-1].topright = (screen_width, 0)
rects.append(pygame.Rect(0, 0, width, height))
rects[-1].bottomright = (screen_width, screen_height)
rects.append(pygame.Rect(0, 0, width, height))
rects[-1].center = (screen_width // 2, screen_height // 2)
rects.append(pygame.Rect(0, 0, width, height))
rects[-1].bottomleft = (0, screen_height)
for rect in rects:
    pygame.draw.rect(screen, color,  rect)
clock = pygame.time.Clock()
pygame.display.flip()
running = True
timer = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    color_index = random.randint(0, 18)
    if color_index == 18:
        color = (random.randint(0, 225), random.randint(0, 255), random.randint(0, 255))
    else:
        color = COLORS[color_index]
    screen_fill = (rect)
    pygame.display.flip()
    pygame.time.delay(random.randint(200, 800))

pygame.quit()