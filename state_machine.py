#이벤트 체크 함수 정의
#상태 이벤트 e = (종류, 실제값) 튜플로 정의
from sdl2 import SDLK_SPACE, SDL_KEYDOWN, SDLK_RIGHT, SDLK_LEFT, SDL_KEYUP, SDLK_UP, SDLK_DOWN


def start_event(e):
    return e[0] == 'START'

def right_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RIGHT

def right_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_RIGHT

def left_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LEFT

def left_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_LEFT

def up_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_UP

def up_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_UP

def down_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_DOWN

def down_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_DOWN

def space_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE



class StateMachine:
    def __init__(self, obj):
        self.obj = obj # 어떤 객체를 위한 상태 머신인지 알려줌, onj = boy.self
        self.event_q = [] # 상태 이벤트를 보관할 큐
        pass

    def start(self, state):
        self.cur_state = state # 시작 상태를 받아서, 그걸로 현재 상태를 정의
        self.cur_state.enter(self.obj, ('START', 0))
        print(f'Enter into {state}')
        pass

    def update(self):
        self.cur_state.do(self.obj) # Idle.do()
        # 혹시 event가 있나?
        if self.event_q:
            e = self.event_q.pop(0)
            for check_event, next_state in self.transitions[self.cur_state].items():
                if check_event(e):
                    print(f'Exit from {self.cur_state}')
                    self.cur_state.exit(self.obj, e)
                    self.cur_state = next_state
                    print(f'Enter into {next_state}')
                    self.cur_state.enter(self.obj, e) # 상태 변환의 이우를 명확히 알려줘
                    return  # 제대로 이벤트에 따른 상태 변환 완료
            # 이 시점으로 왔다는 것은 event에 따른 전환 실패
            print(f'        WARNING: {e} not handled at state {self.cur_state}')


    def draw(self):
        self.cur_state.draw(self.obj)

    def add_event(self, e):
        print(f'    DEBUG: add event {e}')
        self.event_q.append(e)

    def set_transitions(self, transitions):
        self.transitions = transitions
