import pygame
import sys
import pygame_widgets
from pygame_widgets.button import Button
from pygame_widgets.button import ButtonArray
from pygame_widgets.slider import Slider
import colorsys
from UIScene import *
import gif_pygame
from imageConverter import load_and_convert
import easygui

class PickPage:
    def __init__(self, display, gameStateManager, drawingScene):
        self.w = display.get_width()
        self.h = display.get_height()
        self.choose = gif_pygame.load("assets/Choose-a-page-5-2-2024.gif")
        self.background = pygame.image.load("assets/background.jpeg")
        self.background = pygame.transform.scale(self.background, (self.w, self.h+100))
        self.display = display
        self.gameStateManager = gameStateManager
        self.buttonFont = pygame.font.SysFont('comicsansms',50)
        self.drawingScene = drawingScene
        self.loading_text = self.buttonFont.render('Refer to console for loading.', False, (0, 0, 0))
        
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

        self.uploadBTN = Button(
        # Mandatory Parameters
        self.display,  # Surface to place button on
        self.w * 1/8 ,  # X-coordinate of top left corner
        (self.h-200),  # Y-coordinate of top left corner
        200,  # Width
        100,  # Height

        # Optional Parameters
        text='Upload Custom',  # Text to display
        font=self.buttonFont,
        fontSize=50,  # Size of font
        margin=20,  # Minimum distance between text/image and edge of button
        inactiveColour=(200, 50, 0),  # Colour of button when not being interacted with
        hoverColour=(150, 0, 0),  # Colour of button when being hovered over
        pressedColour=(0, 200, 20),  # Colour of button when being clicked  # Radius of border corners (leave empty for not curved)
        image=pygame.transform.scale(pygame.image.load('assets/paintborder.jpeg'), (500, 100)),
        radius=20,
        onClick=lambda: self.loadCustomPage()  # Function to call when clicked on
        )
        self.uploadBTN.hide()

        self.pickCustomBTN = Button(
        # Mandatory Parameters
        self.display,  # Surface to place button on
        (self.w * 3/4),  # X-coordinate of top left corner
        (self.h-200),  # Y-coordinate of top left corner
        200,  # Width
        100,  # Height

        # Optional Parameters
        text='Pick Custom',  # Text to display
        font=self.buttonFont,
        fontSize=50,  # Size of font
        margin=20,  # Minimum distance between text/image and edge of button
        inactiveColour=(200, 50, 0),  # Colour of button when not being interacted with
        hoverColour=(150, 0, 0),  # Colour of button when being hovered over
        pressedColour=(0, 200, 20),  # Colour of button when being clicked  # Radius of border corners (leave empty for not curved)
        image=pygame.transform.scale(pygame.image.load('assets/paintborder.jpeg'), (500, 100)),
        radius=20,
        onClick=lambda: self.pickCustomPage()  # Function to call when clicked on
        )
        self.pickCustomBTN.hide()

    def hideButtonBack(self):
        self.gameStateManager.set_state('start')
        self.backBTN.hide()
        #self.testBTN1.hide()
        #self.testBTN2.hide()
        self.pages.hide()
        self.pickCustomBTN.hide()
        self.uploadBTN.hide()

    def createThumbnails(self):
        self.pages = ButtonArray(
            self.display,  # Surface to place button array on
            50,  # X-coordinate
            250,  # Y-coordinate
            self.w,  # Width
            500,  # Height
            (6, 2),  # Shape: 2 buttons wide, 2 buttons tall
            colour = (255, 255, 255),
            border=100,  # Distance between buttons and edge of array
            texts=('Cat in a pumpkin', 'Eevee', 'Flowers', 'Frog', 'Ice Cream', 'Mandala', 'Mudkip', 'Pikachu', 'Pumpkin', 'Santa', 'Toucan', 'Triangles'),  # Sets the texts of each button (counts left to right then top to bottom)
            fontSize=50,
            # When clicked, print number
            onClicks=(lambda: self.loadPage('Color_Pages/catpumpkin.jpeg'), lambda: self.loadPage('Color_Pages/eevee.png'), lambda: self.loadPage('Color_Pages/flowers.jpeg'), lambda: self.loadPage('Color_Pages/frog.jpeg'), lambda: self.loadPage('Color_Pages/icecream.jpeg'), lambda: self.loadPage('Color_Pages/mandala.jpeg'), lambda: self.loadPage('Color_Pages/mudkip.png'), lambda: self.loadPage('Color_Pages/pikachu.png'), lambda: self.loadPage('Color_Pages/pumpkin.jpeg'), lambda: self.loadPage('Color_Pages/santa.jpeg'), lambda: self.loadPage('Color_Pages/toucan.jpeg'), lambda: self.loadPage('Color_Pages/triangles.jpeg'))
        )

    def loadPage(self, page):
        self.drawingScene.setPage(page)    
        self.gameStateManager.set_state('draw')
        self.backBTN.hide()
        self.pickCustomBTN.hide()
        self.uploadBTN.hide()
        self.pages.hide()

    def loadCustomPage(self):
        load_and_convert()


    def pickCustomPage(self):
        source_file = easygui.fileopenbox(default = "Custom_Pages/*.*")
        if source_file == True:
            self.loadPage(source_file)
        
    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        self.backBTN.show()
        self.pickCustomBTN.show()
        self.uploadBTN.show()
        self.createThumbnails()
        self.pages.show()
        #self.testBTN1.show()
        #self.testBTN2.show()
        self.display.blit(self.background, (0, 0))
        self.choose.render(self.display, ((self.w/2) - (self.choose.get_width()/2), 25))
        self.display.blit(self.loading_text,(0,self.h * 28/32))
