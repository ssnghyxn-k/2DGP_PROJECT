
from pico2d import *

class MICROPHONE:
    def __init__(self):
        self.image = load_image('microphone.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(600, 250)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return 580, 230, 620, 270

    def handle_collision(self, group, other):
        if group == 'boy:microphone':
            print('Collide mic')