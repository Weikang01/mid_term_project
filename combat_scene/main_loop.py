# -*- coding: utf-8 -*-
from combat_scene.Player import *
from combat_scene.config import *
from combat_scene.load import *
import pygame

pygame.display.set_caption('Diamond Warrior')
pygame.display.set_icon(icon_img)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()
player = Player((WIDTH / 2, HEIGHT / 2))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    player.handle_event(event)
    screen.fill(BLACK)
    screen.blit(player.image, player.rect)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
