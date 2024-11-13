from pico2d import load_image

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
        if left_down(e) or right_up(e):
            boy.dir_x = -1
            boy.dir_y = 0
        elif right_down(e) or left_up(e):
            boy.dir_x = 1
            boy.dir_y = 0
        elif up_down(e) or down_up(e):
            boy.dir_x = 0
            boy.dir_y = 1
        elif down_down(e) or up_up(e):
            boy.dir_x = 0
            boy.dir_y = -1


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
        self.x, self.y = 1200 // 2, 700 // 2
        self.frame = 0
        self.dir_x = 0
        self.dir_y = 0
        self.action = 3
        self.image = load_image('animation_sheet.png')
        self.state_machine = StateMachine(self)  #Boy's state machine
        self.state_machine.start(Idle) #초기 상태가 Idle
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