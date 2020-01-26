from model.vehicle_handling.vehicle import Player, Enemy
from model.vehicle_handling.spawn_enemies import spawn_chance


class Model:
    # player = Player(400, 400, 20, 20, 1, 8, 1, 8)
    # vehicles.append(Enemy(1, "enemy car", 400, 500))
    def __init__(self):
        self.vehicles = [Player(0)]
        self.player = self.vehicles[0]

    # methods
    def update(self):
        spawn_chance(self.vehicles)

        # updates location of all vehicles
        for i, item in enumerate(self.vehicles):
            self.vehicles[i].move(self.vehicles)

        # checks for which vehicle to despawn next
        for i, item in enumerate(self.vehicles):
            if isinstance(self.vehicles[i], Enemy):
                self.vehicles[i].check_to_despawn(self.vehicles)

    # getters
    @property
    def vehicles(self):
        return self.__vehicles

    @property
    def player(self):
        return self.__player

    # setters
    @vehicles.setter
    def vehicles(self, vehicles):
        self.__vehicles = vehicles

    @player.setter
    def player(self, player):
        self.__player = player
