
from pico2d import *

class CONE:
    def __init__(self):
        self.image = load_image('cone.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(1000, 100)