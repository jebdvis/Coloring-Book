import pygame
from pygame.locals import *
import pygame_widgets
from pygame_widgets.button import Button
from pygame_widgets.slider import Slider
import colorsys
from PIL import Image, ImageDraw, ImageFilter, ImageOps
import PIL
import PIL.ImageOps
import numpy as np
import imageConverter
from imageConverter import convertImage

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

def gradientRect(window, top_color, bot_color, target_rect):
    color_rect = pygame.Surface((2, 2))
    pygame.draw.line(color_rect, top_color, (0,0) , (1,0))
    pygame.draw.line(color_rect, bot_color, (0,1), (1,1))
    color_rect = pygame.transform.smoothscale(color_rect, (target_rect.width, target_rect.height))
    window.blit(color_rect, target_rect)


class ColorPage:

    def __init__(self, display, gameStateManager):
        #self.set_loaded_img('Color_Pages/pikachu2.png')
        
        self.UI_loaded = False

        self.loaded_img = None

        self.undo_stack = []

        self.display = display
        self.gameStateManager = gameStateManager

        self.myfont = pygame.font.SysFont("monospace", 18)

        self.hue_label = self.myfont.render("HUE", 1, (255,255,255))
        self.satur_label = self.myfont.render("SAT", 1, (255,255,255))
        self.bright_label = self.myfont.render("BRT", 1, (255,255,255))

        self.ui_surf = pygame.Surface((self.display.get_width()/7, self.display.get_height()))

        #Color Sample Box
        self.color_samp = pygame.Surface((50,50))

        #initializes icons for UI
        self.undo_icon = pygame.image.load("Icons/undo_icon.png")
        self.undo_size = (30, 30)
        self.undo_icon = pygame.transform.scale(self.undo_icon, self.undo_size)

        self.save_icon = pygame.image.load("Icons/save_icon.png")
        self.save_size = (30,30)
        self.save_icon = pygame.transform.scale(self.save_icon,self.save_size)

        self.home_icon = pygame.image.load("Icons/home_icon.png")
        self.home_size = (30,30)
        self.home_icon = pygame.transform.scale(self.home_icon,self.home_size)

        #Creates buttons on UI using loaded icons
        self.button1 = Button(self.display,(51/56)*self.display.get_width(),250,60,60,inactiveColour=(150, 150, 150),hoverColour=(125, 125, 125),pressedColour=(60, 60, 60),radius=20,onClick= self.undo_func, image = self.undo_icon,)
        self.button2 = Button(self.display,(51/56)*self.display.get_width(),150,60,60,inactiveColour=(150, 150, 150),hoverColour=(125, 125, 125),pressedColour=(60, 60, 60),radius=20,onClick=lambda: print('Click'),image = self.save_icon,)
        self.button3 = Button(self.display,(51/56)*self.display.get_width(),50,60,60,inactiveColour=(150, 150, 150),hoverColour=(125, 125, 125),pressedColour=(60, 60, 60),radius=20,onClick=lambda: print('Click'),image = self.home_icon,)

        #Creates sliders on UI to use for color selection
        self.hue = Slider(self.display, int((98/112) * self.display.get_width()), int((9/16) * self.display.get_height()), 20, 300, min=0, max=360, step=1, vertical=True)
        self.satur = Slider(self.display, int((103/112) * self.display.get_width()), int((9/16) * self.display.get_height()), 20, 300, min=0, max=100.0, step=1, vertical=True)
        self.bright = Slider(self.display, int((108/112) * self.display.get_width()), int((9/16) * self.display.get_height()), 20, 300, min=0, max=100.0, step=1, vertical=True)

        self.hideUI()

    def hideUI(self):
        self.button1.hide()
        self.button2.hide()
        self.button3.hide()
        self.hue.hide()
        self.satur.hide()
        self.bright.hide()
        self.UI_loaded = False
        print('not loaded')

    def showUI(self):
        self.set_loaded_img('Color_Pages/pikachu2.png')
        self.load_img()
        self.button1.show()
        self.button2.show()
        self.button3.show()
        self.hue.show()
        self.satur.show()
        self.bright.show()
        self.UI_loaded = True
        print('loaded')
        #print(self.UI_loaded)

    def run(self):
        if self.UI_loaded == False:
            self.showUI()
            #print(self.UI_loaded)
        #print('NEXT')
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT: 
                pygame.display.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print('CLICK')
            # Check if the mouse button clicked is the left button (button 1)
                if event.button == 1:
                    # Get the coordinates of the mouse click
                    click_x, click_y = event.pos
                    # Call the function with the click coordinates
                    #click_x = click_x + int((3/7)*self.display.get_width() - (self.drawn_img_width/2))
                    if click_x < self.display.get_width() and click_y < self.display.get_height():
                        color = self.display.get_at((click_x, click_y))
                        # Check if the color is black or close to black
                        if (color[0] > 20 or color[1] > 20 or color[2] > 20) and click_x < (6/7)* self.display.get_width():
                            self.py_img = pygame_flood_fill(self.py_img,(click_x,click_y),hsv_to_rgb(self.hue.getValue(),self.satur.getValue(),self.bright.getValue()),30)
                            self.undo_stack.append([(click_x, click_y), (color[0],color[1],color[2])])
        



        #Fills white color for background, Black for UI surface, and the current chosen color for the color sample box
        self.display.fill((255,255,255))
        self.ui_surf.fill((0,0,0))
        self.color_samp.fill(hsv_to_rgb(self.hue.getValue(), self.satur.getValue(), self.bright.getValue()))

        #(3/7)*self.display.get_width() - (self.drawn_img_width/2)
        self.display.blit(self.py_img, (0, 0)) 

        #draws UI surface and color sample box
        self.display.blit(self.ui_surf, ((6/7)*self.display.get_width(),0))
        self.display.blit(self.color_samp, ((51/56) * self.display.get_width(), (7/16) * self.display.get_height()))

        #Draws labels for the color picker sliders
        self.display.blit(self.hue_label, (int((98/112) * self.display.get_width()), int((17/32) * self.display.get_height())))
        self.display.blit(self.satur_label, (int((103/112) * self.display.get_width()), int((17/32) * self.display.get_height())))
        self.display.blit(self.bright_label, (int((109/112) * self.display.get_width()), int((17/32) * self.display.get_height())))

        #saturation and brightness gradients
        #gradientRect( window, (0, 255, 0), (0, 100, 0), pygame.Rect( 100,100, 100, 50 ) )
        gradientRect(self.display, hsv_to_rgb(self.hue.getValue(), 100, 100), (255,255,255), pygame.Rect(int((105/112) * self.display.get_width()), int((9/16)*self.display.get_height()),10,300))
        gradientRect(self.display, (255, 255, 255), (0,0,0), pygame.Rect(int((110/112) * self.display.get_width()), int((9/16)*self.display.get_height()),10,300))

        pygame_widgets.update(events)  # Call once every loop to allow widgets to render and listen
        pygame.display.update()


    #sets file path of image to be loaded(File path should always be to the folder holding coloring pages)
    def set_loaded_img(self, loaded_img):
        self.loaded_img = loaded_img

    def load_img(self):
        input_image = Image.open(self.loaded_img)
        image_width, image_height = input_image.size

        input_image = input_image.convert("RGB")

        self.drawn_img_height = self.display.get_height()
        self.drawn_img_width = (self.display.get_height()/image_height) * image_width

        # Convert the Pillow image to Pygame surface
        self.py_img = pygame.image.frombytes(input_image.tobytes(), input_image.size, input_image.mode)
        self.py_img = pygame.transform.scale(self.py_img, (self.drawn_img_width, self.drawn_img_height))

    def undo_func(self):
        if len(self.undo_stack) > 0:
            self.py_img = pygame_flood_fill(self.py_img, self.undo_stack[-1][0], self.undo_stack[-1][1], 200)
            del self.undo_stack[-1]

    #sets game state to home and hides buttons/sliders
    def set_gameState_home(self):
        lambda: print("hi!")



if __name__ == "__main__":
    #convertImage('Color_Pages/pikachu2.png')

    pygame.init()

    info = pygame.display.Info()
    w = info.current_w
    h = info.current_h

    screen = pygame.display.set_mode((w, h-55))

    page = ColorPage(screen, 1)
    page.set_loaded_img('Color_Pages/pikachu2.png')
    page.load_img()
    while True:
        page.run()