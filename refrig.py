
from pico2d import *

class REFRIG:
    def __init__(self):
        self.image = load_image('refrig.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(200, 500)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return 100, 400, 300, 600

