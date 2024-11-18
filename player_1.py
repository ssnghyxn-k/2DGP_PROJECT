from pico2d import *

class PLAYER_1:
    def __init__(self):
        self.image = load_image('player_1.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(300, 150)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return 280, 100, 320, 200