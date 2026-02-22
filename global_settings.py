import math
import pygame
from pygame import constants

# game settings
RES = WIDTH, HEIGHT = 1600, 900  # screen resolution for the game
HALF_WIDTH = WIDTH // 2  # half the width of the screen
HALF_HEIGHT = HEIGHT // 2  # half the height of the screen
FPS = 60
GAME_TITLE_PREFIX = ""
GAME_TITLE = "DEMONS DUNGEON"

# Player Settings:
PLAYER_MAX_HEALTH = 100 # maximum health of the player, which determines how much damage the player can take before dying
PLAYER_MAX_AMMO = 100 # maximum ammo of the player, which determines how many times the player can shoot
PLAYER_SIZE_SCALE = 60 # scale factor
PLAYER_ANGLE = 0 # initial angle of the player (facing right)
PLAYER_ROT_SPEED = 0.002 # rotation speed of the player, which determines how fast the player can turn left or right
PLAYER_POS = 2, 2  # spawn position of the player on the map (in terms of map coordinates)
PLAYER_SPEED = 0.004 # movement speed of the player, which determines how fast the player moves through the game world

# Mouse settings:
MOUSE_MAX_REL = 40
MOUSE_SENSITIVITY = 0.0003
MOUSE_BORDER_LEFT = 100
MOUSE_BORDER_RIGHT = WIDTH - MOUSE_BORDER_LEFT


# Colour constants:
# Here, the common constants used in the game are defined.
# These variables store the colours that are used in the game to constantly change the colour of the obstacles.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (200, 200, 200)
SUNSET = (253, 72, 47)
RED = (255, 0 , 0)
GREENYELLOW = (184, 255, 0)
BRIGHTBLUE = (47, 228, 253)
ORANGE = (255, 113, 0)
YELLOW = (255, 236, 0)
PURPLE = (252, 67, 255)


FLOOR_COLOR = (30, 30, 30)

# Texture settings
TEXTURE_SIZE = 256
HALF_TEXTURE_SIZE = TEXTURE_SIZE // 2

# Raycasting settings
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH // 2
HALF_NUM_RAYS = NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = 20
SCREEN_DIST = HALF_WIDTH / math.tan(HALF_FOV)
SCALE = WIDTH // NUM_RAYS


# Textual writings settings
FONT = "assets/font/AmazDooMRight2.ttf"
MENU_BACKGROUND_IMAGE = "assets/menu/menu_background.jpg"
LEADERBOARD_FILE = "assets/files/leaderboard.json"

PERMITTED_KEYS_FOR_PLAYER_NAME = [
    pygame.K_0,
    pygame.K_1,
    pygame.K_2,
    pygame.K_3,
    pygame.K_4,
    pygame.K_5,
    pygame.K_6,
    pygame.K_7,
    pygame.K_8,
    pygame.K_9,
    pygame.K_a,
    pygame.K_AMPERSAND,
    pygame.K_ASTERISK,
    pygame.K_AT,
    pygame.K_b,
    pygame.K_BACKQUOTE,
    pygame.K_BACKSLASH,
    pygame.K_c,
    pygame.K_COLON,
    pygame.K_COMMA,
    pygame.K_d,
    pygame.K_DOLLAR,
    pygame.K_e,
    pygame.K_EQUALS,
    pygame.K_EXCLAIM,
    pygame.K_f,
    pygame.K_g,
    pygame.K_GREATER,
    pygame.K_h,
    pygame.K_HASH,
    pygame.K_i,
    pygame.K_j,
    pygame.K_k,
    pygame.K_l,
    pygame.K_LEFTBRACKET,
    pygame.K_LEFTPAREN,
    pygame.K_LESS,
    pygame.K_m,
    pygame.K_MINUS,
    pygame.K_n,
    pygame.K_o,
    pygame.K_p,
    pygame.K_PERCENT,
    pygame.K_PERIOD,
    pygame.K_PLUS,
    pygame.K_q,
    pygame.K_QUESTION,
    pygame.K_QUOTE,
    pygame.K_QUOTEDBL,
    pygame.K_r,
    pygame.K_RIGHTBRACKET,
    pygame.K_RIGHTPAREN,
    pygame.K_s,
    pygame.K_SEMICOLON,
    pygame.K_SLASH,
    pygame.K_SPACE,
    pygame.K_t,
    pygame.K_u,
    pygame.K_UNDERSCORE,
    pygame.K_v,
    pygame.K_w,
    pygame.K_x,
    pygame.K_y,
    pygame.K_z,
]