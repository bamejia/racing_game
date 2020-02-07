import pygame
from model.game_model import check_if_player_is_alive
from controller.enemy_input import enemy_input
import time


def game_thread(game):
    """  This function runs in a separate thread on the server and computes all the model class updates.
         The server's main thread reads from the model class passed in the tuple

    Args:
        game (tuple): contains the game's model, player inputs, a mutex lock, and a reference to a boolean to see if
                      the game has ended

    Returns:
        None
    """
    game_model, all_player_inputs, lock, has_ended_ref = game
    clock = pygame.time.Clock()
    while True:
        lock.acquire()
        if game_model.ready:
            enemy_input(game_model.vehicles)
            if False in all_player_inputs:
                print("Game has ended")
                lock.release()
                break
            if has_ended_ref[0]:
                print("Game h4s ended")
                lock.release()
                break

            game_model.update(all_player_inputs)

            if not check_if_player_is_alive(game_model.player) or\
                    not check_if_player_is_alive(game_model.player2):
                time.sleep(2.5)
                lock.release()
                has_ended_ref[0] = True
                break
            lock.release()
        else:
            lock.release()
        # print(clock.get_fps())
        clock.tick(120)
