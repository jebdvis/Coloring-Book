import pygame
import sys
import pygame_widgets
from pygame_widgets.button import Button
from pygame_widgets.slider import Slider
import colorsys
from UIScene import *
import gif_pygame

class PickPage:
    def __init__(self, display, gameStateManager):
        self.w = display.get_width()
        self.h = display.get_height()
        self.choose = gif_pygame.load("assets/Choose-a-page-5-2-2024.gif")
        self.background = pygame.image.load("assets/background.jpeg")
        self.background = pygame.transform.scale(self.background, (self.w, self.h+100))
        self.display = display
        self.gameStateManager = gameStateManager
        self.buttonFont = pygame.font.SysFont('comicsansms',50)
        
        self.backBTN = Button(
        # Mandatory Parameters
        self.display,  # Surface to place button on
        (self.w/2) - (300/2),  # X-coordinate of top left corner
        (self.h-200),  # Y-coordinate of top left corner
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

        self.testBTN = Button(
        # Mandatory Parameters
        self.display,  # Surface to place button on
        50,  # X-coordinate of top left corner
        100,  # Y-coordinate of top left corner
        300,  # Width
        100,  # Height

        # Optional Parameters
        text='Test page',  # Text to display
        font=self.buttonFont,
        fontSize=50,  # Size of font
        margin=20,  # Minimum distance between text/image and edge of button
        inactiveColour=(200, 50, 0),  # Colour of button when not being interacted with
        hoverColour=(150, 0, 0),  # Colour of button when being hovered over
        pressedColour=(0, 200, 20),  # Colour of button when being clicked  # Radius of border corners (leave empty for not curved)
        image=pygame.transform.scale(pygame.image.load('assets/paintborder.jpeg'), (300, 100)),
        radius=20,
        onClick=lambda: self.hideButtonDraw()  # Function to call when clicked on
        )
        self.testBTN.hide()

    def hideButtonBack(self):
        self.gameStateManager.set_state('start')
        self.backBTN.hide()

    def hideButtonDraw(self):
        self.gameStateManager.set_state('draw')
        self.backBTN.hide()
        self.testBTN.hide()

    #def createThumbnails(self):

                    
    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        self.backBTN.show()
        self.testBTN.show()
        self.display.blit(self.background, (0, 0))
        self.choose.render(self.display, ((self.w/2) - (self.choose.get_width()/2), 25))