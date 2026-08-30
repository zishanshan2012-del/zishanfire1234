import pygame
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("My pygame window")
runnig = True
while runnig:
    for event in pygame.event.get():
        if event.type == pygame.Quit:
            runnig = False
pygame.quit()