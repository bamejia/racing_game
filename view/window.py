import pygame
import os
import global_variables as gv


class Window:
    def __init__(self):
        pygame.init()
        pygame.key.set_repeat(1, 1)

        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (gv.WINDOW_X_POS, gv.WINDOW_Y_POS)

        self.__display = pygame.display
        self.__display.set_caption(gv.WINDOW_NAME)

        self.__surface = pygame.display.set_mode(gv.WINDOW_SIZE)

        self.__clock = pygame.time.Clock()

    """ GETTERS """

    @property
    def display(self):
        return self.__display

    @property
    def surface(self):
        return self.__surface

    @property
    def clock(self):
        return self.__clock
