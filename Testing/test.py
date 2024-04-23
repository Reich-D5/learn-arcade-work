import arcade

WIDTH = HEIGHT = 30
MARGIN = 10
ROW_COUNT = COLUMN_COUNT = 20

SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN


class MyGame(arcade.Window):

    """
    Main application class.
    """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)

        self.grid = []
        for row in range(ROW_COUNT):
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)

        self.grid[1][5] = 5

    def on_draw(self):
        """
        Render the screen.
        """
        arcade.start_render()

        arcade.draw_rectangle_filled(WIDTH / 2 + MARGIN, HEIGHT / 2 + MARGIN, WIDTH, HEIGHT, arcade.color.WHITE)

        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                x = column * (WIDTH + MARGIN) + WIDTH / 2 + MARGIN
                y = row * (HEIGHT + MARGIN) + HEIGHT / 2 + MARGIN
                color = arcade.color.WHITE
                if self.grid[row][column] == 1:
                    color = arcade.color.GREEN
                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)

    def on_mouse_press(self, x, y, button, key_modifiers):
        print("click")
        print(f"Mouse coordinates: ({x}, {y})")
        grid_x = int(x // (WIDTH + MARGIN))
        grid_y = int(y // (HEIGHT + MARGIN))
        print(f"Grid coordinates: ({grid_x}, {grid_y})")
        if 0 <= grid_x < COLUMN_COUNT and 0 <= grid_y < ROW_COUNT:
            column = x // (WIDTH + MARGIN)
            row = y // (HEIGHT + MARGIN)
            self.grid[row][column] = (self.grid[row][column] + 1) % 2


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()
