from pico2d import *
import play_mode
import game_world

class Trainer:
    trainer_sound = None

    def __init__(self):
        self.x, self.y = 600, 350
        self.frame = 0
        self.dir = 2
        self.image = load_image('h_trainer.png')
        Trainer.trainer_sound = load_wav('trainer.wav')
        Trainer.trainer_sound.set_volume(30)

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
            self.x += dx / distance * 3
            self.y += dy / distance * 3

        self.frame = (self.frame + 1) % 4

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def draw(self):
        # clip_draw(x, y, w, h, cx, cy)
        self.image.clip_draw(self.frame * 64, self.dir * 64, 64, 64, self.x, self.y)
        #draw_rectangle(*self.get_bb())

    def handle_collision(self, group, other):
        if group == 'boy:trainer':
            Trainer.trainer_sound.play()
            game_world.remove_object(self)