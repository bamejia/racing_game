import pygame
import global_variables as gv

top_big_healthbar_l_ratio = 1 / 20
left_big_healthbar_w_ratio = 1 / 40
right_big_healthbar_w_ratio = 22 / 40

top_left_health_border_x_placement = round(gv.WINDOW_W * left_big_healthbar_w_ratio)
top_left_health_border_y_placement = round(gv.WINDOW_L * top_big_healthbar_l_ratio)

top_right_health_border_x_placement = round(gv.WINDOW_W * right_big_healthbar_w_ratio)
top_right_health_border_y_placement = round(gv.WINDOW_L * top_big_healthbar_l_ratio)


def display_health(surface, vehicle):
    # top_left_health_border_x_placement = WINDOW_W * big_healthbar_w_ratio
    # top_left_health_border_x_placement = int(round(WINDOW_W / 120))
    # top_health_border_x_thickness = WINDOW_W/600
    # top_health_border_x_thickness = WINDOW_L / 432

    # health on top of car
    pygame.draw.rect(surface, gv.BLACK, (vehicle.x - round(gv.WINDOW_W/120) - gv.WINDOW_W/600, vehicle.y +
                                      round(vehicle.l * 4 / 5) - gv.WINDOW_L/432,
                                      round(gv.WINDOW_W / 24) + 2, 3 + 2))
    pygame.draw.rect(surface, gv.RED, (vehicle.x - round(gv.WINDOW_W/120), vehicle.y + round(vehicle.l * 4 / 5),
                                    round(gv.WINDOW_W / 24), 3))
    pygame.draw.rect(surface, gv.GREEN, (vehicle.x - 10, vehicle.y + round(vehicle.l * 4 / 5),
                                      vehicle.health / 20, 3))
    
    if vehicle.movement_pattern == "player2":
        # health in top right
        pygame.draw.rect(surface, gv.BLACK, (round(top_right_health_border_x_placement) - 1,
                                          round(top_right_health_border_y_placement) - 1,
                                          round(gv.PLAYER_STARTING_HEALTH / 2) + 2, 20 + 2))
        pygame.draw.rect(surface, gv.RED, (round(top_right_health_border_x_placement),
                                        round(top_right_health_border_y_placement),
                                        gv.PLAYER_STARTING_HEALTH / 2, 20))
        pygame.draw.rect(surface, gv.GREEN, (round(top_right_health_border_x_placement),
                                          round(top_right_health_border_y_placement),
                                          round(vehicle.health / 2), 20))
        return

    # health in top left
    pygame.draw.rect(surface, gv.BLACK, (round(top_left_health_border_x_placement) - 1,
                                      round(top_left_health_border_y_placement) - 1,
                                      round(gv.PLAYER_STARTING_HEALTH / 2) + 2, 20 + 2))
    pygame.draw.rect(surface, gv.RED, (round(top_left_health_border_x_placement),
                                    round(top_left_health_border_y_placement),
                                    gv.PLAYER_STARTING_HEALTH / 2, 20))
    pygame.draw.rect(surface, gv.GREEN, (round(top_left_health_border_x_placement),
                                      round(top_left_health_border_y_placement),
                                      round(vehicle.health / 2), 20))

