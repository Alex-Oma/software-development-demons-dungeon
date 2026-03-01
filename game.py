import pygame as pg
import sys
from global_settings import *
from render_engine import *
from raycaster import *
from sound_manager import *
from game_levels import *
from level_map import *
from player import *
from weapon import *
from objects_manager import *
from hud_screen import *
from chaser import *

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
        self.map = LevelMap(self, game_levels['level_1'])
        self.player = Player(self)
        self.hud_screen = HudScreen(self)
        self.render_engine = RenderEngine(self)
        self.raycaster = Raycaster(self)
        self.objects_manager = ObjectsManager(self)
        self.weapon = Weapon(self)
        self.chaser = Chaser(self)
        self.sound_manager = SoundManager(self)
        pg.mixer.music.play(-1)

    def update(self):
        '''
            This method is responsible for updating the game state, including player movement, raycasting, object handling, and weapon updates. It also manages the frame rate and updates the window caption with the current frames per second (FPS).
        '''
        # Update the player state, including movement and interactions
        self.player.update()
        # Update the raycasting calculations to determine what objects are visible to the player
        self.raycaster.update()
        # Update the objects in the game world, including their positions, interactions, and any necessary state changes based on player actions or game events.
        self.objects_manager.update()
        # Update the weapon state, including handling shooting animations and interactions with the game world
        self.weapon.update()

        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        # Update the window caption with the current frames per second (FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        '''
            This method is responsible for drawing the game elements on the screen, including the object renderer and weapon. It can also include additional drawing methods for the map and player if needed.
        '''
        self.render_engine.draw()
        # Draw the weapon on the screen after rendering the game world to ensure it appears in the foreground.
        self.weapon.draw()
        self.hud_screen.draw(self.player.get_player_score(), 1, self.player.get_player_ammo(), self.player.get_player_kill_count(), self.player.get_player_health())

        # Debugging line to display the player's map position on the HUD.
        # self.hud_screen.draw(self.player.get_player_score(), 1, self.player.get_player_ammo(), self.player.get_player_kill_count(), str(self.player.map_pos))

    def check_events(self):
        self.global_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif event.type == self.global_event:
                self.global_trigger = True

            # Pass the event to the player's weapon fire event handler to check for shooting actions when the left mouse button is pressed.
            self.player.weapon_fire_event(event)


    def get_game_result(self):
        # Here we capture the results of the game played by a player so that we pass it back to main menu to update the leaderboard if needed
        game_result = {}
        game_result["points_scored"] = self.player.get_player_score()
        game_result["enemies_killed"] = self.player.get_player_kill_count()
        game_result["levels_cleared"] = 0
        return game_result


    def run(self):
        '''
            This method is the main game loop that continuously checks for events, updates the game state, and draws the game elements on the screen. It ensures that the game runs smoothly and responds to user input.
        '''
        while True:
            # Check for user input and other events
            self.check_events()
            # Update the game state, including player movement and interactions
            self.update()
            # Draw the game elements on the screen
            self.draw()
