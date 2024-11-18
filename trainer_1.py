
from pico2d import *

class TRAINER_1:
    def __init__(self):
        self.image = load_image('trainer_1.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(1000, 100)