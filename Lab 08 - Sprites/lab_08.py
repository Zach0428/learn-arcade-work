import random
import arcade
import math
import os

SPRITE_SCALING = 0.5
SPRITE_SCALING_COIN = 0.5
COIN_COUNT = 50
SPRITE_SCALING_PLAYER = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Collect Coins Moving in Circles Example"

MOVEMENT_SPEED = 2
BANANA = .03

good_sound = arcade.load_sound(":resources:sounds/coin4.wav")
bad_sound = arcade.load_sound(":resources:sounds/error1.wav")


class Coin(arcade.Sprite):

    def reset_pos(self):

        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                         SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):

        self.center_y -= 1

        if self.top < 0:
            self.reset_pos()


class Banana(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.circle_angle = 0

        self.circle_radius = 0

        self.circle_speed = 0.008

        self.circle_center_x = 0
        self.circle_center_y = 0

    def update(self):

        self.center_x = self.circle_radius * math.sin(self.circle_angle) \
            + self.circle_center_x
        self.center_y = self.circle_radius * math.cos(self.circle_angle) \
            + self.circle_center_y

        self.circle_angle += self.circle_speed


class Player(arcade.Sprite):

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):

        super().__init__(width, height, title)

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        self.player_list = None
        self.banana_list = None
        self.coin_list = None

        self.score = 0
        self.player_sprite = None
        self.coin_sprite_list = None

    def start_new_game(self):

        self.player_list = arcade.SpriteList()
        self.banana_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        self.score = 0

        self.player_sprite = Player("malePerson_walk1 (1).png", SPRITE_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 70
        self.player_list.append(self.player_sprite)

        self.coin_sprite_list = arcade.SpriteList()

<<<<<<< HEAD
        # Create the coins
        for i in range(50):
=======
        for i in range(COIN_COUNT):
>>>>>>> 4c6c2671553c647f17b47ad1aaf3ef3d35b349ff

            coin = Coin("coinGold.png", SPRITE_SCALING_COIN)

            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            self.coin_sprite_list.append(coin)

        for i in range(50):

            banana = Banana("banana.png", BANANA)

            banana.circle_center_x = random.randrange(SCREEN_WIDTH)
            banana.circle_center_y = random.randrange(SCREEN_HEIGHT)

            banana.circle_radius = random.randrange(10, 200)

            banana.circle_angle = random.random() * 2 * math.pi

            self.banana_list.append(banana)

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        arcade.start_render()
        self.coin_sprite_list.draw()
        self.player_list.draw()
        self.banana_list.draw()

        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

        output = "Score: " + str(self.score)
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

        if len(self.coin_sprite_list) == 0:
            end = "Game Over"
<<<<<<< HEAD
            arcade.draw_text(end, 400, 300, arcade.color.WHITE, 16, anchor_x="center")
=======
            arcade.draw_text(end, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, arcade.color.WHITE, 16, anchor_x="center")
>>>>>>> 4c6c2671553c647f17b47ad1aaf3ef3d35b349ff

    def on_key_press(self, key, modifiers):

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):

        if len(self.coin_sprite_list) > 0:
            self.banana_list.update()
            self.player_list.update()
            self.coin_list.update()
            self.coin_sprite_list.update()

            hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                            self.banana_list)

            for banana in hit_list:
                self.score -= 1
                banana.remove_from_sprite_lists()
                arcade.play_sound(bad_sound)

            hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                            self.coin_sprite_list)

            for coin in hit_list:
                coin.remove_from_sprite_lists()
                self.score += 1
                arcade.play_sound(good_sound)


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.start_new_game()
    arcade.run()


if __name__ == "__main__":
    main()
