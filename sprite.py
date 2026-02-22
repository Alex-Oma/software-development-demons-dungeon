import pygame as pg
from global_settings import *

class Sprite:
    '''
        This class is responsible for creating and rendering sprites in the game.
        It loads the sprite image, calculates its position and size on the screen based on the player's position and angle, and adds it to the list of objects to be rendered by the raycasting engine.
        The sprite's projection is calculated using the distance from the player and the angle between the player and the sprite, allowing for proper scaling and positioning on the screen.
    '''
    def __init__(self, game, path='assets/sprites/static/candlebra.png',
                 pos=(10.5, 3.5), scale=0.7, shift=0.27):
        # Initialize the sprite object with the game instance, image path, position, scale, and height shift.
        self.game = game
        # Store a reference to the player object from the game instance for later use in calculations.
        self.player = game.player
        # Set the sprite's position in the game world using the provided coordinates.
        self.x, self.y = pos
        # Load the sprite image from the specified path and convert it for optimal rendering with transparency support.
        self.image = pg.image.load(path).convert_alpha()
        self.IMAGE_WIDTH = self.image.get_width()
        self.IMAGE_HALF_WIDTH = self.image.get_width() // 2
        self.IMAGE_RATIO = self.IMAGE_WIDTH / self.image.get_height()
        # Initialize variables for the sprite's position and distance calculations, which will be updated in the get_sprite method.
        self.dx, self.dy, self.theta, self.screen_x, self.dist, self.norm_dist = 0, 0, 0, 0, 1, 1
        self.sprite_half_width = 0
        self.SPRITE_SCALE = scale
        self.SPRITE_HEIGHT_SHIFT = shift

    def get_sprite_projection(self):
        '''
            Calculate the projection of the sprite on the screen based on its distance from the player and its angle relative to the player's view.
        '''
        # Calculate the projected size of the sprite on the screen using the distance from the player and a scaling factor.
        proj = SCREEN_DIST / self.norm_dist * self.SPRITE_SCALE
        proj_width, proj_height = proj * self.IMAGE_RATIO, proj

        # Scale the sprite image to the calculated projected size for rendering on the screen.
        image = pg.transform.scale(self.image, (proj_width, proj_height))

        # Calculate the horizontal position of the sprite on the screen, adjusting for its width to center it correctly.
        self.sprite_half_width = proj_width // 2
        height_shift = proj_height * self.SPRITE_HEIGHT_SHIFT
        pos = self.screen_x - self.sprite_half_width, HALF_HEIGHT - proj_height // 2 + height_shift

        # Add the sprite's distance, scaled image, and position to the list of objects to be rendered by the raycasting engine, ensuring proper depth sorting.
        self.game.raycaster.append_object_to_render(self.norm_dist, image, pos)

    def get_sprite(self):
        '''
            This method calculates the sprite's position and distance from the player, determines if it is within the player's field of view, and if so, calls the get_sprite_projection method to prepare it for rendering.
        '''
        # Calculate the difference in x and y coordinates between the sprite and the player to determine the sprite's position relative to the player.
        dx = self.x - self.player.x
        dy = self.y - self.player.y
        self.dx, self.dy = dx, dy
        # Calculate the angle (theta) from the player to the sprite using the arctangent of the y and x differences, which will be used to determine the sprite's position on the screen.
        self.theta = math.atan2(dy, dx)

        # Calculate the angle difference (delta) between the player's viewing angle and the angle to the sprite, adjusting for cases where the sprite is behind the player or to the left of the player's view.
        delta = self.theta - self.player.angle
        if (dx > 0 and self.player.angle > math.pi) or (dx < 0 and dy < 0):
            delta += math.tau

        # Calculate the horizontal position of the sprite on the screen based on the angle difference and the number of rays in the raycasting engine, which will be used to determine where to render the sprite.
        delta_rays = delta / DELTA_ANGLE
        self.screen_x = (HALF_NUM_RAYS + delta_rays) * SCALE

        # Calculate the distance from the player to the sprite using the Pythagorean theorem, and then calculate the normalized distance by adjusting for the angle difference to ensure proper scaling of the sprite on the screen.
        self.dist = math.hypot(dx, dy)
        self.norm_dist = self.dist * math.cos(delta)
        # Check if the sprite is within the horizontal bounds of the screen and is not too close to the player (to avoid rendering issues), and if so, call the get_sprite_projection method to prepare it for rendering.
        if -self.IMAGE_HALF_WIDTH < self.screen_x < (WIDTH + self.IMAGE_HALF_WIDTH) and self.norm_dist > 0.5:
            self.get_sprite_projection()

    def update(self):
        '''
            Update the sprite's position and projection by calling the get_sprite method, which will recalculate its position and distance from the player and prepare it for rendering if it is within the player's field of view.
        '''
        self.get_sprite()
