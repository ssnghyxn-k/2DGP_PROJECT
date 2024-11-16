from pico2d import *

class PLAYER_3:
    def __init__(self):
        self.image = load_image('player_3.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 600)