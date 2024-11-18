from pico2d import *

class PLAYER_2:
    def __init__(self):
        self.image = load_image('player_2.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(900, 300)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return 880, 250, 920, 350