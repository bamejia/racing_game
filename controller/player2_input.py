import pygame
from model.pause_menu import pause
from model.direction import Dir
import global_variables as gv
import sys


def player_input2(player, events):
    pygame.key.set_repeat()
    for event in events:

        keys = pygame.key.get_pressed()
        # num_of_keys = keys.count(True)

        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
        if keys[pygame.K_w] and not keys[pygame.K_a] and not keys[pygame.K_d] and not keys[pygame.K_s]:
            player.input_direction = Dir.NORTH
        elif keys[pygame.K_w] and keys[pygame.K_d] and not keys[pygame.K_a] and not keys[pygame.K_s]:
            player.input_direction = Dir.NORTHEAST
        elif keys[pygame.K_d] and not keys[pygame.K_w] and not keys[pygame.K_a] and not keys[pygame.K_s]:
            player.input_direction = Dir.EAST
        elif keys[pygame.K_d] and keys[pygame.K_s] and not keys[pygame.K_a] and not keys[pygame.K_w]:
            player.input_direction = Dir.SOUTHEAST
        elif keys[pygame.K_s] and not keys[pygame.K_w] and not keys[pygame.K_a] and not keys[pygame.K_d]:
            player.input_direction = Dir.SOUTH
        elif keys[pygame.K_a] and keys[pygame.K_s] and not keys[pygame.K_w] and not keys[pygame.K_d]:
            player.input_direction = Dir.SOUTHWEST
        elif keys[pygame.K_a] and not keys[pygame.K_s] and not keys[pygame.K_w] and not keys[pygame.K_d]:
            player.input_direction = Dir.WEST
        elif keys[pygame.K_a] and not keys[pygame.K_s] and keys[pygame.K_w] and not keys[pygame.K_d]:
            player.input_direction = Dir.NORTHWEST
        else:
            player.input_direction = Dir.NONE

        if keys[pygame.K_BACKSPACE]:
            gv.PAUSE = True
            pause()
    pygame.key.set_repeat(1, 1)
    return True
