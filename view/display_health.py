import pygame
import global_variables as gv


""" CONSTANTS """
top_big_healthbar_l_ratio = 1 / 20
left_big_healthbar_w_ratio = 1 / 40
right_big_healthbar_w_ratio = 45 / 80

top_left_health_x_placement = round(gv.WINDOW_W * left_big_healthbar_w_ratio)
top_left_health_y_placement = round(gv.WINDOW_L * top_big_healthbar_l_ratio)

top_right_health_x_placement = round(gv.WINDOW_W * right_big_healthbar_w_ratio)
top_right_health_y_placement = round(gv.WINDOW_L * top_big_healthbar_l_ratio)

top_health_width = round(gv.WINDOW_W / 2.4)
top_health_length = 20

top_health_border_x_shift = 3
top_health_border_y_shift = 3
top_health_border_width = 6
top_health_border_length = 6

health_on_car_x_shift = round(gv.WINDOW_W/120)
health_on_car_x_border_shift = round(gv.WINDOW_W/800)
health_on_car_y_border_shift = round(gv.WINDOW_L/600)
health_on_car_width = round(gv.WINDOW_W/24)
health_on_car_length = round(gv.WINDOW_L/288)
health_on_car_border_x_extender = round(gv.WINDOW_W/600)
health_on_car_border_y_extender = round(gv.WINDOW_L / 386)


def display_health(surface, vehicle):

    # health on top of car
    pygame.draw.rect(surface, gv.BLACK, (vehicle.x - health_on_car_x_shift - health_on_car_x_border_shift, vehicle.y +
                                         round(vehicle.l * 4 / 5) - health_on_car_y_border_shift,
                                         health_on_car_width + health_on_car_border_x_extender, health_on_car_length +
                                         health_on_car_border_y_extender))
    pygame.draw.rect(surface, gv.RED, (vehicle.x - health_on_car_x_shift, vehicle.y + round(vehicle.l * 4 / 5),
                                       health_on_car_width, health_on_car_length))
    pygame.draw.rect(surface, gv.GREEN, (vehicle.x - health_on_car_x_shift, vehicle.y + round(vehicle.l * 4 / 5),
                                         round(health_on_car_width * (vehicle.health / gv.PLAYER_STARTING_HEALTH)),
                                         health_on_car_length))
    
    if vehicle.movement_pattern == "player2":
        # health in top right
        pygame.draw.rect(surface, gv.BLACK, (top_right_health_x_placement - top_health_border_x_shift,
                                             top_right_health_y_placement - top_health_border_y_shift,
                                             top_health_width + top_health_border_width,
                                             top_health_length + top_health_border_length))
        pygame.draw.rect(surface, gv.RED, (top_right_health_x_placement,
                                           top_right_health_y_placement,
                                           top_health_width, top_health_length))
        pygame.draw.rect(surface, gv.GREEN, (top_right_health_x_placement,
                                             top_right_health_y_placement,
                                             round(top_health_width * (vehicle.health / gv.PLAYER_STARTING_HEALTH)),
                                             top_health_length))
        return

    # health in top left
    pygame.draw.rect(surface, gv.BLACK, (top_left_health_x_placement - top_health_border_x_shift,
                                         top_left_health_y_placement - top_health_border_y_shift,
                                         top_health_width + top_health_border_width,
                                         top_health_length + top_health_border_length))
    pygame.draw.rect(surface, gv.RED, (top_left_health_x_placement,
                                       top_left_health_y_placement,
                                       top_health_width, top_health_length))
    pygame.draw.rect(surface, gv.GREEN, (top_left_health_x_placement,
                                         top_left_health_y_placement,
                                         round(top_health_width * (vehicle.health / gv.PLAYER_STARTING_HEALTH)),
                                         top_health_length))

