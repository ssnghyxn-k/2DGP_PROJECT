from pico2d import *
import play_mode

class Player_2:
    def __init__(self):
        self.x, self.y = 700, 400
        self.frame = 0
        self.dir = 2
        self.image = load_image('player_2.png')

    def update(self):
        if play_mode.boy.x > self.x:
            self.dir = 1  # 오른쪽
        elif play_mode.boy.x < self.x:
            self.dir = 2  # 왼쪽
        elif play_mode.boy.y > self.y:
            self.dir = 3  # 위
        elif play_mode.boy.y < self.y:
            self.dir = 0  # 아래

        dx, dy = play_mode.boy.x - self.x, play_mode.boy.y - self.y
        distance = (dx ** 2 + dy ** 2) ** 0.5
        if distance > 0:
            self.x += dx / distance * 2.5
            self.y += dy / distance * 2.5

        self.frame = (self.frame + 1) % 4

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def draw(self):
        # clip_draw(x, y, w, h, cx, cy)
        self.image.clip_draw(self.frame * 64, self.dir * 64, 64, 64, self.x, self.y)
        #draw_rectangle(*self.get_bb())

    def handle_collision(self, group, other):
        if group == 'm_ball:player_2':
            pass