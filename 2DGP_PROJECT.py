from pico2d import *

open_canvas(1200,700)
character = load_image('animation_sheet.png')
ground = load_image('TR_GROUND.png')

def handle_events():
    global running
    global dir_x
    global dir_y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
            elif event.key == SDLK_LEFT:
                dir_x -= 1
            elif event.key == SDLK_UP:
                dir_y += 1
            elif event.key == SDLK_DOWN:
                dir_y -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                dir_x += 1
            elif event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1

running = True
x = 1200 // 2
y = 700 // 2
frame = 0
facing_right = True
dir_x = 0
dir_y = 0
row = 0

while running:
    clear_canvas()
    ground.draw(400,300)
    c_size = 50
    if dir_x > 0:  # 오른쪽 이동
        row = 560
        character.clip_draw(frame * 210, row, 210, 280, x, y, c_size, c_size)
    elif dir_x < 0:  # 왼쪽 이동
        row = 280
        character.clip_draw(frame * 210, row, 210, 280, x, y, c_size, c_size)
    elif dir_y > 0:  # 위쪽 이동
        row = 0
        character.clip_draw(frame * 210, row, 210, 280, x, y, c_size, c_size)
    elif dir_y < 0:  # 아래쪽 이동
        row = 840
        character.clip_draw(frame * 210, row, 210, 280, x, y, c_size, c_size)

    if dir_x != 0 or dir_y != 0:
        character.clip_draw(frame * 210, row, 210, 280, x, y, c_size, c_size)
        frame = (frame + 1) % 4
    else:
        character.clip_draw(0, row, 210, 280, x, y, c_size, c_size)

    update_canvas()
    handle_events()
    x += dir_x * 10
    y += dir_y * 10
    delay(0.05)

close_canvas()