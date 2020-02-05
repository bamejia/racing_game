import sys
import pygame
import controller.player_key_input as cp

is_paused = False


def pause(input_is_paused):
    pause_repeat = False
    clock = pygame.time.Clock()
    global is_paused
    is_paused = input_is_paused
    while is_paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            keys = pygame.key.get_pressed()
            if not keys[pygame.K_RETURN] and not keys[pygame.K_t]:
                pause_repeat = True
            if keys[pygame.K_ESCAPE] or keys[pygame.K_BACKSPACE]:
                cp.escape_repeat = False
                return True
            if (keys[pygame.K_RETURN] or keys[pygame.K_t]) and pause_repeat:
                is_paused = False
        clock.tick(30)
    return False
