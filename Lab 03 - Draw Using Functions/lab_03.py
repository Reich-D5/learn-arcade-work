import arcade
import math
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sunrise with Birds"

BIRD_COUNT = 5
BIRD_SIZE = 20
BIRD_SPEED = 2
BIRD_COLORS = [arcade.color.BLACK, arcade.color.WHITE]

def draw_sunrise(delta_time):
    arcade.start_render()

    # Draw sky gradient
    for y in range(SCREEN_HEIGHT):
        color = lerp_color((0, 51, 102), (255, 204, 153), y / SCREEN_HEIGHT)  # Dark blue to light orange
        arcade.draw_lrbt_rectangle_filled(0, SCREEN_WIDTH, y, y + 1, color)

    arcade.draw_circle_filled(100, 500, 120, arcade.color.YELLOW)
    arcade.draw_circle_filled(100, 500, 140, arcade.color.YELLOW)

    for angle in range(0, 360, 30):
        arcade.draw_line(100, 500,
                         100 + 180 * math.cos(math.radians(angle)),
                         500 + 180 * math.sin(math.radians(angle)),
                         arcade.color.YELLOW, 3)

    draw_cloud(200, 450)
    draw_cloud(500, 550)
    draw_cloud(650, 480)

    for bird in birds:
        bird[0] += BIRD_SPEED
        if bird[0] > SCREEN_WIDTH:
            bird[0] = -BIRD_SIZE
            bird[1] = random.randint(SCREEN_HEIGHT // 2, SCREEN_HEIGHT - BIRD_SIZE)
        draw_bird(bird[0], bird[1], bird[2])

    # Draw mountains
    arcade.draw_polygon_filled(((0, 200),
                                (200, 400),
                                (400, 200),
                                (800, 200),
                                (800, 0),
                                (0, 0)),
                               arcade.color.DARK_GREEN)

    # Draw mountain shadows
    arcade.draw_polygon_filled(((0, 200),
                                (200, 400),
                                (210, 390),
                                (20, 200)),
                               (100, 100, 100))
    arcade.draw_polygon_filled(((200, 400),
                                (400, 200),
                                (400, 210),
                                (210, 390)),
                               (100, 100, 100))

    # Draw the ground
    arcade.draw_lrbt_rectangle_filled(0, SCREEN_WIDTH, 0, 200, arcade.color.GREEN)

def draw_cloud(x, y):
    arcade.draw_circle_filled(x, y, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(x + 50, y, 40, arcade.color.WHITE)
    arcade.draw_circle_filled(x - 40, y, 30, arcade.color.WHITE)

def draw_bird(x, y, color_index):
    arcade.draw_triangle_filled(x, y, x - BIRD_SIZE, y - BIRD_SIZE // 2, x - BIRD_SIZE, y + BIRD_SIZE // 2, BIRD_COLORS[color_index])

# Function to interpolate between two colors
def lerp_color(color1, color2, t):
    r = int(color1[0] * (1 - t) + color2[0] * t)
    g = int(color1[1] * (1 - t) + color2[1] * t)
    b = int(color1[2] * (1 - t) + color2[2] * t)
    return (r, g, b)

# Main function
def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    arcade.set_background_color(arcade.color.LIGHT_BLUE)

    # Create a list to hold the birds
    global birds
    birds = []
    for _ in range(BIRD_COUNT):
        x = random.randint(0, SCREEN_WIDTH - BIRD_SIZE)
        y = random.randint(SCREEN_HEIGHT // 2, SCREEN_HEIGHT - BIRD_SIZE)
        color_index = random.randint(0, len(BIRD_COLORS) - 1)
        birds.append([x, y, color_index])

    arcade.schedule(draw_sunrise, 1/60)

    arcade.run()

# Call the main function
if __name__ == "__main__":
    main()