from pico2d import *

class MAP_3:
    def __init__(self):
        self.image = load_image('map_3.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(600, 350)
        #draw_rectangle(*self.get_bb())

    # def get_bb(self):
    #     return 1120, 340, 1180, 450