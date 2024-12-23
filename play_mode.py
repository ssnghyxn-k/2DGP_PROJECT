import random

from pico2d import *
import game_framework
import game_world
import title_mode

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
from s_ball import s_Ball
from drink import Drink
from burger import Burger
from trainer import Trainer
from m_ball import m_Ball
from post import Post
from dog import Dog
from cat import Cat
from pig import Pig
from sheep import Sheep
from meat import Meat
from hay import Hay
from beef import Beef
from dry_grass import Dry_grass
from ostrich import Ostrich

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
        else:
            boy.handle_event(event)

def init():
    global boy
    global tu_ground
    global current_scene, previous_scene
    global bgm

    bgm = load_music('play_mode.mp3')
    bgm.set_volume(64)
    bgm.repeat_play()

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
        # if 200 <= boy.x <= 300:           #x가 200~300일때
        #     if boy.y > 700:               #위로 가면
        #         current_scene = 'map_2'
        #     elif boy.y < 0:               #아래 가면
        #         current_scene = 'map_5'
        #
        #     if 0 <= boy.y <= 200 and 360 <= boy.y < 700:
        #         if boy.x < 200:
        #             boy.x = 200
        #         elif boy.x < 300:
        #             boy.x = 300
        #
        # elif 0 <= boy.x <= 200 and 300 <= boy.x <= 1200:  #x가 0~200, 300~1200일때
        #     if boy.x < 0:
        #         current_scene = 'map_4' #왼쪽
        #     elif boy.x > 1200:
        #         current_scene = 'map_3' #오른쪽
        #
        #     if boy.y > 360:
        #         boy.y = 360
        #     elif boy.y < 320:
        #         boy.y = 320

        if boy.x < 0:
            current_scene = 'map_4'   # left -> training
        elif boy.x > 1200:
            current_scene = 'map_3'   # right -> stadium
        elif boy.y > 700:
            current_scene = 'map_2'   # top -> market
        elif boy.y < 0:
            current_scene = 'map_5'   # bottom -> field

    elif current_scene == 'map_2': # market
         if 450 < boy.x < 740:
             if boy.y < 0:
                current_scene = 'TR_GROUND'
             elif boy.y > 150:
                 if boy.x < 460:
                     boy.x = 460
                     boy.y = boy.y
                 elif boy.x > 730:
                     boy.x = 730
                     boy.y = boy.y
         else:
             if boy.y < 0:
                boy.y = 0
             elif boy.y > 150:
                boy.y = 150
         if boy.x < 0:
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

    elif current_scene == 'map_5': # field
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
            meat = Meat()
            game_world.add_object(meat, 0)
            game_world.add_collision_pair('boy:meat', boy, meat)
            hay = Hay()
            game_world.add_object(hay, 1)
            game_world.add_collision_pair('boy:hay', boy, hay)
            beef = [Beef() for i in range(5)]
            for beefs in beef:
                game_world.add_object(beefs, 1)
                game_world.add_collision_pair('boy:beef', boy, beefs)
            dry_grass = [Dry_grass() for i in range(5)]
            for dry_grasses in dry_grass:
                game_world.add_object(dry_grasses, 1)
                game_world.add_collision_pair('boy:dry_grass', boy, dry_grasses)
            boy.x = 550
            boy.y = 10

        elif current_scene == 'map_3':
            map_3 = MAP_3()
            player_1 = Player_1()
            player_2 = Player_2()
            player_3 = Player_3()
            manager = Manager()
            m_ball = m_Ball()
            post = Post()
            game_world.add_object(map_3, 0)
            game_world.add_object(player_1, 1)
            game_world.add_object(player_2, 1)
            game_world.add_object(player_3, 1)
            game_world.add_object(manager, 1)
            game_world.add_object(m_ball, 1)
            game_world.add_object(post, 1)
            game_world.add_collision_pair('m_ball:player_1',m_ball, player_1)
            game_world.add_collision_pair('m_ball:player_2',m_ball, player_2)
            game_world.add_collision_pair('m_ball:player_3',m_ball, player_3)
            game_world.add_collision_pair('m_ball:post',m_ball, post)

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
            dog = Dog()
            cat = Cat()
            game_world.add_object(map_5, 0)
            game_world.add_object(dog, 1)
            game_world.add_object(cat, 1)
            game_world.add_collision_pair('boy:dog', boy, dog)
            game_world.add_collision_pair('boy:cat', boy, cat)
            pig = [Pig() for i in range(5)]
            for pigs in pig:
                game_world.add_object(pigs, 1)
                game_world.add_collision_pair('boy:pig', boy, pigs)
            sheep = [Sheep() for i in range(5)]
            for sheeps in sheep:
                game_world.add_object(sheeps, 1)
                game_world.add_collision_pair('boy:sheep', boy, sheeps)
            ostrich = [Ostrich() for i in range(5)]
            for os in ostrich:
                game_world.add_object(os, 1)
                game_world.add_collision_pair('boy:ostrich', boy, os)

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

