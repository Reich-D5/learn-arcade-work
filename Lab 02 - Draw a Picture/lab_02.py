import arcade
"""
# set parameters for called function
arcade.open_window(600, 600, "Drawing a game")

# set color for background
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

# begin the drawing of the screen
arcade.start_render()

# arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.GREEN)
arcade.draw_lrbt_rectangle_filled(0, 599, 0, 300, arcade.csscolor.GREEN)
arcade.draw_rectangle_filled(100, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_circle_filled(100, 350, 30, arcade.csscolor.DARK_GREEN)

# finish drawing
arcade.finish_render()

arcade.run()
"""



SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 600
SCREEN_TITLE = "American Football Stadium"

def draw_stadium():
    arcade.draw_rectangle_filled(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 1100, 400, arcade.color.GREEN)

    # Draw lines for the field
    for i in range(21):
        arcade.draw_line(100 + i * 50, 100, 100 + i * 50, 500, arcade.color.WHITE)

    # Draw the end zones
    arcade.draw_rectangle_filled(50, SCREEN_HEIGHT // 2, 100, 400, arcade.color.GREEN)
    arcade.draw_rectangle_filled(1250, SCREEN_HEIGHT // 2, 100, 400, arcade.color.GREEN)

    #draw_bleachers(225, arcade.color.GRAY)  # Left side bleachers
    #draw_bleachers(1075, arcade.color.GRAY)  # Right side bleachers

    # Draw the yard markers
    for i in range(20):
        arcade.draw_text(str(i*5), 125 + i*50, 510, arcade.color.WHITE, 12, anchor_x="center")

"""def draw_bleachers(x, color):
    y_start = 150
    for i in range(6):
        arcade.draw_rectangle_filled(x, y_start + i * 40, 200, 20, color)"""


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.set_background_color(arcade.color.SKY_BLUE)

    arcade.start_render()

    draw_stadium()

    arcade.finish_render()

    arcade.run()


if __name__ == "__main__":
    main()