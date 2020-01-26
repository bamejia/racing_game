from Model.vehicle_movement_handler import vehicle_movement_handler
from Model.direction import Dir


class Vehicle:
    def __init__(self, x, y, w, l, top_speed, cur_x_vel, cur_y_vel, cur_direction, acceleration, handling,
                 lives=100, reaction_speed=0, input_x_vel=0, input_y_vel=0, input_direction=Dir.NONE):
        self.x = x
        self.y = y
        self.w = w
        self.l = l
        self.top_speed = top_speed
        self.cur_x_vel = cur_x_vel  # current x velocity
        self.cur_y_vel = cur_y_vel
        self.cur_direction = cur_direction
        self.input_x_vel = input_x_vel
        self.input_y_vel = input_y_vel
        self.input_direction = input_direction
        self.acceleration = acceleration
        self.handling = handling
        self.lives = lives
        self.reaction_speed = reaction_speed
        self.reaction_direction = Dir.NONE

    def move(self):
        vehicle_movement_handler(self)

    # getters
    @property
    def cur_x_vel(self):
        return self.__cur_x_vel

    @property
    def cur_y_vel(self):
        return self.__cur_y_vel

    @property
    def lives(self):
        return self.__lives

    @property
    def cur_direction(self):
        return self.__cur_direction

    @property
    def reaction_speed(self):
        return self.__reaction_speed

    @property
    def input_x_vel(self):
        return self.__input_x_vel

    @property
    def input_y_vel(self):
        return self.__input_y_vel

    # setters
    # def add_to_cur_speed(self, direction_added, speed_added):
    #     if self.__cur_direction

    @cur_x_vel.setter
    def cur_x_vel(self, cur_x_vel):
        self.__cur_x_vel = cur_x_vel
        if self.__cur_x_vel < 0 and self.input_direction == Dir.NONE:
            self.__cur_x_vel = 0
        elif self.__cur_x_vel < 0:
            self.__cur_x_vel = abs(self.__cur_x_vel)
            self.cur_direction = Dir.opposite(self.cur_direction)

    @cur_y_vel.setter
    def cur_y_vel(self, cur_y_vel):
        self.__cur_y_vel = cur_y_vel
        if self.__cur_y_vel < 0 and self.input_direction == Dir.NONE:
            self.__cur_y_vel = 0
        elif self.__cur_y_vel < 0:
            self.__cur_y_vel = abs(self.__cur_y_vel)
            self.cur_direction = Dir.opposite(self.cur_direction)

    @lives.setter
    def lives(self, lives):
        self.__lives = lives

    @cur_direction.setter
    def cur_direction(self, cur_direction):
        self.__cur_direction = cur_direction

    @reaction_speed.setter
    def reaction_speed(self, reaction_speed):
        self.__reaction_speed = reaction_speed
        if self.__reaction_speed < 0:
            self.__reaction_speed = 0
        if self.__reaction_speed > 0:
            self.__reaction_speed -= friction

    @input_x_vel.setter
    def input_x_vel(self, input_x_vel):
        self.__input_x_vel = input_x_vel
        if self.__input_x_vel < 0 and self.input_direction == Dir.NONE:
            self.__input_x_vel = 0
        elif self.__input_x_vel < 0:
            self.__input_x_vel = abs(self.__input_x_vel)
            self.cur_direction = Dir.opposite(self.cur_direction)
        if self.__input_x_vel > self.top_speed:
            self.__input_x_vel = self.top_speed
        if self.__input_x_vel > 0:
            self.__input_x_vel -= friction

    @input_y_vel.setter
    def input_y_vel(self, input_y_vel):
        self.__input_y_vel = input_y_vel
        if self.__input_y_vel < 0 and self.input_direction == Dir.NONE:
            self.__input_y_vel = 0
        elif self.__input_y_vel < 0:
            self.__input_y_vel = abs(self.__input_y_vel)
            self.cur_direction = Dir.opposite(self.cur_direction)
        if self.__input_y_vel > self.top_speed:
            self.__input_y_vel = self.top_speed
        if self.__input_y_vel > 0:
            self.__input_y_vel -= friction


# class Player(Vehicle):
#     def __init__(self):
#         super().__init__(0, 0, 12, 12, 2, 2)


class Enemy(Vehicle):
    def __init__(self, x=None, y=None):
        if x is not None and y is None:
            super().__init__(x, 30, 20, 20, 8, 2, 0, Dir.SOUTH, 0, 0, 100, 0, 0, 0, Dir.SOUTH)
        elif x is not None or y is not None:
            super().__init__(x, y, 20, 20, 8, 2, 0, Dir.SOUTH, 0, 0, 100, 0, 0, 0, Dir.SOUTH)
        else:
            super().__init__(30, 30, 20, 20, 8, 2, 0, Dir.SOUTH, 0, 0, 100, 0, 0, 0, Dir.SOUTH)

