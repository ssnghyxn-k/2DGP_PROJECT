from pico2d import *
import game_world
import random

class Drink:
    def __init__(self):
        self.x, self.y = random.randint(100, 1100), random.randint(10, 590)
        # self.frame = random.randint(0, 7)
        # self.speed = random.uniform(3, 5)
        self.image = load_image('drink.png')

    def update(self):
        # self.y -= self.speed
        # self.frame = (self.frame + 1) % 8
        pass

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self, group, other):
        if group == 'boy:drink':
            game_world.remove_object(self)

