from model.direction import Dir
import model.vehicle_handling.collision_and_boundaries as cb
import global_variables as gv

# final variables
acceleration_marker = 0
acceleration_MOD = 6
handling_marker = 0
handling_MOD = 5


def vehicle_movement_handler(vehicle, other_vehicles):

    # Input Movement
    input_handler(vehicle)

    # Current Movement
    # vehicle.x_input_against_x_reaction()
    # vehicle.y_input_against_y_reaction()
    vehicle.cur_x_vel = vehicle.input_x_vel # + vehicle.reaction_x_vel
    vehicle.cur_y_vel = vehicle.input_y_vel + gv.TRAFFIC_SPEED #+ vehicle.reaction_y_vel

    # Update Position
    vehicle.x += vehicle.cur_x_vel
    vehicle.y += vehicle.cur_y_vel

    # Check Collision and Boundaries
    collision_and_boundary_handler(vehicle, other_vehicles)

    friction_handler(vehicle)


def input_handler(vehicle):
    # Input Movement
    if vehicle.input_direction == Dir.NORTH:
        vehicle.acceleration_count = (vehicle.acceleration_count - 1) % acceleration_MOD
        if vehicle.acceleration_count == acceleration_marker:
            vehicle.acceleration_on_input_y_vel(-vehicle.acceleration)
    elif vehicle.input_direction == Dir.NORTHEAST:
        vehicle.acceleration_count = (vehicle.acceleration_count - 1) % acceleration_MOD
        vehicle.handling_count = (vehicle.handling_count + 1) % handling_MOD
        if vehicle.handling_count == handling_marker:
            vehicle.acceleration_on_input_x_vel(vehicle.handling)
        if vehicle.acceleration_count == acceleration_marker:
            vehicle.acceleration_on_input_y_vel(-vehicle.acceleration)
    elif vehicle.input_direction == Dir.EAST:
        vehicle.handling_count = (vehicle.handling_count + 1) % handling_MOD
        if vehicle.handling_count == handling_marker:
            vehicle.acceleration_on_input_x_vel(vehicle.handling)
    elif vehicle.input_direction == Dir.SOUTHEAST:
        vehicle.acceleration_count = (vehicle.acceleration_count + 1) % acceleration_MOD
        vehicle.handling_count = (vehicle.handling_count + 1) % handling_MOD
        if vehicle.handling_count == handling_marker:
            vehicle.acceleration_on_input_x_vel(vehicle.handling)
        if vehicle.acceleration_count == acceleration_marker:
            vehicle.acceleration_on_input_y_vel(vehicle.acceleration)
    elif vehicle.input_direction == Dir.SOUTH:
        vehicle.acceleration_count = (vehicle.acceleration_count + 1) % acceleration_MOD
        if vehicle.acceleration_count == acceleration_marker:
            vehicle.acceleration_on_input_y_vel(vehicle.acceleration)
    elif vehicle.input_direction == Dir.SOUTHWEST:
        vehicle.acceleration_count = (vehicle.acceleration_count + 1) % acceleration_MOD
        vehicle.handling_count = (vehicle.handling_count - 1) % handling_MOD
        if vehicle.handling_count == handling_marker:
            vehicle.acceleration_on_input_x_vel(-vehicle.handling)
        if vehicle.acceleration_count == acceleration_marker:
            vehicle.acceleration_on_input_y_vel(vehicle.acceleration)
    elif vehicle.input_direction == Dir.WEST:
        vehicle.handling_count = (vehicle.handling_count - 1) % handling_MOD
        if vehicle.handling_count == handling_marker:
            vehicle.acceleration_on_input_x_vel(-vehicle.handling)
    elif vehicle.input_direction == Dir.NORTHWEST:
        vehicle.acceleration_count = (vehicle.acceleration_count - 1) % acceleration_MOD
        vehicle.handling_count = (vehicle.handling_count - 1) % handling_MOD
        if vehicle.handling_count == handling_marker:
            vehicle.acceleration_on_input_x_vel(-vehicle.handling)
        if vehicle.acceleration_count == acceleration_marker:
            vehicle.acceleration_on_input_y_vel(-vehicle.acceleration)


def collision_and_boundary_handler(vehicle, other_vehicles):
    collided_vehicle = cb.check_all_collision(vehicle, other_vehicles)
    if collided_vehicle is not None:
        collided_vehicle.reaction_x_vel = int(round(vehicle.cur_x_vel * 14 / 13))
        collided_vehicle.reaction_y_vel = int(round((vehicle.cur_y_vel - gv.TRAFFIC_SPEED) * 14 / 13))

        collided_vehicle.reaction_on_input_x_vel()
        collided_vehicle.reaction_on_input_y_vel()

        vehicle.reaction_x_vel = int(round(collided_vehicle.cur_x_vel * 5 / 13))
        vehicle.reaction_y_vel = int(round((collided_vehicle.cur_y_vel - gv.TRAFFIC_SPEED) * 5 / 13))

        vehicle.reaction_on_input_x_vel()
        vehicle.reaction_on_input_y_vel()

        """ prevents cars from going into each other """
        if vehicle.x > collided_vehicle.x:
            if vehicle.y > collided_vehicle.y:
                if abs(vehicle.x - (collided_vehicle.x + collided_vehicle.w)) > \
                        abs(vehicle.y - (collided_vehicle.y + collided_vehicle.l)):
                    vehicle.y = collided_vehicle.y + collided_vehicle.l
                else:
                    vehicle.x = collided_vehicle.x + collided_vehicle.w
            else:
                if abs(vehicle.x - (collided_vehicle.x + collided_vehicle.w)) > \
                        abs((vehicle.y + vehicle.l) - collided_vehicle.y):
                    vehicle.y = collided_vehicle.y - vehicle.l
                else:
                    vehicle.x = collided_vehicle.x + collided_vehicle.w
        else:
            if vehicle.y > collided_vehicle.y:
                if abs((vehicle.x + vehicle.w) - collided_vehicle.x) > \
                        abs(vehicle.y - (collided_vehicle.y + collided_vehicle.l)):
                    vehicle.y = collided_vehicle.y + collided_vehicle.l
                else:
                    vehicle.x = collided_vehicle.x - vehicle.w
            else:
                if abs((vehicle.x + vehicle.w) - collided_vehicle.x) > \
                        abs((vehicle.y + vehicle.l) - collided_vehicle.y):
                    vehicle.y = collided_vehicle.y - vehicle.l
                else:
                    vehicle.x = collided_vehicle.x - vehicle.w

        vehicle.health -= 5
        collided_vehicle.health -= 5

    # vehicle.x_input_against_x_reaction()
    # vehicle.y_input_against_y_reaction()

    # Check vehicle to remain within boundaries
    cb.check_boundary(vehicle)

    if not cb.check_on_road(vehicle):  # Check if off road to add more friction
        vehicle.off_road_on_input_y_vel(1)
        # vehicle.reaction_y_vel += 1


def friction_handler(vehicle):
    # FRICTION
    # if vehicle.input_x_vel == 0 or vehicle.input_y_vel == 0:
    vehicle.friction_count = (vehicle.friction_count+1) % (vehicle.friction_marker + 1)
    # else:
    #     vehicle.friction_count = 0
    if vehicle.friction_count == vehicle.friction_marker:
        if vehicle.input_x_vel > 0:
            if vehicle.input_x_vel - gv.FRICTION < 0:
                vehicle.friction_on_input_x_vel(0)
            else:
                vehicle.friction_on_input_x_vel(vehicle.input_x_vel - gv.FRICTION)
        elif vehicle.input_x_vel < 0:
            if vehicle.input_x_vel + gv.FRICTION > 0:
                vehicle.friction_on_input_x_vel(0)
            else:
                vehicle.friction_on_input_x_vel(vehicle.input_x_vel + gv.FRICTION)
        if vehicle.input_y_vel > 0:
            if vehicle.input_y_vel - gv.FRICTION < 0:
                vehicle.friction_on_input_y_vel(0)
            else:
                vehicle.friction_on_input_y_vel(vehicle.input_y_vel - gv.FRICTION)
        elif vehicle.input_y_vel < 0:
            if vehicle.input_y_vel + gv.FRICTION > 0:
                vehicle.friction_on_input_y_vel(0)
            else:
                vehicle.friction_on_input_y_vel(vehicle.input_y_vel + gv.FRICTION)

        # FRICTION on Reaction
        if vehicle.reaction_x_vel > 0:
            if vehicle.reaction_x_vel - gv.REACTION_FRICTION < 0:
                vehicle.reaction_x_vel = 0
            else:
                vehicle.reaction_x_vel -= gv.REACTION_FRICTION
        elif vehicle.reaction_x_vel < 0:
            if vehicle.reaction_x_vel + gv.REACTION_FRICTION > 0:
                vehicle.reaction_x_vel = 0
            else:
                vehicle.reaction_x_vel += gv.REACTION_FRICTION
        if vehicle.reaction_y_vel > 0:
            if vehicle.reaction_y_vel - gv.REACTION_FRICTION < 0:
                vehicle.reaction_y_vel = 0
            else:
                vehicle.reaction_y_vel -= gv.REACTION_FRICTION
        elif vehicle.reaction_y_vel < 0:
            if vehicle.reaction_y_vel + gv.REACTION_FRICTION > 0:
                vehicle.reaction_y_vel = 0
            else:
                vehicle.reaction_y_vel += gv.REACTION_FRICTION
