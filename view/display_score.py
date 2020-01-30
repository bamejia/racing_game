import global_variables as gv
import pygame

pygame.font.init()
score_text_size = 80

score_font = pygame.font.Font(None, score_text_size)
score_y_placement = round(gv.WINDOW_L * 1 / 30)


def display_score(view, vehicle):

    score = str(vehicle.score)
    score_w = 0
    character_w = score_font.size(score[0])[0]

    """ gets width of each character and adds them together"""
    for n in enumerate(score):
        score_w += character_w

    score_x_placement = round((gv.WINDOW_W / 2) - (score_w / 2))

    """ renders each character spaced out by their individual widths """
    for i, item in enumerate(score):
        view.surface.blit(score_font.render(score[i], 255, gv.WHITE, gv.BLACK),
                          (score_x_placement + character_w * i, score_y_placement))


