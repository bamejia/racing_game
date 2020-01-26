import pygame
from global_variables import RED, GREEN, BLACK, WINDOW_W, WINDOW_L, PLAYER_STARTING_HEALTH

big_healthbar_l_ratio = 1 / 25
big_healthbar_w_ratio = 1 / 30


def display_health(surface, vehicle):
    # top_health_border_x_placement = int(round(WINDOW_W/120))
    # top_health_border_x_placement = int(round(WINDOW_W / 120))
    # top_health_border_x_thickness = WINDOW_W/600
    # top_health_border_x_thickness = WINDOW_L / 432

    # health on top of car
    pygame.draw.rect(surface, BLACK, (vehicle.x - int(round(WINDOW_W/120)) - WINDOW_W/600, vehicle.y +
                                      int(round(vehicle.l * 4 / 5)) - WINDOW_L/432,
                                      int(round(WINDOW_W / 24)) + 2, 3 + 2))
    pygame.draw.rect(surface, RED, (vehicle.x - int(round(WINDOW_W/120)), vehicle.y + int(round(vehicle.l * 4 / 5)),
                                    int(round(WINDOW_W / 24)), 3))
    pygame.draw.rect(surface, GREEN, (vehicle.x - 10, vehicle.y + int(round(vehicle.l * 4 / 5)),
                                      vehicle.health / 20, 3))

    # health in top left
    pygame.draw.rect(surface, BLACK, (int(round(WINDOW_W * big_healthbar_w_ratio)) - 1,
                                      int(round(WINDOW_L * big_healthbar_l_ratio)) - 1,
                                      int(round(PLAYER_STARTING_HEALTH / 2)) + 2, 20 + 2))
    pygame.draw.rect(surface, RED, (int(round(WINDOW_W * big_healthbar_w_ratio)),
                                    int(round(WINDOW_L * big_healthbar_l_ratio)),
                                    PLAYER_STARTING_HEALTH / 2, 20))
    pygame.draw.rect(surface, GREEN, (int(round(WINDOW_W * big_healthbar_w_ratio)),
                                      int(round(WINDOW_L * big_healthbar_l_ratio)),
                                      int(round(vehicle.health / 2)), 20))
