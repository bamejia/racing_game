import global_variables as gv
import pygame

line_width = 18
line_length = 70
blank_space = 120
white_line_y_placement = -line_length - blank_space
white_line_speed = round(gv.TRAFFIC_SPEED * 9 / 4)


def display_race(view, vehicles):

    """ draws background """
    view.surface.fill(gv.PEACH_PINK)
    view.surface.blit(view.street, (gv.ROAD_X_PLACEMENT, 0))

    draw_white_lines(view.surface)
    # surface.blit(potato[potatoIndex], (player.x, player.y))
    # surface.blit(player_car, (player.x, player.y))

    """ draws all the cars on screen """
    for i, item in enumerate(vehicles):
        view.surface.blit(view.vehicle_types[vehicles[i].movement_pattern], (vehicles[i].x, vehicles[i].y))


def draw_white_lines(surface):
    global white_line_y_placement
    white_line_x_placement = round(gv.ROAD_X_PLACEMENT + (gv.ROAD_W/ 2))
    quarter_road_w = round(gv.ROAD_W / 4)
    half_line_width = round(line_width/2)
    i = 0
    while i < (line_length + blank_space) * 6:
        pygame.draw.rect(surface, gv.VERY_LIGHT_GREY, (white_line_x_placement - quarter_road_w - half_line_width,
                                                        white_line_y_placement + i,
                         line_width, line_length))
        pygame.draw.rect(surface, gv.VERY_LIGHT_GREY, (white_line_x_placement - half_line_width,
                                                        white_line_y_placement + i,
                                                        line_width, line_length))
        pygame.draw.rect(surface, gv.VERY_LIGHT_GREY, (white_line_x_placement + quarter_road_w - half_line_width,
                                                        white_line_y_placement + i,
                                                        line_width, line_length))
        i += line_length + blank_space

    pygame.draw.rect(surface, gv.VERY_LIGHT_GREY, (gv.ROAD_X_PLACEMENT, 0, line_width, gv.WINDOW_L))
    pygame.draw.rect(surface, gv.VERY_LIGHT_GREY, (gv.ROAD_X_PLACEMENT + gv.ROAD_W - line_width, 0, line_width, gv.WINDOW_L))

    white_line_y_placement = (white_line_y_placement + white_line_speed) % (line_length + blank_space) - (line_length + blank_space)
