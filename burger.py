from pico2d import *
import game_world
import random

class Burger:
    burger_sound = None

    def __init__(self):
        self.x, self.y = random.randint(100, 1100), random.randint(10, 590)
        # self.frame = random.randint(0, 7)
        # self.speed = random.uniform(3, 5)
        self.image = load_image('burger.png')
        self.removed = False
        Burger.burger_sound = load_wav('burger.wav')
        Burger.burger_sound.set_volume(30)

    def update(self):
        # self.y -= self.speed
        # self.frame = (self.frame + 1) % 8
        pass

    def draw(self):
        self.image.draw(self.x, self.y)
        #draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self, group, other):
        if self.removed:
            return
        if group == 'boy:burger':
            Burger.burger_sound.play()
            self.removed = True
            game_world.remove_object(self)

