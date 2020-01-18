from combat_scene.load import *
from combat_scene.config import *
from random import randint

def terrain_group():
    sprites = terrain_sprites()
    map_list = []
    group = pygame.sprite.Group()
    for y in range(0, HEIGHT // 32 + 1):
        row_list = []
        for x in range(0, WIDTH // 32 + 1):
            row_list.append(randint(0, len(sprites) - 1))
        map_list.append(row_list)


def generate_map(map_l):
    for y in range(len(map_l)):
        for x in range(len(map_l[y])):
            screen.blit(map_sprite_list[map_l[y][x]], (x * 32, y * 32))
