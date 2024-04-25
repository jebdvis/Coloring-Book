import pygame
import pygame.font

''''Global variables'''
# Colours
BLACK   = (  0,  0,  0)
WHITE   = (255,255,255)
GREEN   = (  0,255,  0)
RED     = (255,  0,  0)
BLUE    = (  0,  0,255)

# Dimensions of screen
size = (400,500)
WIDTH = 500
HEIGHT = 400
screen = pygame.display.set_mode(size)
screen.fill(WHITE)


'''Draws a shape object using sprite'''
class Shape(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color, shape, display):
        super().__init__() # Inherits things from pygame.sprite.Sprite (I think)
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
            pygame.draw.rect(self.display, BLACK, (self.x, self.y, self.width, self.height), 4)
            # Fill
            pygame.draw.rect(self.display, self.color, (self.x + 2, self.y + 2, self.width - 4, self.height - 4))
            # Updates display
            pygame.display.update()
    # Updates and changes color variable for shape fill
    def changeColor(self, color):
        self.color = color # Needed to keep shape's color as the new color
         # Redraws the shape with the new color
        pygame.draw.rect(self.display, color, (self.x + 2, self.y + 2, self.width - 4, self.height - 4))
        # Updates display
        pygame.display.update()


'''Game class'''
class Game(object):
    def __init__(self):
        self.game_over = False
        self.shape = Shape(50, 50, 100, 100, GREEN, 'rect', screen)
    
    def updateColor(self):
        self.shape.changeColor(RED)
        
    def process_events(self):
        """ Process all of the events. Return a "True" if we need
            to close the window. """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                #if self.shape.collidepoint(event.pos):
                self.updateColor()
        return False
    
    def display_frame(self, screen):
        """ Display everything to the screen for the game. """
        screen.fill(WHITE)
        if not self.game_over:
            self.shape.draw()
 
        pygame.display.flip()
    

def main():
    """ Main program function. """
    # Initialize Pygame and set up the window
    pygame.init()
    # Create our objects and set the data
    done = False
    clock = pygame.time.Clock()
 
    # Create an instance of the Game class
    game = Game()
 
    # Main game loop
    while not done:
 
        # Draw the current frame
        game.display_frame(screen)
        
        # Process events (keystrokes, mouse clicks, etc)
        done = game.process_events()
 
        # Pause for the next frame
        clock.tick(60)
 
    # Close window and exit
    pygame.quit()
 
# Call the main function, start up the game
if __name__ == "__main__":
    main()