from pico2d import *

class TR_GROUND:
    def __init__(self):
        self.image = load_image('TR_GROUND.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(600, 350)