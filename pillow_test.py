from PIL import Image, ImageDraw
import pygame 
from pygame.locals import *
import numpy as np

def pygame_flood_fill(surface, xy, new_color, threshh):
    py_to_img = Image.frombytes("RGB", surface.get_size(), pygame.image.tostring(surface, "RGB"))

    # Perform flood fill
    ImageDraw.floodfill(py_to_img, xy=xy, value=new_color, thresh=threshh)

    # Convert the Pillow image back to Pygame surface
    updated_surface = pygame.image.fromstring(py_to_img.tobytes(), py_to_img.size, py_to_img.mode)
    return updated_surface
  
# Take colors input 
YELLOW = (255, 255, 0) 
BLUE = (0, 0, 255) 
  
# Construct the GUI game 
pygame.init() 
  
# Set dimensions of game GUI 

info = pygame.display.Info()
w = info.current_w
h = info.current_h

screen = pygame.display.set_mode((w, h-55))

input_image = Image.open("test_img.png")
image_width, image_height = input_image.size

# Convert the Pillow image to Pygame surface
py_img = pygame.image.fromstring(input_image.tobytes(), input_image.size, input_image.mode)
py_img = pygame.transform.scale(py_img, (w, h))
  
# Set value of running variable 
running=True
  
# Setting what happens when game is in running state 
while running: 
    for event in pygame.event.get(): 
        
      # Close if the user quits the game 
        if event.type == QUIT: 
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the mouse button clicked is the left button (button 1)
            if event.button == 1:
                # Get the coordinates of the mouse click
                click_x, click_y = event.pos
                # Call the function with the click coordinates
                py_img = pygame_flood_fill(py_img,(click_x,click_y),(255,255,0),200)
                

    # Set the background color 
    screen.fill((255,255,255)) 
    screen.blit(py_img, (0, 0)) 
    
    # Update the GUI pygame 
    pygame.display.update() 
  
# Quit the GUI game 
pygame.quit()