from pico2d import *
import game_framework
import play_mode
import game_world

class m_Ball:
    def __init__(self):
        self.x, self.y = play_mode.boy.x, play_mode.boy.y
        self.image = load_image('ball21x21.png')

    def update(self):
        if play_mode.boy.dir_x > 0:        # right
            self.x = play_mode.boy.x + 30
            self.y = play_mode.boy.y - 10
        elif play_mode.boy.dir_x < 0:      # left
            self.x = play_mode.boy.x - 30
            self.y = play_mode.boy.y - 10
        elif play_mode.boy.dir_y > 0:  # up
            self.x = play_mode.boy.x
            self.y = play_mode.boy.y + 30
        elif play_mode.boy.dir_y < 0:      # down
            self.x = play_mode.boy.x
            self.y = play_mode.boy.y - 30

    def draw(self):
        self.image.draw(self.x, self.y)
        #draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self, group, other):
        if group in ['m_ball:player_1', 'm_ball:player_2', 'm_ball:player_3']:
            game_framework.quit()
        elif group == 'm_ball:post':
            play_mode.boy.money += 50
            game_world.remove_object(self)



