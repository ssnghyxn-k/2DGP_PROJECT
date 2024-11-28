from pico2d import *
import game_framework
import game_world
import play_mode
from boy import Boy
from small_ball import SMALL_BALL

score = 0

def init():
    global boy, small_ball

    boy = Boy()
    game_world.add_object(boy, 1)

    small_ball = SMALL_BALL()
    game_world.add_object(small_ball, 1)

def finish():
    game_world.clear()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(play_mode)
        else:
            boy.handle_event(event)

def update():
    game_world.update()
    game_world.handle_collisions()

def handle_collision(self, group, other):
    global score
    if group == 'boy:small_ball':
        score += 10
        game_world.remove_object(other)


def draw_text(text, x, y, font_size = 20, color = (255, 255, 255)):
    font = load_font('ENCR10B.TTF', font_size)
    font.draw(x, y, text, color)

def draw():
    clear_canvas()
    game_world.render()
    draw_text(f"Score: {score}", 50, 550, 30, (255, 255, 255))  # Display score
    update_canvas()

def pause():
    pass

def resume():
    pass