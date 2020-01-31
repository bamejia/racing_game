import pygame
import global_variables as gv

btn_x_left_ratio = 1 / 40
btn_x_right_ratio = 42 / 40
btn_y_top_ratio = 5 / 50
btn_y_bottom_ratio = 51 / 50


class TitleScreenView:
    def __init__(self, window):
        pygame.font.init()

        self.__display = window.display
        self.__surface = window.surface

        self.__title_font = pygame.font.Font(gv.TITLE_FONT, gv.TITLE_TEXT_SIZE)
        self.__title_size = self.title_font.size(gv.TITLE_TEXT)
        title_x_placement = round(gv.WINDOW_W / 2 - self.__title_size[0] / 2)
        title_y_placement = round(gv.WINDOW_L * 6 / 30)

        self.__author_font = pygame.font.Font(gv.AUTHOR_FONT, gv.AUTHOR_TEXT_SIZE)
        self.__author_size = self.author_font.size(gv.AUTHOR_TEXT)
        author_x_placement = round(gv.WINDOW_W / 2 - self.__author_size[0] / 2)
        author_y_placement = round(gv.WINDOW_L * 10 / 30)

        # Button text font and placement positions
        self.__btn_font = pygame.font.Font(gv.BUTTON_FONT, gv.BUTTON_TEXT_SIZE)

        self.__p1_start_btn_size = self.__btn_font.size(gv.BUTTON_TEXTS[0])
        p1_btn_x_placement = round(gv.WINDOW_W / 2 - self.__p1_start_btn_size[0] / 2)
        p1_btn_y_placement = round(gv.WINDOW_L * 15 / 30)

        self.__p2_start_btn_size = self.__btn_font.size(gv.BUTTON_TEXTS[1])
        p2_btn_x_placement = round(gv.WINDOW_W / 2 - self.__p2_start_btn_size[0] / 2)
        p2_btn_y_placement = round(gv.WINDOW_L * 18 / 30)

        self.__options_btn_size = self.__btn_font.size(gv.BUTTON_TEXTS[2])
        options_btn_x_placement = round(gv.WINDOW_W / 2 - self.__options_btn_size[0] / 2)
        options_btn_y_placement = round(gv.WINDOW_L * 21 / 30)

        self.__exit_btn_size = self.__btn_font.size(gv.BUTTON_TEXTS[3])
        exit_btn_x_placement = round(gv.WINDOW_W / 2 - self.__exit_btn_size[0] / 2)
        exit_btn_y_placement = round(gv.WINDOW_L * 24 / 30)

        # holds x and y positions of the named variables
        self.__title_pos = (title_x_placement, title_y_placement)
        self.__author_pos = (author_x_placement, author_y_placement)
        self.__p1_start_pos = (p1_btn_x_placement, p1_btn_y_placement)
        self.__p2_start_pos = (p2_btn_x_placement, p2_btn_y_placement)
        self.__options_pos = (options_btn_x_placement, options_btn_y_placement)
        self.__exit_pos = (exit_btn_x_placement, exit_btn_y_placement)

        # button position and sizes
        self.__p1_btn_pos_size = (self.p1_start_pos[0] - round(self.p1_start_btn_size[0] * btn_x_left_ratio),
                                  self.p1_start_pos[1] - round(self.p1_start_btn_size[1] * btn_y_top_ratio),
                                  round(self.p1_start_btn_size[0] * btn_x_right_ratio),
                                  round(self.p1_start_btn_size[1] * btn_y_bottom_ratio))

        self.__p2_btn_pos_size = (self.p2_start_pos[0] - round(self.p2_start_btn_size[0] * btn_x_left_ratio),
                                  self.p2_start_pos[1] - round(self.p2_start_btn_size[1] * btn_y_top_ratio),
                                  round(self.p2_start_btn_size[0] * btn_x_right_ratio),
                                  round(self.p2_start_btn_size[1] * btn_y_bottom_ratio))

        self.__options_btn_pos_size = (self.options_pos[0] - round(self.options_btn_size[0] * btn_x_left_ratio),
                                       self.options_pos[1] - round(self.options_btn_size[1] * btn_y_top_ratio),
                                       round(self.options_btn_size[0] * btn_x_right_ratio),
                                       round(self.options_btn_size[1] * btn_y_bottom_ratio))

        self.__exit_btn_pos_size = (self.exit_pos[0] - round(self.exit_btn_size[0] * btn_x_left_ratio),
                                    self.exit_pos[1] - round(self.exit_btn_size[1] * btn_y_top_ratio),
                                    round(self.exit_btn_size[0] * btn_x_right_ratio),
                                    round(self.exit_btn_size[1] * btn_y_bottom_ratio))
        self.__btn_colors = [gv.ORANGE, gv.ORANGE, gv.ORANGE, gv.ORANGE]

    """ METHODS """
    def show_screen(self, btn_hover, btn_press):
        self.surface.fill(gv.TANISH_YELLOW)
        if btn_hover != -1:
            self.btn_colors[btn_hover] = gv.YELLOW
        else:
            for i, item in enumerate(self.btn_colors):
                self.btn_colors[i] = gv.ORANGE

        text = self.title_font.render(gv.TITLE_TEXT, True, gv.RED)
        self.surface.blit(text, self.title_pos)

        text = self.author_font.render(gv.AUTHOR_TEXT, True, gv.DARK_RED)
        self.surface.blit(text, self.author_pos)

        pygame.draw.rect(self.surface, self.btn_colors[0], self.p1_btn_pos_size)
        text = self.btn_font.render(gv.BUTTON_TEXTS[0], True, gv.BLACK)
        self.surface.blit(text, self.p1_start_pos)

        pygame.draw.rect(self.surface, self.btn_colors[1], self.p2_btn_pos_size)
        text = self.btn_font.render(gv.BUTTON_TEXTS[1], True, gv.BLACK)
        self.surface.blit(text, self.p2_start_pos)

        pygame.draw.rect(self.surface, self.btn_colors[2], self.options_btn_pos_size)
        text = self.btn_font.render(gv.BUTTON_TEXTS[2], True, gv.BLACK)
        self.surface.blit(text, self.options_pos)

        pygame.draw.rect(self.surface, self.btn_colors[3], self.exit_btn_pos_size)
        text = self.btn_font.render(gv.BUTTON_TEXTS[3], True, gv.BLACK)
        self.surface.blit(text, self.exit_pos)

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
    def title_pos(self):
        return self.__title_pos

    @property
    def author_font(self):
        return self.__author_font

    @property
    def author_pos(self):
        return self.__author_pos

    @property
    def btn_font(self):
        return self.__btn_font

    @property
    def p1_start_pos(self):
        return self.__p1_start_pos

    @property
    def p2_start_pos(self):
        return self.__p2_start_pos

    @property
    def options_pos(self):
        return self.__options_pos

    @property
    def exit_pos(self):
        return self.__exit_pos

    @property
    def p1_start_btn_size(self):
        return self.__p1_start_btn_size

    @property
    def p2_start_btn_size(self):
        return self.__p2_start_btn_size

    @property
    def options_btn_size(self):
        return self.__options_btn_size

    @property
    def exit_btn_size(self):
        return self.__exit_btn_size

    @property
    def p1_btn_pos_size(self):
        return self.__p1_btn_pos_size

    @property
    def p2_btn_pos_size(self):
        return self.__p2_btn_pos_size

    @property
    def options_btn_pos_size(self):
        return self.__options_btn_pos_size

    @property
    def exit_btn_pos_size(self):
        return self.__exit_btn_pos_size

    @property
    def btn_colors(self):
        return self.__btn_colors

    """ SETTERS """
    @btn_colors.setter
    def btn_colors(self, btn_colors):
        self.__btn_colors = btn_colors
