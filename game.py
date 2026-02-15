import pygame as pg
import sys
from global_settings import *
from sound_manager import *

class Game:
    def __init__(self):
        '''
            This method initializes the game by setting up the Pygame environment, creating the game window, and initializing the clock for managing the frame rate. It also sets up a global event timer that triggers every 40 milliseconds and calls the `new_game` method to start a new game session.
        '''
        # Initialize Pygame and set up the game window
        pg.init()
        # Hide the mouse cursor
        pg.mouse.set_visible(False)
        # Set up the game window with the specified resolution
        self.screen = pg.display.set_mode(RES)
        # Initialize the clock for managing the frame rate
        self.clock = pg.time.Clock()
        # Initialize the delta time for frame rate independent movement
        self.delta_time = 1
        # Initialize a global trigger for handling timed events
        self.global_trigger = False
        # Set up a global event that triggers every 40 milliseconds
        self.global_event = pg.USEREVENT + 0
        pg.time.set_timer(self.global_event, 40)

        # Calling the new_game method to initialize the game state init
        self.new_game()

    def new_game(self):
        '''
            This method initializes the game state by creating instances of the main classes. It also starts playing background music in a loop.
        '''

        # Initialize the main classes for the game
        self.sound = SoundManager(self)
        pg.mixer.music.play(-1)

    def update(self):
        '''
            This method is responsible for updating the game state, including player movement, raycasting, object handling, and weapon updates. It also manages the frame rate and updates the window caption with the current frames per second (FPS).
        '''

        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        '''
            This method is responsible for drawing the game elements on the screen, including the object renderer and weapon. It can also include additional drawing methods for the map and player if needed.
        '''
        pass

    def check_events(self):
        self.global_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif event.type == self.global_event:
                self.global_trigger = True

    def run(self):
        '''
            This method is the main game loop that continuously checks for events, updates the game state, and draws the game elements on the screen. It ensures that the game runs smoothly and responds to user input.
        '''
        while True:
            self.check_events()
            self.update()
            self.draw()
