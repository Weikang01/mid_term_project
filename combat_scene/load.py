import pygame
from combat_scene.common import *
from glob import glob
abs_path = absolute_path()
# font_01 = pygame.font.Font(f'{abs_path}/Assets/Fonts/Cosima-DemoBold.otf', 23)
nikonin01 = pygame.image.load(f'{abs_path}Assets/Sprite/nikonin/pipo-nekonin001.png')
icon_img = pygame.image.load(f'{abs_path}/Assets/Sprite/Decor/icon.png')
def terrain_sprites():
    gpath_list = glob(fr'{abs_path}/Assets/Sprite/Decor/grass0?.png')
    terrain_group = pygame.sprite.Group()
    map_sprite_list = []
    for i in gpath_list:
        map_sprite_list.append(pygame.image.load(i))
    return map_sprite_list