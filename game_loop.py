import sys
import pygame
from pygame.locals import *

from objects import *

import fullscreen
import collision
import difficulty
import Input
import Display

# -----------------------------------------------------------------------------#
score_1 = 0
score_2 = 0
Difficulty = 'Medium'


def set_difficulty(diff):
    global Difficulty
    Difficulty = diff


def win_p1(scr):
    screen = scr
    for i in range(0, 30):
        screen.fill((0, 0, 0))
        font = pygame.font.Font("GB_boot.ttf", i)
        text = font.render('PLAYER 1 WINS!!!', True, (255, 255, 255))
        screen.blit(text,
                    (screen.get_width() / 2 - text.get_width() / 2, screen.get_height() / 2 - text.get_height() / 2))
        pygame.display.update()
    pygame.time.delay(4000)
    return


def win_p2(scr):
    screen = scr
    for i in range(0, 30):
        screen.fill((0, 0, 0))
        font = pygame.font.Font("GB_boot.ttf", i)
        text = font.render('PLAYER 2 WINS!!!', True, (255, 255, 255))
        screen.blit(text,
                    (screen.get_width() / 2 - text.get_width() / 2, screen.get_height() / 2 - text.get_height() / 2))
        pygame.display.update()
    pygame.time.delay(4000)
    return


def game(surface):
    screen = surface

    pygame.mouse.set_visible(0)

    Bat_1 = bat(posy=screen.get_height() / 2)
    Bat_2 = bat(posx=(screen.get_width() - 10), posy=screen.get_height() / 2)
    Ball = ball(posx=screen.get_width() / 2, posy=screen.get_height() / 2)

    global Difficulty
    difficulty.update(Bat_2, Difficulty)

    background = pygame.image.load('gfx/bg_1.bmp').convert()

    Bat_1.score = score_1
    Bat_2.score = score_2

    def new_round():
        global score_1
        global score_2

        if Ball.pos[0] - (Ball.image.get_width() / 2) < 0:
            score_1 += 1
            if score_1 > 20:
                score_1 = 0
                win_p2(screen)
                pygame.quit()
                sys.exit()
            else:
                game(screen)


        elif Ball.pos[0] + (Ball.image.get_width() / 2) > screen.get_width():
            score_2 += 1
            if score_2 > 20:
                score_2 = 0
                win_p1(screen)
                pygame.quit()
                sys.exit()
            else:
                game(screen)

    clock = pygame.time.Clock()
    pygame.font.init()
    bs_font = pygame.font.Font("GB_boot.ttf", 20)

    while True:

        clock.tick(40)

        screen.blit(background)

        running = Input.check(screen, Bat_1, Bat_2, Ball)

        if running is False:
            return

        collision.check(screen, Ball, Bat_1, Bat_2)

        new_round()

        Display.update(screen, Ball, Bat_1, Bat_2, bs_font)
