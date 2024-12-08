from pico2d import *

class Hay:
    def __init__(self):
        self.x, self.y = 940, 200
        self.image = load_image('hay.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)
        #draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def handle_collision(self, group, other):
        if group == 'boy:hay':
            pass