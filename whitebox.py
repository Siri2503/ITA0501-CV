import pygame
import sys
pygame.init()
width, height = 500, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("White Rectangle on Black Background")
black = (0, 0, 0)
white = (255, 255, 255)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(black)
    rect_width = 100
    rect_height = 50
    rect_x = (width - rect_width) // 2
    rect_y = (height - rect_height) // 2
    pygame.draw.rect(screen, white, (rect_x, rect_y, rect_width, rect_height))
    pygame.display.flip()
    pygame.time.Clock().tick(60)
pygame.quit()
sys.exit()
