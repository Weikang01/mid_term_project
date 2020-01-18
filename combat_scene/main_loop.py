# -*- coding: utf-8 -*-
from combat_scene.Player import *
from combat_scene.config import *
from combat_scene.load import *
from combat_scene.test_client_tcp import *
from combat_scene.test_box import *
from threading import Thread
import pygame

pygame.display.set_caption('Diamond Warrior')
pygame.display.set_icon(icon_img)

# INITIALIZATION
pygame.init()
font_01 = pygame.font.Font(f'{abs_path}/Assets/Fonts/Cosima-DemoBold.otf', 23)
font_02 = pygame.font.Font(f'{abs_path}/Assets/Fonts/Cosima-DemoBold.otf', 15)
font_display = font_01.render('press arrows to move press j to attack', True, (255, 255, 255))
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()
player = Player((WIDTH / 2, HEIGHT / 2))
box = Test_Box((100, 100))
box_pos = (100, 100)


def set_box_pos():
    global box_pos
    box_pos = cur_position()


t = Thread(target=set_box_pos)
t.setDaemon(True)
t.start()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    player.handle_event(event)
    screen.fill(BLACK)
    # TODO screen.blit(box, box_pos)
    screen.blit(player.image, player.rect)
    screen.blit(font_display, (10, 10))
    pos_display = font_02.render(str(player.get_position()), True, (255, 255, 255))
    screen.blit(pos_display, (10, 40))
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
