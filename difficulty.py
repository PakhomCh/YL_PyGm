import pygame
from pygame.locals import *


def update(Bat_2, Diff):
    if Diff == 'Easy':
        Bat_2.spd_incr = -0.5
    elif Diff == 'Medium':
        Bat_2.spd_incr = 0
    elif Diff == 'Hard':
        Bat_2.spd_incr = 1
    elif Diff == 'V_Hard':
        Bat_2.spd_incr = 2
