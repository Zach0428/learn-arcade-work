""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 3
right_sound = arcade.load_sound(":resources:sounds/laser2.wav")
left_sound = arcade.load_sound(":resources:sounds/coin1.wav")
wall_hit = arcade.load_sound(":resources:sounds/error1.wav")

def snow():
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 4, 0, arcade.color.WHITE)

def cloud(x,y):
    arcade.draw_circle_filled(300 + x, 500 + y, 20, arcade.color.WHITE)
    arcade.draw_circle_filled(320 + x, 515 + y, 20, arcade.color.WHITE)
    arcade.draw_circle_filled(340 + x, 500 + y, 20, arcade.color.WHITE)
    arcade.draw_rectangle_filled(320 + x, 485 + y, 80, 25, arcade.color.BLACK)

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
    arcade.draw_point(0, 20, arcade.color.YELLOW, 7)



class Cloud:
    def __init__(self, position_x, position_y, radius, color):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color

    def draw(self):
            """ Draw the balls with the instance variables we have. """
            arcade.draw_arc_filled(self.position_x, 15 + self.position_y, 50, 50, arcade.color.WHITE, 0, 180)
            arcade.draw_arc_filled(20 + self.position_x, 30 + self.position_y, 50, 50, arcade.color.WHITE, 0, 180)
            arcade.draw_arc_filled(40 + self.position_x, 15 + self.position_y, 50, 50, arcade.color.WHITE, 0, 180)

class Snowman:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):
        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, 190 + self.position_y, 50, arcade.color.WHITE)
        arcade.draw_circle_filled(self.position_x, 190 + self.position_y, 50, arcade.color.WHITE)
        arcade.draw_circle_filled(self.position_x, 270 + self.position_y, 40, arcade.color.WHITE)
        arcade.draw_circle_filled(self.position_x, 330 + self.position_y, 30, arcade.color.WHITE)
        arcade.draw_circle_filled(self.position_x, 270 + self.position_y, 5, arcade.color.RED, num_segments=32)
        arcade.draw_circle_filled(self.position_x, 175 + self.position_y, 5, arcade.color.RED, num_segments=32)
        arcade.draw_circle_filled(self.position_x, 225 + self.position_y, 5, arcade.color.RED, num_segments=32)
        arcade.draw_triangle_filled(self.position_x - 5, 330 + self.position_y, self.position_x - 5, 340 + self.position_y, 15 + self.position_x, 335 + self.position_y, arcade.color.ORANGE)
        arcade.draw_circle_filled(self.position_x - 10, 345 + self.position_y, 3, arcade.color.BLACK, num_segments=32)
        arcade.draw_circle_filled(10 + self.position_x, 345 + self.position_y, 3, arcade.color.BLACK, num_segments=32)
        arcade.draw_line(self.position_x - 40, 280 + self.position_y, self.position_x - 60, 220 + self.position_y, arcade.color.BROWN, 5)
        arcade.draw_line(35 + self.position_x, 290 + self.position_y, 70 + self.position_x, 290 + self.position_y, arcade.color.BROWN, 5)
        arcade.draw_line(70 + self.position_x, 325 + self.position_y, 70 + self.position_x, 290 + self.position_y, arcade.color.BROWN, 5)


    def update(self):
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        if self.position_x < self.radius:
            self.position_x = self.radius
            arcade.play_sound(wall_hit)

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius
            arcade.play_sound(wall_hit)

        if self.position_y < self.radius:
            self.position_y = self.radius
            arcade.play_sound(wall_hit)

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius
            arcade.play_sound(wall_hit)

class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")
        self.cloud = Cloud(50, 50, 15, arcade.color.AUBURN)
        self.set_mouse_visible(False)
        self.snowman = Snowman(50, 50, 0, 0, 15, arcade.color.AUBURN)

    def on_draw(self):
        arcade.start_render()
        snow()
        cloud(40, 0)
        self.cloud.draw()
        self.snowman.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        self.cloud.position_x = x
        self.cloud.position_y = y

    def on_mouse_press(self, x, y, button: int, modifiers: int):
        print(button)
        if button == arcade.MOUSE_BUTTON_LEFT:
            arcade.play_sound(left_sound)
        if button == arcade.MOUSE_BUTTON_RIGHT:
            arcade.play_sound(right_sound)

    def update(self, delta_time):
        self.snowman.update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.snowman.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.snowman.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.snowman.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.snowman.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.snowman.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.snowman.change_y = 0

def main():
    window = MyGame()
    arcade.run()


main()