from combat_scene.load import *
from combat_scene.config import *
from random import randint

def terrain_sprites():
    gpath_list = glob(fr'{abs_path}/Assets/Sprite/Decor/grass0?.png')
    map_sprite_list = []
    for i in gpath_list:
        map_sprite_list.append(pygame.image.load(i))
    return map_sprite_list

sprites = terrain_sprites()
group = pygame.sprite.Group()


def generate_number():
    map_list = []
    for y in range(0, HEIGHT // 32 + 1):
        row_list = []
        for x in range(0, WIDTH // 32 + 1):
            row_list.append(randint(0, len(sprites) - 1))
        map_list.append(row_list)
    return map_list

def generate_map(map_l):
    for y in range(len(map_l)):
        for x in range(len(map_l[y])):
            sprites[map_l[y][x]]
            screen.blit(, (x * 32, y * 32))
