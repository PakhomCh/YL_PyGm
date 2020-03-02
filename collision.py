from objects import *


def check(screen, Ball, Bat_1, Bat_2):
    if Ball.pos[1] < 20 or Ball.pos[1] > screen.get_height() - 15:
        pygame.mixer.music.load('sfx/Wall.wav')
        pygame.mixer.music.play()
        Ball.move[1] = -Ball.move[1]

    if (Ball.pos[0] - (Ball.image.get_width() / 2)) < ((Bat_1.pos[0] + (Bat_1.image.get_width() / 2)) + 8) \
            and (Ball.pos[1] - (Ball.image.get_height() / 2) + 10) > (Bat_1.pos[1] - (Bat_1.image.get_height() / 2)) \
            and (Ball.pos[1] + (Ball.image.get_height() / 2) - 10) < (Bat_1.pos[1] + (Bat_1.image.get_height() / 2)):
        pygame.mixer.music.load('sfx/Bat_1.wav')
        pygame.mixer.music.play()
        Ball.move[0] = -Ball.move[0] + 0.2
        Ball.pos[0] = Ball.pos[0] + 2
        Ball.move[0] += 0.1
        Ball.move[1] += 0.1

    if (Ball.pos[0] + (Ball.image.get_width() / 2)) > ((Bat_2.pos[0] - (Bat_2.image.get_width() / 2)) - 8) \
            and (Ball.pos[1] - (Ball.image.get_height() / 2) + 10) > (Bat_2.pos[1] - (Bat_2.image.get_height() / 2)) \
            and (Ball.pos[1] + (Ball.image.get_height() / 2) - 10) < (Bat_2.pos[1] + (Bat_2.image.get_height() / 2)):
        pygame.mixer.music.load('sfx/Bat_2.wav')
        pygame.mixer.music.play()
        Ball.move[0] = (-Ball.move[0]) - 0.2
        Ball.pos[0] = Ball.pos[0] - 2
        Ball.move[0] -= 0.1
        Ball.move[1] -= 0.1

    if (Bat_1.pos[1] + (Bat_1.image.get_height() / 2)) > (screen.get_height() - 15):
        Bat_1.pos[1] = ((screen.get_height() - 15) - (Bat_1.image.get_height() / 2))
    if (Bat_1.pos[1] - (Bat_1.image.get_height() / 2)) < 15:
        Bat_1.pos[1] = (10 + (Bat_1.image.get_height() / 2))

    if (Bat_2.pos[1] + (Bat_2.image.get_height() / 2)) > (screen.get_height() - 20):
        Bat_2.pos[1] = ((screen.get_height() - 20) - (Bat_2.image.get_height() / 2))
    if (Bat_2.pos[1] - (Bat_2.image.get_height() / 2)) < 20:
        Bat_2.pos[1] = (20 + (Bat_2.image.get_height() / 2))

    if Ball.move[1] < -14:
        Ball.move[1] = -14
    elif Ball.move[1] > 14:
        Ball.move[1] = 14

    if Ball.move[0] < -14:
        Ball.move[0] = -14
    elif Ball.move[0] > 14:
        Ball.move[0] = 14
