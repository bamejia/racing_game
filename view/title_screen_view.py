import pygame
import global_variables as gv


class TitleScreenView:
    def __init__(self, window):
        pygame.font.init()

        self.__display = window.display
        self.__surface = window.surface

        self.__title_font = pygame.font.Font(gv.TITLE_FONT, gv.TITLE_TEXT_SIZE)
        self.__title_w = self.title_font.size(gv.TITLE_TEXT)[0]
        title_x_placement = round(gv.WINDOW_W / 2 - self.__title_w / 2)
        title_y_placement = round(gv.WINDOW_L * 1 / 30)

        self.__author_font = pygame.font.Font(gv.AUTHOR_FONT, gv.AUTHOR_TEXT_SIZE)
        self.__author_w = self.author_font.size(gv.AUTHOR_TEXT)[0]
        author_x_placement = round(gv.WINDOW_W / 2 - self.__author_w / 2)
        author_y_placement = round(gv.WINDOW_L * 8 / 30)

        # Button fonts and sizes
        self.__p1_start_btn_font = pygame.font.Font(gv.BUTTON_FONT, gv.BUTTON_TEXT_SIZE)
        self.__p1_start_btn_w = self.__p1_start_btn_font.size(gv.P1_BUTTON_TEXT)[0]
        p1_btn_x_placement = round(gv.WINDOW_W / 2 - self.__p1_start_btn_w / 2)
        p1_btn_y_placement = round(gv.WINDOW_L * 15 / 30)

        self.__p2_start_btn_font = pygame.font.Font(gv.BUTTON_FONT, gv.BUTTON_TEXT_SIZE)
        self.__p2_start_btn_w = self.__p2_start_btn_font.size(gv.P2_BUTTON_TEXT)[0]
        p2_btn_x_placement = round(gv.WINDOW_W / 2 - self.__p2_start_btn_w / 2)
        p2_btn_y_placement = round(gv.WINDOW_L * 18 / 30)

        self.__options_btn_font = pygame.font.Font(gv.BUTTON_FONT, gv.BUTTON_TEXT_SIZE)
        self.__options_btn_w = self.__options_btn_font.size(gv.OPTIONS_BUTTON_TEXT)[0]
        options_btn_x_placement = round(gv.WINDOW_W / 2 - self.__options_btn_w / 2)
        options_btn_y_placement = round(gv.WINDOW_L * 21 / 30)

        self.__exit_start_btn_font = pygame.font.Font(gv.BUTTON_FONT, gv.BUTTON_TEXT_SIZE)
        self.__exit_start_btn_w = self.__exit_start_btn_font.size(gv.EXIT_BUTTON_TEXT)[0]
        exit_btn_x_placement = round(gv.WINDOW_W / 2 - self.__exit_start_btn_w / 2)
        exit_btn_y_placement = round(gv.WINDOW_L * 24 / 30)

        # holds x and y positions of the named variables
        self.__title_pos = (title_x_placement, title_y_placement)
        self.__author_pos = (author_x_placement, author_y_placement)
        self.__p1_start_pos = (p1_btn_x_placement, p1_btn_y_placement)
        self.__p2_start_pos = (p2_btn_x_placement, p2_btn_y_placement)
        self.__options_pos = (options_btn_x_placement, options_btn_y_placement)
        self.__exit_pos = (exit_btn_x_placement, exit_btn_y_placement)

        self.count = 0

    """ METHODS """
    def show_screen(self):
        self.surface.fill(gv.PEACH_PINK)
        text = self.title_font.render(gv.TITLE_TEXT, True, gv.BLACK, gv.WHITE)
        self.surface.blit(text, (0, self.count))
        self.count += 1


        self.display.update()

    """ GETTERS """
    @property
    def display(self):
        return self.__display

    @property
    def surface(self):
        return self.__surface

    @property
    def title_font(self):
        return self.__title_font

    @property
    def title_w(self):
        return self.__title_w

    @property
    def author_font(self):
        return self.__author_font

    @property
    def author_w(self):
        return self.__author_w
