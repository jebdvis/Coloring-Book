import pygame
from pygame.locals import *
import pygame_widgets
from pygame_widgets.button import Button

pygame.init()

#grabs info of display ot use for window size
info = pygame.display.Info()
w = info.current_w
h = info.current_h

screen = pygame.display.set_mode((w, h-55))

undo_icon = pygame.image.load("undo_icon.png")
undo_size = (30, 30)
undo_icon = pygame.transform.scale(undo_icon, undo_size)

save_icon = pygame.image.load("save_icon.png")
save_size = (30,30)
save_icon = pygame.transform.scale(save_icon,save_size)

button1 = Button(screen,100,100,60,60,inactiveColour=(150, 150, 150),hoverColour=(125, 125, 125),pressedColour=(60, 60, 60),radius=20,onClick=lambda: print('Click'),image = undo_icon,)
button2 = Button(screen,200,100,60,60,inactiveColour=(150, 150, 150),hoverColour=(125, 125, 125),pressedColour=(60, 60, 60),radius=20,onClick=lambda: print('Click'),image = save_icon,)
butto3 = Button(screen,300,100,60,60,inactiveColour=(150, 150, 150),hoverColour=(125, 125, 125),pressedColour=(60, 60, 60),radius=20,onClick=lambda: print('Click'),image = save_icon,)


while True:
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT: 
            pygame.display.quit()
        
    pygame_widgets.update(events)  # Call once every loop to allow widgets to render and listen
    pygame.display.update()