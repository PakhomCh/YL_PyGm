import pygame
from pygame.locals import *

panel = pygame.image.load('gfx/panel.png')
panel_2 = pygame.image.load('gfx/panel_2.png')


def update(screen, Ball, Bat_1, Bat_2, bs_font):
    global panel, panel_2

    Ball.pos[0] += Ball.move[0]
    Ball.pos[1] += Ball.move[1]

    screen = pygame.display.get_surface()

    screen.fill((192, 192, 192))

    score_1_tmp = 'SCORE: ' + str(Bat_1.score)
    scorecaption_1 = bs_font.render(score_1_tmp, False, (255, 255, 145))

    score_2_tmp = 'SCORE: ' + str(Bat_2.score)
    scorecaption_2 = bs_font.render(score_2_tmp, False, (255, 255, 145))

    screen.blit(panel, (screen.get_width() / 2 - panel.get_width() / 2, 20))
    screen.blit(panel_2, (0, 20))
    screen.blit(scorecaption_1, ((screen.get_width() - scorecaption_1.get_width() - 10), 2))
    screen.blit(scorecaption_2, ((8, 2)))
    screen.blit(Bat_1.image, Bat_1.pos)
    screen.blit(Bat_2.image, Bat_2.pos)
    screen.blit(Ball.image, Ball.pos)

    pygame.display.update()
