from pico2d import *
import random

class s_Ball:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 599
        self.frame = random.randint(0, 7)
        self.speed = random.uniform(3, 10)
        self.image = load_image('ball21x21.png')

    def update(self):
        if self.y > 50:
            self.y -= self.speed
        else:
            self.y = 50
        self.frame = (self.frame + 1) % 8

    def draw(self):
        self.image.draw(self.x, self.y)