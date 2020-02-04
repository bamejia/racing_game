import pygame
from view.game_view import GameView
from model.game_model import GameModel, check_if_player_is_alive
from controller.player_key_input import player_input, player_input2
from controller.enemy_input import enemy_input
from online_multiplayer.client import Client
from online_multiplayer.server import server
import time
import socket
from _thread import start_new_thread
from model.direction import Dir


def online_start(window, create_server=False):
    game_view = GameView(window)
    game_model = None

    if create_server:
        hostname = socket.gethostname()
        host_ip = socket.gethostbyname(hostname)
        port = 5555
        server_addr = (host_ip, port)
        start_new_thread(server, (host_ip, port))
        # server(server_addr)
    else:
        # server_addr = input("Please enter server IP and port to connect to: ")
        hostname = socket.gethostname()
        host_ip = socket.gethostbyname(hostname)
        port = 5555
        server_addr = (host_ip, port)

    try:
        client = Client(server_addr)
    except Exception as err:
        print("Can't connect to server:{}".format(err))
        return

    all_player_inputs = [Dir.NONE, Dir.NONE]
    while True:

        try:
            events = pygame.event.get()
            all_player_inputs[client.player_index] = player_input(events)
            if game_model is not None and game_model.ready:
                # if len(game_model.vehicles) > 1 and game_model.player2.movement_pattern == MOVEMENT_PATTERNS[1]:
                #     player_input2(game_model.vehicles[1], events)

                game_model = client.communicate(all_player_inputs[client.player_index])
                # enemy_input(game_model.vehicles)
                game_view.update(game_model.vehicles)

                if not check_if_player_is_alive(game_model.player) or\
                        not check_if_player_is_alive(game_model.player2):
                    time.sleep(2.5)
                    break
            else:
                try:
                    game_model = client.communicate(all_player_inputs[client.player_index])
                except Exception as err:
                    print("error when assigning to game model:", err)

        except Exception as err:
            print("Online start ERROR:", err)
            break

        # print(window.clock.get_fps())
        window.clock.tick(120)