import pygame
from model.pause_menu import pause
from model.direction import Dir
import global_variables as gv
import sys

pause_repeat = True
escape_repeat = True


def title_screen_input(events):
    global escape_repeat
    for event in events:
        keys = pygame.key.get_pressed()
        # num_of_keys = keys.count(True)

        if not keys[pygame.K_ESCAPE] and not keys[pygame.K_BACKSPACE]:
            escape_repeat = True

        if event.type == pygame.QUIT or (keys[pygame.K_ESCAPE] and escape_repeat):
            pygame.quit()
            sys.exit()


def player_input(player, events):
    global pause_repeat
    global escape_repeat
    for event in events:
        keys = pygame.key.get_pressed()
        # num_of_keys = keys.count(True)

        if not keys[pygame.K_RETURN] and not keys[pygame.K_t]:
            pause_repeat = True

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if (keys[pygame.K_ESCAPE] or keys[pygame.K_BACKSPACE]) and escape_repeat:
            escape_repeat = False
            return False
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

        if (keys[pygame.K_RETURN] or keys[pygame.K_t]) and pause_repeat:
            pause_repeat = False
            escape_repeat_ref = [escape_repeat]
            pause(True, escape_repeat_ref)
            if not escape_repeat:
                return False

    return True


def player_input2(player, events):
    global pause_repeat
    global escape_repeat
    for event in events:
        keys = pygame.key.get_pressed()
        # num_of_keys = keys.count(True)

        if not keys[pygame.K_RETURN] and not keys[pygame.K_t]:
            pause_repeat = True

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if (keys[pygame.K_ESCAPE] or keys[pygame.K_BACKSPACE]) and escape_repeat:
            escape_repeat = False
            return False
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

        if (keys[pygame.K_RETURN] or keys[pygame.K_t]) and pause_repeat:
            pause_repeat = False
            escape_repeat_ref = [escape_repeat]
            pause(True, escape_repeat_ref)
            if not escape_repeat:
                return False

    return True
