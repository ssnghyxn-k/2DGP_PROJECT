from pico2d import *

class MAP_3:
    def __init__(self):
        self.image = load_image('map_3.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(600, 350)