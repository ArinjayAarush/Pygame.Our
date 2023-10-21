import pygame
import sys


pygame.init()
screen = pygame.display.set_mode((800,400))
clock = pygame.time.Clock()
icon = pygame.image.load("dozen.png")
pygame.display.set_caption('Dozen')
pygame.display.set_icon(icon)
textfont = pygame.font.Font("font/Pixeltype.ttf",50)

sky_surface = pygame.image.load("graphics/Sky.png")
ground_surface = pygame.image.load("graphics/ground.png")
text_surface = textfont.render('Aarush OP!', False ,'Black')
snail_surface = pygame.image.load("graphics/snail/snail1")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(0,300))
    pygame.display.update()
    clock.tick(60)
    