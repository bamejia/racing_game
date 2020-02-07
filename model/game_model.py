from model.vehicle_handling.vehicle import Player, Enemy, Vehicle
from model.vehicle_handling.spawn_enemies import spawn_chance
import json


def check_if_player_is_alive(player):
    return player.is_alive()


class GameModel:
    """
        Holds the values of all the current vehicles in the game,
        as well as calculates their movements based on user input
        that is passed when it updates
    """

    # player = Player(400, 400, 20, 20, 1, 8, 1, 8)
    # vehicles.append(Enemy(1, "enemy car", 400, 500))
    def __init__(self, vehicles=None, player=None, player2=None, ready=True, num_players=1):
        """  Creates a list of all vehicles spawned, including the player(s).
             Creates variable(s) that point towards the player(s) to make finding them easier

        Args:
            vehicles (list):    holds all current Vehicle objects that have been spawned
            player (Player):    references player1
            player2 (Player):   references player2, if spawned, otherwise None
            ready (bool):       for online multiplayer, whether all players are connected or not
            num_players (int):  number of players in the game
        """

        self.vehicles = vehicles
        self.player = player
        self.player2 = player2
        self.ready = ready  # For online play, if both players are ready to start
        self.num_players = num_players
        if vehicles is None:
            if num_players == 2:
                self.vehicles = [Player(0), Player(1, "player2", x=600)]
                self.player2 = self.vehicles[1]
                self.ready = ready
            else:
                self.vehicles = [Player(0)]
                self.player2 = player2
            self.player = self.vehicles[0]
        else:
            for i, item in enumerate(self.vehicles):
                if i >= 2:
                    self.vehicles[i] = Enemy.from_json(json.dumps(vehicles[i]))
                elif i < 2:
                    self.vehicles[i] = Player.from_json(json.dumps(vehicles[i]))
            self.player = Player.from_json(json.dumps(player))
            self.player2 = Player.from_json(json.dumps(player2))

    """ METHODS """
    def update(self, player_inputs=None):
        """  Updates the location and state of all the vehicles depending on the inputs by the player(s)

        Args:
            player_inputs (enum Dir): player inputs from a local game

        Returns:
            None
        """

        a = 0
        player_count = 0
        while a < len(self.vehicles) and player_count < self.num_players:
            if "player2" in self.vehicles[a].movement_pattern:
                # print("P2")
                self.player2 = self.vehicles[a]
                player_count += 1
            elif "player" in self.vehicles[a].movement_pattern:
                # print("p!")
                self.player = self.vehicles[a]
                player_count += 1
            else:
                # print("count")
                pass
            a += 1

        spawn_chance(self.vehicles)     # chance to spawn random enemies

        self.player.input_direction = player_inputs[0]
        if self.player2 is not None:
            self.player2.input_direction = player_inputs[1]

        """ updates location of all vehicles """
        for i, item in enumerate(self.vehicles):
            self.vehicles[i].update_location(self.vehicles)

        """ checks for which vehicle to despawn next """
        for i, item in enumerate(self.vehicles):
            if isinstance(self.vehicles[i], Enemy):
                self.vehicles[i].check_to_despawn(self.vehicles)

        if self.player.is_below_screen():   # if player is too far below the window, they will lose health
            self.player.health -= 10
        if self.player2 is not None and self.player2.is_below_screen():
            self.player2.health -= 10

        self.player.score += 1  # player gains points for every frame they are alive

    @staticmethod
    def from_json(json_string):     # converts object from JSON file to GameModel Object
        json_dict = json.loads(json_string)
        return GameModel(**json_dict)
