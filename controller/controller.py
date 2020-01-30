from controller.player_input import player_input, player_input2, title_screen_input
from controller.enemy_input import enemy_input
from model.game_model import GameModel
from view.game_view import GameView
from view.title_screen_view import TitleScreenView
from view.window import Window
import pygame
import sys
import global_variables as gv

""" temporary """
import time


class Controller:
    def __init__(self):
        self.__window = Window()
        self.__title_screen_view = object
        self.__game_view = object
        self.__game_model = object

    def run(self):

        title_screen_view = TitleScreenView(self.window)

        has_not_quit_game = True
        while has_not_quit_game:

            events = pygame.event.get()

            title_screen_view.show_screen()
            title_screen_input(events)


            # print(self.window.clock.get_fps())
            #
            # has_not_quit_game = player_input(self.game_model.vehicles[0], events)
            # player_input2(self.game_model.vehicles[1], events)
            # # print(self.game_model.player.cur_x_vel, self.game_model.player.reaction_x_vel, self.game_model.player.cur_y_vel, self.game_model.player.reaction_y_vel)
            #
            # enemy_input(self.game_model.vehicles)
            #
            # self.game_model.update()
            # self.game_view.update(self.game_model.vehicles)

            # if not self.game_model.check_if_player_is_alive():
            #     time.sleep(2) # temp
            #     pygame.quit()
            #     sys.exit()

            # print(self.game_view.clock.get_fps())

            self.window.clock.tick(120)

    """ GETTERS """
    @property
    def window(self):
        return self.__window

    @property
    def title_screen_view(self):
        return self.__title_screen_view

    @property
    def game_view(self):
        return self.__game_view

    @property
    def game_model(self):
        return self.__game_model

    """ SETTERS """
    @title_screen_view.setter
    def title_screen_view(self, title_screen_view):
        self.__title_screen_view = title_screen_view

    @game_view.setter
    def game_view(self, game_view):
        self.__game_view = game_view

    @game_model.setter
    def game_model(self, game_model):
        self.__game_model = game_model

