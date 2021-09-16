# Import the "arcade" Library
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def snow():
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 4, 0, arcade.color.WHITE)


def snowman(x, y):
    arcade.draw_circle_filled(300 + x, 190 + y, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(300 + x, 190 + y, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(300 + x, 270 + y, 40, arcade.color.WHITE)
    arcade.draw_circle_filled(300 + x, 330 + y, 30, arcade.color.WHITE)
    arcade.draw_circle_filled(300 + x, 270 + y, 5, arcade.color.RED, num_segments=32)
    arcade.draw_circle_filled(300 + x, 175 + y, 5, arcade.color.RED, num_segments=32)
    arcade.draw_circle_filled(300 + x, 225 + y, 5, arcade.color.RED, num_segments=32)
    arcade.draw_triangle_filled(295 + x, 330 + y, 295 + x, 340 + y, 315 + x, 335 + y, arcade.color.ORANGE)
    arcade.draw_circle_filled(290 + x, 345 + y, 3, arcade.color.BLACK, num_segments=32)
    arcade.draw_circle_filled(310 + x, 345 + y, 3, arcade.color.BLACK, num_segments=32)
    arcade.draw_arc_filled(300 + x, 325 + y, 25, 20, arcade.color.BLACK, 180, 360)
    arcade.draw_line(260 + x, 280 + y, 240 + x, 220 + y, arcade.color.BROWN, 5)
    arcade.draw_line(335 + x, 290 + y, 370 + x, 290 + y, arcade.color.BROWN, 5)
    arcade.draw_line(370 + x, 325 + y, 370 + x, 290 + y, arcade.color.BROWN, 5)


def cloud(x, y):
    arcade.draw_circle_filled(300 + x, 500 + y, 20, arcade.color.WHITE)
    arcade.draw_circle_filled(320 + x, 515 + y, 20, arcade.color.WHITE)
    arcade.draw_circle_filled(340 + x, 500 + y, 20, arcade.color.WHITE)
    arcade.draw_rectangle_filled(320 + x, 485 + y, 80, 25, arcade.color.BLACK)


def moon():
    arcade.draw_circle_filled(700, 500, 50, arcade.color.WHITE)


def igloo(x, y):
    arcade.draw_arc_filled(500 + x, 150 + y, 200, 300, arcade.color.BLUE, 0, 180)
    arcade.draw_rectangle_filled(550 + x, 185 + y, 40, 70, arcade.color.RED)
    arcade.draw_rectangle_filled(460 + x, 200 + y, 40, 40, arcade.color.BLACK)


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 3")
    arcade.set_background_color(arcade.color.BLACK)
    arcade.start_render()
    snow()
    snowman(20, 0)
    snowman(-150, 0)
    cloud(40, 0)
    cloud(-70, 0)
    cloud(-190, 0)
    moon()
    igloo(-20, 0)
    igloo(190, 0)
    # Finish Render.
    arcade.finish_render()
    # Keep the window up until something closes it.
    arcade.run()


# Call the main function to get the program started.
main()
