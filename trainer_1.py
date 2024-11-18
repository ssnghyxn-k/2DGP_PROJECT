
from pico2d import *

class TRAINER_1:
    def __init__(self):
        self.image = load_image('trainer_1.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(1000, 100)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return 920, 20, 1080, 180

    def handle_collision(self, group, other):
        if group == 'boy:trainer_1':
            print('Collide trainer_1')