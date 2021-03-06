import sys
import pygame


def pause(is_paused, escape_repeat, pause_repeat=False):
    clock = pygame.time.Clock()
    while is_paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            keys = pygame.key.get_pressed()
            # num_of_keys = keys.count(True)
            if not keys[pygame.K_RETURN] and not keys[pygame.K_t]:
                pause_repeat = True
            if keys[pygame.K_ESCAPE] or keys[pygame.K_BACKSPACE]:
                escape_repeat[0] = False
                return
            if (keys[pygame.K_RETURN] or keys[pygame.K_t]) and pause_repeat:
                is_paused = False
    clock.tick(30)
