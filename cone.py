
from pico2d import *

class CONE:
    def __init__(self):
        self.image = load_image('cone.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(150, 80)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return 100, 40, 200, 120