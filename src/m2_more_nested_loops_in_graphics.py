"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of TWO-DIMENSIONAL GRAPHICS.

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Victoria Szalay.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to test them. """
    run_test_draw_upside_down_wall()


def run_test_draw_upside_down_wall():
    """ Tests the    draw_upside_down_wall    function. """
    # Tests 1 and 2 are ALREADY DONE (here).
    window = rg.RoseWindow(550, 300, 'Upside-down wall, Tests 1 and 2')

    rectangle = rg.Rectangle(rg.Point(125, 230), rg.Point(155, 250))
    draw_upside_down_wall(rectangle, 8, window)

    rectangle = rg.Rectangle(rg.Point(375, 175), rg.Point(425, 225))
    draw_upside_down_wall(rectangle, 4, window)

    window.close_on_mouse_click()


def draw_upside_down_wall(rectangle, n, window):
    """
    See   MoreWalls.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws an "upside-down wall" on the given window, where:
      -- The BOTTOM of the wall is a single "brick"
            that is the given rg.Rectangle.
      -- There are n rows in the wall.
      -- Each row is a row of "bricks" that are the same size
            as the given rg.Rectangle.
      -- Each row has one more brick than the row below it.
      -- Each row is centered on the bottom row.

    Preconditions:
      :type rectangle: rg.Rectangle
      :type n: int
      :type window: rg.RoseWindow
    and n is nonnegative.
    """
    # ------------------------------------------------------------------
    # Done: 2. Implement and test this function.
    #     Some tests are already written for you (above).
    # ------------------------------------------------------------------
    rectangle.move_by(-1*rectangle.get_width(),1*rectangle.get_height())
    for n in range(n+1):
        for k in range(n):
            shift_1_x = rectangle.corner_1.x + (rectangle.get_width())*(n/2)
            shift_1_y = rectangle.corner_1.y - (rectangle.get_height())*(n)
            shift_2_x = rectangle.corner_2.x + (rectangle.get_width()) * (n/ 2)
            shift_2_y = rectangle.corner_2.y - (rectangle.get_height()) * (n)
            if k == 0:
                new_rectangles = rg.Rectangle(rg.Point(shift_1_x,shift_1_y),rg.Point(shift_2_x,shift_2_y))
                new_rectangles.attach_to(window)
            different_shift_1_x = new_rectangles.corner_1.x - (new_rectangles.get_width())*(k)
            different_shift_1_y = new_rectangles.corner_1.y
            different_shift_2_x = new_rectangles.corner_2.x - (new_rectangles.get_width())*(k)
            different_shift_2_y = new_rectangles.corner_2.y
            different_rectangles = rg.Rectangle(rg.Point(different_shift_1_x,different_shift_1_y),rg.Point(different_shift_2_x,different_shift_2_y))
            different_rectangles.attach_to(window)

        window.render()


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
