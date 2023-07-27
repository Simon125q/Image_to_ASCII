# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 08:27:13 2023

@author: PLSZOMI
"""

from PIL import Image

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_image(image, new_width):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayscale(image):
    grayscale_image = image.convert("L")
    return grayscale_image

def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = ''.join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return characters

def main(new_width = 100):
    path = "C:/Users/PLSZOMI/Desktop/mario.png"
    try:
        image = Image.open(path)
    except:
        print(path, " is not a valid path to an image.")
        
    new_image_data = pixels_to_ascii((grayscale(resize_image(image, new_width))))
    
    pixel_count = len(new_image_data)
    ascii_image = '\n'.join(new_image_data[i:(i + new_width)] for i in range(0, pixel_count, new_width))
    
    print(ascii_image)
    
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)
        
main()