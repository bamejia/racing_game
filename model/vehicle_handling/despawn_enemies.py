from global_variables import WINDOW_L

off_screen_distance = 300


def check_if_below_screen(vehicle):
    if vehicle.y > WINDOW_L + off_screen_distance:
        return True
    return False


def despawn(vehicle, vehicles):
    index = vehicles.index(vehicle)
    del vehicles[index]
    while index < len(vehicles):
        vehicles[index].index = index
        index += 1
