import arcade
from lab_03 import draw_sunrise

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
OBJECT_RADIUS = 10
OBJECT_WIDTH = 100
OBJECT_HEIGHT = 20
OBJECT_SPEED = 5


class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")
        self.mouse_object_x = SCREEN_WIDTH // 2
        self.mouse_object_y = SCREEN_HEIGHT // 2
        self.keyboard_object_x = SCREEN_WIDTH // 2
        self.keyboard_object_y = OBJECT_RADIUS
        self.is_left_pressed = False
        self.is_right_pressed = False

    def on_draw(self):
        arcade.start_render()

        draw_sunrise(1/60)

        arcade.draw_circle_filled(self.mouse_object_x, self.mouse_object_y, OBJECT_RADIUS, arcade.color.LIGHT_BLUE)
        arcade.draw_rectangle_filled(self.keyboard_object_x, self.keyboard_object_y, OBJECT_WIDTH, OBJECT_HEIGHT, arcade.color.ORANGE)

    def update(self, delta_time):
        if self.is_left_pressed and self.keyboard_object_x > OBJECT_WIDTH // 2:
            self.keyboard_object_x -= OBJECT_SPEED
        elif self.is_right_pressed and self.keyboard_object_x < SCREEN_WIDTH - OBJECT_WIDTH // 2:
            self.keyboard_object_x += OBJECT_SPEED

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        if OBJECT_RADIUS <= x <= SCREEN_WIDTH - OBJECT_RADIUS:
            self.mouse_object_x = x
        if OBJECT_RADIUS <= y <= SCREEN_HEIGHT - OBJECT_RADIUS:
            self.mouse_object_y = y

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.is_left_pressed = True
        elif key == arcade.key.RIGHT:
            self.is_right_pressed = True

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.is_left_pressed = False
        elif key == arcade.key.RIGHT:
            self.is_right_pressed = False

    def on_mouse_press(self, x, y, button, modifiers):
        laser_sound = arcade.load_sound(resources:sounds/laser.wav)
        if button == arcade.MOUSE_BUTTON_LEFT:
            arcade.play_sound(laser_sound)



def main():
    window = MyGame()
    arcade.run()

main()