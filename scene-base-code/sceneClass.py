import pygame
from pygame.locals import *
from pygame.sprite import Sprite

# Basic Colors
BLACK   = (  0,  0,  0)
WHITE   = (255,255,255)
GREEN   = (  0,255,  0)
RED     = (255,  0,  0)
BLUE    = (  0,  0,255)

class Button:
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            self.outline = pygame.draw.rect(win, outline, (self.x-2, self.y-2, self.width+4, self.height+4), 0)
            
        self.boundary = pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x, y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False
    
    def getHitbox(self):
        return self.boundary
    
    def changeColor(self, color):
        self.color = color


class Scene:
    def __init__(self, display, gamestate):
        self.display = display
        self.gamestate = gamestate
        self.changeScene(self.gamestate)

    def processEvents(self):
        if self.gamestate == 'start':
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.startHitbox.collidepoint(event.pos):
                        self.startBTN.changeColor(GREEN)
                        #self.gamestate = 'test'
                else:
                    if self.startHitbox.collidepoint(pygame.mouse.get_pos()):
                        self.startBTN.changeColor(BLUE)
                        #print("mouse is over 'newGameButton'")
                    else:
                        self.startBTN.changeColor(RED)
        if self.gamestate == 'test':
            pygame.quit()


    def startScreen(self, display):
        self.startBTN = Button(RED, 50, 50, 100, 50, text='START')
        self.startBTN.draw(display, True)
        self.startHitbox = self.startBTN.getHitbox()

    def changeScene(self, gamestate):
        if gamestate == 'test':
            self.testScreen(self.display)
        if gamestate == 'start':
            self.startScreen(self.display)

    def drawScene(self, gamestate):
        if gamestate == 'test':
            self.testScreen(self.display)
        if gamestate == 'start':
            self.startScreen(self.display)

