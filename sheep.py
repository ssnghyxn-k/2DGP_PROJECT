from pico2d import *
import random


def randomize_state():
    states = ["walk_down", "walk_right", "walk_up", "walk_left"]
    return random.choice(states)


class Sheep:
    def __init__(self):
        self.x, self.y = random.randint(100,1100), random.randint(100,600)
        self.frame = 0
        self.dir = 3
        self.state = randomize_state()
        self.image = load_image('sheep.png')
        self.last_update_time = 0
        self.frame_interval = 0.2
        self.last_direction_change_time = 0  # 방향 변경 시간
        self.direction_change_interval = 1  # 방향 변경 간격 (초)
        self.state_change_interval = 1  # 상태 변경 간격 (초)
        self.last_state_change_time = 0  # 마지막 상태 변경 시간

    def update(self):
        current_time = get_time()

        frame_interval = self.frame_interval
        if current_time - self.last_update_time >= frame_interval:
            self.last_update_time = current_time
            self.frame = (self.frame + 1) % 4

            #print(f"Current sheep state: {self.state}")

        # 상태 변경
        if current_time - self.last_state_change_time >= self.state_change_interval:
            self.last_state_change_time = current_time
            self.state = randomize_state()

        if self.state == "walk_down":
            self.dir = 4
            self.move()
        elif self.state == "walk_right":
            self.dir = 3
            self.move()
        elif self.state == "walk_up":
            self.dir = 2
            self.move()
        elif self.state == "walk_left":
            self.dir = 1
            self.move()


    def move(self):
        if self.dir == 4:   # down
            self.y -= 1
            if self.y < 100:
                self.y = 100
        elif self.dir == 3: # right
            self.x += 1
            if self.x > 1100:
                self.x = 1100
        elif self.dir == 2: # up
            self.y += 1
            if self.y > 600:
                self.y = 600
        elif self.dir == 1: #left
            self.x -= 1
            if self.x < 100:
                self.x = 100

    def get_bb(self):
        return self.x - 16, self.y - 16, self.x + 16, self.y + 16

    def draw(self):
        if self.state == "walk_down":
            self.image.clip_draw(self.frame * 64, self.dir * 64, 64, 64, self.x, self.y)
        elif self.state == "walk_right":
            self.image.clip_draw(self.frame * 64, self.dir * 64, 64, 64, self.x, self.y)
        elif self.state == "walk_up":
            self.image.clip_draw(self.frame * 64, self.dir * 64, 64, 64, self.x, self.y)
        elif self.state == "walk_left":
            self.image.clip_composite_draw(self.frame * 64, 3 * 64, 64, 64, 0.0, 'h', self.x, self.y, 64, 64)
        draw_rectangle(*self.get_bb())

    def handle_collision(self, group, other):
        pass