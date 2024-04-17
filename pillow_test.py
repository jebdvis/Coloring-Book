from PIL import Image, ImageDraw, ImageFilter, ImageOps
import PIL
import PIL.ImageOps
import pygame 
from pygame.locals import *
import numpy as np
import pygame_widgets
from pygame_widgets.slider import Slider
import colorsys

def pygame_flood_fill(surface, xy, new_color, threshh):
    py_to_img = Image.frombytes("RGB", surface.get_size(), pygame.image.tostring(surface, "RGB"))

    # Perform flood fill
    ImageDraw.floodfill(py_to_img, xy=xy, value=new_color, thresh=threshh)

    # Convert the Pillow image back to Pygame surface
    updated_surface = pygame.image.fromstring(py_to_img.tobytes(), py_to_img.size, py_to_img.mode)
    return updated_surface
  
def hsv_to_rgb(hue, saturation, brightness):
    # Convert hue from degrees to a fraction between 0 and 1
    hue_fraction = hue / 360.0
    
    # Convert HSB to RGB using colorsys module
    r, g, b = colorsys.hsv_to_rgb(hue_fraction, saturation / 100.0, brightness / 100.0)
    
    # Convert RGB values from range [0, 1] to range [0, 255]
    r = int(r * 255)
    g = int(g * 255)
    b = int(b * 255)
    
    return (r, g, b)

def convert_to_BW(filename):
    with Image.open(filename) as img:
        img.load()
    cmyk_img = img.convert("CMYK")
    gray_img = img.convert("L")  # Grayscale
    edges = gray_img.filter(ImageFilter.FIND_EDGES)
    #edges.show()
    inverted_image = PIL.ImageOps.invert(edges)
    inverted_image.save('test-images/convertedimage.png')
    inverted_image.show()


    #converts input images into black and white to be traced



# Take colors input 

  
# Construct the GUI game 
pygame.init() 
  
# Set dimensions of game GUI 
convert_to_BW('test-images/pikachu.png')

info = pygame.display.Info()
w = info.current_w
h = info.current_h

screen = pygame.display.set_mode((w, h-55))

hue = Slider(screen, 500, 200, 40, 300, min=0, max=360, step=1, vertical=True)
satur = Slider(screen, 700, 200, 40, 300, min=0, max=100.0, step=1, vertical=True)
bright = Slider(screen, 900, 200, 40, 300, min=0, max=100.0, step=1, vertical=True)

input_image = Image.open("test-images/convertedimage.png")
image_width, image_height = input_image.size

# Convert the Pillow image to Pygame surface
py_img = pygame.image.fromstring(input_image.tobytes(), input_image.size, input_image.mode)
py_img = pygame.transform.scale(py_img, (w-500, h))
  
# Set value of running variable 
running=True

  
# Setting what happens when game is in running state 
while running: 
    events = pygame.event.get()
    for event in events: 
        
      # Close if the user quits the game 
        if event.type == QUIT: 
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the mouse button clicked is the left button (button 1)
            if event.button == 1:
                # Get the coordinates of the mouse click
                click_x, click_y = event.pos
                # Call the function with the click coordinates
                color = screen.get_at((click_x, click_y))
                # Check if the color is black or close to black
                if color[0] > 20 or color[1] > 20 or color[2] > 20:
                    py_img = pygame_flood_fill(py_img,(click_x,click_y),hsv_to_rgb(hue.getValue(),satur.getValue(),bright.getValue()),200)
                

    # Set the background color 
    screen.fill((255,255,255)) 
    screen.blit(py_img, (0, 0)) 
    
    # Update the GUI pygame 
    pygame_widgets.update(events)
    pygame.display.update() 
  
# Quit the GUI game 
pygame.quit()