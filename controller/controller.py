from controller.player_input import title_screen_input
from controller.player_mouse_input import title_screen_mouse_input
from controller.game_choice.online_start import online_start
from view.title_screen_view import TitleScreenView
from view.window import Window
from controller.game_choice.p1_start import p1_start
from controller.game_choice.p2_start import p2_start
from controller.game_choice.option_menu import option_menu
import pygame
import sys
import global_variables as gv

""" temporary """
import time


class Controller:
    def __init__(self):
        self.__window = Window()
        self.__title_screen_view = object
        self.__choice = (gv.BUTTON_TEXTS[0], gv.BUTTON_TEXTS[1], gv.BUTTON_TEXTS[2], gv.BUTTON_TEXTS[3])

    def run(self):

        title_screen_view = TitleScreenView(self.window)

        while True:
            events = pygame.event.get()
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            btn_hover, btn_press, btn_choice = title_screen_mouse_input(title_screen_view, mouse, click)

            title_screen_view.show_screen(btn_hover, btn_press)
            title_screen_input(events)

            """ 1 PLAYER START chosen """
            if btn_choice == self.choice[0]:
                p1_start(self.window)
            """ 2 PLAYER START chosen """
            if btn_choice == self.choice[1]:
                p2_start(self.window)
            """ OPTIONS chosen """
            if btn_choice == self.choice[2]:
                online_start(self.window, True)
                # option_menu(self.window)
            """ EXIT chosen """
            if btn_choice == self.choice[3]:
                online_start(self.window)
                # pygame.quit()
                # sys.exit()

            # print(self.window.clock.get_fps())

            self.window.clock.tick(120)

    """ GETTERS """
    @property
    def window(self):
        return self.__window

    @property
    def title_screen_view(self):
        return self.__title_screen_view

    @property
    def choice(self):
        return self.__choice

    """ SETTERS """
    @title_screen_view.setter
    def title_screen_view(self, title_screen_view):
        self.__title_screen_view = title_screen_view

    @choice.setter
    def choice(self, choice):
        self.__choice = choice

