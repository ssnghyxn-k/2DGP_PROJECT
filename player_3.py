from pico2d import *

class PLAYER_3:
    def __init__(self):
        self.image = load_image('player_3.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(300, 300)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return 280, 250, 320, 350