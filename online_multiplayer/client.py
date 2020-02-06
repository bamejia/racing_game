import socket
import json
from model.direction import Dir
from model.game_model import GameModel
import model.vehicle_handling.vehicle as v


class Client:
    def __init__(self, server_addr):
        self.__client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__server_addr = server_addr
        self.__player_index = self.connect()

    """ METHODS """
    def connect(self):
        """
        connects to server
        :return:
        player index (0:player 1 | 1:player 2)
        if could not connect, returns None
        """
        # http_request = f'GET / HTTP/1.1\r\nHost:{self.server_addr[0]}\r\n\r\n'
        self.client.connect(self.server_addr)
        js = json.loads(self.client.recv(2048 * 2))
        return js

    """ METHODS """
    def communicate(self, player_inputs):
        """
        sending and receiving off information between the client and server
        :param player_inputs:
        player movement inputs of their vehicle
        :return:
        GameModel object
        """
        if isinstance(player_inputs, Dir):
            player_input = player_inputs.name
            self.client.sendall(json.dumps(player_input).encode())
        else:
            player_input = "false"
            self.client.sendall(player_input.encode())
        try:
            # json_string = self.client.recv(1024*20).decode()  # 1024 * 63
            # if json_string == "none":
            #     return None
            input_string = self.client.recv(1024*40)
            # if input_string == "ready":
            #     print("READY:", input_string)
            #     return True
            if input_string == 'none':
                return None
            input_vehicles = json.loads(input_string)

            new_vehicles = []
            i = 0
            if len(input_vehicles) % 4 != 0:
                print("MISSING DATA")
                return None
            while i < len(input_vehicles):
                if 'player' in input_vehicles[i]:
                    new_vehicles.append(v.Player(i / 4, input_vehicles[i], input_vehicles[i+1], input_vehicles[i+2],
                                                 _health=input_vehicles[i+3]))
                else:
                    new_vehicles.append(v.Enemy(i / 4, input_vehicles[i], input_vehicles[i + 1], input_vehicles[i + 2],
                                        _health=input_vehicles[i + 3]))
                i += 4
            # print(new_vehicles)
            return new_vehicles

            # obj = GameModel.from_json(json_string)
            # return obj
        except Exception as err:
            print("ERROR IN receiving:", err)
            return None

    """ GETTERS """
    @property
    def client(self):
        return self.__client

    @property
    def server_addr(self):
        return self.__server_addr

    @property
    def player_index(self):
        return self.__player_index
