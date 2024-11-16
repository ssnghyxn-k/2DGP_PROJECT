
from pico2d import *

class FITNESS_BALL:
    def __init__(self):
        self.image = load_image('fitness_ball.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(600, 600)