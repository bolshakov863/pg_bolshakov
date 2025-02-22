import pygame
from all_colors import *
pygame.init()

size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Моя игра")
BACKGROUND = (50, 255, 50)
screen.fill(BACKGROUND)
rect1 = pygame.Rect(100, 100, 200, 150)
rect2 = pygame.Rect(250, 150, 200, 150)
rect3 = pygame.Rect(500, 100, 250, 150)
rect4 = pygame.Rect(600, 300, 200, 150)
width = 5
def collision(rect, other_rect):
    if rect.colliderect(other_rect):
        pygame.draw.rect(screen, RED, rect, width)
        pygame.draw.rect(screen, RED, other_rect, width)
    else:
        pygame.draw.rect(screen, BLUE, rect, width)
        pygame.draw.rect(screen, BLUE, other_rect, width)

collision(rect1, rect2)
collision(rect3, rect4)
#FPS = 60
clock = pygame.time.Clock()
running = True
while running:
    old_pos = player.topleft
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#    screen.fill(BACKGROUND)
    pygame.display.flip()
#    clock.tick(FPS)

pygame.quit()