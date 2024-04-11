import pygame_widgets
import pygame
from pygame.locals import *
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox

pygame.init()
info = pygame.display.Info()
w = info.current_w
h = info.current_h

win = pygame.display.set_mode((600, 500),HWSURFACE|DOUBLEBUF|RESIZABLE)
fake_screen = win.copy()
pic = pygame.surface.Surface((600, 500))
pic.fill((255, 255, 255))

#slider = Slider(win, 100, 100, 800, 40, min=0, max=255, step=1)
#output = TextBox(win, 475, 200, 50, 50, fontSize=30)

#output.disable()  # Act as label instead of textbox

run = True
while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            quit()
        elif event.type == VIDEORESIZE:
                win = pygame.display.set_mode(event.size, HWSURFACE|DOUBLEBUF|RESIZABLE)

    fake_screen.fill('black')
    fake_screen.blit(pic, (100, 100))
    win.blit(pygame.transform.scale(fake_screen, win.get_rect().size), (0, 0))
    pygame.display.flip()

   # win.fill((255, 255, 255))



    #output.setText(slider.getValue())

    pygame_widgets.update(events)
    pygame.display.update()