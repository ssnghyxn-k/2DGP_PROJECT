from pico2d import *

import game_world
import play_mode
import random


class Dry_grass:
    def __init__(self):
        self.x, self.y = 650, random.randint(200, 600)
        self.image = load_image('dry_grass.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)
        #draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25

    def handle_collision(self, group, other):
        if group == 'boy:dry_grass' and play_mode.boy.money > 5:
            game_world.remove_object(self)