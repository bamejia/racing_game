import pygame
# import global_variables as gv
from global_variables import BLACK, WINDOW_W


btn_x_left_ratio = 3 / 50
btn_x_right_ratio = 55 / 50
btn_y_top_ratio = 4 / 50
btn_y_bottom_ratio = 51 / 50


class Label:
    def __init__(self, font, text, text_size, center_text_horizontally=False, input_width=0, input_length=0,
                 text_color=BLACK, bg=False):
        self.btn_font = pygame.font.Font(font, text_size)
        self.btn_size = self.btn_font.size(text)
        self.bg = bg

        # title_x_placement = 0
        if center_text_horizontally:
            title_x_placement = round(WINDOW_W / 2 - self.btn_size[0] / 2)
        else:
            title_x_placement = input_width
        title_y_placement = round(input_length)

        self.btn_pos = (title_x_placement, title_y_placement)

        self.btn_pos_size = (self.btn_pos[0] - round(self.btn_size[0] * btn_x_left_ratio),
                             self.btn_pos[1] - round(self.btn_size[1] * btn_y_top_ratio),
                             round(self.btn_size[0] * btn_x_right_ratio),
                             round(self.btn_size[1] * btn_y_bottom_ratio))

        self.text = self.btn_font.render(text, True, text_color)

    def draw(self, surface, color=BLACK):
        if self.bg:
            pygame.draw.rect(surface, color, self.btn_pos_size)
        surface.blit(self.text, self.btn_pos)


class Button:
    def __init__(self, font, text, text_size, center_text_horizontally=False, input_width=0, input_length=0,
                 text_color=BLACK, bg=True):
        self.btn_font = pygame.font.Font(font, text_size)
        self.btn_size = self.btn_font.size(text)
        self.bg = bg

        title_x_placement = 0
        if center_text_horizontally:
            title_x_placement = round(WINDOW_W / 2 - self.btn_size[0] / 2)
        else:
            title_x_placement = input_width
        title_y_placement = round(input_length)

        self.btn_pos = (title_x_placement, title_y_placement)

        self.btn_pos_size = (self.btn_pos[0] - round(self.btn_size[0] * btn_x_left_ratio),
                             self.btn_pos[1] - round(self.btn_size[1] * btn_y_top_ratio),
                             round(self.btn_size[0] * btn_x_right_ratio),
                             round(self.btn_size[1] * btn_y_bottom_ratio))

        self.text = self.btn_font.render(text, True, text_color)

    def draw(self, surface, color=BLACK):
        if self.bg:
            pygame.draw.rect(surface, color, self.btn_pos_size)
        surface.blit(self.text, self.btn_pos)

