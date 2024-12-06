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
from state_machine import up_up, up_down, down_up, down_down

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
        boy.x += boy.dir_x * 8
        boy.y += boy.dir_y * 8
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
        self.x, self.y = 300, 300
        self.frame = 0
        self.dir_x = 0
        self.dir_y = 0
        self.action = 3
        self.condition = 50  # 컨디션
        self.hunger = 50     # 허기짐
        self.overall = 50    # OVR 50
        self.level = 1       # LEVEL
        self.ball_count = 0
        self.last_collision_time = 0
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
        self.font.draw(1000, 650, f'Hunger:{self.hunger:02d}', (255, 255, 0))
        self.font.draw(10, 680, f'Level:{self.level:02d}', (255, 255, 255))
        self.font.draw(self.x - 10, self.y + 50, f'{self.overall:02d}', (255, 255, 0))
        draw_rectangle(*self.get_bb())


    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def draw_text_box(self, text, x=100, y=100, box_width=600, box_height=100):
        draw_rectangle(x, y, x + box_width, y + box_height)  # 대화창 배경
        self.font.draw(x + 20, y + box_height - 20, text, (255, 255, 255))  # 대화 내용

    def handle_collision(self, group, other):
        current_time = time.time()

        if group == 'boy:bed'and (current_time - self.last_collision_time > 600):  # 게임 시간 10분마다 취침 가능
            self.condition += random.randint(20,30)
            self.font.draw(1000, 680, f'Condition:{self.condition:02d}', (0, 255, 255))
            self.last_collision_time = current_time

        elif group == 'boy:refrig' and (current_time - self.last_collision_time > 300):  # 게임 시간 5분 마다 식사 가능
            self.hunger += random.randint(20,30)
            self.font.draw(1000, 650, f'Hunger:{self.hunger:02d}', (255, 255, 0))
            self.last_collision_time = current_time

        elif group == 'boy:small_ball':
            self.overall += 1

        elif group == 'boy:drink' and self.condition < 100:
            self.condition += 10
            while self.condition >= 100:
                self.level += 1
                self.condition = 50

        elif group == 'boy:burger':
            self.condition -= 5
            # if self.condition >= 100:
            #     self.level += 1
            #     self.condition = 50

        elif group == 'boy:trainer':
            pass

        elif group == 'boy:player_1':
            pass

        elif group == 'boy:player_2':
            pass

        elif group == 'boy:player_3':
            pass

        elif group == 'boy:microphone':
            pass



