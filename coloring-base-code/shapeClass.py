import pygame
import pygame.font

''''Global variables'''
# Basic Colors
BLACK   = (  0,  0,  0)
WHITE   = (255,255,255)
GREEN   = (  0,255,  0)
RED     = (255,  0,  0)
BLUE    = (  0,  0,255)

'''
# Dimensions/display of screen
size = (400,500)
WIDTH = 500
HEIGHT = 400
screen = pygame.display.set_mode(size)
screen.fill(WHITE)
'''

'''Draws a shape object using sprite'''
class Shape(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color, shape, display):
        super().__init__() # Inherits things from pygame.sprite.Sprite (I think)
        # Initialize variables
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.shape = shape
        self.display = display

    # Draws the shape
    def draw(self):
        # Checks which shape is needing to be drawn; there will probably be more types in the actual program
        if (self.shape == 'rect'):
            # Outline
            self.outline = pygame.draw.rect(self.display, BLACK, (self.x, self.y, self.width, self.height), 4)
            # Fill
            self.fill = pygame.draw.rect(self.display, self.color, (self.x + 2, self.y + 2, self.width - 4, self.height - 4))
            
        if (self.shape == 'circle'):
            # Outline
            self.outline = pygame.draw.circle(self.display, BLACK, (self.x, self.y), self.width, 3)
            # Fill
            self.fill = pygame.draw.circle(self.display, self.color, (self.x, self.y), self.width - 3)
            # Updates display
            pygame.display.update()

    # Updates and changes color variable for shape fill
    def changeColor(self, color):
        self.color = color # Needed to keep shape's color as the new color

    # Returns the shape object's shape type (represented by the fill)
    def getShape(self):
        return self.fill
    
    # Returns the shape object's current color (for color swatches)
    def getColor(self):
        return self.color
        