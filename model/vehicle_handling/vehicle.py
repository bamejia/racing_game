from model.vehicle_handling.vehicle_movement_handler import vehicle_movement_handler
import global_variables as gv
from model.vehicle_handling import off_screen_handling
from model.direction import Dir


class Vehicle:
    def __init__(self, index, movement_pattern, x, y, w, l, acceleration, max_speed, handling, max_handling,
                 health, input_x_vel=0, input_y_vel=0, input_direction=Dir.NONE, reaction_x_vel=0, reaction_y_vel=0,
                 reaction_direction=Dir.NONE, cur_x_vel=0, cur_y_vel=0, cur_direction=Dir.NONE,
                 friction_marker=gv.FRICTION_MARKER):
        self.__movement_pattern = movement_pattern
        self.__index = index
        self.__x = x
        self.__y = y
        self.__w = w
        self.__l = l
        self.__max_speed = max_speed
        self.__cur_x_vel = cur_x_vel  # current x velocity
        self.__cur_y_vel = cur_y_vel
        self.__cur_direction = cur_direction
        self.__handling = handling
        self.__max_handling = max_handling
        self.__input_x_vel = input_x_vel
        self.__input_y_vel = input_y_vel
        self.__input_direction = input_direction
        self.__acceleration = acceleration
        self.__health = health
        self.__reaction_x_vel = reaction_x_vel
        self.__reaction_y_vel = reaction_y_vel
        self.__reaction_direction = reaction_direction
        self.__acceleration_count = 0
        self.__handling_count = 0
        self.__friction_count = 0
        self.__friction_marker = friction_marker

    """ methods """

    def update_location(self, other_vehicles):
        vehicle_movement_handler(self, other_vehicles)

    def is_alive(self):
        if self.health > 0:
            return True
        return False

    def is_next_to_road(self):
        if abs(self.cur_x_vel) >= self.max_handling:
            if self.x + self.cur_x_vel < gv.ROAD_X_PLACEMENT:
                return Dir.WEST
            elif self.x + self.w + self.cur_x_vel > gv.ROAD_X_PLACEMENT + gv.ROAD_W:
                return Dir.EAST
        else:
            if self.x + self.cur_x_vel - self.handling < gv.ROAD_X_PLACEMENT:
                return Dir.WEST
            elif self.x + self.w + self.cur_x_vel + self.handling > gv.ROAD_X_PLACEMENT + gv.ROAD_W:
                return Dir.EAST
        return Dir.NONE

    """ getters """
    @property
    def index(self):
        return self.__index

    @property
    def movement_pattern(self):
        return self.__movement_pattern

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def w(self):
        return self.__w

    @property
    def l(self):
        return self.__l

    @property
    def cur_x_vel(self):
        return self.__cur_x_vel

    @property
    def cur_y_vel(self):
        return self.__cur_y_vel

    @property
    def acceleration(self):
        return self.__acceleration

    @property
    def max_speed(self):
        return self.__max_speed

    @property
    def handling(self):
        return self.__handling

    @property
    def max_handling(self):
        return self.__max_handling

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
    def input_direction(self):
        return self.__input_direction

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

    @x.setter
    def x(self, x):
        self.__x = x

    @y.setter
    def y(self, y):
        self.__y = y

    @cur_x_vel.setter
    def cur_x_vel(self, cur_x_vel):
        self.__cur_x_vel = cur_x_vel

    @cur_y_vel.setter
    def cur_y_vel(self, cur_y_vel):
        self.__cur_y_vel = cur_y_vel

    @max_speed.setter
    def max_speed(self, max_speed):
        self.__max_speed = max_speed

    @max_handling.setter
    def max_handling(self, max_handling):
        self.__max_handling = max_handling

    @health.setter
    def health(self, health):
        self.__health = health
        if self.__health < 0:
            self.__health = 0

    @cur_direction.setter
    def cur_direction(self, cur_direction):
        self.__cur_direction = cur_direction

    def x_input_against_x_reaction(self):
        if self.reaction_x_vel < 0 and self.input_x_vel < 0:
            self.__reaction_x_vel = self.reaction_x_vel - self.input_x_vel
            if self.__reaction_x_vel > 0:
                self.__reaction_x_vel = 0
        elif self.reaction_x_vel > 0 and self.input_x_vel > 0:
            self.__reaction_x_vel = self.reaction_x_vel - self.input_x_vel
            if self.__reaction_y_vel < 0:
                self.__reaction_y_vel = 0
        if self.reaction_x_vel > 0 and self.input_x_vel < 0:
            self.__reaction_x_vel = self.reaction_x_vel + self.input_x_vel
            if self.__reaction_y_vel < 0:
                self.__reaction_y_vel = 0
        elif self.reaction_x_vel < 0 and self.input_x_vel > 0:
            self.__reaction_x_vel = self.reaction_x_vel + self.input_x_vel
            if self.__reaction_y_vel > 0:
                self.__reaction_y_vel = 0

    @reaction_x_vel.setter
    def reaction_x_vel(self, reaction_x_vel):
        self.__reaction_x_vel = reaction_x_vel

    def y_input_against_y_reaction(self):
        if self.reaction_y_vel > 0 and self.input_y_vel < 0:
            self.__reaction_y_vel = self.reaction_y_vel + self.input_y_vel
            if self.__reaction_y_vel < 0:
                self.__reaction_y_vel = 0
        elif self.reaction_y_vel < 0 and self.input_y_vel > 0:
            self.__reaction_y_vel = self.reaction_y_vel + self.input_y_vel
            if self.__reaction_y_vel > 0:
                self.__reaction_y_vel = 0
        if self.reaction_y_vel < 0 and self.input_y_vel < 0:
            self.__reaction_y_vel = self.reaction_y_vel - self.input_y_vel
            if self.__reaction_y_vel > 0:
                self.__reaction_y_vel = 0
        elif self.reaction_y_vel > 0 and self.input_y_vel > 0:
            self.__reaction_y_vel = self.reaction_y_vel - self.input_y_vel
            if self.__reaction_y_vel < 0:
                self.__reaction_y_vel = 0


    @reaction_y_vel.setter
    def reaction_y_vel(self, reaction_y_vel):
        self.__reaction_y_vel = reaction_y_vel

    @input_direction.setter
    def input_direction(self, input_direction):
        self.__input_direction = input_direction

    @input_x_vel.setter
    def input_x_vel(self, input_x_vel):
        self.__input_x_vel = input_x_vel

    def acceleration_on_input_x_vel(self, acceleration):
            if self.__input_x_vel + acceleration > self.max_handling:
                return
            elif self.__input_x_vel + acceleration < -1 * self.max_handling:
                return
            else:
                self.__input_x_vel += acceleration

    def friction_on_input_x_vel(self, input_x_vel):
        self.__input_x_vel = input_x_vel

    @input_y_vel.setter
    def input_y_vel(self, input_y_vel):
        self.__input_y_vel = input_y_vel

    def acceleration_on_input_y_vel(self, acceleration):
        if self.__input_y_vel + acceleration > int(round(self.max_speed / 2)):
            return
        elif self.__input_y_vel + acceleration < -1 * self.max_speed:
            return
        else:
            self.__input_y_vel += acceleration

    def off_road_on_input_y_vel(self, off_road_y):
        if self.__input_y_vel + off_road_y > self.max_speed:
            return
        elif self.__input_y_vel + off_road_y < -1 * self.max_speed:
            return
        else:
            self.__input_y_vel += off_road_y

    def friction_on_input_y_vel(self, input_y_vel):
        self.__input_y_vel = input_y_vel

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
        if off_screen_handling.check_if_below_screen(self):
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
        if off_screen_handling.check_if_below_screen(self):
            off_screen_handling.despawn(self, vehicles)

