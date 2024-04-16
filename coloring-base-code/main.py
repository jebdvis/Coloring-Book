import pygame
from shapeClass import Shape # Shape class import

# Basic Colors
BLACK   = (  0,  0,  0)
WHITE   = (255,255,255)
GREEN   = (  0,255,  0)
RED     = (255,  0,  0)
BLUE    = (  0,  0,255)

# Dimensions/display of screen
size = (400,500)
WIDTH = 500
HEIGHT = 400
screen = pygame.display.set_mode(size)
screen.fill(WHITE)

# Loop Switch
done = False

# Screen Update Speed (FPS)
clock = pygame.time.Clock()

# Create colorable shapes using Shape class
shape1 = Shape(50, 50, 100, 100, WHITE, 'rect', screen)
shape2 = Shape(100, 200, 50, 50, WHITE, 'circle', screen)
shape3 = Shape(150, 150, 50, 100, WHITE, 'rect', screen)
shapes = [shape1, shape2, shape3] # List of shape objects

# Create color palette
color1 = Shape(100, 300, 50, 50, GREEN, 'rect', screen)
color2 = Shape(175, 300, 50, 50, RED, 'rect', screen)
color3 = Shape(250, 300, 50, 50, BLUE, 'rect', screen)
colors = [color1, color2, color3]

# Default the currently selected color to white
currentColor = WHITE

# ------- Main Program Loop -------
while not done:
    # --- Main Event Loop ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # --- Process events loop ---
        elif event.type == pygame.MOUSEBUTTONDOWN: # If the left button is clicked
            for shape_i in range(len(shapes)): # For all shapes on the page
                hitbox_s = shapes[shape_i].getShape() # Get the current shape's hitbox (fill)
                if hitbox_s.collidepoint(event.pos): # If the mouse click was on top of the hitbox, change the color
                    shapes[shape_i].changeColor(currentColor)
            for color_i in range(len(shapes)): # For each color swatch of the palette
                hitbox_c = colors[color_i].getShape() # Get the swatch's hitbox
                if hitbox_c.collidepoint(event.pos): # If the mouse click was on top of the hitbox, set the current color to that swatch
                    currentColor = colors[color_i].getColor()
    
    # Draws all colorable shapes
    for draw_this in range(len(shapes)):
        shapes[draw_this].draw()
    
    # Draws the color swatches
    for load_color in range(len(colors)):
        colors[load_color].draw()

    # Updates display
    pygame.display.flip()
    pygame.display.update()

    #Setting FPS
    clock.tick(60)

#Shutdown
pygame.quit()