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
import easygui
import shutil

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
    new_image = cv2.convertScaleAbs(convert_img, alpha=2.3, beta=0)
    #save image to be used in pygame
    cv2.imwrite(filename, new_image)

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
            bg.save(filename)
        else:
            im.save(filename)
    
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
    cv2.imwrite(filename, result)

def convertImage(filename):
    remove_transparency(filename)
    upscale(filename)
    convert_to_BW(filename)

def choose_png_and_copy():
#opens file explorer for user to choose file
    source_file = easygui.fileopenbox(filetypes=["*.png"])
    if source_file:
    #puts a copy of the file in the coloring page folder
        shutil.copy(source_file, 'Color_Pages')


def load_and_convert():
    #opens file explorer for user to choose file
    source_file = easygui.fileopenbox(filetypes=["*.png"])
    if source_file:
        #puts a copy of the file in the coloring page folder
        shutil.copy(source_file, 'Color_Pages')
        file_path = source_file.split("\\")
        print("Loading!!!!")
        convertImage("Color_Pages"+"\\" + file_path[-1])
        print("Finished Converting!")
     

if __name__ == "__main__":
    load_and_convert()