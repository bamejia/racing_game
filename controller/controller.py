from controller.player_input import player_input
from controller.enemy_input import enemy_input
from model.model import Model
from view.view import View
import global_variables as gv


class Controller:
    def __init__(self):
        self.view = View()
        self.model = Model()

    def run(self):

        print(gv.WINDOW_W)
        print(gv.WINDOW_L)

        has_not_quit_game = True
        while has_not_quit_game:

            has_not_quit_game = player_input(self.model.player)
            enemy_input(self.model.vehicles)

            self.model.update()
            self.view.display_race(self.model.vehicles)

            # if player.health <= 0:
            #     break

            # print(self.view.clock.get_fps())

            self.view.clock.tick(120)

