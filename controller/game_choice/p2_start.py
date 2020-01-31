import pygame
from view.game_view import GameView
from model.game_model import GameModel
from controller.player_input import player_input, player_input2
from controller.enemy_input import enemy_input
from model.vehicle_handling.spawn_enemies import spawn_chance
from global_variables import MOVEMENT_PATTERNS


def p2_start(window):
    game_view = GameView(window)
    game_model = GameModel(2)

    has_not_quit_game = True
    while has_not_quit_game:
        events = pygame.event.get()

        spawn_chance(game_model.vehicles)

        has_not_quit_game = player_input(game_model.player, events)
        if len(game_model.vehicles) > 1 and game_model.player2.movement_pattern == MOVEMENT_PATTERNS[1]:
            player_input2(game_model.vehicles[1], events)
        # print(self.game_model.player.cur_x_vel, self.game_model.player.reaction_x_vel, self.game_model.player.cur_y_vel, self.game_model.player.reaction_y_vel)

        enemy_input(game_model.vehicles)

        game_model.update()
        game_view.update(game_model.vehicles)

        # if not self.game_model.check_if_player_is_alive():
        #     time.sleep(2) # temp
        #     pygame.quit()
        #     sys.exit()

        pygame.key.set_repeat(1, 1)

        # print(window.clock.get_fps())
        window.clock.tick(120)