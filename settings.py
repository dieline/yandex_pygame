import math

# game settings
WIDTH = 1200
HEIGHT = 800
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 120
TILE = 100
FPS_POS = WIDTH - 65, 5

# texture settings
TEXTURE_HEIGHT = 1200
TEXTURE_WIDTH = 1200
TEXTURE_SCALE = TEXTURE_WIDTH // TILE

# minimap settings
MAP_SCALE = 5
MAP_TILE = TILE // MAP_SCALE
MAP_POS = 0, HEIGHT - HEIGHT // MAP_SCALE

# ray casting settings
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 300
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = 3 * DIST * TILE
SCALE = WIDTH // NUM_RAYS


# player
player_pos = (HALF_WIDTH, HALF_HEIGHT)
player_angle = 0
player_speed = 1
DOUBLE_PI = math.pi * 2

# color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
GREEN = (0, 220, 0)
BLUE = (0, 0, 220)
DARKGRAY = (65, 63, 60)
PURPLE = (120, 0, 120)
SKYBLUE = (0, 186, 255)
YELLOW = (220, 220, 0)
