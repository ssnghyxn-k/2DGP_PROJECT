from pico2d import *
import random

class Dog:
    def __init__(self):
        self.x, self.y = 600, 500
        self.frame = 0
        self.dir = 0
        self.state = "sleep"
        self.image = load_image('dog.png')
        self.last_update_time = 0  # 애니메이션 업데이트 시간
        self.frame_interval = 0.2  # 애니메이션 프레임 갱신 간격
        self.sleep_frame_interval = 0.5
        self.run_frame_interval = 0.1
        self.last_direction_change_time = 0  # 방향 변경 시간
        self.direction_change_interval = 1  # 방향 변경 간격 (초)
        self.state_change_interval = 3  # 상태 변경 간격 (초)
        self.last_state_change_time = 0  # 마지막 상태 변경 시간

    def update(self):
        current_time = get_time()

        if self.state == "sleep":
            frame_interval = self.sleep_frame_interval
        elif self.state == "run":
            frame_interval = self.run_frame_interval
        else:
            frame_interval = self.frame_interval

        if current_time - self.last_update_time >= frame_interval:
            self.last_update_time = current_time
            if self.state == "sleep":
                self.frame = (self.frame + 1) % 2
            elif self.state == "run":
                self.frame = (self.frame + 1) % 3
            else:
                self.frame = (self.frame + 1) % 4

            print(f"Current state: {self.state}")

        # 상태 변경
        if current_time - self.last_state_change_time >= self.state_change_interval:
            self.last_state_change_time = current_time
            self.randomize_state()

        if self.state == "idle":
            self.dir = 4
        elif self.state == "walk_down":
            self.dir = 8
            self.move()
        elif self.state == "walk_right":
            self.dir = 7
            self.move()
        elif self.state == "walk_up":
            self.dir = 6
            self.move()
        elif self.state == "walk_left":
            self.dir = 5
            self.move()
        elif self.state == "sit":
            self.dir = 3
        elif self.state == "pant":
            self.dir = 2
        elif self.state == "sleep":
            self.dir = 1
        elif self.state == "run":
            self.dir = 0
            self.move()

    def move(self):
        if self.dir == 8:   # down
            self.y -= 2
            if self.y < 100:
                self.y = 100
        elif self.dir == 7: # right
            self.x += 2
            if self.x > 1100:
                self.x = 1100
        elif self.dir == 6: # up
            self.y += 2
            if self.y > 600:
                self.y = 600
        elif self.dir == 5: #left
            self.x -= 2
            if self.x < 100:
                self.x = 100
        elif self.dir == 4:
            self.x = self.x
            self.y = self.y
        elif self.dir == 3:
            self.x = self.x
            self.y = self.y
        elif self.dir == 2:
            self.x = self.x
            self.y = self.y
        elif self.dir == 1:
            self.x = self.x
            self.y = self.y
        elif self.dir == 0:
            self.x += 2
            if self.x > 1100:
                self.x = 1100

    def randomize_state(self):
        states = ["idle", "walk_down", "walk_right", "walk_up", "walk_left", "sit", "pant", "sleep", "run"]
        self.state = random.choice(states)

    def get_bb(self):
        return self.x - 16, self.y - 16, self.x + 16, self.y + 16

    def draw(self):
        if self.state == "walk_down":
            self.image.clip_draw(self.frame * 32, self.dir * 32, 32, 32, self.x, self.y)
        elif self.state == "walk_right":
            self.image.clip_draw(self.frame * 32, self.dir * 32, 32, 32, self.x, self.y)
        elif self.state == "walk_up":
            self.image.clip_draw(self.frame * 32, self.dir * 32, 32, 32, self.x, self.y)
        elif self.state == "walk_left":
            self.image.clip_draw(self.frame * 32, self.dir * 32, 32, 32, self.x, self.y)
        elif self.state == "sit":
            self.image.clip_draw(self.frame * 32, self.dir * 32, 32, 32, self.x, self.y)
        elif self.state == "pant":
            self.image.clip_draw(self.frame * 32, self.dir * 32, 32, 32, self.x, self.y)
        elif self.state == "sleep":
            if self.frame == 0:
                self.image.clip_draw(self.frame * 32, self.dir * 32, 32, 32, self.x, self.y)
            elif self.frame == 1:
                self.image.clip_draw(self.frame * 32, self.dir * 32, 32, 32, self.x, self.y)
        elif self.state == "run":
            if self.frame == 0:
                self.image.clip_draw(self.frame * 32, self.dir * 32, 32, 32, self.x, self.y)
            elif self.frame == 1:
                self.image.clip_draw(self.frame * 32, self.dir * 32, 32, 32, self.x, self.y)
            elif self.frame == 2:
                self.image.clip_draw(self.frame * 64, self.dir * 64, 64, 64, self.x, self.y)
        elif self.state == "idle":
            self.image.clip_draw(self.frame * 32, self.dir * 32, 32, 32, self.x, self.y)

        draw_rectangle(*self.get_bb())

    def handle_collision(self, group, other):
        pass