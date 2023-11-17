# Header comment here.

from cs1.ppm import *

# Pixels

# Negate the red value of the given pixel.
# (That is, replace the red value `r` with `255 - r`.)
# pixel - A pixel, represented as a tuple of three integers (0-255).
# Returns a modified pixel, represented as a tuple of three integers (0-255).
def pixel_negate_red(pixel):
    pass

# Negate the green value of the given pixel.
# (That is, replace the green value `g` with `255 - g`.)
# pixel - A pixel, represented as a tuple of three integers (0-255).
# Returns a modified pixel, represented as a tuple of three integers (0-255).
def pixel_negate_green(pixel):
    pass

# Negate the blue value of the given pixel.
# (That is, replace the blue value `b` with `255 - b`.)
# pixel - A pixel, represented as a tuple of three integers (0-255).
# Returns a modified pixel, represented as a tuple of three integers (0-255).
def pixel_negate_blue(pixel):
    pass

# Negate all three values of the given pixel.
# (That is, replace each value `v` with `255 - v`.)
# pixel - A pixel, represented as a tuple of three integers (0-255).
# Returns a modified pixel, represented as a tuple of three integers (0-255).
def pixel_negate_all(pixel):
    pass

# Remove all red from the given pixel.
# (That is, replace the red value with 0.)
# pixel - A pixel, represented as a tuple of three integers (0-255).
# Returns a modified pixel, represented as a tuple of three integers (0-255).
def pixel_remove_red(pixel):
    pass

# Remove all green from the given pixel.
# (That is, replace the green value with 0.)
# pixel - A pixel, represented as a tuple of three integers (0-255).
# Returns a modified pixel, represented as a tuple of three integers (0-255).
def pixel_remove_green(pixel):
    pass

# Remove all blue from the given pixel.
# (That is, replace the blue value with 0.)
# pixel - A pixel, represented as a tuple of three integers (0-255).
# Returns a modified pixel, represented as a tuple of three integers (0-255).
def pixel_remove_blue(pixel):
    pass

# Convert the given pixel to grayscale.
# (That is, replace all three RGB values with their average, rounded down.)
# pixel - A pixel, represented as a tuple of three integers (0-255).
# Returns a modified pixel, represented as a tuple of three integers (0-255).
def pixel_grayscale(pixel):
    pass

# Images

# Negate all red values in the given image.
# image - An image, represented as a 2d list of pixels.
# Returns None (NoneType).
def image_negate_red(image):
    pass

# Negate all green values in the given image.
# image - An image, represented as a 2d list of pixels.
# Returns None (NoneType).
def image_negate_green(image):
    pass

# Negate all blue values in the given image.
# image - An image, represented as a 2d list of pixels.
# Returns None (NoneType).
def image_negate_blue(image):
    pass

# Negate all red, green, and blue values in the given image.
# image - An image, represented as a 2d list of pixels.
# Returns None (NoneType).
def image_negate_all(image):
    pass

# Remove all red from the given image.
# image - An image, represented as a 2d list of pixels.
# Returns None (NoneType).
def image_remove_red(image):
    pass

# Remove all green from the given image.
# image - An image, represented as a 2d list of pixels.
# Returns None (NoneType).
def image_remove_green(image):
    pass

# Remove all blue from the given image.
# image - An image, represented as a 2d list of pixels.
# Returns None (NoneType).
def image_remove_blue(image):
    pass

# Convert the given image to grayscale.
# image - An image, represented as a 2d list of pixels.
# Returns None (NoneType).
def image_grayscale(image):
    pass

# Flip the given image horizontally.
# image - An image, represented as a 2d list of pixels.
# Returns None (NoneType).
def image_flip_horizontal(image):
    pass

# Flip the given image vertically.
# image - An image, represented as a 2d list of pixels.
# Returns None (NoneType).
def image_flip_vertical(image):
    pass

# Read

# Read a PPM file from the given path.
# path - A path to a PPM file; e.g. `"images/joly.ppm"` (str).
# Returns an image, as a 2d list of pixels.
def read_ppm(path):
    pass

# Write

# Write an image to a PPM file at the given path.
# path - A path to store the written PPM file;
#   e.g. `"images/joly_negate_red.ppm"` (str).
# image - An image, as a 2d list of pixels.
def write_ppm(path, image):
    pass
    
# Main    
    
def main():
    
    # (get input from user here)
    
    print('Reading image...')
    
    # (read the PPM file here)
    
    print('Filtering image...')
    
    # (filter the image here)

    print('Writing filtered image...')
    
    # (write the filtered image here)
    
    print('Displaying filtered image...')
    display_ppm('out.ppm')

main()
