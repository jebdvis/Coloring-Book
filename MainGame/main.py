import pygame
import sys
import pygame_widgets
from pygame_widgets.button import Button
from pygame_widgets.slider import Slider
import colorsys
from pickPageScene import *
from UIScene import *
import gif_pygame

pygame.init()
#print(pygame.font.get_fonts())

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
        
        self.gameStateManager = GameStateManager('start')
        
        self.draw = ColorPage(self.screen, self.gameStateManager)
        self.start = Start(self.screen, self.gameStateManager)
        self.credits = Credits(self.screen, self.gameStateManager)
        self.pickPage = PickPage(self.screen, self.gameStateManager, self.draw)
        
        self.states = {'start':self.start, 'draw':self.draw, 'credits':self.credits, 'pickPage':self.pickPage}

        
    def run(self):
        while True:                    
            self.states[self.gameStateManager.get_state()].run()
                    
            pygame_widgets.update(pygame.event.get())
            pygame.display.update()
              # Call once every loop to allow widgets to render and listen
            self.clock.tick(FPS)

class Start:
    def __init__(self, display, gameStateManager):
        self.logo = gif_pygame.load("assets/My-Coloring-Book-5-2-2024.gif")
        self.background = pygame.image.load("assets/background.jpeg")
        self.background = pygame.transform.scale(self.background, (w, h+100))
        self.display = display
        self.gameStateManager = gameStateManager
        self.buttonFont = pygame.font.SysFont('comicsansms',50)
        
        self.startBTN = Button(
        # Mandatory Parameters
        self.display,  # Surface to place button on
        (w/2) - (300/2),  # X-coordinate of top left corner
        250,  # Y-coordinate of top left corner
        300,  # Width
        100,  # Height

        # Optional Parameters
        text='Start',  # Text to display
        font=self.buttonFont,
        fontSize=50,  # Size of font
        margin=20,  # Minimum distance between text/image and edge of button
        inactiveColour=(200, 50, 0),  # Colour of button when not being interacted with
        hoverColour=(150, 0, 0),  # Colour of button when being hovered over
        pressedColour=(0, 200, 20),  # Colour of button when being clicked  # Radius of border corners (leave empty for not curved)
        image=pygame.transform.scale(pygame.image.load('assets/paintborder.jpeg'), (300, 100)),
        radius=20,
        onClick=lambda: self.hideButtonPick()  # Function to call when clicked on
        )

        self.creditBTN = Button(
        # Mandatory Parameters
        self.display,  # Surface to place button on
        (w/2) - (300/2),  # X-coordinate of top left corner
        400,  # Y-coordinate of top left corner
        300,  # Width
        100,  # Height

        # Optional Parameters
        text='Credits',  # Text to display
        font=self.buttonFont,
        fontSize=50,  # Size of font
        margin=20,  # Minimum distance between text/image and edge of button
        inactiveColour=(200, 50, 0),  # Colour of button when not being interacted with
        hoverColour=(150, 0, 0),  # Colour of button when being hovered over
        pressedColour=(0, 200, 20),  # Colour of button when being clicked  # Radius of border corners (leave empty for not curved)
        image=pygame.transform.scale(pygame.image.load('assets/paintborder.jpeg'), (300, 100)),
        radius=20,
        onClick=lambda: self.hideButtonCredits()  # Function to call when clicked on
        )

        self.quitBTN = Button(
        # Mandatory Parameters
        self.display,  # Surface to place button on
        (w/2) - (300/2),  # X-coordinate of top left corner
        550,  # Y-coordinate of top left corner
        300,  # Width
        100,  # Height

        # Optional Parameters
        text='Quit',  # Text to display
        font=self.buttonFont,
        fontSize=50,  # Size of font
        margin=20,  # Minimum distance between text/image and edge of button
        inactiveColour=(200, 50, 0),  # Colour of button when not being interacted with
        hoverColour=(150, 0, 0),  # Colour of button when being hovered over
        pressedColour=(0, 200, 20),  # Colour of button when being clicked  # Radius of border corners (leave empty for not curved)
        image=pygame.transform.scale(pygame.image.load('assets/paintborder.jpeg'), (300, 100)),
        radius=20,
        onClick=lambda: pygame.quit()  # Function to call when clicked on
        )
        
    def hideButtonPick(self):
        #self.gameStateManager.set_state('draw')
        self.gameStateManager.set_state('pickPage')
        self.startBTN.hide()
        self.creditBTN.hide()
        self.quitBTN.hide()

    def hideButtonCredits(self):
        self.gameStateManager.set_state('credits')
        self.creditBTN.hide()
        self.startBTN.hide()
        self.quitBTN.hide()
                    
    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        self.startBTN.show()
        self.creditBTN.show()
        self.quitBTN.show()
        self.display.blit(self.background, (0, 0))
        self.logo.render(self.display, ((w/2) - (self.logo.get_width()/2), 50))


class Credits:
    def __init__(self, display, gameStateManager):
        self.credits = gif_pygame.load("assets/Credits-5-2-20243.gif")
        self.background = pygame.image.load("assets/background.jpeg")
        self.background = pygame.transform.scale(self.background, (w, h+100))
        self.display = display
        self.gameStateManager = gameStateManager
        self.buttonFont = pygame.font.SysFont('comicsansms',50)
        
        self.backBTN = Button(
        # Mandatory Parameters
        self.display,  # Surface to place button on
        (w/2) - (300/2),  # X-coordinate of top left corner
        (h-250),  # Y-coordinate of top left corner
        300,  # Width
        100,  # Height

        # Optional Parameters
        text='Back',  # Text to display
        font=self.buttonFont,
        fontSize=50,  # Size of font
        margin=20,  # Minimum distance between text/image and edge of button
        inactiveColour=(200, 50, 0),  # Colour of button when not being interacted with
        hoverColour=(150, 0, 0),  # Colour of button when being hovered over
        pressedColour=(0, 200, 20),  # Colour of button when being clicked  # Radius of border corners (leave empty for not curved)
        image=pygame.transform.scale(pygame.image.load('assets/paintborder.jpeg'), (300, 100)),
        radius=20,
        onClick=lambda: self.hideButtonBack()  # Function to call when clicked on
        )
        self.backBTN.hide()

    def hideButtonBack(self):
        self.gameStateManager.set_state('start')
        self.backBTN.hide()
                    
    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        self.backBTN.show()
        self.display.blit(self.background, (0, 0))
        self.credits.render(self.display, ((w/2) - (self.credits.get_width()/2), 50))

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
        