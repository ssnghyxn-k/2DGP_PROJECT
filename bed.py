
from pico2d import *

class BED:
    def __init__(self):
        self.image = load_image('bed.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(950, 550)