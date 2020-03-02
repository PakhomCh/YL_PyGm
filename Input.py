import pygame
from pygame.locals import *
import sys

# ------------------------------------------------------------------------------#

players = 1
input_dev = 1


def check(screen, Bat_1, Bat_2, Ball):
    global players
    global input_dev

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.event.pump()
    key = pygame.key.get_pressed()

    if players == 1:
        if input_dev == 1:
            if key[K_UP]:
                Bat_1.pos[1] -= Bat_1.move_speed
            if key[K_DOWN]:
                Bat_1.pos[1] += Bat_1.move_speed
            if key[K_ESCAPE]:
                return False
        elif input_dev == 2:
            x, y = pygame.mouse.get_pos()
            Bat_1.pos[1] = y

            if key[K_ESCAPE]:
                return False

        Bat_2.update(Ball.pos[1])

    elif players == 2:
        if input_dev == 1:
            if key[K_w]:
                Bat_1.pos[1] -= Bat_1.move_speed
            if key[K_s]:
                Bat_1.pos[1] += Bat_1.move_speed
            if key[K_UP]:
                Bat_2.pos[1] -= Bat_2.move_speed
            if key[K_DOWN]:
                Bat_2.pos[1] += Bat_2.move_speed
            if key[K_ESCAPE]:
                return False
        elif input_dev == 2:
            x, y = pygame.mouse.get_pos()
            if key[K_UP]:
                Bat_1.pos[1] -= Bat_1.move_speed
            if key[K_DOWN]:
                Bat_1.pos[1] += Bat_1.move_speed
            if key[K_ESCAPE]:
                return False
            Bat_2.pos[1] = y


def set_players(plyrs=1):
    global players
    players = plyrs


def set_inputdev(dev=1):
    global input_dev
    input_dev = dev
