
from pico2d import *

class MANAGER:
    def __init__(self):
        self.image = load_image('manager.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(900, 150)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return 870, 100, 930, 200