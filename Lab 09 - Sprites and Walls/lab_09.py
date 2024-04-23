import arcade
import random

# Set up constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SPEED = 5

class MyGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, "Scrolling Landscape")

        # Set up player
        self.player = arcade.Sprite("resources:images/animated_characters/male_adventurer", scale=0.5)
        self.player.center_x = SCREEN_WIDTH // 2
        self.player.center_y = SCREEN_HEIGHT // 2
        self.player.change_x = 0
        self.player.change_y = 0

        # Set up coins
        self.coins = arcade.SpriteList()
        for _ in range(20):
            coin = arcade.Sprite("resources.coinSilver.png", scale=0.5)
            coin.center_x = random.randint(0, SCREEN_WIDTH)
            coin.center_y = random.randint(0, SCREEN_HEIGHT)
            self.coins.append(coin)

        # Set up walls
        self.walls = arcade.SpriteList()
        for i in range(200, SCREEN_WIDTH, 300):
            wall = arcade.Sprite("images/wall1.png", scale=0.5)
            wall.center_x = i
            wall.center_y = random.randint(100, SCREEN_HEIGHT - 100)
            self.walls.append(wall)

        for i in range(400, SCREEN_WIDTH, 300):
            wall = arcade.Sprite("images/wall2.png", scale=0.5)
            wall.center_x = i
            wall.center_y = random.randint(100, SCREEN_HEIGHT - 100)
            self.walls.append(wall)

        # Set up score
        self.score = 0

        # Load coin sound
        self.coin_sound = arcade.load_sound("sounds/coin.wav")

    def on_draw(self):
        arcade.start_render()

        # Draw player, coins, and walls
        self.player.draw()
        self.coins.draw()
        self.walls.draw()

        # Draw score
        arcade.draw_text(f"Score: {self.score}", 10, SCREEN_HEIGHT - 30, arcade.color.WHITE, 16)

    def update(self, delta_time):
        # Update player movement
        self.player.update()

        # Update player position based on keyboard input
        self.player.center_x += self.player.change_x
        self.player.center_y += self.player.change_y

        # Check for collision with walls
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

        # Check for collision with coins
        for coin in self.coins:
            if arcade.check_for_collision(self.player, coin):
                coin.kill()
                self.score += 1
                arcade.play_sound(self.coin_sound)

    def on_key_press(self, key, modifiers):
        # Handle player movement
        if key == arcade.key.LEFT:
            self.player.change_x = -PLAYER_SPEED
        elif key == arcade.key.RIGHT:
            self.player.change_x = PLAYER_SPEED
        elif key == arcade.key.UP:
            self.player.change_y = PLAYER_SPEED
        elif key == arcade.key.DOWN:
            self.player.change_y = -PLAYER_SPEED

    def on_key_release(self, key, modifiers):
        # Stop player movement when key is released
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.player.change_y = 0

def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

if __name__ == "__main__":
    main()