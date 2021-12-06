"""
Scroll around a large screen.

Artwork from https://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_move_scrolling
"""

import random
import arcade
import math

SPRITE_SCALING = 0.5

DEFAULT_SCREEN_WIDTH = 800
DEFAULT_SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Move with Scrolling Screen Example"
SPRITE_SCALING_COIN = .5

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 220

# How fast the camera pans to the player. 1.0 is instant.
CAMERA_SPEED = 0.1

# How fast the character moves
PLAYER_MOVEMENT_SPEED = 4

COIN_COUNT = 20

METEOR = 14

BULLET_SPEED = 3

HEALTHBAR_WIDTH = 25
HEALTHBAR_HEIGHT = 3
HEALTHBAR_OFFSET_Y = -10

HEALTH_NUMBER_OFFSET_X = -10
HEALTH_NUMBER_OFFSET_Y = -25


sound = arcade.load_sound(":resources:sounds/coin4.wav")


class SpriteWithHealth(arcade.Sprite):
    """ Sprite with hit points """

    def __init__(self, image, scale, max_health):
        super().__init__(image, scale)

        # Add extra attributes for health
        self.max_health = max_health
        self.cur_health = max_health

    def draw_health_number(self):
        """ Draw how many hit points we have """

        health_string = f"{self.cur_health}/{self.max_health}"
        arcade.draw_text(health_string,
                         start_x=self.center_x + HEALTH_NUMBER_OFFSET_X,
                         start_y=self.center_y + HEALTH_NUMBER_OFFSET_Y,
                         font_size=12,
                         color=arcade.color.WHITE)

    def draw_health_bar(self):
        """ Draw the health bar """

        # Draw the 'unhealthy' background
        if self.cur_health < self.max_health:
            arcade.draw_rectangle_filled(center_x=self.center_x,
                                         center_y=self.center_y + HEALTHBAR_OFFSET_Y,
                                         width=HEALTHBAR_WIDTH,
                                         height=3,
                                         color=arcade.color.RED)

        # Calculate width based on health
        health_width = HEALTHBAR_WIDTH * (self.cur_health / self.max_health)

        arcade.draw_rectangle_filled(center_x=self.center_x - 0.5 * (HEALTHBAR_WIDTH - health_width),
                                     center_y=self.center_y - 10,
                                     width=health_width,
                                     height=HEALTHBAR_HEIGHT,
                                     color=arcade.color.GREEN)


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title, resizable=True)

        # Sprite lists
        self.player_list = None
        self.wall_list = None

        # Set up the player
        self.player_sprite = None

        # Physics engine so we don't run into walls.
        self.physics_engine = None

        # Create the cameras. One for the GUI, one for the sprites.
        # We scroll the 'sprite world' but not the GUI.
        self.camera_sprites = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)

        self.coin_list = None

        self.meteor_list = None

        self.bullet_list = None

        self.score = 0

        self.gun_sound = arcade.load_sound(":resources:sounds/hurt5.wav")
        self.hit_sound = arcade.load_sound(":resources:sounds/hit4.wav")
        self.death_sound = arcade.load_sound(":resources:sounds/hit5.wav")

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.meteor_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = SpriteWithHealth(":resources:images/animated_characters/female_person/femalePerson_idle.png",
                                           scale=0.4, max_health=5)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 64
        self.player_list.append(self.player_sprite)

        # -- Set up several columns of wall

        wall = arcade.Sprite("../Lab 12 - Final Lab/lava.png", SPRITE_SCALING)
        wall.center_x = 64
        wall.center_y = 64
        self.wall_list.append(wall)

        # Roof
        for x in range(64, 1458, 64):
            wall = arcade.Sprite("../Lab 12 - Final Lab/planetMid.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 960
            self.wall_list.append(wall)

        for x in range(320, 512, 64):
            wall = arcade.Sprite("../Lab 12 - Final Lab/lava.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 64
            self.wall_list.append(wall)

        # --- Place boxes inside a loop
        for x in range(128, 320, 64):
            wall = arcade.Sprite("../Lab 12 - Final Lab/grassMid.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 64
            self.wall_list.append(wall)

        for x in range(512, 832, 64):
            wall = arcade.Sprite("../Lab 12 - Final Lab/grassMid.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 64
            self.wall_list.append(wall)

        for x in range(832, 1152, 64):
            wall = arcade.Sprite("../Lab 12 - Final Lab/lava.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 64
            self.wall_list.append(wall)

        for x in range(1152, 1458, 64):
            wall = arcade.Sprite("../Lab 12 - Final Lab/grassMid.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 64
            self.wall_list.append(wall)

        # Sides
        for y in range(64, 1010, 64):
            wall = arcade.Sprite("../Lab 12 - Final Lab/stoneCenter.png", SPRITE_SCALING)
            wall.center_x = 0
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(64, 1010, 64):
            wall = arcade.Sprite("../Lab 12 - Final Lab/stoneCenter.png", SPRITE_SCALING)
            wall.center_x = 1468
            wall.center_y = y
            self.wall_list.append(wall)

        # Walls
        coordinate_list = [[256, 128],
                           [256, 192],
                           [256, 256],
                           [256, 320],
                           [576, 128],
                           [576, 192],
                           [576, 256],
                           [256, 448],
                           [256, 512],
                           [256, 576],
                           [64, 512],
                           [128, 512],
                           [128, 640],
                           [128, 704],
                           [128, 192],
                           [192, 192],
                           [64, 320],
                           [128, 320],
                           [128, 832],
                           [192, 832],
                           [256, 832],
                           [256, 704],
                           [320, 704],
                           [384, 704],
                           [448, 704],
                           [384, 832],
                           [384, 896],
                           [320, 576],
                           [448, 512],
                           [512, 512],
                           [576, 512],
                           [384, 448],
                           [384, 384],
                           [384, 320],
                           [576, 704],
                           [576, 640],
                           [384, 192],
                           [512, 192],
                           [512, 320],
                           [512, 384],
                           [576, 384],
                           [640, 384],
                           [704, 384],
                           [704, 512],
                           [704, 576],
                           [704, 640],
                           [448, 832],
                           [512, 832],
                           [576, 832],
                           [704, 768],
                           [768, 768],
                           [832, 768],
                           [768, 832],
                           [832, 832],
                           [768, 576],
                           [832, 576],
                           [896, 576],
                           [832, 512],
                           [832, 448],
                           [896, 768],
                           [896, 704],
                           [768, 128],
                           [768, 192],
                           [704, 192],
                           [768, 320],
                           [832, 192],
                           [896, 192],
                           [960, 192],
                           [960, 256],
                           [960, 320],
                           [960, 384],
                           [896, 320],
                           [960, 512],
                           [1024, 512],
                           [1088, 512],
                           [1024, 576],
                           [1024, 640],
                           [1024, 768],
                           [1024, 832],
                           [1088, 448],
                           [1088, 320],
                           [1088, 256],
                           [1088, 192],
                           [1152, 192],
                           [1152, 128],
                           [1216, 192],
                           [1280, 192],
                           [1280, 256],
                           [1344, 256],
                           [1216, 320],
                           [1344, 320],
                           [1344, 384],
                           [1344, 448],
                           [1280, 448],
                           [1216, 448],
                           [1216, 512],
                           [1216, 576],
                           [1216, 704],
                           [1280, 704],
                           [1344, 704],
                           [1344, 640],
                           [1408, 576],
                           [1088, 832],
                           [1152, 896],
                           [1280, 768],
                           [1280, 832],
                           [1344, 832]]

        for coordinate in coordinate_list:
            wall = arcade.Sprite("../Lab 12 - Final Lab/stoneCenter.png", SPRITE_SCALING)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        for i in range(COIN_COUNT):
            coin = arcade.Sprite("../Lab 12 - Final Lab/coinGold.png", SPRITE_SCALING_COIN)

            coin_placed_successfully = False

            while not coin_placed_successfully:
                coin.center_x = random.randrange(64, 1458)
                coin.center_y = random.randrange(64, 960)
                wall_hit_list = arcade.check_for_collision_with_list(coin, self.wall_list)
                coin_hit_list = arcade.check_for_collision_with_list(coin, self.coin_list)

                if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:
                    coin_placed_successfully = True

            self.coin_list.append(coin)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)
        for i in range(METEOR):
            meteor = arcade.Sprite(":resources:images/space_shooter/meteorGrey_small1.png", 1)
            meteor.center_x = random.randrange(64, 1458)
            meteor.center_y = random.randrange(64, 960)
            while meteor.change_x == 0 and meteor.change_y == 0:
                meteor.change_x = random.randrange(-4, 5)
                meteor.change_y = random.randrange(-4, 5)

            meteor_placed_successfully = False

            while not meteor_placed_successfully:
                meteor.center_x = random.randrange(64, 1458)
                meteor.center_y = random.randrange(64, 960)
                wall_hit_list = arcade.check_for_collision_with_list(meteor, self.wall_list)

                if len(wall_hit_list) == 0:
                    meteor_placed_successfully = True

            self.meteor_list.append(meteor)

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Select the camera we'll use to draw all our sprites
        self.camera_sprites.use()

        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()
        self.coin_list.draw()
        self.meteor_list.draw()
        self.bullet_list.draw()

        for self.player_sprite in self.player_list:
            self.player_sprite.draw_health_number()
            self.player_sprite.draw_health_bar()

        # Select the (unscrolled) camera for our GUI
        self.camera_gui.use()

        # Draw the GUI
        # arcade.draw_rectangle_filled(self.width // 2,
        #                              20,
        #                              self.width,
        #                              40,
        #                              arcade.color.ALMOND)
        # text = f"Scroll value: ({self.camera_sprites.position[0]:5.1f}, " \
        #        f"{self.camera_sprites.position[1]:5.1f})"
        # arcade.draw_text(text, 10, 10, arcade.color.BLACK_BEAN, 20)

        output = "Score: " + str(self.score)
        arcade.draw_text(output, 5, 5, arcade.color.WHITE, 16)

        if self.player_sprite.cur_health <= 0:
            arcade.draw_text("Game Over", DEFAULT_SCREEN_WIDTH / 2, DEFAULT_SCREEN_HEIGHT / 2, arcade.color.GOLD,
                             60, anchor_x="center")

        if len(self.coin_list) == 0:
            arcade.draw_text("You Win!", DEFAULT_SCREEN_WIDTH / 2, DEFAULT_SCREEN_HEIGHT / 2, arcade.color.GOLD, 60,
                             anchor_x="center")

    def on_mouse_press(self, x, y, button, modifiers):
        """ Called whenever the mouse button is clicked. """

        arcade.play_sound(self.gun_sound)

        bullet = arcade.Sprite(":resources:images/space_shooter/laserBlue01.png", 0.8)

        start_x = self.player_sprite.center_x
        start_y = self.player_sprite.center_y
        bullet.center_x = start_x
        bullet.center_y = start_y

        dest_x = x + self.camera_sprites.position[0]
        dest_y = y + self.camera_sprites.position[1]

        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff)

        bullet.angle = math.degrees(angle)
        print(f"Bullet angle: {bullet.angle:.2f}")

        bullet.change_x = math.cos(angle) * BULLET_SPEED
        bullet.change_y = math.sin(angle) * BULLET_SPEED

        self.bullet_list.append(bullet)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        if self.player_sprite.cur_health > 0:
            """ Movement and game logic """

            hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

            for coin in hit_list:
                self.score += 1
                arcade.play_sound(sound)
                coin.remove_from_sprite_lists()

            if len(self.coin_list) > 0:
                self.player_list.update()
                self.physics_engine.update()
                self.scroll_to_player()

            for meteor in self.meteor_list:
                meteor.center_x += meteor.change_x
                walls_hit = arcade.check_for_collision_with_list(meteor, self.wall_list)

                for wall in walls_hit:
                    if meteor.change_x > 0:
                        meteor.right = wall.left
                    elif meteor.change_x < 0:
                        meteor.left = wall.right
                if len(walls_hit) > 0:
                    meteor.change_x *= -1

                meteor.center_y += meteor.change_y
                walls_hit = arcade.check_for_collision_with_list(meteor, self.wall_list)
                for wall in walls_hit:
                    if meteor.change_y > 0:
                        meteor.top = wall.bottom
                    elif meteor.change_y < 0:
                        meteor.bottom = wall.top
                if len(walls_hit) > 0:
                    meteor.change_y *= -1

                self.bullet_list.update()

                for bullet in self.bullet_list:

                    # Check this bullet to see if it hit a coin
                    hit_list = arcade.check_for_collision_with_list(bullet, self.meteor_list)

                    # If it did, get rid of the bullet
                    if len(hit_list) > 0:
                        bullet.remove_from_sprite_lists()

                    # If the bullet flies off-screen, remove it.
                    if bullet.bottom > self.width or bullet.top < 0 or bullet.right < 0 or bullet.left > self.width:
                        bullet.remove_from_sprite_lists()

            hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.meteor_list)

            for meteor in hit_list:
                self.player_sprite.cur_health -= 1

                meteor.remove_from_sprite_lists()

                if self.player_sprite.cur_health <= 0:
                    self.player_sprite.remove_from_sprite_lists()
                    arcade.play_sound(self.death_sound)
                else:
                    # Not dead
                    arcade.play_sound(self.hit_sound)

    def scroll_to_player(self):
        """
        Scroll the window to the player.

        if CAMERA_SPEED is 1, the camera will immediately move to the desired position.
        Anything between 0 and 1 will have the camera move to the location with a smoother
        pan.
        """

        position = self.player_sprite.center_x - self.width / 2, \
            self.player_sprite.center_y - self.height / 2
        self.camera_sprites.move_to(position, CAMERA_SPEED)

    def on_resize(self, width, height):
        """
        Resize window
        Handle the user grabbing the edge and resizing the window.
        """
        self.camera_sprites.resize(int(width), int(height))
        self.camera_gui.resize(int(width), int(height))


def main():
    """ Main function """
    window = MyGame(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
