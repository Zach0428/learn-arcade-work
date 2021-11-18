import arcade

WIDTH = 60
HEIGHT = 60
MARGIN = 5
COLUMN_COUNT = 10
ROW_COUNT = 10

SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)

        # Create grid of numbers
        self.grid = []
        for row in range(ROW_COUNT):
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)

        print(self.grid)

        # self.grid = [[0 for x in range(10)] for y in range(10)]

    def on_draw(self):
        """
        Render the screen.
        """

        arcade.start_render()

        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                x = WIDTH / 2 + column * (WIDTH + MARGIN) + MARGIN
                y = HEIGHT / 2 + row * (HEIGHT + MARGIN) + MARGIN
                if self.grid[row][column] == 0:
                    color = arcade.color.BALL_BLUE
                else:
                    color = arcade.color.ORANGE_PEEL
                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        row = int(y // (HEIGHT + MARGIN))
        column = int(x // (WIDTH + MARGIN))
        print("Click", row, column)

        if self.grid[row][column] == 0:
            self.grid[row][column] = 1
        else:
            self.grid[row][column] = 0

        if row < (ROW_COUNT - 1):
            if self.grid[row + 1][column] == 0:
                self.grid[row + 1][column] = 1
            else:
                self.grid[row + 1][column] = 0

        if row >= 1:
            if self.grid[row - 1][column] == 0:
                self.grid[row - 1][column] = 1
            else:
                self.grid[row - 1][column] = 0

        if column < (COLUMN_COUNT - 1):
            if self.grid[row][column + 1] == 0:
                self.grid[row][column + 1] = 1
            else:
                self.grid[row][column + 1] = 0

        if column >= 1:
            if self.grid[row][column - 1] == 0:
                self.grid[row][column - 1] = 1
            else:
                self.grid[row][column - 1] = 0


def main():

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()
