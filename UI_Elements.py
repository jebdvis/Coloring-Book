import pygame
from pygame.locals import *
import pygame_widgets
from pygame_widgets.button import Button
from pygame_widgets.slider import Slider
import colorsys

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

def gradientRect(window, top_color, bot_color, target_rect):
    color_rect = pygame.Surface((2, 2))
    pygame.draw.line(color_rect, top_color, (0,0) , (1,0))
    pygame.draw.line(color_rect, bot_color, (0,1), (1,1))
    color_rect = pygame.transform.smoothscale(color_rect, (target_rect.width, target_rect.height))
    window.blit(color_rect, target_rect)

pygame.init()

#Sets Font for labels
myfont = pygame.font.SysFont("monospace", 18)

#Creates Labels to be drawn
hue_label = myfont.render("HUE", 1, (255,255,255))
satur_label = myfont.render("SAT", 1, (255,255,255))
bright_label = myfont.render("BRT", 1, (255,255,255))

#grabs info of display ot use for window size
info = pygame.display.Info()
w = info.current_w
h = info.current_h

screen = pygame.display.set_mode((w, h-55))

#Black UI Surface
ui_surf = pygame.Surface((w/7, h))

#Color Sample Box
color_samp = pygame.Surface((50,50))

#initializes icons for UI
undo_icon = pygame.image.load("undo_icon.png")
undo_size = (30, 30)
undo_icon = pygame.transform.scale(undo_icon, undo_size)

save_icon = pygame.image.load("save_icon.png")
save_size = (30,30)
save_icon = pygame.transform.scale(save_icon,save_size)

home_icon = pygame.image.load("home_icon.png")
home_size = (30,30)
home_icon = pygame.transform.scale(home_icon,home_size)

#Creates buttons on UI using loaded icons
button1 = Button(screen,(51/56)*w,250,60,60,inactiveColour=(150, 150, 150),hoverColour=(125, 125, 125),pressedColour=(60, 60, 60),radius=20,onClick=lambda: print('Click'),image = undo_icon,)
button2 = Button(screen,(51/56)*w,150,60,60,inactiveColour=(150, 150, 150),hoverColour=(125, 125, 125),pressedColour=(60, 60, 60),radius=20,onClick=lambda: print('Click'),image = save_icon,)
button3 = Button(screen,(51/56)*w,50,60,60,inactiveColour=(150, 150, 150),hoverColour=(125, 125, 125),pressedColour=(60, 60, 60),radius=20,onClick=lambda: print('Click'),image = home_icon,)

#Creates sliders on UI to use for color selection
hue = Slider(screen, int((98/112) * w), int((9/16) * h), 20, 300, min=0, max=360, step=1, vertical=True)
satur = Slider(screen, int((103/112) * w), int((9/16) * h), 20, 300, min=0, max=100.0, step=1, vertical=True)
bright = Slider(screen, int((108/112) * w), int((9/16) * h), 20, 300, min=0, max=100.0, step=1, vertical=True)


running = True

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT: 
            running = False

    #Fills white color for background, Black for UI surface, and the current chosen color for the color sample box
    screen.fill((255,255,255))
    ui_surf.fill((0,0,0))
    color_samp.fill(hsv_to_rgb(hue.getValue(), satur.getValue(), bright.getValue()))

    #draws UI surface and color sample box
    screen.blit(ui_surf, ((6/7)*w,0))
    screen.blit(color_samp, ((51/56) * w, (6/16) * h))

    #Draws labels for the color picker sliders
    screen.blit(hue_label, (int((98/112) * w), int((17/32) * h)))
    screen.blit(satur_label, (int((103/112) * w), int((17/32) * h)))
    screen.blit(bright_label, (int((109/112) * w), int((17/32) * h)))

    #saturation and brightness gradients
    #gradientRect( window, (0, 255, 0), (0, 100, 0), pygame.Rect( 100,100, 100, 50 ) )
    gradientRect(screen, hsv_to_rgb(hue.getValue(), 100, 100), (255,255,255), pygame.Rect(int((105/112) * w), int((9/16)*h),10,300))
    gradientRect(screen, (255, 255, 255), (0,0,0), pygame.Rect(int((110/112) * w), int((9/16)*h),10,300))

    pygame_widgets.update(events)  # Call once every loop to allow widgets to render and listen
    pygame.display.update()
    
pygame.quit()
    