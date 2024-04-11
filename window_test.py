import pygame
from pygame.locals import *
pygame.init()

info = pygame.display.Info()
w = info.current_w
h = info.current_h

screen = pygame.display.set_mode((w, h-55), SCALED)



while True:
    for event in pygame.event.get():
        if event.type == QUIT: 
            pygame.display.quit()
        
    
        
