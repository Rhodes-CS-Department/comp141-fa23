# TODO: Write header comment here. (See "Style Guide" on Canvas. Delete this comment.)

from cs1.graphics import *

# Draw the eyes on a potato of radius 150 pixels.
# centerx - the x-coordinate of the potato center (int).
# centery - the y-coordinate of the potato center (int).
# Returns None (NoneType).
def draw_eyes(centerx, centery):
    # Remove this print statement when writing this function.
    print("Drawing eyes.")



# Draw the hair on a potato of radius 150 pixels.
# centerx - the x-coordinate of the potato center (int).
# centery - the y-coordinate of the potato center (int).
# Returns None (NoneType).
def draw_hair(centerx, centery):
    # Remove this print statement when writing this function.
    print("Drawing hair.")



# Draw the mouth on a potato of radius 150 pixels.
# centerx - the x-coordinate of the potato center (int).
# centery - the y-coordinate of the potato center (int).
# Returns None (NoneType).
def draw_mouth(centerx, centery):
    # Remove this print statement when writing this function.
    print("Drawing mouth.")



# *** DO NOT CHANGE ANY OF THE CODE BELOW. ***
import random

MOVE_HEADS = True

def reset_pen():
    set_color("black")
    set_background_color("white")
    set_line_thickness(1)

def main():
    open_canvas(800, 400)

    # Draw the left potato:
    # Draw a potato-colored circle, centered approximately at (200, 200).
    mj = 0
    if MOVE_HEADS:
        mj = 40
    cx = random.randint(-mj, mj) + 200
    cy = random.randint(-mj, mj) + 200
    set_background_color_rgb(224, 144, 76)
    set_color_rgb(224, 144, 76)
    draw_filled_circle(cx, cy, 150)

    # Draw the features of the left potato.
    reset_pen()
    draw_eyes(cx, cy)
    reset_pen()
    draw_hair(cx, cy)
    reset_pen()
    draw_mouth(cx, cy)
    reset_pen()

    # Draw the right potato:
    # Draw a potato-colored circle, centered approximately at (600, 200).
    cx = random.randint(-mj, mj) + 600
    cy = random.randint(-mj, mj) + 200
    set_color_rgb(224, 144, 76)
    set_background_color_rgb(224, 144, 76)
    draw_filled_circle(cx, cy, 150)

    # Draw the features of the right potato.
    reset_pen()
    draw_eyes(cx, cy)
    reset_pen()
    draw_hair(cx, cy)
    reset_pen()
    draw_mouth(cx, cy)

# Start program.
main()
