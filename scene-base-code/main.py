import pygame
import sys
import pygame_widgets
from pygame_widgets.button import Button
from pygame_widgets.slider import Slider
import colorsys

info = pygame.display.Info()
w = info.current_w
h = info.current_h
FPS = 60

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

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((w, h-55))
        self.clock = pygame.time.Clock()
        
        self.gameStateManager = GameStateManager('start')
        self.start = Start(self.screen, self.gameStateManager)
        self.level = Level(self.screen, self.gameStateManager)
        self.states = {'start':self.start, 'level':self.level}
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    self.gameStateManager.set_state('level')
                    
            self.states[self.gameStateManager.get_state()].run()
                    
            pygame.display.update()
            self.clock.tick(FPS)
            
class Level:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
    def run(self):
        self.display.fill('red')
        
class Start:
    def __init__(self, display, gameStateManager):
        self.display = display
        #self.gameStateManager = gameStateManager
        #self.startBTN = Button('green', 50, 50, 100, 50, text='START')
        #self.startHitbox = self.startBTN.getHitbox()
    def run(self):
        self.display.fill('blue')
        '''
        self.startBTN.draw(self.display, True)
        for event in pygame.event.get():
            if self.startHitbox.collidepoint(event.pos):
                    self.gameStateManager.set_state('level')
        '''
        
class GameStateManager:
    def __init__(self, currentState):
        self.currentState = currentState
    def get_state(self):
        return self.currentState
    def set_state(self, gamestate):
        self.currentState = gamestate
        
if __name__ == '__main__':
    game = Game()
    game.run()
        