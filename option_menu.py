import pygame
from pygame.locals import *

import fullscreen
import game_loop
import Input
import sys

screen = 0

h_color = (0, 255, 0)
color = (0, 128, 0)


def options(surface):
    global screen
    global h_color
    global color

    screen = surface
    screen.fill((0, 0, 0))
    pygame.font.init()

    font = pygame.font.Font("GB_boot.ttf", 20)

    text = ['FULLSCREEN ', 'DIFFICULTY', 'SET INPUT DEVICE', 'BACK TO MAIN']
    options = []

    for txt in text:
        options.append(font.render(txt, False, color))

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
                        screen = fullscreen.fullscreen()
                    elif selected == 1:
                        difficulty_menu()
                    elif selected == 2:
                        input_menu()

                    elif selected == 3:
                        return screen

        screen.fill((0, 0, 0))
        for i in range(0, len(options)):
            x, y = centre_menu(screen, options[i])
            if i == selected:
                options[i] = font.render(text[i], False, h_color)
            else:
                options[i] = font.render(text[i], False, color)
            screen.blit(options[i], (x, (y + i * dist_btw)))

        pygame.display.update()


def difficulty_menu():
    global screen
    global h_color
    global color
    screen.fill((0, 0, 0))
    pygame.font.init()

    font = pygame.font.Font("GB_boot.ttf", 20)

    text = ['EASY', 'MEDIUM', 'HARD', 'VERY HARD', 'BACK TO OPTIONS']
    options = []

    for txt in text:
        options.append(font.render(txt, False, color))

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
                        game_loop.set_difficulty('Easy')
                    elif selected == 1:
                        game_loop.set_difficulty('Medium')
                    elif selected == 2:
                        game_loop.set_difficulty('Hard')
                    elif selected == 3:
                        game_loop.set_difficulty('V_Hard')
                    elif selected == 4:
                        return

        screen.fill((0, 0, 0))
        for i in range(0, len(options)):
            x, y = centre_menu(screen, options[i])
            if i == selected:
                options[i] = font.render(text[i], False, h_color)
            else:
                options[i] = font.render(text[i], False, color)
            screen.blit(options[i], (x, (y + i * dist_btw)))

        pygame.display.update()


def input_menu():
    global h_color
    global color
    global screen
    screen.fill((0, 0, 0))
    pygame.font.init()

    font = pygame.font.Font("GB_boot.ttf", 20)

    text = ['KEYBOARD', 'MOUSE', 'BACK TO OPTIONS']
    options = []

    for txt in text:
        options.append(font.render(txt, False, color))

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
                        Input.set_inputdev(1)
                    elif selected == 1:
                        Input.set_inputdev(2)
                    elif selected == 2:
                        return

        screen.fill((0, 0, 0))
        for i in range(0, len(options)):
            x, y = centre_menu(screen, options[i])
            if i == selected:
                options[i] = font.render(text[i], False, h_color)
            else:
                options[i] = font.render(text[i], False, color)
            screen.blit(options[i], (x, (y + i * dist_btw)))

        pygame.display.update()
