world = [[] for _ in range(10)]

def add_object(o, depth = 0):
    world[depth].append(o)

def add_objects(ol, depth = 0):
    world[depth] += ol


def update():
    for layer in world:
        for o in layer:
            o.update()


def render():
    for layer in world:
        for o in layer:
            o.draw()

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            remove_collision_object(o)
            del o
            return
    print(f"Warning: Attempted to remove non-existing object: {o}")


def clear():
    for layer in world:
        for o in layer[:]:
            remove_object(o)
    collision_pairs.clear()

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

collision_pairs = {}

def add_collision_pair(group, a, b):
    if group not in collision_pairs:
        print(f'Added new group {group}')
        collision_pairs[group] = [ [], [] ]
    if a:
        collision_pairs[group][0].append(a)
    if b:
        collision_pairs[group][1].append(b)

def remove_collision_object(o):
    for pairs in collision_pairs.values():
        if o in pairs[0]:
            pairs[0].remove(o)
        if o in pairs[1]:
            pairs[1].remove(o)


def handle_collisions():
    processed_collisions = set()
    for group, pairs in list(collision_pairs.items()):
        for a in pairs[0]:
            for b in pairs[1]:
                if a == b:
                    continue
                if (a, b) in processed_collisions or (b, a) in processed_collisions:
                    continue  # 중복 충돌 방지
                if collide(a, b):
                    a.handle_collision(group, b)
                    b.handle_collision(group, a)
                    processed_collisions.add((a,b))
