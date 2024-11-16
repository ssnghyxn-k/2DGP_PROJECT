
from pico2d import *

class GOAL_POST:
    def __init__(self):
        self.image = load_image('goal_post.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(1100, 350)