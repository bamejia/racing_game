from controller.player_key_input import title_screen_input
from controller.player_mouse_input import title_screen_mouse_input
from controller.game_choice.online_start import online_start
from view.title_screen_view import TitleScreenView
from view.window import Window
from controller.game_choice.p1_start import p1_start
from controller.game_choice.p2_start import p2_start
import pygame
import sys
import global_variables as gv


class Controller:
    """
    Reads inputs from the user and depending on what they choose, will redirect them to their respective destinations
    It also is the root of the game and all other functions stem from it
    """
    def __init__(self):
        self.window = Window()
        self.title_screen_view = None
        self.btn_func = {   # Functions that will run after a respective button is clicked
            gv.ButtonText.SINGLE_PLAYER.value: lambda: p1_start(self.window),
            gv.ButtonText.LOCAL_2_Player.value: lambda: p2_start(self.window),
            gv.ButtonText.ONLINE_MULTIPLAYER.value: lambda: online_start(self.window),
            gv.ButtonText.EXIT.value: lambda: [i for i in (pygame.quit(), sys.exit())]
        }

    def run(self):
        """  The heart of the game, that keeps everything running, and the place from which every other function
             is called

        Returns:
            None
        """

        self.title_screen_view = TitleScreenView(self.window)

        while True:
            events = pygame.event.get()     # Events such as clicking the x button of the window to close or keyboard
                                            # inputs, however key board inputs are mostly gotten from
                                            # pygame.key.get_pressed() for gameplay as it makes it allows for checking
                                            # of continous pressing, rather than a single KEYDOWN event
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            # Checks mouse input by the player
            btn_hover, btn_press, btn_choice = \
                title_screen_mouse_input(self.title_screen_view.all_buttons, mouse, click)

            self.title_screen_view.show_screen(btn_hover, btn_press)    # Displays title screen and the mouse's effect
                                                                        # on the buttons
            title_screen_input(events)  # Checks for key inputs by the player at the title screen

            if btn_choice is not None:  # Based on the player's clicks, will choose a button option
                self.btn_func[btn_choice]()

            # print(self.window.clock.get_fps())
            self.window.clock.tick(120)

