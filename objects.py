import pygame
from pygame.locals import *
import random


# ------------------------------------------------------------------------------#

class bat(object):
    def __init__(self, posx=5, posy=112):
        self.image = pygame.image.load('gfx/bat_1.png').convert_alpha()
        self.pos = [posx, posy]
        self.move_speed = 6
        self.score = 0
        self.spd_incr = 0

    def update(self, ball_pos_y):
        self.move_speed = 2 + (self.spd_incr)
        if ball_pos_y > self.pos[1]:
            self.pos[1] += self.move_speed
        elif ball_pos_y < self.pos[1]:
            self.pos[1] -= self.move_speed


class comp_bat(bat):
    def update(self, ball_pos_y):
        self.move_speed = 2
        if ball_pos_y > self.pos[1]:
            self.pos[1] += self.move_speed
        elif ball_pos_y < self.pos[1]:
            self.pos[1] -= self.move_speed


class ball(object):
    def __init__(self, posx=20, posy=20):
        self.image = pygame.image.load('gfx/ball.png').convert_alpha()
        self.pos = [posx, posy]
        tmp = random.randint(0, 3)
        if tmp == 0:
            self.move = [3, 2]
        elif tmp == 1:
            self.move = [-3, 2]
        elif tmp == 2:
            self.move = [3, -2]
        elif tmp == 3:
            self.move = [-3, 2]
