from win32api import GetSystemMetrics


# Whether to pause or not
PAUSE = False

# window variables
WINDOW_NAME = "Racing Game"
WINDOW_X_POS = 300
WINDOW_Y_POS = 100
WINDOW_W_RATIO = 5/8
WINDOW_L_RATIO = 4/5
WINDOW_W, WINDOW_L = WINDOW_SIZE = int(round(GetSystemMetrics(0) * WINDOW_W_RATIO)),\
                                                          int(round(GetSystemMetrics(1) * WINDOW_L_RATIO))

# road variables
ROAD_W_RATIO = 3/5
ROAD_W, ROAD_L = ROAD_DIMENSIONS = (int(round(WINDOW_W*ROAD_W_RATIO)), int(round(WINDOW_L)))
ROAD_X_PLACEMENT = (int(round(WINDOW_W * (1 - ROAD_W_RATIO) / 2)))


# colors
WHITE = (255, 255, 255)
VERY_LIGHT_GREAT = (200, 200, 200)
BLACK = (0, 0, 0)
BLUE = (0, 0, 150)
GREEN = (0, 125, 0)
RED = (125, 0, 0)
YELLOW = (255, 255, 0)
TANISH_GREY = (125, 125, 100)
ORANGE = (255, 120, 0)
LIGHT_GREY_BLUE = (125, 150, 150)
PEACH_PINK = (255, 152, 154)
TURQOISE = (0, 152, 154)


# traffic variables
TRAFFIC_SPEED = 2  # 2
FRICTION = 1
REACTION_FRICTION = 1
FRICTION_MARKER = 6
REACTION_SPEED_MAX = 12

# player defaults
PLAYER_WIDTH = 32
PLAYER_LENGTH = 68
PLAYER_ACCELERATION = 1
PLAYER_MAX_SPEED = 4
PLAYER_HANDLING = 1
PLAYER_MAX_HANDLING = 4
PLAYER_STARTING_HEALTH = 1000

# enemy defaults
ENEMY_WIDTH = PLAYER_WIDTH
ENEMY_LENGTH = PLAYER_LENGTH
ENEMY_ACCELERATION = 1
ENEMY_MAX_SPEED = 3
ENEMY_HANDLING = 1
ENEMY_MAX_HANDLING = 2
ENEMY_STARTING_HEALTH = PLAYER_STARTING_HEALTH

# car types
MOVEMENT_PATTERNS = (
    "player",
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

