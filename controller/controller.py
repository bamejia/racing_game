from controller.player_input import player_input, player_input2
from controller.enemy_input import enemy_input
from model.model import Model
from view.view import View
import pygame
import sys
import global_variables as gv

""" temporary """
import time


class Controller:
    def __init__(self):
        self.view = View()
        self.model = Model()

    def run(self):

        print(gv.WINDOW_W)
        print(gv.WINDOW_L)

        has_not_quit_game = True
        while has_not_quit_game:

            events = pygame.event.get()

            has_not_quit_game = player_input(self.model.vehicles[0], events)
            player_input2(self.model.vehicles[1], events)
            # print(self.model.player.cur_x_vel, self.model.player.reaction_x_vel, self.model.player.cur_y_vel, self.model.player.reaction_y_vel)

            enemy_input(self.model.vehicles)

            self.model.update()
            self.view.update(self.model.vehicles)

            # if not self.model.check_if_player_is_alive():
            #     time.sleep(2) # temp
            #     pygame.quit()
            #     sys.exit()

            # print(self.view.clock.get_fps())

            self.view.clock.tick(120)

