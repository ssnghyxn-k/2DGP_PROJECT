import random

from pico2d import *
import game_framework

import game_world
from boy import Boy
from tr_ground import TR_GROUND
from map_2 import MAP_2
from map_3 import MAP_3
from map_4 import MAP_4
from map_5 import MAP_5


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
    global current_scene, previous_scene

    current_scene = 'TR_GROUND.png'
    previous_scene = current_scene

    boy = Boy()
    game_world.add_object(boy, 1)

    tr_ground = TR_GROUND()
    game_world.add_object(tr_ground, 0)


def finish():
    game_world.clear()


def update_scene():
    global current_scene, previous_scene

    if boy.x > 1200:
        current_scene = 'map_3'
    elif boy.x < 0:
        current_scene = 'map_2'
    elif boy.y > 700:
        current_scene = 'map_4'
    elif boy.y < 0:
        current_scene = 'map_5'


    if previous_scene != current_scene:
        #print(f"DEBUG: Switching scene from {previous_scene} to {current_scene}")
        game_world.clear()
        if current_scene == 'TR_GROUND':
            tr_ground = TR_GROUND()
            game_world.add_object(tr_ground, 0)
            boy.x = 600
            boy.y = 350

        elif current_scene == 'map_2':
            map_2 = MAP_2()
            game_world.add_object(map_2, 0)
            boy.x = 600
            boy.y = 350

        elif current_scene == 'map_3':
            map_3 = MAP_3()
            game_world.add_object(map_3, 0)
            boy.x = 600
            boy.y = 350

        elif current_scene == 'map_4':
            map_4 = MAP_4()
            game_world.add_object(map_4, 0)
            boy.x = 600
            boy.y = 350

        elif current_scene == 'map_5':
            map_5 = MAP_5()
            game_world.add_object(map_5, 0)
            boy.x = 600
            boy.y = 350

        game_world.add_object(boy, 1)
        boy.y = 700 // 2
        previous_scene = current_scene


def update():
    game_world.update()
    update_scene()
    game_world.handle_collisions()


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass

