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
from bed import BED
from refrig import REFRIG
from goal_post import GOAL_POST
from player_1 import PLAYER_1
from player_2 import PLAYER_2
from player_3 import PLAYER_3
from manager import MANAGER
from cone import CONE
from fitness_ball import FITNESS_BALL
from trainer_1 import TRAINER_1

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
    global boy, bed, refrig
    global tu_ground
    global current_scene, previous_scene

    current_scene = 'TR_GROUND'
    previous_scene = current_scene

    boy = Boy()
    game_world.add_object(boy, 1)

    tr_ground = TR_GROUND()
    game_world.add_object(tr_ground, 0)

    bed = BED()
    game_world.add_collision_pair('boy:bed', boy, bed)

    refrig = REFRIG()
    game_world.add_collision_pair('boy:refrig', boy, refrig)



def finish():
    game_world.clear()


def update_scene():
    global current_scene, previous_scene

    if current_scene == 'TR_GROUND':
        if boy.x < 0:
            current_scene = 'map_2'
        elif boy.x > 1200:
            current_scene = 'map_3'
        elif boy.y > 700:
            current_scene = 'map_4'
        elif boy.y < 0:
            current_scene = 'map_5'

    elif current_scene == 'map_2':
         if boy.x > 1200:
            current_scene = 'TR_GROUND'
         elif boy.x < 0:
             boy.x = 0
             boy.dir_x = 0
         elif boy.y > 380:
             boy.y = 380
             boy.dir_y = 0
         elif boy.y < 0:
             boy.y = 0
             boy.dir_y = 0

    elif current_scene == 'map_3':
         if boy.x < 0:
            current_scene = 'TR_GROUND'
         elif boy.x > 1200:
             boy.x = 1200
             boy.dir_x = 0
         elif boy.y > 700:
             boy.y = 700
             boy.dir_y = 0
         elif boy.y < 0:
             boy.y = 0
             boy.dir_y = 0

    elif current_scene == 'map_4':
        if boy.y < 0:
            current_scene = 'TR_GROUND'
        elif boy.y > 700:
            boy.y = 700
            boy.dir_y = 0
        elif boy.x < 0:
            boy.x = 0
            boy.dir_x = 0
        elif boy.x > 1200:
            boy.x =1200
            boy.dir_x = 0

    elif current_scene == 'map_5':
        if boy.y > 700:
            current_scene = 'TR_GROUND'
        elif boy.y < 0:
            boy.y = 0
            boy.dir_y = 0
        elif boy.x < 0:
            boy.x = 0
            boy.dir_x = 0
        elif boy.x > 1200:
            boy.x = 1200
            boy.dir_x = 0


    if previous_scene != current_scene:
        game_world.clear()
        if current_scene == 'TR_GROUND':
            tr_ground = TR_GROUND()
            game_world.add_object(tr_ground, 0)
            boy.x = 400
            boy.y = 350

        elif current_scene == 'map_2':
            map_2 = MAP_2()
            bed = BED()
            refrig = REFRIG()
            game_world.add_object(map_2, 0)
            game_world.add_object(bed, 1)
            game_world.add_object(refrig, 1)
            boy.x = 1100
            boy.y = 100

        elif current_scene == 'map_3':
            map_3 = MAP_3()
            goal_post = GOAL_POST()
            player_1 = PLAYER_1()
            player_2 = PLAYER_2()
            player_3 = PLAYER_3()
            manager = MANAGER()
            game_world.add_object(map_3, 0)
            game_world.add_object(goal_post, 1)
            game_world.add_object(player_1, 1)
            game_world.add_object(player_2, 1)
            game_world.add_object(player_3, 1)
            game_world.add_object(manager, 1)
            boy.x = 600
            boy.y = 20


        elif current_scene == 'map_4':
            map_4 = MAP_4()
            cone = CONE()
            fitness_ball = FITNESS_BALL()
            trainer_1 = TRAINER_1()
            game_world.add_object(map_4, 0)
            game_world.add_object(cone, 1)
            game_world.add_object(fitness_ball, 1)
            game_world.add_object(trainer_1, 1)
            boy.x = 800
            boy.y = 50

        elif current_scene == 'map_5':
            map_5 = MAP_5()
            game_world.add_object(map_5, 0)
            boy.x = 600
            boy.y = 350


        game_world.add_object(boy, 1)
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

