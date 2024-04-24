from PIL import Image, ImageDraw, ImageFilter, ImageOps, ImageEnhance
import PIL
import cv2
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

#functions are good and work

def convert_to_BW(filename):
    #opens image of given filename
    img = Image.open(filename)
    #converts image to grayscale, this will allow for the black lines to be isolated
    gray_img = img.convert("L")  # Grayscale
    #saves image so that it can be readin as a numpy file for openCV contrast conversion
    gray_img.save('test-images/gray_image.png')
    #reads in saved image
    convert_img = cv2.imread('test-images/gray_image.png')
    #uses openCV to change image contrast, allowing black lines to be isolated and therefore make a good coloring book.
    new_image = cv2.convertScaleAbs(convert_img, alpha=5, beta=0)
    #save image to be used in pygame
    cv2.imwrite('gray_contrast_img.png', new_image)

def remove_transparency(filename, bg_colour=(255, 255, 255)):
    #source https://stackoverflow.com/questions/35859140/remove-transparency-alpha-from-any-image-using-pil
    # Only process if image has transparency (http://stackoverflow.com/a/1963146)
        im = Image.open(filename)
        # Need to convert to RGBA if LA format due to a bug in PIL (http://stackoverflow.com/a/1963146)
        if im.mode in ('RGBA', 'LA') or (im.mode == 'P' and 'transparency' in im.info):
            alpha = im.convert('RGBA').split()[-1]

            # Create a new background image of our matt color.
            # Must be RGBA because paste requires both images have the same format
            # (http://stackoverflow.com/a/8720632  and  http://stackoverflow.com/a/9459208)
            bg = Image.new("RGBA", im.size, bg_colour + (255,))
            bg.paste(im, mask=alpha)
            bg.show()
            bg.save('test-images/removed_background.png')
        else:
            im.save('test-images/removed_background.png')
    
def upscale(filename):
    #reads in image
    img = cv2.imread(filename)
    #creates new upscale model
    sr = cv2.dnn_superres.DnnSuperResImpl_create()
    #references ESDR_x4 upscaling model
    path = "EDSR_x4.pb"
    sr.readModel(path)
    sr.setModel("edsr",4)
    #upscale the image
    result = sr.upsample(img)
    #save the image
    cv2.imwrite('test-images/upscaled_test.png', result)

    


# Take colors input 

  
# Construct the GUI game 
pygame.init() 
  
# Set dimensions of game GUI 
remove_transparency('test-images/pikachu2.png')
upscale('test-images/removed_background.png')
convert_to_BW('test-images/upscaled_test.png')

info = pygame.display.Info()
w = info.current_w
h = info.current_h

screen = pygame.display.set_mode((w, h-55))

hue = Slider(screen, 500, 200, 40, 300, min=0, max=360, step=1, vertical=True)
satur = Slider(screen, 700, 200, 40, 300, min=0, max=100.0, step=1, vertical=True)
bright = Slider(screen, 900, 200, 40, 300, min=0, max=100.0, step=1, vertical=True)

input_image = Image.open("gray_contrast_img.png")
image_width, image_height = input_image.size

input_image = input_image.convert("RGB")

# Convert the Pillow image to Pygame surface
py_img = pygame.image.frombytes(input_image.tobytes(), input_image.size, input_image.mode)
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