import pygame

from model.pause_menu import pause
from view.game_view import GameView
from model.game_model import GameModel, check_if_player_is_alive
from controller.player_key_input import player_input
from controller.enemy_input import enemy_input
from model.vehicle_handling.spawn_enemies import spawn_chance
import time


def p1_start(window):
    """  After Single Player is chosen at the title screen (potentially Local 2 Player as well), will call this function
         and create instances of GameView and GameModel to start up a game

    Args:
        window (class Window): contains python.display, python.surface, and python.time.Clock

    Returns:
        None
    """
    game_view = GameView(window, True, True)
    game_model = GameModel()

    all_player_inputs = [None, None]    # Keeps track of each player's inputs
    while True:
        events = pygame.event.get()

        all_player_inputs[0] = player_input(events)
        # if game_model.player2 is not None:
        #     all_player_inputs[1] = player_input2(game_model.vehicles[1], events)

        if True in all_player_inputs:   # If 'enter' or 't' is pressed, will pause the game
            will_escape = pause(True)
            if will_escape:  # If escape is pressed while paused, will break while loop and return to title screen
                break
        elif False in all_player_inputs:    # If escape is pressed, will break while loop and return to title screen
            break
        else:
            enemy_input(game_model.vehicles)

            game_model.update(all_player_inputs)
            game_view.update(game_model.vehicles)

            if not check_if_player_is_alive(game_model.player):     # Breaks while loop if player 1 is dead
                time.sleep(2.5)
                break
            if game_model.player2 is not None and not check_if_player_is_alive(game_model.player2):
                                                                    # Breaks while loop if player 2 is dead
                time.sleep(2.5)
                break

        # print(window.clock.get_fps())
        window.clock.tick(120)
