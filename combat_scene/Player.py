# -*- coding: utf-8 -*-
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.set_frame_sheet()
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 1
        self.set_frame_image()
        self.set_press_control()

    def set_press_control(self):
        self.left_down = False
        self.right_down = False
        self.up_down = False
        self.down_down = False

    def set_frame_sheet(self):
        self.sheet = pygame.image.load('/home/tarena/PycharmProjects/month02/project_01/combat_scene/nekonin006.png')
        self.sheet.set_clip(pygame.Rect(32, 0, 32, 32))
        self.image = self.sheet.subsurface(self.sheet.get_clip())

    def set_frame_image(self):
        self.left_states = {0: (0, 32, 32, 32), 1: (32, 32, 32, 32), 2: (64, 32, 32, 32)}
        self.right_states = {0: (0, 64, 32, 32), 1: (32, 64, 32, 32), 2: (64, 64, 32, 32)}
        self.up_states = {0: (0, 96, 32, 32), 1: (32, 96, 32, 32), 2: (64, 96, 32, 32)}
        self.down_states = {0: (0, 0, 32, 32), 1: (32, 0, 32, 32), 2: (64, 0, 32, 32)}

    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]

    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect

    def update(self, direction):
        if direction == 'left':
            self.clip(self.left_states)
            self.rect.x -= 5
        if direction == 'right':
            self.clip(self.right_states)
            self.rect.x += 5
        if direction == 'up':
            self.clip(self.up_states)
            self.rect.y -= 5
        if direction == 'down':
            self.clip(self.down_states)
            self.rect.y += 5

        if direction == 'stand_left':
            self.clip(self.left_states[1])
        if direction == 'stand_right':
            self.clip(self.right_states[1])
        if direction == 'stand_up':
            self.clip(self.up_states[1])
        if direction == 'stand_down':
            self.clip(self.down_states[1])

        self.image = self.sheet.subsurface(self.sheet.get_clip())

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            global running
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                self.left_down = True
                self.update('left')
            if event.key == pygame.K_RIGHT:
                self.right_down = True
                self.update('right')
            if event.key == pygame.K_UP:
                self.up_down = True
                self.update('up')
            if event.key == pygame.K_DOWN:
                self.down_down = True
                self.update('down')

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT:
                self.left_down = False
                if not self.right_down \
                        and not self.up_down \
                        and not self.down_down:
                    self.update('stand_left')
            if event.key == pygame.K_RIGHT:
                self.right_down = False
                if not self.left_down \
                        and not self.up_down \
                        and not self.down_down:
                    self.update('stand_right')
            if event.key == pygame.K_UP:
                self.up_down = False
                if not self.left_down \
                        and not self.right_down \
                        and not self.down_down:
                    self.update('stand_up')
            if event.key == pygame.K_DOWN:
                self.down_down = False
                if not self.left_down \
                        and not self.right_down \
                        and not self.up_down:
                    self.update('stand_down')
