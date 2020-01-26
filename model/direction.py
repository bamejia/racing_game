from enum import Enum
from enum import unique

@unique
class Dir(Enum):
    NONE = 0
    NORTH = 1
    NORTHEAST = 2
    EAST = 3
    SOUTHEAST = 4
    SOUTH = -1
    SOUTHWEST = -2
    WEST = -3
    NORTHWEST = -4

    @staticmethod
    def opposite(input_dir):
        opposite = input_dir.value * -1
        for direct in Dir:
            if direct.value == opposite:
                return direct
