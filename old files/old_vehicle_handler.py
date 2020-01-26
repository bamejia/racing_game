from Model.direction import Dir
import math


def vehicle_handler(vehicle):
    # Reactionary Movement
    if vehicle.reaction_speed == 0:
        vehicle.reaction_direction = Dir.NONE
    elif vehicle.reaction_direction == Dir.NORTH:
        vehicle.y -= vehicle.reaction_speed
    elif vehicle.reaction_direction == Dir.NORTHEAST:
        a = int(round(math.sqrt(pow(vehicle.reaction_speed, 2) / 2)))
        vehicle.x += a
        vehicle.y -= a
    elif vehicle.reaction_direction == Dir.EAST:
        vehicle.x += vehicle.reaction_speed
    elif vehicle.reaction_direction == Dir.SOUTHEAST:
        a = int(round(math.sqrt(pow(vehicle.reaction_speed, 2) / 2)))
        vehicle.x += a
        vehicle.y += a
    elif vehicle.reaction_direction == Dir.SOUTH:
        vehicle.y += vehicle.reaction_speed
    elif vehicle.reaction_direction == Dir.SOUTHWEST:
        a = int(round(math.sqrt(pow(vehicle.reaction_speed, 2) / 2)))
        vehicle.x -= a
        vehicle.y += a
    elif vehicle.reaction_direction == Dir.WEST:
        vehicle.x -= vehicle.reaction_speed
    elif vehicle.reaction_direction == Dir.NORTHWEST:
        a = int(round(math.sqrt(pow(vehicle.reaction_speed, 2) / 2)))
        vehicle.x -= a
        vehicle.y -= a

    # Input Movement
    # if vehicle.input_speed == 0:
    #     vehicle.input_direction = Dir.NONE
    if vehicle.input_direction == Dir.NORTH:
        if vehicle.cur_direction == Dir.SOUTHEAST and vehicle.cur_direction == Dir.SOUTH and \
                vehicle.cur_direction == Dir.SOUTHWEST:
            vehicle.input_speed -= vehicle.acceleration
            vehicle.cur_speed = vehicle.input_speed + vehicle.reaction_speed
        else:
            vehicle.input_speed += vehicle.acceleration
            vehicle.cur_direction = Dir.NORTH
    elif vehicle.input_direction == Dir.NORTHEAST:
        if vehicle.cur_direction == Dir.EAST and vehicle.cur_direction == Dir.SOUTHWEST and \
                vehicle.cur_direction == Dir.SOUTH:
            vehicle.input_speed -= vehicle.acceleration
        else:
            vehicle.input_speed += vehicle.acceleration
            vehicle.cur_direction = Dir.NORTHEAST
    elif vehicle.input_direction == Dir.EAST:
        if vehicle.cur_direction == Dir.NORTHWEST and vehicle.cur_direction == Dir.WEST and \
                vehicle.cur_direction == Dir.SOUTHWEST:
            vehicle.input_speed -= vehicle.acceleration
        else:
            vehicle.input_speed += vehicle.acceleration
            vehicle.cur_direction = Dir.EAST
    elif vehicle.input_direction == Dir.SOUTHEAST:
        if vehicle.cur_direction == Dir.WEST and vehicle.cur_direction == Dir.NORTHWEST and \
                vehicle.cur_direction == Dir.NORTH:
            vehicle.input_speed -= vehicle.acceleration
        else:
            vehicle.input_speed += vehicle.acceleration
            vehicle.cur_direction = Dir.SOUTHEAST
    elif vehicle.input_direction == Dir.SOUTH:
        if vehicle.cur_direction == Dir.NORTHWEST and vehicle.cur_direction == Dir.NORTH and \
                vehicle.cur_direction == Dir.NORTHEAST:
            vehicle.input_speed -= vehicle.acceleration
        else:
            vehicle.input_speed += vehicle.acceleration
            vehicle.cur_direction = Dir.SOUTH
    elif vehicle.input_direction == Dir.SOUTHWEST:
        if vehicle.cur_direction == Dir.NORTH and vehicle.cur_direction == Dir.NORTHEAST and \
                vehicle.cur_direction == Dir.EAST:
            vehicle.input_speed -= vehicle.acceleration
        else:
            vehicle.input_speed += vehicle.acceleration
            vehicle.cur_direction = Dir.SOUTHWEST
    elif vehicle.input_direction == Dir.WEST:
        if vehicle.cur_direction == Dir.NORTHEAST and vehicle.cur_direction == Dir.EAST and \
                vehicle.cur_direction == Dir.SOUTHEAST:
            vehicle.input_speed -= vehicle.acceleration
        else:
            vehicle.input_speed += vehicle.acceleration
            vehicle.cur_direction = Dir.WEST
    elif vehicle.input_direction == Dir.NORTHWEST:
        if vehicle.cur_direction == Dir.EAST and vehicle.cur_direction == Dir.SOUTHEAST and \
                vehicle.cur_direction == Dir.SOUTH:
            vehicle.input_speed -= vehicle.acceleration
        else:
            vehicle.input_speed += vehicle.acceleration
            vehicle.cur_direction = Dir.NORTHWEST

    # Player Movement
    if vehicle.cur_speed == 0:
        vehicle.cur_direction = Dir.NONE
    elif vehicle.cur_direction == Dir.NORTH:
        vehicle.y -= vehicle.cur_speed
    elif vehicle.cur_direction == Dir.NORTHEAST:
        a = int(round(math.sqrt(pow(vehicle.cur_speed, 2) / 2)))
        vehicle.x += a
        vehicle.y -= a
    elif vehicle.cur_direction == Dir.EAST:
        vehicle.x += vehicle.cur_speed
    elif vehicle.cur_direction == Dir.SOUTHEAST:
        a = int(round(math.sqrt(pow(vehicle.cur_speed, 2) / 2)))
        vehicle.x += a
        vehicle.y += a
    elif vehicle.cur_direction == Dir.SOUTH:
        vehicle.y += vehicle.cur_speed
    elif vehicle.cur_direction == Dir.SOUTHWEST:
        a = int(round(math.sqrt(pow(vehicle.cur_speed, 2) / 2)))
        vehicle.x -= a
        vehicle.y += a
    elif vehicle.cur_direction == Dir.WEST:
        vehicle.x -= vehicle.cur_speed
    elif vehicle.cur_direction == Dir.NORTHWEST:
        a = int(round(math.sqrt(pow(vehicle.cur_speed, 2) / 2)))
        vehicle.x -= a
        vehicle.y -= a

    # Friction Movement
    if vehicle.cur_speed > 0:
        if vehicle.cur_speed - friction < 0:
            vehicle.cur_speed = 0
        else:
            vehicle.cur_speed -= friction
    # vehicle.cur_speed -= friction
    # vehicle.reaction_speed -= friction
    vehicle.y += traffic_speed  # Default Speed