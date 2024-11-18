
from pico2d import *

class BED:
    def __init__(self):
        self.image = load_image('bed.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(950, 500)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return 850, 400, 1050, 600