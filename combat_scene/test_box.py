import pygame
from combat_scene.config import *


class Test_Box(pygame.Surface):
    def __init__(self, position):
        super().__init__((15, 15))
        self.fill(WHITE)
        self.rect = self.get_rect()
        self.rect.topleft = position

    def update(self, pos):
        self.rect = pos
