from pico2d import *

class MAP_2:
    def __init__(self):
        self.image = load_image('map_2.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(600, 350)