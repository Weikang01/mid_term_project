# -*- coding: utf-8 -*-
import pygame
import math


class Player(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.set_frame_sheet()
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 1
        self.set_frame_image()
        self.set_press_control()
        self.set_directional_offsets()
        self.test_properties()

    def test_properties(self):
        self.speed = 5
        self.name = 'player01'

    def set_press_control(self):
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

    def get_position(self):
        return (self.rect.x, self.rect.y)

    def get_name(self):
        return self.name

    def set_directional_offsets(self):
        self.left_speed = 0
        self.right_speed = 0
        self.up_speed = 0
        self.down_speed = 0

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
        self.rect.x += (self.right_speed - self.left_speed)
        self.rect.y += (self.down_speed - self.up_speed)

        if direction == 'left':
            self.clip(self.left_states)
            if self.right_pressed:
                self.right_speed = 0
            if self.up_pressed or self.left_pressed:
                self.left_speed = math.sqrt(2) / 2 * self.speed
            else:
                self.left_speed = self.speed

        if direction == 'right':
            self.clip(self.right_states)
            if self.left_pressed:
                self.left_speed = 0
            if self.up_pressed or self.left_pressed:
                self.right_speed = math.sqrt(2) / 2 * self.speed
            self.right_speed = self.speed

        if direction == 'up':
            self.clip(self.up_states)
            if self.down_pressed:
                self.down_speed = 0
            if self.left_pressed or self.right_pressed:
                self.up_speed = math.sqrt(2) / 2 * self.speed
            else:
                self.up_speed = self.speed

        if direction == 'down':
            self.clip(self.down_states)
            if self.up_pressed:
                self.up_speed = 0
            if self.left_pressed or self.right_pressed:
                self.down_speed = math.sqrt(2) / 2 * self.speed
            else:
                self.down_speed = self.speed

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
                self.left_pressed = True
                self.update('left')
            if event.key == pygame.K_RIGHT:
                self.right_pressed = True
                self.update('right')
            if event.key == pygame.K_UP:
                self.up_pressed = True
                self.update('up')
            if event.key == pygame.K_DOWN:
                self.down_pressed = True
                self.update('down')

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.left_pressed = False
                self.left_speed = 0
                if not self.right_pressed \
                        and not self.up_pressed \
                        and not self.down_pressed:
                    self.update('stand_left')
            if event.key == pygame.K_RIGHT:
                self.right_pressed = False
                self.right_speed = 0
                if not self.left_pressed \
                        and not self.up_pressed \
                        and not self.down_pressed:
                    self.update('stand_right')
            if event.key == pygame.K_UP:
                self.up_pressed = False
                self.up_speed = 0
                if not self.left_pressed \
                        and not self.right_pressed \
                        and not self.down_pressed:
                    self.update('stand_up')
            if event.key == pygame.K_DOWN:
                self.down_pressed = False
                self.down_speed = 0
                if not self.left_pressed \
                        and not self.right_pressed \
                        and not self.up_pressed:
                    self.update('stand_down')
