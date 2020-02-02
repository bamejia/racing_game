import pygame
import socket
from view.game_view import GameView
from model.game_model import GameModel, check_if_player_is_alive
from controller.player_input import player_input, player_input2
from controller.enemy_input import enemy_input
from model.direction import Dir
from _thread import *
from threading import Lock
from model.vehicle_handling.spawn_enemies import spawn_chance
from global_variables import MOVEMENT_PATTERNS
from online_multiplayer.client import Client
import time


def game_thread(game):
    game_model, all_player_inputs, lock, has_ended = game
    clock = pygame.time.Clock()
    # game_view = GameView(window)
    while True:
        lock.acquire()
        try:
            if game_model.ready:
                lock.release()
                enemy_input(game_model.vehicles)
                lock.acquire()
                if False in all_player_inputs:
                    print("Game has ended")
                    lock.release()
                    break
                if has_ended[0]:
                    print("Game h4s ended")
                    break
                # if len(game_model.vehicles) > 1 and game_model.player2.movement_pattern == MOVEMENT_PATTERNS[1]:
                #     player_input2(game_model.vehicles[1], events)
                # print(self.game_model.player.cur_x_vel, self.game_model.player.reaction_x_vel, self.game_model.player.cur_y_vel, self.game_model.player.reaction_y_vel)

                game_model.update(all_player_inputs)
                # game_view.update(game_model.vehicles)

                if not check_if_player_is_alive(game_model.player) or\
                        not check_if_player_is_alive(game_model.player2):
                    time.sleep(2.5)
                    lock.release()
                    break
                lock.release()
            else:
                lock.release()
                pass
            # print(clock.get_fps())
            clock.tick(120)
        except Exception as err:
            print("error in thread:", err)
