import pygame
from view.game_view import GameView
from controller.player_text_input import player_text_input2
from model.game_model import GameModel
from controller.player_key_input import player_input, player_input2
from online_multiplayer.client import Client
from online_multiplayer.server import server
import socket
from _thread import start_new_thread
from threading import Lock
from model.direction import Dir


def online_start(window, create_server=False):
    """  After online multiplayer is selected, this function will run and create instances of GameView and GameModel
         Based on whether the user wished to join a server or create their own on a local network, the user will then
         connect to the specified server, and enter a loop that constantly listens for data from the server and displays
         the game as usual.

         The GameModel instance will not be updated in the client, but instead, the car_type, xy positions, and health
          of each vehicle will be calculated on the server and then sent back to the client for display with
          GameView.update()

    Args:
        window (class Window): contains pygame.display, pygame.Surface, and pygame.time.Clock()
        create_server (bool): whether to create a local server or not

    Returns:
        None
    """
    game_view = GameView(window, visible_top_health_bar=True)
    game_model = GameModel(num_players=2, ready=True)

    """ Creates a server on the local computer for LAN use and joins it """
    if create_server:
        hostname = socket.gethostname()
        host_ip = socket.gethostbyname(hostname)
        port = 5555
        server_addr = (host_ip, port)
        start_new_thread(server, (host_ip, port))
    else:
        """ Asks the user for the ip address and port number of the server they wish to join """
        full_input_ip_addr = player_text_input2("Please enter IP address and port of host")
        split_addr = full_input_ip_addr.split(':')
        if len(split_addr) == 2:
            host_ip = split_addr[0]
            try:
                port = int(split_addr[1])
            except Exception as err:
                print("Not a valid port: %s" % err)
                return
        else:
            print('IP Address was not formatted correctly')
            return
        server_addr = (host_ip, port)
        print(server_addr)

    """ Attempts to connect to specified server """
    try:
        client = Client(server_addr)
    except Exception as err:
        print("Can't connect to server:{}".format(err))
        return

    view_thread_run_ref = [False]   # Used to tell when to stop the view thread, after the game is over
    lock = Lock()   # Used to prevent data from being corrupted when reading and writing from different threads
    all_player_inputs = [Dir.NONE, Dir.NONE]
    while True:

        try:
            events = pygame.event.get()
            all_player_inputs[client.player_index] = player_input(events)
            if game_model is not None and game_model.ready:     # While the game is not ready, the game will not display
                                                                # For now, will always be ready.
                                                                # Does not affect gameplay

                input_vehicles = client.communicate(all_player_inputs[client.player_index])
                if input_vehicles is None:  # None is sent from the server when the game has terminated
                    break
                lock.acquire()
                game_model.vehicles = input_vehicles
                lock.release()

                if game_model.vehicles is None:
                    break
                if not view_thread_run_ref[0]:      # Creates a new thread to keep the game frame rate independent of
                                                    # the frequency at which information is obtained from the server
                    view_thread_run_ref[0] = True
                    start_new_thread(view_thread, (game_view, game_model, window, lock, view_thread_run_ref))
            else:  # Will never be called for now
                input_vehicles = client.communicate(all_player_inputs[client.player_index])
                lock.acquire()
                game_model.vehicles = input_vehicles
                lock.release()
                if game_model.vehicles is True:
                    game_model.ready = True
                elif game_model.vehicles is None:
                    break

        except Exception as err:
            print("Online start ERROR:", err)
            break

        # print(window.clock.get_fps())
        window.clock.tick(120)

    view_thread_run_ref[0] = False      # After the game loop ends, this will tell the view_thread to stop


def view_thread(view, model, window, lock, view_thread_run_ref):
    """ The function called in a separate threat that updates the game's visuals """
    try:
        while view_thread_run_ref[0]:
            lock.acquire()
            view.update(model.vehicles)
            lock.release()
            window.clock.tick(120)
    except Exception as err:
        print("VIEW THREAD:", err)
