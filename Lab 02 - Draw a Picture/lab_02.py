import arcade

SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 600
SCREEN_TITLE = "American Football Stadium"

def draw_stadium():
    arcade.draw_rectangle_filled(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 1100, 400, arcade.color.GREEN)
    for i in range(21):
        arcade.draw_line(100 + i * 50, 100, 100 + i * 50, 500, arcade.color.WHITE)

    arcade.draw_rectangle_filled(50, SCREEN_HEIGHT // 2, 100, 400, arcade.color.GREEN)
    arcade.draw_rectangle_filled(1250, SCREEN_HEIGHT // 2, 100, 400, arcade.color.GREEN)

    for i in range(20):
        arcade.draw_text(str(i*5), 125 + i*50, 510, arcade.color.WHITE, 12, anchor_x="center")


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.set_background_color(arcade.color.SKY_BLUE)

    arcade.start_render()

    draw_stadium()

    arcade.finish_render()

    arcade.run()


if __name__ == "__main__":
    main()