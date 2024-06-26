import pygame
import sys
import pygame_widgets
from pygame_widgets.button import Button
from pygame_widgets.slider import Slider
import colorsys
from pygame.locals import *

info = pygame.display.Info()
w = info.current_w
h = info.current_h
FPS = 60

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
    def run(self):
        self.display.fill('blue')
        
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
        