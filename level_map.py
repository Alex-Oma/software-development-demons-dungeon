import pygame as pg

class LevelMap:
    '''
        The LevelMap class is responsible for creating the world map from the game level.
        It takes the game level as input and creates a dictionary that contains the positions of all the walls in the game.
        The keys of the dictionary are tuples that represent the (x, y) coordinates of the wall, and the values are the type of wall (e.g., 1 for a regular wall, 2 for a door, etc.).
    '''
    def __init__(self, game, game_level):
        '''
            This method initializes the LevelMap class. It takes the game and the game level as input and creates the world map from the game level.
        :param game: This parameter is the game object that contains all the necessary information about the game, such as the player's position, the screen, etc. It is used to access the game state and update it based on the level map.
        :param game_level: This parameter is a 2D list that represents the layout of the game level. Each element in the list represents a tile in the game, where '1' represents a wall, 'o' represents an open space, and other values can represent different types of walls or objects. The LevelMap class uses this 2D list to create the world map, which is a dictionary that contains the positions of all the walls in the game.
        '''
        self.game = game
        self.map = game_level
        self.world_map = {}
        self.rows = len(self.map)
        self.cols = len(self.map[0])
        self.get_map()

    def get_world_map(self):
        '''
            This method returns the world map, which is a dictionary that contains the positions of all the walls in the game.
            The keys of the dictionary are tuples that represent the (x, y) coordinates of the wall, and the values are the type of wall (e.g., 1 for a regular wall, 2 for a door, etc.).
        '''
        return self.world_map

    def get_map(self):
        '''
            This method creates the world map from the game level. It iterates through the 2D list that represents the game level and adds the positions of all the walls to the world map dictionary.
        '''
        for j, row in enumerate(self.map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value

