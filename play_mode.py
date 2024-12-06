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
from player_1 import Player_1
from player_2 import Player_2
from player_3 import Player_3
from manager import Manager
from microphone import MICROPHONE
from s_ball import s_Ball
from drink import Drink
from burger import Burger
from trainer import Trainer

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

    current_scene = 'TR_GROUND'
    previous_scene = current_scene

    boy = Boy()
    game_world.add_object(boy, 1)

    tr_ground = TR_GROUND()
    game_world.add_object(tr_ground, 0)


def finish():
    game_world.clear()


def update_scene():
    global current_scene, previous_scene

    if current_scene == 'TR_GROUND':
        if boy.x < 0:
            current_scene = 'map_4'
        elif boy.x > 1200:
            current_scene = 'map_3'
        elif boy.y > 700:
            current_scene = 'map_2'
        elif boy.y < 0:
            current_scene = 'map_5'

    elif current_scene == 'map_2': # market
         if boy.y < 0:
            current_scene = 'TR_GROUND'
         elif boy.x < 0:
             boy.x = 0
             boy.dir_x = 0
         elif boy.y > 700:
             boy.y = 700
             boy.dir_y = 0
         elif boy.x > 1200:
             boy.x = 1200
             boy.dir_x = 0

    elif current_scene == 'map_3': # stadium
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

    elif current_scene == 'map_4': # training
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
            game_world.add_object(map_2, 0)
            boy.x = 550
            boy.y = 10

        elif current_scene == 'map_3':
            map_3 = MAP_3()
            player_1 = Player_1()
            player_2 = Player_2()
            player_3 = Player_3()
            manager = Manager()
            game_world.add_object(map_3, 0)
            game_world.add_object(player_1, 1)
            game_world.add_object(player_2, 1)
            game_world.add_object(player_3, 1)
            game_world.add_object(manager, 1)
            boy.x = 200
            boy.y = 350


        elif current_scene == 'map_4':
            map_4 = MAP_4()
            game_world.add_object(map_4, 0)
            small_ball = [s_Ball() for i in range(10)]
            for ball in small_ball:
                game_world.add_object(ball, 1)
                game_world.add_collision_pair('boy:small_ball', boy, ball)
            drink = [Drink() for i in range(10)]
            for drinks in drink:
                game_world.add_object(drinks, 1)
                game_world.add_collision_pair('boy:drink', boy, drinks)
            burger = [Burger() for i in range(7)]
            for burgers in burger:
                game_world.add_object(burgers, 1)
                game_world.add_collision_pair('boy:burger', boy, burgers)
            trainer = Trainer()
            game_world.add_object(trainer, 1)
            game_world.add_collision_pair('boy:trainer', boy, trainer)

            boy.x = 800
            boy.y = 50

        elif current_scene == 'map_5':
            map_5 = MAP_5()
            microphone = MICROPHONE()
            game_world.add_object(map_5, 0)
            game_world.add_object(microphone, 1)
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

