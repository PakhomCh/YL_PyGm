import pygame
from pygame.locals import *
import sys

from objects import *
import game_loop
import fullscreen
import Input
import option_menu

# ------------------------------------------------------------------------------#
screen = pygame.display.set_mode((320, 240))


def menu():
    global screen

    pygame.init()

    pygame.display.set_caption('PONG DUALS')

    pygame.font.init()

    font = pygame.font.Font("GB_boot.ttf", 20)

    h_color = (0, 255, 0)
    color = (0, 128, 0)

    text = ['START GAME - 1 PLAYER', 'START GAME - 2 PLAYER', 'OPTIONS', 'QUIT GAME']
    options = []

    for txt in text:
        options.append(font.render(txt, True, color))

    dist_btw = options[0].get_height() + 5

    def centre_menu(surface, opt):
        menu_x = (screen.get_width() / 2 - opt.get_width() / 2)
        menu_y = (screen.get_height() / 2 - opt.get_height() / 2 - 30)
        return (menu_x, menu_y)

    selected = 0

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    selected -= 1
                if event.key == K_DOWN:
                    selected += 1

                if selected < 0:
                    selected = 0
                if selected > len(options) - 1:
                    selected = len(options) - 1

                if event.key == K_RETURN:
                    if selected == 0:
                        game_loop.game(screen)
                    elif selected == 1:
                        Input.set_players(2)
                        game_loop.game(screen)
                    elif selected == 2:
                        screen = option_menu.options(screen)
                    elif selected == 3:
                        pygame.quit()
                        sys.exit()

        screen.fill((0, 0, 0))
        for i in range(0, len(options)):
            x, y = centre_menu(screen, options[i])
            if i == selected:
                options[i] = font.render(text[i], False, h_color)
            else:
                options[i] = font.render(text[i], False, color)
            screen.blit(options[i], (x, (y + i * dist_btw)))

        pygame.display.update()
