import pygame
from model.pause_menu import pause
from model.direction import Dir
import global_variables as gv


def player_input(player):
    for event in pygame.event.get():

        keys = pygame.key.get_pressed()
        num_of_keys = keys.count(True)

        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            pygame.quit()
            quit()
        if keys[pygame.K_UP] and num_of_keys == 1:
            player.input_direction = Dir.NORTH
        elif keys[pygame.K_UP] and keys[pygame.K_RIGHT] and num_of_keys == 2:
            player.input_direction = Dir.NORTHEAST
        elif keys[pygame.K_RIGHT] and num_of_keys == 1:
            player.input_direction = Dir.EAST
        elif keys[pygame.K_RIGHT] and keys[pygame.K_DOWN] and num_of_keys == 2:
            player.input_direction = Dir.SOUTHEAST
        elif keys[pygame.K_DOWN] and num_of_keys == 1:
            player.input_direction = Dir.SOUTH
        elif keys[pygame.K_LEFT] and keys[pygame.K_DOWN] and num_of_keys == 2:
            player.input_direction = Dir.SOUTHWEST
        elif keys[pygame.K_LEFT] and num_of_keys == 1:
            player.input_direction = Dir.WEST
        elif keys[pygame.K_UP] and keys[pygame.K_LEFT] and num_of_keys == 2:
            player.input_direction = Dir.NORTHWEST
        else:
            player.input_direction = Dir.NONE

        if keys[pygame.K_RETURN]:
            gv.PAUSE = True
            pause()

    return True
