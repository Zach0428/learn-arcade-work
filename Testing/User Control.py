import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


class Ball:
    def __init__(self, position_x, position_y, radius, color):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  self.radius,
                                  self.color)


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.ASH_GREY)

        # Create our ball
        self.ball = Ball(50, 50, 15, arcade.color.AUBURN)
        self.set_mouse_visible(False)

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        self.ball.draw()


    def on_mouse_motion(self, x, y, dx, dy):
        self.ball.position_x = x
        self.ball.position_y = y

    def on_mouse_press(self, x, y, button: int, modifiers: int):
        print(button)
        if button == arcade.MOUSE_BUTTON_LEFT:
            print("Left button hit!", x, y)
        if button == arcade.MOUSE_BUTTON_RIGHT:
            print("Right button hit!", x, y)
        if button == arcade.MOUSE_BUTTON_MIDDLE:
            print("Scroll wheel hit!", x, y)

def main():
    window = MyGame(640, 480, "Drawing Example")
    arcade.run()


main()