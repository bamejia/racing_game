import global_variables as gv
import pygame


# CONSTANTS
line_width = gv.ROAD_W * 1 / 62
line_length = gv.ROAD_L * 1 / 20
blank_space = gv.ROAD_L * 1 / 8
lines_in_a_column = gv.WINDOW_L / (line_length + blank_space) + 2
lines_in_a_row = 4
white_line_speed = round(gv.TRAFFIC_SPEED * 9 / 4)  # 9 / 6
white_line_x_placement = gv.ROAD_X_PLACEMENT

# GLOBAL VARIABLES
white_line_y_placement = -line_length - blank_space
white_line_y_placement_staggered = (-line_length - blank_space) / 7


def display_race(view, vehicles):

    """ draws background """
    view.surface.fill(gv.DARK_GREEN)
    view.surface.blit(view.street, (gv.ROAD_X_PLACEMENT, 0))

    draw_white_lines(view.surface)
    # surface.blit(potato[potatoIndex], (player.x, player.y))
    # surface.blit(player_car, (player.x, player.y))

    """ draws all the cars on screen """
    for i, item in enumerate(vehicles):
        view.surface.blit(view.vehicle_types[vehicles[i].movement_pattern], (vehicles[i].x, vehicles[i].y))


def draw_white_lines(surface):
    global white_line_y_placement
    global white_line_y_placement_staggered
    road_division = round(gv.ROAD_W / (lines_in_a_row+1))
    half_line_width = round(line_width/2)
    i = 1
    j = 0
    while j < (line_length + blank_space) * lines_in_a_column:  # Draws each traffic line depending on set variables
        while i <= lines_in_a_row:
            pygame.draw.rect(surface, gv.VERY_LIGHT_GREY, (white_line_x_placement + road_division*i - half_line_width,
                                                           white_line_y_placement + j,
                                                           line_width, line_length))
            i += 1
        i = 1
        j += line_length + blank_space

    # Draws white lines on the side of the road
    pygame.draw.rect(surface, gv.VERY_LIGHT_GREY, (gv.ROAD_X_PLACEMENT, 0, line_width, gv.WINDOW_L))
    pygame.draw.rect(surface, gv.VERY_LIGHT_GREY, (gv.ROAD_X_PLACEMENT + gv.ROAD_W - line_width, 0, line_width, gv.WINDOW_L))

    # Moves lines down every frame according to the set variable, white_line_speed
    white_line_y_placement = (white_line_y_placement + white_line_speed) % (line_length + blank_space) - \
                             (line_length + blank_space)
    white_line_y_placement_staggered = (white_line_y_placement + white_line_speed) % (line_length + blank_space) - \
                             (line_length + blank_space) / 7
