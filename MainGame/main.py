import pygame
import sys
import pygame_widgets
from pygame_widgets.button import Button
from pygame_widgets.slider import Slider
import colorsys

pygame.init()

#grabs info of display ot use for window size
info = pygame.display.Info()
w = info.current_w
h = info.current_h

screen = pygame.display.set_mode((w, h-55))
FPS = 60

class Game:
    def __init__(self):
        
        self.screen = pygame.display.set_mode((w, h))
        self.clock = pygame.time.Clock()
        
        self.startBTN = Button(
        # Mandatory Parameters
        self.screen,  # Surface to place button on
        100,  # X-coordinate of top left corner
        100,  # Y-coordinate of top left corner
        300,  # Width
        150,  # Height

        # Optional Parameters
        text='Start',  # Text to display
        fontSize=50,  # Size of font
        margin=20,  # Minimum distance between text/image and edge of button
        inactiveColour=(200, 50, 0),  # Colour of button when not being interacted with
        hoverColour=(150, 0, 0),  # Colour of button when being hovered over
        pressedColour=(0, 200, 20),  # Colour of button when being clicked
        radius=20,  # Radius of border corners (leave empty for not curved)
        onClick=lambda: self.gameStateManager.set_state('level')  # Function to call when clicked on
    )
        
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
                    
            pygame_widgets.update(pygame.event.get())
            pygame.display.update()
              # Call once every loop to allow widgets to render and listen
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
        