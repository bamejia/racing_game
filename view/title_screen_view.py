import pygame
import pygame_gui
import global_variables as gv
from view.button import Button

btn_x_left_ratio = 1 / 50
btn_x_right_ratio = 52 / 50
btn_y_top_ratio = 4 / 50
btn_y_bottom_ratio = 51 / 50


class TitleScreenView:
    def __init__(self, window):
        pygame.font.init()

        self.display = window.display
        self.surface = window.surface
        self.gui_manager = window.gui_manager

        """ Making buttons """
        title_y_placement = round(gv.WINDOW_L * 6 / 30)
        self.title_btn = Button(gv.TITLE_FONT, gv.TITLE_TEXT, gv.TITLE_TEXT_SIZE, True, 0, title_y_placement,
                                gv.RED, False)  # Labeled as buttons, but are purely for placing on screen

        author_y_placement = round(gv.WINDOW_L * 10 / 30)
        self.author_btn = Button(gv.BUTTON_FONT, gv.AUTHOR_TEXT, gv.BUTTON_TEXT_SIZE, True, 0, author_y_placement,
                                 gv.DARK_RED, False)

        p1_btn_y_placement = round(gv.WINDOW_L * 15 / 30)
        self.p1_btn = Button(gv.BUTTON_FONT, gv.BUTTON_TEXTS[0], gv.BUTTON_TEXT_SIZE, True, 0, p1_btn_y_placement)

        p2_btn_y_placement = round(gv.WINDOW_L * 18 / 30)
        self.p2_btn = Button(gv.BUTTON_FONT, gv.BUTTON_TEXTS[1], gv.BUTTON_TEXT_SIZE, True, 0, p2_btn_y_placement)

        options_btn_y_placement = round(gv.WINDOW_L * 21 / 30)
        self.options_btn = Button(gv.BUTTON_FONT, gv.BUTTON_TEXTS[2], gv.BUTTON_TEXT_SIZE, True, 0, options_btn_y_placement)

        exit_btn_y_placement = round(gv.WINDOW_L * 24 / 30)
        self.exit_btn = Button(gv.BUTTON_FONT, gv.BUTTON_TEXTS[3], gv.BUTTON_TEXT_SIZE, True, 0, exit_btn_y_placement)

        self.all_buttons = {
            gv.BUTTON_TEXTS[0]: self.p1_btn,
            gv.BUTTON_TEXTS[1]: self.p2_btn,
            gv.BUTTON_TEXTS[2]: self.options_btn,
            gv.BUTTON_TEXTS[3]: self.exit_btn,
        }

        self.cur_btn_colors = {     # Color state of each button
            gv.BUTTON_TEXTS[0]: gv.ORANGE,
            gv.BUTTON_TEXTS[1]: gv.ORANGE,
            gv.BUTTON_TEXTS[2]: gv.ORANGE,
            gv.BUTTON_TEXTS[3]: gv.ORANGE
        }

        # y_placement = round(gv.WINDOW_L * 28 / 30)
        # self.new_btn = Button(gv.BUTTON_FONT, gv.BUTTON_TEXTS[0], gv.BUTTON_TEXT_SIZE, True, 0, y_placement)



    """ METHODS """
    def show_screen(self, btn_hover, btn_press):
        self.surface.fill(gv.TANISH_YELLOW)
        self.cur_btn_colors = {i: gv.ORANGE for i in self.cur_btn_colors}   # Resets color of buttons
        if btn_hover is not None:   # If mouse is hovering or clicking a button, will change their color respectively
            self.cur_btn_colors[btn_hover] = gv.MID_DARK_PEACH
            if btn_press:
                self.cur_btn_colors[btn_hover] = gv.YELLOW

        self.title_btn.draw(self.surface)
        self.author_btn.draw(self.surface)
        [self.all_buttons[btn].draw(self.surface, self.cur_btn_colors[btn]) for btn in self.all_buttons]
        # self.p1_btn.draw(self.surface, self.cur_btn_colors[gv.BUTTON_TEXTS[0]])
        # self.p2_btn.draw(self.surface, self.cur_btn_colors[gv.BUTTON_TEXTS[1]])
        # self.options_btn.draw(self.surface, self.cur_btn_colors[gv.BUTTON_TEXTS[2]])
        # self.exit_btn.draw(self.surface, self.cur_btn_colors[gv.BUTTON_TEXTS[3]])

        self.display.update()
