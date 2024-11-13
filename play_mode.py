import random

from pico2d import *
import game_framework

import game_world
from boy import Boy
from tr_ground import TR_GROUND
from map_2 import MAP_2
from map_3 import MAP_3

# boy = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)

def init():
    global boy
    global tu_ground

    boy = Boy()
    game_world.add_object(boy, 0)

    # tr_ground = TR_GROUND()
    # game_world.add_object(tr_ground, 1)

    # map_2 = MAP_2()
    # game_world.add_object(map_2, 1)
    #
    # map_3 = MAP_3()
    # game_world.add_object(map_3, 1)



def finish():
    game_world.clear()
    pass


def update():
    game_world.update()
    game_world.handle_collisions()


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass

