import pygame
from pygame_gui.ui_manager import UIManager
import os
import global_variables as gv


class Window:
    def __init__(self):
        pygame.init()
        pygame.key.set_repeat(1, 1)

        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (gv.WINDOW_X_POS, gv.WINDOW_Y_POS)

        self.display = pygame.display
        self.display.set_caption(gv.WINDOW_NAME)

        icon_surface = pygame.image.load("Images/car/red car.png")
        icon_surface = pygame.transform.rotate(icon_surface, 90)
        icon_surface = pygame.transform.scale(icon_surface, (40, 40))
        self.display.set_icon(icon_surface)

        self.surface = pygame.display.set_mode(gv.WINDOW_SIZE)

        self.gui_manager = UIManager(gv.WINDOW_SIZE)

        self.clock = pygame.time.Clock()
