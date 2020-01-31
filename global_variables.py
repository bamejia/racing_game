from win32api import GetSystemMetrics
import pygame


# window variables
WINDOW_NAME = "Racing Game"
WINDOW_X_POS = 300
WINDOW_Y_POS = 100
WINDOW_W_RATIO = 5/8
WINDOW_L_RATIO = 4/5
WINDOW_W, WINDOW_L = WINDOW_SIZE = round(GetSystemMetrics(0) * WINDOW_W_RATIO),\
                                                          round(GetSystemMetrics(1) * WINDOW_L_RATIO)

# title screen variables
TITLE_TEXT = "RACING GAME"
TITLE_TEXT_SIZE = 140
TITLE_FONT = None
AUTHOR_TEXT = "by bamxmejia"
AUTHOR_TEXT_SIZE = 80
AUTHOR_FONT = None
BUTTON_TEXTS = (
    "1 PLAYER START",
    "2 PLAYER START",
    "OPTIONS",
    "EXIT"
)
# P1_BUTTON_TEXT = "1 PLAYER START"
# P2_BUTTON_TEXT = "2 PLAYER START"
# OPTIONS_BUTTON_TEXT = "OPTIONS"
# EXIT_BUTTON_TEXT = "EXIT"
BUTTON_TEXT_SIZE = 80
BUTTON_FONT = None



# road variables
ROAD_W_RATIO = 3/5
ROAD_W, ROAD_L = ROAD_DIMENSIONS = (round(WINDOW_W*ROAD_W_RATIO), round(WINDOW_L))
ROAD_X_PLACEMENT = (round(WINDOW_W * (1 - ROAD_W_RATIO) / 2))


# colors
WHITE = (255, 255, 255)
VERY_LIGHT_GREY = (200, 200, 200)
BLACK = (0, 0, 0)
BLUE = (0, 0, 150)
TANISH_YELLOW = (255, 255, 100)
BRIGHT_RED = (255,0,0)
RED = (210, 0, 0)
DARK_RED = (125, 0, 0)
YELLOW = (255, 255, 0)
TANISH_GREY = (125, 125, 100)
ORANGE = (255, 120, 0)
DARK_ORANGE = (255, 120, 0)
LIGHT_GREY_BLUE = (125, 150, 150)
PEACH_PINK = (255, 152, 154)
PEACH = (255, 161, 100)
MID_DARK_PEACH = (255, 157, 0)
DARK_PEACH = (238, 138, 49)
BROWN = (185, 113, 62)
TURQOISE = (0, 152, 154)
GREEN = (0, 175, 0)
DARK_GREEN = (0, 100, 40)
TAN = (255, 195, 155)


# traffic variables
TRAFFIC_SPEED = 3  # 2
FRICTION = 1
REACTION_FRICTION = 1
FRICTION_MARKER = 12
REACTION_SPEED_MAX = 12

# player defaults
PLAYER_WIDTH = 32
PLAYER_LENGTH = 68
PLAYER_ACCELERATION = 1
PLAYER_MAX_SPEED = 5
PLAYER_HANDLING = 1
PLAYER_MAX_HANDLING = 4
PLAYER_STARTING_HEALTH = 1000

# enemy defaults
ENEMY_WIDTH = PLAYER_WIDTH
ENEMY_LENGTH = PLAYER_LENGTH
ENEMY_ACCELERATION = 1
ENEMY_MAX_SPEED = 4
ENEMY_HANDLING = 1
ENEMY_MAX_HANDLING = 2
ENEMY_STARTING_HEALTH = PLAYER_STARTING_HEALTH

# for testing
BOTTOM_BORDER = False


# car types
MOVEMENT_PATTERNS = (
    "player",
    "player2",
    "random",
    "side to side",
    "up and down",
    "diagonal",
    "tracker",
    "static",
    "speed demon"
)

# power up types
POWER_UPS = (
    "force bubble",
    "one shot",
    "speed"
)

