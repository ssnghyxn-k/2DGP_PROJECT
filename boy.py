from pico2d import load_image, load_font, draw_rectangle

import game_world
import time
import random
import game_framework
from state_machine import left_up, start_event
from state_machine import right_down
from state_machine import right_up
from state_machine import left_down
from state_machine import StateMachine
from state_machine import up_up, up_down, down_up, down_down, space_down

class Idle:
    @staticmethod
    def enter(boy,e):
        if left_up(e) or right_down(e):
            boy.action = 2
            boy.face_dir = -1
        elif right_up(e) or left_down(e) or start_event(e):
            boy.action = 3
            boy.face_dir = 1

        boy.dir = 0 # 정지 상태
        boy.frame = 0

    @staticmethod
    def exit(boy, e):
        pass

    @staticmethod
    def do(boy):
        boy.frame = 0

    @staticmethod
    def draw(boy):
        c_size = 50
        row = 0
        if boy.dir_x > 0:  # 오른쪽 이동
            row = 560
            boy.image.clip_draw(boy.frame * 210, row, 210, 280, boy.x, boy.y, c_size, c_size)
        elif boy.dir_x < 0:  # 왼쪽 이동
            row = 280
            boy.image.clip_draw(boy.frame * 210, row, 210, 280, boy.x, boy.y, c_size, c_size)
        elif boy.dir_y > 0:  # 위쪽 이동
            row = 0
            boy.image.clip_draw(boy.frame * 210, row, 210, 280, boy.x, boy.y, c_size, c_size)
        elif boy.dir_y < 0:  # 아래쪽 이동
            row = 840
            boy.image.clip_draw(boy.frame * 210, row, 210, 280, boy.x, boy.y, c_size, c_size)
        else:
            boy.image.clip_draw(0, row, 210, 280, boy.x, boy.y, c_size, c_size)


class Run:
    @staticmethod
    def enter(boy,e):
        boy.frame = 0
        if left_down(e):
            boy.dir_x = -1
            boy.dir_y = 0
        elif right_down(e):
            boy.dir_x = 1
            boy.dir_y = 0
        elif up_down(e):
            boy.dir_x = 0
            boy.dir_y = 1
        elif down_down(e):
            boy.dir_x = 0
            boy.dir_y = -1
        elif left_up(e):
            boy.dir_x = 1
            boy.dir_y = 0
        elif right_up(e):
            boy.dir_x = -1
            boy.dir_y = 0
        elif up_up(e):
            boy.dir_x = 0
            boy.dir_y = -1
        elif down_up(e):
            boy.dir_x = 0
            boy.dir_y = 1

    @staticmethod
    def exit(boy,e):
        pass

    @staticmethod
    def do(boy):
        boy.x += boy.dir_x * 5
        boy.y += boy.dir_y * 5
        boy.frame = (boy.frame + 1) % 4

    @staticmethod
    def draw(boy):
        c_size = 50
        row = 0
        if boy.dir_x > 0:  # 오른쪽 이동
            row = 560
            boy.image.clip_draw(boy.frame * 210, row, 210, 280, boy.x, boy.y, c_size, c_size)
        elif boy.dir_x < 0:  # 왼쪽 이동
            row = 280
            boy.image.clip_draw(boy.frame * 210, row, 210, 280, boy.x, boy.y, c_size, c_size)
        elif boy.dir_y > 0:  # 위쪽 이동
            row = 0
            boy.image.clip_draw(boy.frame * 210, row, 210, 280, boy.x, boy.y, c_size, c_size)
        elif boy.dir_y < 0:  # 아래쪽 이동
            row = 840
            boy.image.clip_draw(boy.frame * 210, row, 210, 280, boy.x, boy.y, c_size, c_size)
        else:
            boy.image.clip_draw(0, row, 210, 280, boy.x, boy.y, c_size, c_size)


class Boy:
    def __init__(self):
        self.x, self.y = 600, 350
        self.frame = 0
        self.dir_x = 0
        self.dir_y = 0
        self.action = 3

        self.condition = 50  # 컨디션   --> if 100: level += 1
        self.overall = 50    # OVR 50  --> increase 50: level += 1
        self.level = 1       # LEVEL   --> base
        self.money = 0       # Money   --> buy food for pets
        self.beef_count = 0  # meat count
        self.hay_count = 0   # hay count
        self.heart = 0

        self.font = load_font('ENCR10B.TTF', 20)
        self.image = load_image('animation_sheet.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start(Idle)
        self.state_machine.set_transitions(
            {
                Idle: {right_down: Run, left_down: Run, up_down: Run, down_down: Run,
            right_up: Idle, left_up: Idle, up_up: Idle, down_up: Idle},
                Run: {right_down: Run, left_down: Run, up_down: Run, down_down: Run,
            right_up: Idle, left_up: Idle, up_up: Idle, down_up: Idle}
            }
        )

    def update(self):
        self.state_machine.update() #State machine 시킴
        #self.frame = (self.frame + 1) % 8

    def handle_event(self, event):
        # event: 입력 이벤트
        # 우리가 state machine 전달해 줄건 (  ,  )
        self.state_machine.add_event(('INPUT', event))

    def draw(self):
        self.state_machine.cur_state.draw(self)
        self.font.draw(1000, 680, f'Condition:{self.condition:02d}', (0, 255, 255))
        self.font.draw(10, 680, f'Level:{self.level:02d}', (255, 255, 255))
        self.font.draw(self.x - 10, self.y + 50, f'{self.overall:02d}', (255, 255, 0))
        self.font.draw(1000, 650, f'Money:{self.money:02d}$', (0, 255, 0))
        self.font.draw(1000, 30, f'Heart:{self.heart:01d}', (255, 0, 255))

        #draw_rectangle(*self.get_bb())


    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def draw_text_box(self, text, x=100, y=100, box_width=600, box_height=100):
        draw_rectangle(x, y, x + box_width, y + box_height)  # 대화창 배경
        self.font.draw(x + 20, y + box_height - 20, text, (255, 255, 255))  # 대화 내용

    def handle_collision(self, group, other, event=None):
        current_time = time.time()

        if group == 'boy:small_ball':
            self.overall += 1

        elif group == 'boy:drink' and self.condition < 100:
            self.condition += 10
            while self.condition >= 100:
                self.level += 1
                self.condition = 50

        elif group == 'boy:burger' and self.condition > 10:
            self.condition -= 5
            if self.condition <= 10:
                self.level -= 1
                self.condition = 50

        elif group == 'boy:trainer' and self.condition > 50 and self.money >= 5:
            self.condition -= 5
            self.money -= 5
            self.heart += 1

        elif group == 'boy:player_1':
            pass

        elif group == 'boy:player_2':
            pass

        elif group == 'boy:player_3':
            pass

        elif group == 'boy:manager':
            pass

        elif group == 'boy:dog' and self.beef_count > 0:
            self.beef_count -= 1
            self.heart += 1
            if self.heart >= 10:
                self.level += 1
                self.heart = 0

        elif group == 'boy:cat' and self.beef_count > 0:
            self.beef_count -= 1
            self.heart += 1
            if self.heart >= 10:
                self.level += 1
                self.heart = 0

        elif group == 'boy:pig' and self.hay_count > 0:
            self.hay_count -= 1
            self.heart += 1
            if self.heart >= 10:
                self.level += 1
                self.heart = 0

        elif group == 'boy:sheep' and self.hay_count > 0:
            self.hay_count -= 1
            self.heart += 1
            if self.heart >= 10:
                self.level += 1
                self.heart = 0

        elif group == 'boy:ostrich' and self.hay_count > 0:
            self.hay_count -= 1
            self.heart += 1
            if self.heart >= 10:
                self.level += 1
                self.heart = 0

        elif group == 'boy:meat':
            pass

        elif group == 'boy:hay':
            pass

        elif group == 'boy:beef' and self.money > 5:
            self.money -= 5
            self.beef_count += 1

        elif group == 'boy:dry_grass' and self.money > 5:
            self.money -= 5
            self.hay_count += 1
