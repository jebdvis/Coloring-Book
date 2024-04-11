#3 sliders that take in HSB values and converts those values to RGB values

import pygame_widgets
import pygame
import colorsys
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox

def hsb_to_rgb(hue, saturation, brightness):
    # Convert hue from degrees to a fraction between 0 and 1
    hue_fraction = hue / 360.0
    
    # Convert HSB to RGB using colorsys module
    r, g, b = colorsys.hsv_to_rgb(hue_fraction, saturation / 100.0, brightness / 100.0)
    
    # Convert RGB values from range [0, 1] to range [0, 255]
    r = int(r * 255)
    g = int(g * 255)
    b = int(b * 255)
    
    return (r, g, b)

pygame.init()
win = pygame.display.set_mode((1000, 600))



hue = Slider(win, 500, 200, 40, 300, min=0, max=360, step=1, vertical=True)
satur = Slider(win, 700, 200, 40, 300, min=0, max=100.0, step=1, vertical=True)
bright = Slider(win, 900, 200, 40, 300, min=0, max=100.0, step=1, vertical=True)





run = True
while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            quit()

    win.fill(hsb_to_rgb(hue.getValue(),satur.getValue(),bright.getValue()))


    pygame_widgets.update(events)
    pygame.display.update()