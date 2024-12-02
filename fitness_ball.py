
from pico2d import *

class FITNESS_BALL:
    def __init__(self):
        self.image = load_image('fitness_ball.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(110, 420)
        # draw_rectangle(*self.get_bb())

    def get_bb(self):
        return 70, 380, 150, 460

    def handle_collision(self, group, other):
        if group == 'boy:fitness_ball':
            print('Collide fitness_ball')

