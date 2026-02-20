import pygame as pg
import math
from global_settings import *
from render_engine import *


class Raycaster:
    '''
        The Raycaster class is responsible for performing ray casting calculations to determine the visible walls and objects in the game world.
        It calculates the depth, projected height, texture, and offset for each ray cast from the player's perspective.
        The results of the ray casting are stored in a list, which is then used to generate the list of objects to render on the screen.
    '''

    def __init__(self, game):
        '''
                This method initializes the Raycaster class. It takes the game object as input and sets up the necessary attributes for ray casting calculations.
        :param game: This parameter is the game object that contains all the necessary information about the game, such as the player's position, the screen, etc. It is used to access the game state and update it based on the ray casting calculations.
        '''
        self.game = game
        self.textures = self.game.render_engine.get_wall_textures()
        self.objects_to_render = []
        self.ray_casting_result = []

    def get_objects_to_render_list(self):
        '''
            Returns the list of objects to render, sorted by depth in descending order.
            This method is used to retrieve the list of objects that need to be rendered on the screen, sorted by their depth from the player.
            The sorting is done in descending order, meaning that objects farther from the player will be rendered first, allowing closer objects to be drawn on top of them for proper visual layering.
        '''
        return self.objects_to_render

    def get_ray_casting_result_list(self):
        '''
            Returns the result of the ray casting process, which is a list of tuples containing depth, projected height, texture ID, and texture offset for each ray.
            This method provides access to the raw results of the ray casting calculations, which include the distance from the player to the wall (depth), the height of the wall projection on the screen (proj_height), the ID of the texture to be used for rendering (texture), and the offset for texture mapping (offset).
        '''
        return self.ray_casting_result

    def get_objects_to_render(self):
        '''
            This method processes the results of the ray casting calculations to generate a list of objects that need to be rendered on the screen.
        :return:
        '''
        self.objects_to_render = []
        for ray, values in enumerate(self.get_ray_casting_result_list()):
            # Unpack the ray casting results for the current ray
            depth, proj_height, texture, offset = values

            # Determine the portion of the wall texture to render based on the projected height and the texture offset
            if proj_height < HEIGHT:
                # Extract the appropriate column from the wall texture based on the offset and scale it to the projected height
                wall_column = self.textures[texture].subsurface(
                    offset * (TEXTURE_SIZE - SCALE), 0, SCALE, TEXTURE_SIZE
                )
                # Scale the extracted column to the projected height for rendering
                wall_column = pg.transform.scale(wall_column, (SCALE, proj_height))
                # Calculate the position to render the wall column on the screen, centering it vertically based on the projected height
                wall_pos = (ray * SCALE, HALF_HEIGHT - proj_height // 2)
            else:
                # If the projected height exceeds the screen height, calculate the portion of the texture to render based on the offset and scale it to fit the screen height
                texture_height = TEXTURE_SIZE * HEIGHT / proj_height
                # Extract the appropriate column from the wall texture based on the offset and scale it to fit the screen height
                wall_column = self.textures[texture].subsurface(
                    offset * (TEXTURE_SIZE - SCALE), HALF_TEXTURE_SIZE - texture_height // 2,
                    SCALE, texture_height
                )
                # Scale the extracted column to fit the screen height for rendering
                wall_column = pg.transform.scale(wall_column, (SCALE, HEIGHT))
                # Calculate the position to render the wall column on the screen, starting from the top of the screen since the projected height exceeds the screen height
                wall_pos = (ray * SCALE, 0)

            self.objects_to_render.append((depth, wall_column, wall_pos))

    def append_object_to_render(self, depth, image, pos):
        '''
            This method allows adding an object to the list of objects to render, which can be used for rendering sprites or other game objects in addition to walls.
            :param depth: The distance from the player to the object, used for depth sorting.
            :param image: The image of the object to be rendered.
            :param pos: The position on the screen where the object should be rendered.
        '''
        self.objects_to_render.append((depth, image, pos))

    def ray_cast(self):
        '''
            This method performs the ray casting calculations to determine the depth, projected height, texture, and offset for each ray cast from the player's perspective.
        '''
        self.ray_casting_result = []
        texture_vert, texture_hor = 1, 1
        ox, oy = self.game.player.pos
        x_map, y_map = self.game.player.map_pos

        # Start the ray casting process by initializing the angle of the first ray to be cast.
        # The angle is calculated based on the player's current angle and the field of view (FOV) of the game.
        # The initial angle is set to be slightly offset from the player's angle to avoid issues with rays that are exactly aligned with the player's view.
        ray_angle = self.game.player.angle - HALF_FOV + 0.0001
        for ray in range(NUM_RAYS):
            # Calculate the sine and cosine of the current ray angle, which will be used for determining the direction of the ray and for calculating intersections with walls.
            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)

            # Calculate the horizontal intersections of the ray with the walls in the game world.
            y_hor, dy = (y_map + 1, 1) if sin_a > 0 else (y_map - 1e-6, -1)

            # Calculate the depth of the horizontal intersection by using the player's position and the angle of the ray.
            # The depth is calculated as the distance from the player to the point of intersection along the ray.
            depth_hor = (y_hor - oy) / sin_a
            x_hor = ox + depth_hor * cos_a

            # Calculate the change in depth for each step along the ray as it intersects with horizontal grid lines.
            delta_depth = dy / sin_a
            dx = delta_depth * cos_a

            # Iterate through the horizontal intersections to find the first wall that the ray intersects with.
            for i in range(MAX_DEPTH):
                # Check if the current horizontal intersection point is within the game world and if it corresponds to a wall in the world map.
                tile_hor = int(x_hor), int(y_hor)
                if tile_hor in self.game.map.world_map:
                    texture_hor = self.game.map.world_map[tile_hor]
                    break
                # If the current horizontal intersection does not correspond to a wall, move to the next horizontal intersection by updating the x and y coordinates and the depth along the ray.
                x_hor += dx
                y_hor += dy
                depth_hor += delta_depth

            # Calculate the vertical intersections of the ray with the walls in the game world.
            x_vert, dx = (x_map + 1, 1) if cos_a > 0 else (x_map - 1e-6, -1)

            # Calculate the depth of the vertical intersection by using the player's position and the angle of the ray.
            depth_vert = (x_vert - ox) / cos_a
            y_vert = oy + depth_vert * sin_a

            # Calculate the change in depth for each step along the ray as it intersects with vertical grid lines.
            delta_depth = dx / cos_a
            dy = delta_depth * sin_a

            # Iterate through the vertical intersections to find the first wall that the ray intersects with.
            for i in range(MAX_DEPTH):
                # Check if the current vertical intersection point is within the game world and if it corresponds to a wall in the world map.
                tile_vert = int(x_vert), int(y_vert)
                if tile_vert in self.game.map.world_map:
                    texture_vert = self.game.map.world_map[tile_vert]
                    break

                # If the current vertical intersection does not correspond to a wall, move to the next vertical intersection by updating the x and y coordinates and the depth along the ray.
                x_vert += dx
                y_vert += dy
                depth_vert += delta_depth

            # Determine which intersection (horizontal or vertical) is closer to the player and use that for rendering.
            if depth_vert < depth_hor:
                depth, texture = depth_vert, texture_vert
                y_vert %= 1
                offset = y_vert if cos_a > 0 else (1 - y_vert)
            else:
                depth, texture = depth_hor, texture_hor
                x_hor %= 1
                offset = (1 - x_hor) if sin_a > 0 else x_hor

            # Correct the depth for the fish-eye effect by multiplying it with the cosine of the angle difference between the player's view and the ray angle.
            # This ensures that walls that are farther away do not appear distorted.
            depth *= math.cos(self.game.player.angle - ray_angle)

            # Calculate the projected height of the wall on the screen based on the depth of the intersection.
            proj_height = SCREEN_DIST / (depth + 0.0001)

            # Append the results of the ray casting for the current ray to the ray_casting_result list, which includes the depth, projected height, texture ID, and texture offset for rendering.
            self.ray_casting_result.append((depth, proj_height, texture, offset))

            # Increment the ray angle for the next ray to be cast, ensuring that it covers the entire field of view (FOV) of the game.
            ray_angle += DELTA_ANGLE

    def update(self):
        '''
                This method updates the ray casting results and the list of objects to render. It is called in the game loop to ensure that the rendering is based on the latest ray casting calculations.
        '''
        self.ray_cast()
        self.get_objects_to_render()