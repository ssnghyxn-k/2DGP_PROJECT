from pico2d import *

class Post:
    def __init__(self):
        pass

    def update(self):
        pass

    def draw(self):
        #draw_rectangle(*self.get_bb())
        pass

    def get_bb(self):
        return 1120, 340, 1180, 450

    def handle_collision(self, group, other):
        if group == 'm_ball:post':
            pass