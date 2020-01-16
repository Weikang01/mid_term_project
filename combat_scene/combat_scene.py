import pygame
from random import randint
import os


class OtherPlayers(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, sprite=None):
        super().__init__()
        self.x = x
        self.y = y
        self.sprite = sprite
        self.rect = pygame.Rect((x, y), (x + 19, y + 25))

    def set_pos(self, pos=(0, 0)):
        self.x = pos[0]
        self.y = pos[1]

    def show(self):
        screen.blit(self.sprite, (self.x, self.y))


class Player(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, speed=0.0, sprite=None):
        super().__init__()
        self.x = x
        self.y = y
        self.speed = speed
        self.left_speed = 0
        self.right_speed = 0
        self.up_speed = 0
        self.down_speed = 0
        self.sprite = sprite
        self.init_anim_speed = 10
        self.anim_speed = self.init_anim_speed
        self.rect = pygame.Rect((x, y), (x + 19, y + 25))

    def show(self):
        screen.blit(self.sprite, (self.x, self.y))
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


class Obstacle:
    def __init__(self, anchor_x=0, anchor_y=0):
        self.anchor_x = anchor_x
        self.anchor_y = anchor_y


# find absolute path
path_e = os.path.abspath('./combat_scene.py').split('/')[0:-2]
abs_path = '/'.join(path_e) + '/'

# initiate pygame
pygame.init()
font_01 = pygame.font.Font(f'{abs_path}/Assets/Fonts/Cosima-DemoBold.otf', 23)
screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)

pygame.display.set_caption('Diamond Warrior')
icon_img = pygame.image.load(f'{abs_path}/Assets/Sprite/Decor/icon.png')
pygame.display.set_icon(icon_img)

g_1 = pygame.image.load(f'{abs_path}/Assets/Sprite/Decor/grass01.png')
g_2 = pygame.image.load(f'{abs_path}/Assets/Sprite/Decor/grass02.png')
g_3 = pygame.image.load(f'{abs_path}/Assets/Sprite/Decor/grass03.png')
tree = pygame.image.load(f'{abs_path}/Assets/Sprite/Decor/tree01.png')

map_sprite_list = (g_1, g_2, g_3)

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


def add_trees(tree_l):
    for i in tree_l:
        screen.blit(tree, i)


running = True

p_i = pygame.image.load(f'{abs_path}/Assets/Sprite/nekochan01/idle.png')
p = Player(400, 300, 0.5, p_i)

clock = pygame.time.Clock()
while running:
    screen.fill((0, 0, 0))
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                p.move_up()
            if event.key == pygame.K_s:
                p.move_down()
            if event.key == pygame.K_a:
                p.move_left()
            if event.key == pygame.K_d:
                p.move_right()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                p.up_speed = 0
            if event.key == pygame.K_s:
                p.down_speed = 0
            if event.key == pygame.K_a:
                p.left_speed = 0
            if event.key == pygame.K_d:
                p.right_speed = 0
    if p.x < 0:
        p.x = 0
    if p.y < 0:
        p.y = 0
    if p.x > screen_size[0] - 32:
        p.x = screen_size[0] - 32
    if p.y > screen_size[1] - 32:
        p.y = screen_size[1] - 32
    generate_map(map_list)
    add_trees(tree_pos_list)
    font_display = font_01.render('press w,a,s,d to move', True, (255, 255, 255))
    screen.blit(font_display, (10, 10))
    p.show()
    pygame.display.update()
