import arcade
import os

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 5

# Get the current directory of the script
current_dir = os.path.dirname(os.path.abspath(__file__))
sound_dir = os.path.join(current_dir, 'sounds')

class CustomShape:
    """ Class representing a custom shape """

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, 50, 50, self.color)

    def update_position(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y

class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

        self.shape1 = CustomShape(100, 100, arcade.color.BLUE)
        self.shape2 = CustomShape(200, 200, arcade.color.RED)

        # Load sound files using the full path
        self.click_sound = arcade.load_sound(os.path.join(sound_dir, "click_sound.wav"))
        self.bump_sound = arcade.load_sound(os.path.join(sound_dir, "bump_sound.wav"))

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.shape1.draw()
        self.shape2.draw()

    def update(self, delta_time):
        """ Move objects and check for collision with edges """
        self.shape1.update_position(self.shape1.dx, self.shape1.dy)
        self.shape2.update_position(self.shape2.dx, self.shape2.dy)

        self.check_edge_collision(self.shape1)
        self.check_edge_collision(self.shape2)

    def check_edge_collision(self, shape):
        """ Check if a shape is colliding with the edges of the screen """
        if shape.x < 25 or shape.x > SCREEN_WIDTH - 25 or shape.y < 25 or shape.y > SCREEN_HEIGHT - 25:
            arcade.play_sound(self.bump_sound)

    def on_key_press(self, key, modifiers):
        """ Handle key press events """
        if key == arcade.key.W:
            self.shape1.dy = MOVEMENT_SPEED
        elif key == arcade.key.S:
            self.shape1.dy = -MOVEMENT_SPEED
        elif key == arcade.key.A:
            self.shape1.dx = -MOVEMENT_SPEED
        elif key == arcade.key.D:
            self.shape1.dx = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Handle key release events """
        if key in [arcade.key.W, arcade.key.S]:
            self.shape1.dy = 0
        elif key in [arcade.key.A, arcade.key.D]:
            self.shape1.dx = 0

    def on_mouse_press(self, x, y, button, modifiers):
        """ Handle mouse click events """
        arcade.play_sound(self.click_sound)
        self.shape2.x = x
        self.shape2.y = y

def main():
    window = MyGame()
    arcade.run()

if __name__ == "__main__":
    main()
#crank
