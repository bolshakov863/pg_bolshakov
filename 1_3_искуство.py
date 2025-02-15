import random
from all_colors import *
import pygame
pygame.init()

size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Моя игра")
BACKGROUND = (255, 255, 255)
screen.fill(BACKGROUND)
line_color = RED
FPS = 60
line_width = 5
start_pos = (0, size[1]//2)
end_pos = (size[0], size[1]//2)
clock = pygame.time.Clock()
COLORS = [RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA, GRAY, ORANGE, PINK, BROWN, PURPLE, LIME, NAVY, OLIVE, MAROON, TEAL, SILVER, GOLD]
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    color_index = random.randint(0, 18)
    if color_index == 18:
      BACKGROUND = (random.randint(0, 225), random.randint(0,255), random.randint(0,255))
    else:
      BACKGROUND = COLORS[color_index]
    screen.fill(BACKGROUND)
    screen.fill(BACKGROUND)

    pygame.draw.line(screen, line_color, start_pos, end_pos, line_width)

    pygame.draw.ellipse(screen, ORANGE, (50, 50, 100, 100))

    pygame.draw.ellipse(screen, BLUE, (250, 50, 100, 100))

    pygame.draw.ellipse(screen, RED, (450, 50, 100, 100))

    pygame.draw.ellipse(screen, YELLOW, (50, 450, 100, 100))

    pygame.draw.ellipse(screen, PINK, (250, 450, 100, 100))

    pygame.draw.ellipse(screen, PURPLE, (750, 250, 100, 100))


    pygame.display.flip()
    pygame.time.delay(random.randint(200, 800))

pygame.quit()