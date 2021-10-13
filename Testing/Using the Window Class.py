import arcade
import random

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


class Ball:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)

    def update(self):
        self.position_y += self.change_y
        self.position_x += self.change_x
        if self.position_x <= 0:
            self.change_x *= -1
        if self.position_x >= SCREEN_WIDTH - self.radius:
            self.change_x *= -1
        if self.position_y <= 0:
            self.change_y *= -1
        if self.position_y >= SCREEN_HEIGHT - self.radius:
            self.change_y *= -1



class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.ASH_GREY)

        self.ball_list = []
        for i in range(50):

            x = random.randrange(SCREEN_WIDTH)
            y = random.randrange(SCREEN_HEIGHT)
            cx = random.randrange(-3, 4)
            cy = random.randrange(-3, 5)
            radius = random.randrange(5, 21)
            color = (random.randrange(256),
                     random.randrange(256),
                     random.randrange(256))

            ball = Ball(x, y, cx, cy, radius, color)
            self.ball_list.append(ball)

    def on_draw(self):
        arcade.start_render()

        for ball in self.ball_list:
            ball.draw()

    def on_update(self, delta_time):
        for ball in self.ball_list:
            ball.update()


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT,
                    "Drawing Example")
    arcade.run()


main()
