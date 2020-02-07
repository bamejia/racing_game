import os
import global_variables as gv
from view.display_race import display_race
from view.display_health import display_health
from view.display_score import display_score
import pygame
# from OpenGL.GL import *
# from OpenGL.GLU import *


class GameView:
    def __init__(self, window, visible_score=False, visible_top_health_bar=False):

        self.display = window.display

        self.surface = window.surface
        # surface = pygame.display.set_mode(WINDOW_SIZE, pygame.DOUBLEBUF|pygame.OPENGL)
        self.street = pygame.Surface(gv.ROAD_DIMENSIONS, pygame.OPENGL)

        self.visible_score = visible_score
        self.visible_top_health_bar = visible_top_health_bar

        """ Greatly simplifies how much code is written and allows for simply changing the variable names in the 
            global_variables.py to change names, colors, and sizes """
        self.vehicle_types = {gv.CAR_TYPES[i]: process_image(   # maps car types to images loaded into
                                                                # memory on pygame.Surface objects
            gv.CAR_IMAGE_PATHS[gv.CAR_TYPES[item]], gv.CAR_SIZES[gv.CAR_TYPES[item]][0],
            gv.CAR_SIZES[gv.CAR_TYPES[item]][1]) for i, item in enumerate(gv.CAR_TYPES)}

    """ METHODS """
    def update(self, vehicles):
        """  Updates the game visuals, and displays each vehicle based on their positions modified by the GameModel

        Args:
            vehicles (list): contains vehicle objects to be drawn on screen

        Returns:
            None
        """

        display_race(self, vehicles)

        if self.visible_top_health_bar:     # Whether to show health bars or not
            if len(vehicles) > 1 and vehicles[1].car_type == "player2":
                display_health(self.surface, vehicles[1])
            display_health(self.surface, vehicles[0])

        if self.visible_score:      # Whether to show the player's score or not
            display_score(self, vehicles[0])

        self.display.update()   # Updates the current frame being shown to the player


# Rotates and scales the image to the designated width and length
def process_image(image_path, width, length):
    car_image = pygame.image.load(image_path)
    car_image = pygame.transform.rotate(car_image, 90)
    car_image = pygame.transform.scale(car_image, (width, length))
    return car_image
