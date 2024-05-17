import arcade
import random

class MyGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, "My Arcade Game")
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk7.png")
        self.player_sprite.center_x = width // 2
        self.player_sprite.center_y = height // 2
        self.good_sprite_list = arcade.SpriteList()
        self.bad_sprite_list = arcade.SpriteList()
        self.score = 0
        self.game_over = False
        self.spawn_sprites(":resources:images/items/coinGold_ul.png", self.good_sprite_list, 50, width, height, scale=0.5)
        self.spawn_sprites(":resources:images/items/flagRed2.png", self.bad_sprite_list, 50, width, height, scale=0.5)
        self.player_speed = 5

    def spawn_sprites(self, image_path, sprite_list, count, width, height, scale=1.0):
        for _ in range(count):
            sprite = arcade.Sprite(image_path, scale=scale)
            sprite.center_x = random.randint(0, width)
            sprite.center_y = random.randint(0, height)
            sprite.change_x = random.choice([-2, 2])
            sprite.change_y = random.choice([-2, 2])
            sprite_list.append(sprite)

    def on_draw(self):
        arcade.start_render()
        self.player_sprite.draw()
        self.good_sprite_list.draw()
        self.bad_sprite_list.draw()
        arcade.draw_text(f"Score: {self.score}", 10, 10, arcade.color.WHITE, 14)

        if self.game_over:
            arcade.draw_text("Game Over", self.width // 2 - 50, self.height // 2, arcade.color.RED, 20)

    def on_update(self, delta_time):
        if not self.game_over:
            self.player_sprite.update()
            self.good_sprite_list.update()
            self.bad_sprite_list.update()

            for good_sprite in self.good_sprite_list:
                good_sprite.center_x += good_sprite.change_x
                good_sprite.center_y += good_sprite.change_y
                if good_sprite.left < 0 or good_sprite.right > self.width:
                    good_sprite.change_x *= -1
                if good_sprite.bottom < 0 or good_sprite.top > self.height:
                    good_sprite.change_y *= -1

            for bad_sprite in self.bad_sprite_list:
                bad_sprite.center_x += bad_sprite.change_x
                bad_sprite.center_y += bad_sprite.change_y
                if bad_sprite.left < 0 or bad_sprite.right > self.width:
                    bad_sprite.change_x *= -1
                if bad_sprite.bottom < 0 or bad_sprite.top > self.height:
                    bad_sprite.change_y *= -1

            self.check_collisions()

    def on_key_press(self, key, modifiers):
        if not self.game_over:
            if key == arcade.key.LEFT:
                self.player_sprite.change_x = -self.player_speed
            elif key == arcade.key.RIGHT:
                self.player_sprite.change_x = self.player_speed
            elif key == arcade.key.UP:
                self.player_sprite.change_y = self.player_speed
            elif key == arcade.key.DOWN:
                self.player_sprite.change_y = -self.player_speed

    def on_key_release(self, key, modifiers):
        if key in (arcade.key.LEFT, arcade.key.RIGHT):
            self.player_sprite.change_x = 0
        elif key in (arcade.key.UP, arcade.key.DOWN):
            self.player_sprite.change_y = 0

    def check_collisions(self):
        good_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.good_sprite_list)
        for good_sprite in good_hit_list:
            self.score += 1
            good_sprite.remove_from_sprite_lists()

        bad_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.bad_sprite_list)
        for bad_sprite in bad_hit_list:
            self.score -= 1
            bad_sprite.remove_from_sprite_lists()

        if len(self.good_sprite_list) == 0:
            self.game_over = True

def main():
    window = MyGame(800, 600)
    arcade.run()

if __name__ == "__main__":
    main()
