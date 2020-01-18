import pygame
from random import randint
import os
from socket import *
from multiprocessing import Process, Queue
import signal
import glob


# region classes
class OtherSet_Actions(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, sprite=None):
        super().__init__()
        self.x = x
        self.y = y
        self.sprite = sprite
        self.rect = pygame.Rect((x, y), (x + 19, y + 25))

    def show(self, pos=(0, 0)):
        screen.blit(self.sprite, pos)


class Monsters(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()


class Obstacle:
    def __init__(self, anchor_x=0, anchor_y=0):
        self.anchor_x = anchor_x
        self.anchor_y = anchor_y


# endregion

# region Set_Action

class MyGroup(pygame.sprite.Group):
    def __init__(self, *sprites, name='ANONYMOUS', x=0, y=0, speed=0.0):
        super().__init__(*sprites)
        self.name = name
        self.x = x
        self.y = y
        self.speed = speed
        self.left_speed = 0
        self.right_speed = 0
        self.up_speed = 0
        self.down_speed = 0

    def update(self, *args):
        for i in self.sprites():
            screen.blit(pygame.transform.scale(i.image, (i.image.get_rect().size[0],
                                                            i.image.get_rect().size[1])), (self.x, self.y))

    # region movement_ctrl
    def move_left(self):
        if self.right_speed != 0:
            self.right_speed = 0
        self.left_speed = -self.speed

    def move_right(self):
        if self.left_speed != 0:
            self.left_speed = 0
        self.right_speed = self.speed

    def move_up(self):
        if self.down_speed != 0:
            self.down_speed = 0
        self.up_speed = -self.speed

    def move_down(self):
        if self.up_speed != 0:
            self.up_speed = 0
        self.down_speed = self.speed

    # endregion

    # region attack_ctrl
    def attack(self):
        self.isattack = True

    def stop_attack(self):
        self.isattack = False
    # endregion

class MySprite(pygame.sprite.Sprite):
    def __init__(self, action):
        super().__init__()
        self.groups()
        self.ims = glob.glob(f'{abs_path}Assets/Sprite/nekochan01/{action}*.png')
        self.index = 0
        self.image = pygame.image.load(self.ims[self.index])
        self.images = [pygame.image.load(img) for img in glob.glob(f'{abs_path}Assets/Sprite/nekochan01/{action}*.png')]

    def update(self):
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        if len(self.images) > 1:
            self.index += 1


class Set_Action(pygame.sprite.Sprite):
    def __init__(self, action, name='ANONYMOUS', x=0, y=0, speed=0.0):
        super().__init__()
        self.name = name
        self.x = x
        self.y = y
        self.speed = speed
        self.left_speed = 0
        self.right_speed = 0
        self.up_speed = 0
        self.down_speed = 0
        self.fwd = glob.glob(f'{abs_path}Assets/Sprite/nekochan01/{action}*.png')
        self.index = len(self.fwd) - 1
        self.image = pygame.image.load(self.fwd[self.index])
        self.images = [pygame.image.load(img) for img in
                       glob.glob(f'{abs_path}Assets/Sprite/nekochan01/{action}*.png')]

        self.rect = pygame.Rect((x, y), (x + 19, y + 25))
        self.isattack = False

    def update(self):
        if self.index < 0:
            self.index = len(self.images) - 2
        self.image = self.images[self.index]
        if len(self.images) > 1:
            self.index -= 1
        screen.blit(self.image, (self.x, self.y))
        self.x += (self.right_speed + self.left_speed)
        self.y += (self.down_speed + self.up_speed)

    def move_left(self):
        if self.right_speed != 0:
            self.right_speed = 0
        self.left_speed = -self.speed

    def move_right(self):
        if self.left_speed != 0:
            self.left_speed = 0
        self.right_speed = self.speed

    def move_up(self):
        if self.down_speed != 0:
            self.down_speed = 0
        self.up_speed = -self.speed

    def move_down(self):
        if self.up_speed != 0:
            self.up_speed = 0
        self.down_speed = self.speed

    def attack(self):
        self.isattack = True

    def stop_attack(self):
        self.isattack = False


def action(action, name, x, y, speed):
    p_action = Set_Action(action, name, x, y, speed)
    my_group = pygame.sprite.Group(p_action)
    return my_group


# endregion

# region find absolute path
path_e = os.path.abspath('./combat_scene.py').split('/')[0:-2]
abs_path = '/'.join(path_e) + '/'
# endregion

# region initiate pygame
pygame.init()
screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)
# endregion

# region load resources
font_01 = pygame.font.Font(f'{abs_path}/Assets/Fonts/Cosima-DemoBold.otf', 23)
font_02 = pygame.font.Font(f'{abs_path}/Assets/Fonts/Cosima-DemoBold.otf', 15)
font_03 = pygame.font.Font(f'{abs_path}/Assets/Fonts/Cosima-DemoBold.otf', 10)
pygame.display.set_caption('Diamond Warrior')
icon_img = pygame.image.load(f'{abs_path}/Assets/Sprite/Decor/icon.png')
pygame.display.set_icon(icon_img)
tree = pygame.image.load(f'{abs_path}/Assets/Sprite/Decor/tree01.png')
gpath_list = glob.glob(fr'{abs_path}/Assets/Sprite/Decor/grass0?.png')
map_sprite_list = []
for i in gpath_list:
    map_sprite_list.append(pygame.image.load(i))

o_i = pygame.image.load(f'{abs_path}/Assets/Sprite/nekochan02/idle.png')
# endregion

# region map_generator
map_list = []

for y in range(0, screen_size[1] // 32 + 1):
    row_list = []
    for x in range(0, screen_size[0] // 32 + 1):
        row_list.append(randint(0, len(map_sprite_list) - 1))
    map_list.append(row_list)

tree_pos_list = []
for n in range(1, 10):
    x = randint(0, len(map_list[0]) * 32)
    y = randint(0, len(map_list) * 32)
    tree_pos_list.append((x, y))


def generate_map(map_l):
    for y in range(len(map_l)):
        for x in range(len(map_l[y])):
            screen.blit(map_sprite_list[map_l[y][x]], (x * 32, y * 32))


def sort_trees(tree_l):
    for i in range(len(tree_l) - 1):
        for t in range(i + 1, len(tree_l)):
            if tree_l[i][0] > tree_l[t][0]:
                tree_l[i], tree_l[t] = tree_l[t], tree_l[i]


def add_trees(tree_l):
    sort_trees(tree_l)
    for i in tree_l:
        screen.blit(tree, i)


# endregion

# region socket_handler
def socket_handler(s, q):
    ADDRESS = ('172.40.75.152', 8888)
    s.connect(ADDRESS)
    print(os.getpid())
    print('ppid:', os.getppid())
    while True:
        data = tuple(socket.recv(1024).decode().strip('.').strip(','))
        q.put(data)
        s.send('ok'.encode())


# endregion


init_p = Set_Action('idle_f', 'Set_Action01', 400, 300, 3)
p_group = pygame.sprite.Group(init_p)
o = OtherSet_Actions(0, 0, o_i)

clock = pygame.time.Clock()

# region create process
socket = socket()
signal.signal(signal.SIGCHLD, signal.SIG_IGN)
ppid = os.getpid()
queue = Queue()
process = Process(target=socket_handler, args=(socket, queue))
process.daemon = True
# TODO process.start()
# endregion

running = True
if os.getpid() == ppid:
    while running:
        screen.fill((0, 0, 0))
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    init_p.move_up()
                    p_group = action('backward', init_p.name, init_p.x, init_p.y, init_p.speed)
                if event.key == pygame.K_s:
                    init_p.move_down()
                    p_group = action('forward', init_p.name, init_p.x, init_p.y, init_p.speed)
                if event.key == pygame.K_a:
                    init_p.move_left()
                    p_group = action('left', init_p.name, init_p.x, init_p.y, init_p.speed)
                if event.key == pygame.K_d:
                    init_p.move_right()
                    p_group = action('right', init_p.name, init_p.x, init_p.y, init_p.speed)
                if event.key == pygame.K_j:
                    init_p.attack()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    init_p.up_speed = 0
                    p_group = action('idle_b', init_p.name, init_p.x, init_p.y, init_p.speed)
                if event.key == pygame.K_s:
                    init_p.down_speed = 0
                    p_group = action('idle_f', init_p.name, init_p.x, init_p.y, init_p.speed)
                if event.key == pygame.K_a:
                    init_p.left_speed = 0
                    p_group = action('idle_l', init_p.name, init_p.x, init_p.y, init_p.speed)
                if event.key == pygame.K_d:
                    init_p.right_speed = 0
                    p_group = action('idle_r', init_p.name, init_p.x, init_p.y, init_p.speed)
                if event.key == pygame.K_j:
                    init_p.stop_attack()
        # region Set_Action_position_control
        if init_p.x < 0:
            init_p.x = 0
        if init_p.y < 0:
            init_p.y = 0
        if init_p.x > screen_size[0] - 32:
            init_p.x = screen_size[0] - 32
        if init_p.y > screen_size[1] - 32:
            init_p.y = screen_size[1] - 32
        # endregion
        generate_map(map_list)
        add_trees(tree_pos_list)
        font_display = font_01.render('press w,a,s,d to move\npress j to attack', True, (255, 255, 255))

        # TODO o.show(queue.get())
        p_group.update()

        screen.blit(font_display, (10, 10))
        name_display = font_03.render(f'{init_p.name}', True, (255, 255, 255))

        screen.blit(name_display, (init_p.x - 7, init_p.y - 17))
        if init_p.isattack:
            attack_display = font_01.render('ATTACK!', True, (255, 0, 0))
            screen.blit(attack_display, (init_p.x, init_p.y))
        pygame.display.update()
        clock.tick(60)
