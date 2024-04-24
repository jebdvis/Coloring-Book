import pygame
from pygame.locals import *
from sceneClass import *


pygame.init()

# Basic Colors
BLACK   = (  0,  0,  0)
WHITE   = (255,255,255)
GREEN   = (  0,255,  0)
RED     = (255,  0,  0)
BLUE    = (  0,  0,255)

'''
# Dimensions/display of screen [OLD]
size = (400,500)
WIDTH = 500
HEIGHT = 400
screen = pygame.display.set_mode(size)
screen.fill(WHITE)
'''
# Dimensions/display of screen
info = pygame.display.Info()
w = info.current_w
h = info.current_h

screen = pygame.display.set_mode((w, h-55))
screen.fill(WHITE)

# Loop Switch
done = False

# Screen Update Speed (FPS)
clock = pygame.time.Clock()

gameScene = Scene(screen, 'start')

# Create start button
'''
startBTN = Button(RED, 50, 50, 100, 50, text='START')
startBTN.draw(screen, True)
startHitbox = startBTN.getHitbox()
'''


#Gamestate initialization
gamestate = 'start'

# ------- Main Program Loop -------
while not done:
    mouse = pygame.mouse.get_pos() 
    # --- Main Event Loop ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        else:
            gameScene.processEvents()
    #gameScene.drawScene(gamestate)

    '''
        if event.type == pygame.MOUSEBUTTONDOWN:
            if startHitbox.collidepoint(event.pos):
                #startBTN.changeColor(GREEN)
                gamestate = 'test'
        else:
            if startHitbox.collidepoint(pygame.mouse.get_pos()):
                startBTN.changeColor(BLUE)
                #print("mouse is over 'newGameButton'")
            else:
                startBTN.changeColor(RED)
                '''


    # Updates display
    pygame.display.flip()
    pygame.display.update()
    #startBTN.draw(screen, True)

    #Setting FPS
    clock.tick(60)

#Shutdown
pygame.quit()