# Import the "arcade" Library
import arcade

# Open up a window.
arcade.open_window(800, 600, "Lab 2")

# Set the background color.
arcade.set_background_color(arcade.color.BLACK)

# Get ready to draw.
arcade.start_render()

# Draw the snow
arcade.draw_lrtb_rectangle_filled(0, 800, 150, 0, arcade.color.WHITE)

# Draw snowman base.
arcade.draw_circle_filled(300, 190, 50, arcade.color.WHITE)

# Draw middle body of snowman.
arcade.draw_circle_filled(300, 270, 40, arcade.color.WHITE)

# Draw head of snowman.
arcade.draw_circle_filled(300, 330, 30, arcade.color.WHITE)

# Draw Buttons on snowman.
arcade.draw_circle_filled(300, 270, 5, arcade.color.RED)
arcade.draw_circle_filled(300, 175, 5, arcade.color.RED)
arcade.draw_circle_filled(300, 225, 5, arcade.color.RED)

# Draw the nose.
arcade.draw_triangle_filled(295, 330, 295, 340, 315, 335, arcade.color.ORANGE)

# Draw the eyes.
arcade.draw_circle_filled(290, 345, 3, arcade.color.BLACK)
arcade.draw_circle_filled(310, 345, 3, arcade.color.BLACK)

# Draw mouth.
arcade.draw_arc_filled(300, 325, 25, 20, arcade.color.BLACK, 180, 360)

# Draw arms.
arcade.draw_line(260, 280, 240, 220, arcade.color.BROWN, 5)
arcade.draw_line(335, 290, 370, 290, arcade.color.BROWN, 5)
arcade.draw_line(370, 325, 370, 290, arcade.color.BROWN, 5)

# Draw fists.
arcade.draw_lrtb_rectangle_filled(235, 245, 225, 215, arcade.color.YELLOW)
arcade.draw_lrtb_rectangle_filled(365, 375, 330, 320, arcade.color.YELLOW)

# Draw moon.
arcade.draw_circle_filled(700, 500, 50, arcade.color.WHITE)

# Finish Render.
arcade.finish_render()

# Keep the window up until something closes it.
arcade.run()