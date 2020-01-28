import global_variables as gv
import sys
import pygame


def pause():
    while gv.PAUSE:
        pygame.key.set_repeat()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            keys = pygame.key.get_pressed()
            num_of_keys = keys.count(True)
            if keys[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit()
            if keys[pygame.K_RETURN]:
                gv.PAUSE = False
                pygame.key.set_repeat(1, 1)
