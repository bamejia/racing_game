import os
import global_variables as gv
from view.display_race import display_race
import pygame
# from OpenGL.GL import *
# from OpenGL.GLU import *


class View:
    def __init__(self):
        pygame.init()
        pygame.key.set_repeat(1, 1)

        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (gv.WINDOW_X_POS, gv.WINDOW_Y_POS)

        self.display = pygame.display
        self.display.set_caption(gv.WINDOW_NAME)

        self.surface = pygame.display.set_mode(gv.WINDOW_SIZE)
        # surface = pygame.display.set_mode(WINDOW_SIZE, pygame.DOUBLEBUF|pygame.OPENGL)
        self.street = pygame.Surface(gv.ROAD_DIMENSIONS, pygame.OPENGL)
        # street.blit(pygame.image.load(""))
        # potato = [pygame.image.load("Images/potato/frame_0_delay-0.1s.png"),
        #           pygame.image.load("Images/potato/frame_1_delay-0.1s.png"),
        #           pygame.image.load("Images/potato/frame_2_delay-0.1s.png")]
        # for p, item in enumerate(potato):
        #     w, l = potato[p].get_size()
        #     potato[p] = pygame.transform.scale(potato[p], (int(round(w/2)), int(round(l/2))))
        player_car = pygame.image.load("Images/car/red car.png")
        player_car = pygame.transform.rotate(player_car, 90)
        player_car = pygame.transform.scale(player_car, (gv.PLAYER_WIDTH, gv.PLAYER_LENGTH))  # (30, 60)

        random_enemy_car = pygame.image.load("Images/car/purple car.png")
        random_enemy_car = pygame.transform.rotate(random_enemy_car, 90)
        random_enemy_car = pygame.transform.scale(random_enemy_car, (gv.ENEMY_WIDTH, gv.ENEMY_LENGTH))

        side_to_side_enemy_car = pygame.image.load("Images/car/orange car.png")
        side_to_side_enemy_car = pygame.transform.rotate(side_to_side_enemy_car, 90)
        side_to_side_enemy_car = pygame.transform.scale(side_to_side_enemy_car, (gv.ENEMY_WIDTH, gv.ENEMY_LENGTH))

        up_and_down_enemy_car = pygame.image.load("Images/car/yellow car.png")
        up_and_down_enemy_car = pygame.transform.rotate(up_and_down_enemy_car, 90)
        up_and_down_enemy_car = pygame.transform.scale(up_and_down_enemy_car, (gv.ENEMY_WIDTH, gv.ENEMY_LENGTH))

        diagonal_enemy_car = pygame.image.load("Images/car/pink car.png")
        diagonal_enemy_car = pygame.transform.rotate(diagonal_enemy_car, 90)
        diagonal_enemy_car = pygame.transform.scale(diagonal_enemy_car, (gv.ENEMY_WIDTH, gv.ENEMY_LENGTH))

        tracker_enemy_car = pygame.image.load("Images/car/black car.png")
        tracker_enemy_car = pygame.transform.rotate(tracker_enemy_car, 90)
        tracker_enemy_car = pygame.transform.scale(tracker_enemy_car, (gv.ENEMY_WIDTH, gv.ENEMY_LENGTH))

        static_enemy_car = pygame.image.load("Images/car/green car.png")
        static_enemy_car = pygame.transform.rotate(static_enemy_car, 90)
        static_enemy_car = pygame.transform.scale(static_enemy_car, (gv.ENEMY_WIDTH, gv.ENEMY_LENGTH))

        speed_demon_car = pygame.image.load("Images/car/white car.png")
        speed_demon_car = pygame.transform.rotate(speed_demon_car, 90)
        speed_demon_car = pygame.transform.scale(speed_demon_car, (gv.ENEMY_WIDTH, gv.ENEMY_LENGTH))

        self.vehicle_types = {
            gv.MOVEMENT_PATTERNS[0]: player_car,
            gv.MOVEMENT_PATTERNS[1]: random_enemy_car,
            gv.MOVEMENT_PATTERNS[2]: side_to_side_enemy_car,
            gv.MOVEMENT_PATTERNS[3]: up_and_down_enemy_car,
            gv.MOVEMENT_PATTERNS[4]: diagonal_enemy_car,
            gv.MOVEMENT_PATTERNS[5]: tracker_enemy_car,
            gv.MOVEMENT_PATTERNS[6]: static_enemy_car,
            gv.MOVEMENT_PATTERNS[7]: speed_demon_car
        }

        self.clock = pygame.time.Clock()

    # methods
    def update(self, vehicles):
        display_race(self, vehicles)

    # getters
    @property
    def display(self):
        return self.__display

    @property
    def surface(self):
        return self.__surface

    @property
    def street(self):
        return self.__street

    @property
    def vehicle_types(self):
        return self.__vehicle_types

    @property
    def clock(self):
        return self.__clock

    # setters
    @display.setter
    def display(self, display):
        self.__display = display

    @surface.setter
    def surface(self, surface):
        self.__surface = surface

    @street.setter
    def street(self, street):
        self.__street = street

    @vehicle_types.setter
    def vehicle_types(self, vehicle_types):
        self.__vehicle_types = vehicle_types

    @clock.setter
    def clock(self, clock):
        self.__clock = clock
