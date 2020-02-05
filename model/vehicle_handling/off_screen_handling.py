from global_variables import WINDOW_L, PLAYER_LENGTH
import model.vehicle_handling.spawn_enemies as spawn

off_screen_distance = PLAYER_LENGTH


def check_if_below_screen(vehicle):
    if vehicle.y > WINDOW_L + off_screen_distance:
        return True
    return False


def despawn(vehicle, vehicles):
    """ removes input vehicle from input list of vehicles, essentially, despawning them """
    index = vehicles.index(vehicle)
    if vehicles[index].movement_pattern == "tracker":
        spawn.tracker_cars -= 1
    del vehicles[index]
    while index < len(vehicles):
        vehicles[index].index = index
        index += 1
