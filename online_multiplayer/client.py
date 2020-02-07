import socket
import json
from model.direction import Dir
from model.game_model import GameModel
from global_variables import CAR_TYPES
import model.vehicle_handling.vehicle as v


class Client:
    def __init__(self, server_addr):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_addr = server_addr
        self.player_index = self.connect()

    """ METHODS """
    def connect(self):
        """  Connects to server

        Returns:
            int: player index (0:player 1 | 1:player 2)
            None: if unable to connect to server
        """

        self.client.connect(self.server_addr)
        player_number = json.loads(self.client.recv(1024 * 1))
        return player_number

    """ METHODS """
    def communicate(self, player_inputs):
        """  Sending and receiving off information between the client and server

             The server sends a list of the current vehicle type, xy position, and health of each vehicle
             The vehicle type is in CAR_TYPES in global_variables.py, but it is sent as an int
             It also uses the position of the information in the list, as the current vehicle index

             Example: [1, 400, 400, 850] - would be a car with car_type 'player2', x = 400, y = 400, and health at 850.
                                            The index would be 0, as there is only one car in the list

        Args:
            player_inputs (): direction which the player have chosen to move

        Returns:
            list: a list of vehicle objects updated from the server
        """

        if isinstance(player_inputs, Dir):  # Checks to see if an enum Dir, is being sent
            player_input = player_inputs.name
            self.client.sendall(json.dumps(player_input).encode())
        else:   # If a player has quit the game
            player_input = "false"
            self.client.sendall(player_input.encode())
        try:
            input_string = self.client.recv(380).decode()   # Data from the server received as a string
            # if input_string == "ready":
            #     print("READY:", input_string)
            #     return True
            if input_string == 'none':  # If the server returns 'none' then the game has been closed
                return None
            input_vehicles = json.loads(input_string)   # Converts received string into a list

            if len(input_vehicles) % 4 != 0:    # Checks to make sure the correct amount of data has been sent
                print("MISSING DATA")
                return None

            new_vehicles = []
            i = 0
            while i < len(input_vehicles):  # Loops through the list and creates new Vehicle objects based off the
                                            # parameters from the server
                car_type = CAR_TYPES[input_vehicles[i]]
                if 'player' in car_type:    # Checks to see whether it should create a Player object or Enemy object
                    new_vehicles.append(v.Player(i / 4, car_type, input_vehicles[i+1], input_vehicles[i+2],
                                                 _health=input_vehicles[i+3]))
                else:
                    new_vehicles.append(v.Enemy(i / 4, car_type, input_vehicles[i + 1], input_vehicles[i + 2],
                                        _health=input_vehicles[i + 3]))
                i += 4
            return new_vehicles

        except Exception as err:
            print("ERROR IN receiving:", err)
            return None
