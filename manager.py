
from pico2d import *

class MANAGER:
    def __init__(self):
        self.image = load_image('manager.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(900, 150)