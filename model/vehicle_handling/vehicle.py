from model.vehicle_handling.vehicle_movement_handler import vehicle_movement_handler
import global_variables as gv
from model.vehicle_handling import despawn_enemies
from model.direction import Dir


class Vehicle:
    # __input_x_vel = 0
    # __input_y_vel = 0

    def __init__(self, index, movement_pattern, x, y, w, l, acceleration, max_speed, handling, max_handling,
                 health, input_x_vel=0, input_y_vel=0, input_direction=Dir.NONE, reaction_x_vel=0, reaction_y_vel=0,
                 reaction_direction=Dir.NONE, cur_x_vel=0, cur_y_vel=0, cur_direction=Dir.NONE,
                 friction_marker=gv.FRICTION_MARKER):
        self.movement_pattern = movement_pattern
        self.index = index
        self.x = x
        self.y = y
        self.w = w
        self.l = l
        self.max_speed = max_speed
        self.cur_x_vel = cur_x_vel  # current x velocity
        self.cur_y_vel = cur_y_vel
        self.cur_direction = cur_direction
        self.handling = handling
        self.max_handling = max_handling
        self.input_x_vel = input_x_vel
        self.input_y_vel = input_y_vel
        self.input_direction = input_direction
        self.acceleration = acceleration
        self.health = health
        self.reaction_x_vel = reaction_x_vel
        self.reaction_y_vel = reaction_y_vel
        self.reaction_direction = reaction_direction
        self.acceleration_count = 0
        self.handling_count = 0
        self.friction_count = 0
        self.friction_marker = friction_marker

    def move(self, other_vehicles):
        vehicle_movement_handler(self, other_vehicles)

    def is_alive(self):
        if self.health > 0:
            return True
        return False

    """ getters """
    @property
    def index(self):
        return self.__index

    @property
    def movement_pattern(self):
        return self.__movement_pattern

    @property
    def cur_x_vel(self):
        return self.__cur_x_vel

    @property
    def cur_y_vel(self):
        return self.__cur_y_vel

    @property
    def max_speed(self):
        return self.__max_speed

    @property
    def health(self):
        return self.__health

    @property
    def cur_direction(self):
        return self.__cur_direction

    @property
    def reaction_x_vel(self):
        return self.__reaction_x_vel

    @property
    def reaction_y_vel(self):
        return self.__reaction_y_vel

    @property
    def input_x_vel(self):
        return self.__input_x_vel

    @property
    def input_y_vel(self):
        return self.__input_y_vel

    @property
    def acceleration_count(self):
        return self.__acceleration_count

    @property
    def handling_count(self):
        return self.__handling_count

    @property
    def friction_count(self):
        return self.__friction_count

    @property
    def friction_marker(self):
        return self.__friction_marker

    """ setters """
    @index.setter
    def index(self, index):
        self.__index = index

    @movement_pattern.setter
    def movement_pattern(self, movement_pattern):
        self.__movement_pattern = movement_pattern

    @cur_x_vel.setter
    def cur_x_vel(self, cur_x_vel):
        self.__cur_x_vel = cur_x_vel

    @cur_y_vel.setter
    def cur_y_vel(self, cur_y_vel):
        self.__cur_y_vel = cur_y_vel

    @max_speed.setter
    def max_speed(self, max_speed):
        self.__max_speed = max_speed

    @health.setter
    def health(self, health):
        self.__health = health
        if self.__health < 0:
            self.__health = 0

    @cur_direction.setter
    def cur_direction(self, cur_direction):
        self.__cur_direction = cur_direction

    @reaction_x_vel.setter
    def reaction_x_vel(self, reaction_x_vel):
        self.__reaction_x_vel = reaction_x_vel
        if self.__reaction_x_vel > gv.REACTION_SPEED_MAX:
            self.__reaction_x_vel = gv.REACTION_SPEED_MAX
        elif self.__reaction_x_vel < -1 * gv.REACTION_SPEED_MAX:
            self.__reaction_x_vel = -1 * gv.REACTION_SPEED_MAX

    @reaction_y_vel.setter
    def reaction_y_vel(self, reaction_y_vel):
        self.__reaction_y_vel = reaction_y_vel
        if self.__reaction_y_vel > gv.REACTION_SPEED_MAX:
            self.__reaction_y_vel = gv.REACTION_SPEED_MAX
        elif self.__reaction_y_vel < -1 * gv.REACTION_SPEED_MAX:
            self.__reaction_y_vel = -1 * gv.REACTION_SPEED_MAX

    @input_x_vel.setter
    def input_x_vel(self, input_x_vel):
        self.__input_x_vel = input_x_vel
        if self.__input_x_vel > self.max_handling:
            self.__input_x_vel = self.max_handling
        elif self.__input_x_vel < -1 * self.max_handling:
            self.__input_x_vel = -1 * self.max_handling

    @input_y_vel.setter
    def input_y_vel(self, input_y_vel):
        self.__input_y_vel = input_y_vel
        if self.__input_y_vel > int(round(self.max_speed/2)):
            self.__input_y_vel = int(round(self.max_speed/2))
        elif self.__input_y_vel < -1 * self.max_speed:
            self.__input_y_vel = -1 * self.max_speed

    @acceleration_count.setter
    def acceleration_count(self, acceleration_count):
        self.__acceleration_count = acceleration_count

    @handling_count.setter
    def handling_count(self, handling_count):
        self.__handling_count = handling_count

    @friction_count.setter
    def friction_count(self, friction_count):
        self.__friction_count = friction_count

    @friction_marker.setter
    def friction_marker(self, friction_marker):
        self.__friction_marker = friction_marker


class Player(Vehicle):
    def __init__(self, index, movement_pattern ="player", x=400, y=400, w=gv.PLAYER_WIDTH, l=gv.PLAYER_LENGTH,
                 acceleration=gv.PLAYER_ACCELERATION, max_speed=gv.PLAYER_MAX_SPEED, handling=gv.PLAYER_HANDLING,
                 max_handling=gv.PLAYER_MAX_HANDLING, health=gv.PLAYER_STARTING_HEALTH):
        super().__init__(index, movement_pattern, x, y, w, l, acceleration, max_speed, handling, max_handling, health)

        self.score = 0

    def is_below_screen(self):
        if despawn_enemies.check_if_below_screen(self):
            return True
        return False

    """ getters """
    @property
    def score(self):
        return self.__score

    """ setters """
    @score.setter
    def score(self, score):
        self.__score = score


class Enemy(Vehicle):
    def __init__(self, index, movement_pattern="random", x=None, y=None, w=gv.ENEMY_WIDTH, l=gv.ENEMY_LENGTH,
                 acceleration=gv.ENEMY_ACCELERATION, max_speed=gv.ENEMY_MAX_SPEED, handling=gv.ENEMY_HANDLING,
                 max_handling=gv.ENEMY_MAX_HANDLING, health=gv.ENEMY_STARTING_HEALTH, input_x_vel=0, input_y_vel=0,
                 input_direction=Dir.NONE):
        if x is not None and y is None:
            super().__init__(index, movement_pattern, x, -l-1, w, l, acceleration, max_speed, handling, max_handling,
                             health, input_x_vel, input_y_vel, input_direction)
        elif x is not None or y is not None:
            super().__init__(index, movement_pattern, x, y, w, l, acceleration, max_speed, handling, max_handling,
                             health, input_x_vel, input_y_vel, input_direction)
        else:
            super().__init__(index, movement_pattern, 30, 30, w, l, acceleration, max_speed, handling, max_handling,
                             health, input_x_vel, input_y_vel, input_direction)

    """ methods """
    def check_to_despawn(self, vehicles):
        if despawn_enemies.check_if_below_screen(self):
            despawn_enemies.despawn(self, vehicles)

