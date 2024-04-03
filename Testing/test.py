import arcade
import time

class CountdownTimer(arcade.Window):
    def __init__(self, width, height, title, countdown_duration):
        super().__init__(width, height, title)
        self.countdown_duration = countdown_duration
        self.timer_text = f"Time left: {self.countdown_duration:.1f}"
        self.start_time = time.time()

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(self.timer_text, 10, self.height - 30, arcade.color.WHITE, 20)

    def update(self, delta_time):
        elapsed_time = time.time() - self.start_time
        time_left = max(0, self.countdown_duration - elapsed_time)
        self.timer_text = f"Time left: {time_left:.1f}"
        if time_left <= 0:
            self.timer_text = "Time's up!"

if __name__ == "__main__":
    countdown_duration = 60  # Set the countdown duration in seconds
    window = CountdownTimer(800, 600, "Countdown Timer Example", countdown_duration)
    arcade.run()
#crank
