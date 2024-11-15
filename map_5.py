from pico2d import *

class MAP_5:
    def __init__(self):
        self.image = load_image('map_5.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(600, 350)