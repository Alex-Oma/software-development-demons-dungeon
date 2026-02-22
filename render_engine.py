import pygame as pg
from global_settings import *

class RenderEngine:
    '''
    The RenderEngine class is responsible for rendering the game objects and background in the game.
    It loads wall textures, draws the ceiling and floor, and renders game objects based on their depth to create a 3D effect.
    The class also provides a method to load textures from files and scale them to the desired resolution.
    '''
    def __init__(self, game):
        # The constructor initializes the RenderEngine with a reference to the game instance, sets up the screen for rendering, loads wall textures, and prepares the ceiling image for rendering.
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()
        self.ceiling_image = self.get_texture_from_file('assets/textures/ceiling_texture_2.jpg', (WIDTH, HALF_HEIGHT))
        self.ceiling_offset = 0
        self.blood_pain_screen = self.get_texture_from_file('assets/textures/blood_screen_texture.png', RES)

    def get_wall_textures(self):
        '''
            This method returns the wall textures that have been loaded into the render engine.
        '''
        # The get_wall_textures method is a simple getter that provides access to the wall textures loaded in the RenderEngine.
        # It allows other parts of the game, such as the raycasting engine, to retrieve the textures needed for rendering walls in the game environment.
        return self.wall_textures

    def draw(self):
        '''
            This method is responsible for drawing the game scene, including the background and game objects.
            It first calls the draw_background method to render the ceiling and floor, and then calls the render_game_objects method to render the game objects based on their depth.
        '''
        self.draw_background()
        self.render_game_objects()

    def draw_background(self):
        '''
            This method draws the background of the game scene, including the ceiling and floor.
        '''
        self.ceiling_offset = (self.ceiling_offset + 4.5 * self.game.player.rel) % WIDTH
        self.screen.blit(self.ceiling_image, (-self.ceiling_offset, 0))
        self.screen.blit(self.ceiling_image, (-self.ceiling_offset + WIDTH, 0))
        # floor
        pg.draw.rect(self.screen, FLOOR_COLOR, (0, HALF_HEIGHT, WIDTH, HEIGHT))

    def render_game_objects(self):
        '''
            This method renders the game objects on the screen based on their depth.
            It retrieves the list of objects to render from the raycasting engine, sorts them by depth in descending order, and blits each object's image onto the screen at its corresponding position.
        '''
        # Retrieve the list of objects to render from the raycasting engine, sort them by their depth (distance from the player) in descending order, and then blit each object's image onto the screen at its corresponding position.
        # This sorting ensures that objects farther from the player are rendered first, allowing closer objects to be drawn on top of them for proper visual layering.
        list_objects = sorted(self.game.raycaster.get_objects_to_render_list(), key=lambda t: t[0], reverse=True)
        for depth, image, pos in list_objects:
            # Blit the image of each object onto the screen at its corresponding position.
            # The blitting process involves copying the image onto the screen surface at the specified coordinates, allowing the game objects to be visually represented in the game scene based on their depth and position.
            self.screen.blit(image, pos)

    @staticmethod
    def get_texture_from_file(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        '''
            This method loads a texture from a file and scales it to the specified resolution.
            It uses Pygame's `image.load` function to load the image and `transform.scale` to resize it.
            The loaded texture is returned as a Pygame surface that can be used for rendering in the game.
            :param path: The file path to the texture image that needs to be loaded.
            :param res: A tuple specifying the desired resolution (width, height) to which the loaded texture should be scaled.
            :return: A Pygame surface containing the loaded and scaled texture image, ready to be used for rendering in the game.
        '''

        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)


    def load_wall_textures(self):
        '''
            This method loads wall textures from files and returns a dictionary mapping texture IDs to their corresponding images.
            Each texture is loaded using the `get_texture_from_file` method, which takes the file path and desired resolution as arguments.
            The textures are stored in a dictionary where the keys are the texture IDs (in this case, just 1) and the values are the loaded texture images.
        '''
        return {
            1: self.get_texture_from_file('assets/textures/bricks_texture_1.jpg'),
            2: self.get_texture_from_file('assets/textures/bricks_texture_2.jpg'),
            3: self.get_texture_from_file('assets/textures/bricks_texture_3.jpg'),
            4: self.get_texture_from_file('assets/textures/bricks_texture_4.jpg'),
            5: self.get_texture_from_file('assets/textures/bricks_texture_5.jpg'),
            6: self.get_texture_from_file('assets/textures/exit_portal_7.png'),
        }


    def player_damage_show_blood_screen(self):
        '''
            This method is responsible for rendering the visual effect of the player taking damage.
            When the player takes damage, this method blits a blood screen texture onto the game screen to indicate that the player has been hit.
        '''
        self.screen.blit(self.blood_pain_screen, (0, 0))
