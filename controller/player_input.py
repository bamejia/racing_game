import pygame
from model.pause_menu import pause
from model.direction import Dir
import global_variables as gv
import sys


def player_input(player):
    for event in pygame.event.get():

        keys = pygame.key.get_pressed()
        # num_of_keys = keys.count(True)

        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
        if keys[pygame.K_UP] and not keys[pygame.K_RIGHT] and not keys[pygame.K_DOWN] and not keys[pygame.K_LEFT]:
            player.input_direction = Dir.NORTH
        elif keys[pygame.K_UP] and keys[pygame.K_RIGHT] and not keys[pygame.K_DOWN] and not keys[pygame.K_LEFT]:
            player.input_direction = Dir.NORTHEAST
        elif not keys[pygame.K_UP] and keys[pygame.K_RIGHT] and not keys[pygame.K_DOWN] and not keys[pygame.K_LEFT]:
            player.input_direction = Dir.EAST
        elif not keys[pygame.K_UP] and keys[pygame.K_RIGHT] and keys[pygame.K_DOWN] and not keys[pygame.K_LEFT]:
            player.input_direction = Dir.SOUTHEAST
        elif not keys[pygame.K_UP] and not keys[pygame.K_RIGHT] and keys[pygame.K_DOWN] and not keys[pygame.K_LEFT]:
            player.input_direction = Dir.SOUTH
        elif not keys[pygame.K_UP] and not keys[pygame.K_RIGHT] and keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
            player.input_direction = Dir.SOUTHWEST
        elif not keys[pygame.K_UP] and not keys[pygame.K_RIGHT] and not keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
            player.input_direction = Dir.WEST
        elif keys[pygame.K_UP] and not keys[pygame.K_RIGHT] and not keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
            player.input_direction = Dir.NORTHWEST
        else:
            player.input_direction = Dir.NONE

        if keys[pygame.K_RETURN]:
            gv.PAUSE = True
            pause()

    return True
