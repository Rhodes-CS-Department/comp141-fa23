# This file contains functions to be called from the notebook for testing.
# NOTE: Do not modify this file!

from cs1.graphics import *

# Helper function; not meant to be called directly.
def display_pixel_at(pixel, x, y, size):
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    
    set_color_rgb(red, green, blue)
    draw_filled_rect(x, y, size, size)

# Display a single pixel in a canvas of the given size.
# pixel - The pixel to display, as a tuple with three elements.
# size - The height and width of the canvas to use.
# Returns None (NoneType).
def display_pixel(pixel, size):
    open_canvas(size, size) 
    display_pixel_at(pixel, 0, 0, size)
    
# Display an image using pixels of the given size.
# image - The pixels to display, as a 2d array of tuples.
# size - The height and width of each pixel.
# Returns None (NoneType).
def display_image(image, size):
    height = len(image)
    width = len(image[0])
    
    open_canvas(size * width, size * height)
    for i in range(height):
        for j in range(width):
            display_pixel_at(image[i][j], size * j, size * i, size)
