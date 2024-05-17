import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SPEED = 5
VIEWPORT_MARGIN = 200


class MyGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, "Maze with Scrolling Screen")
        self.player = arcade.Sprite(":resources:images/animated_characters/male_person/malePerson_idle.png", scale=0.5)
        self.player.center_x = SCREEN_WIDTH // 2
        self.player.center_y = SCREEN_HEIGHT // 2
        self.player.change_x = 0
        self.player.change_y = 0
        self.coins = arcade.SpriteList()

        for _ in range(20):
            coin = arcade.Sprite(":resources:images/items/coinGold.png", scale=0.5)
            coin.center_x = random.randint(-SCREEN_WIDTH, SCREEN_WIDTH * 2)
            coin.center_y = random.randint(-SCREEN_HEIGHT, SCREEN_HEIGHT * 2)
            self.coins.append(coin)
        self.walls = self.generate_maze()
        self.score = 0
        self.coin_sound = arcade.load_sound(":resources:sounds/coin4.wav")
        self.view_left = 0
        self.view_bottom = 0

    def generate_maze(self):
        maze = []
        for x in range(-SCREEN_WIDTH, SCREEN_WIDTH * 2, 40):
            row = []
            for y in range(-SCREEN_HEIGHT, SCREEN_HEIGHT * 2, 40):
                row.append(False)
            maze.append(row)
        for _ in range(100):
            x = random.randint(0, len(maze) - 1)
            y = random.randint(0, len(maze[0]) - 1)
            maze[x][y] = True
        walls = arcade.SpriteList()
        for x, row in enumerate(maze):
            for y, cell in enumerate(row):
                if cell:
                    wall = arcade.Sprite(":resources:images/tiles/brickGrey.png", scale=0.5)
                    wall.center_x = x * 40
                    wall.center_y = y * 40
                    walls.append(wall)

        return walls

    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        self.coins.draw()
        self.walls.draw()

        arcade.draw_text(f"Score: {self.score}", 10 + self.view_left, SCREEN_HEIGHT - 30 + self.view_bottom,
                         arcade.color.WHITE, 16)

    def update(self, delta_time):
        self.player.update()
        self.player.center_x += self.player.change_x
        self.player.center_y += self.player.change_y
        changed = False
        left_boundary = self.view_left + VIEWPORT_MARGIN
        if self.player.left < left_boundary:
            self.view_left -= left_boundary - self.player.left
            changed = True
        right_boundary = self.view_left + SCREEN_WIDTH - VIEWPORT_MARGIN
        if self.player.right > right_boundary:
            self.view_left += self.player.right - right_boundary
            changed = True
        top_boundary = self.view_bottom + SCREEN_HEIGHT - VIEWPORT_MARGIN
        if self.player.top > top_boundary:
            self.view_bottom += self.player.top - top_boundary
            changed = True

        bottom_boundary = self.view_bottom + VIEWPORT_MARGIN
        if self.player.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player.bottom
            changed = True

        if changed:
            arcade.set_viewport(self.view_left, SCREEN_WIDTH + self.view_left, self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)

        for wall in self.walls:
            if arcade.check_for_collision(self.player, wall):
                if self.player.change_x > 0:
                    self.player.center_x = wall.left - self.player.width / 2
                elif self.player.change_x < 0:
                    self.player.center_x = wall.right + self.player.width / 2
                elif self.player.change_y > 0:
                    self.player.center_y = wall.bottom - self.player.height / 2
                elif self.player.change_y < 0:
                    self.player.center_y = wall.top + self.player.height / 2

        for coin in self.coins:
            if arcade.check_for_collision(self.player, coin):
                coin.kill()
                self.score += 1
                arcade.play_sound(self.coin_sound)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player.change_x = -PLAYER_SPEED
        elif key == arcade.key.RIGHT:
            self.player.change_x = PLAYER_SPEED
        elif key == arcade.key.UP:
            self.player.change_y = PLAYER_SPEED
        elif key == arcade.key.DOWN:
            self.player.change_y = -PLAYER_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.player.change_y = 0


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()