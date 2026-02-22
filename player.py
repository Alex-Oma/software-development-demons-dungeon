from global_settings import *
import pygame as pg
import math


class Player:
    '''
    The Player class represents the player character in the game. It handles the player's movement, collision detection, and mouse control for looking around.
    The class has methods for updating the player's position and angle based on keyboard and mouse input, as well as properties for retrieving the player's current position and map position.
    The player's movement is calculated based on the player's angle and speed, and collision detection is performed to prevent the player from moving through walls.
    The mouse control allows the player to look around by moving the mouse, with limits on how far the player can look in either direction.
    '''

    def __init__(self, game):
        '''
            This method initializes the Player object with the game instance, sets the player's initial position and angle, and initializes variables for mouse control and timing.
        '''
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE
        self.rel = 0
        # Initialize the shot state to False, indicating that the player has not fired a shot yet.
        self.weapon_shot = False
        # Initialize the player's health to the maximum health defined in the settings, which will be used to keep track of the player's remaining health points in the game.
        self.health = PLAYER_MAX_HEALTH
        # Initialize the player's ammo count to the maximum ammo defined in the settings, which will be used to keep track of how many shots the player has available before needing to reload.
        self.ammo = PLAYER_MAX_AMMO
        # Initialize the player's kill count to 0, which will be used to keep track of the number of enemies the player has killed in the game.
        self.enemies_killed = 0
        # Initialize the player's score to 0, which will be used to keep track of the player's points based on their performance in the game.
        self.score = 0
        self.time_prev = pg.time.get_ticks()

    def increase_score(self, points):
        '''
            This method increases the player's score by the specified number of points.
        :param points: This parameter represents the number of points to be added to the player's current score. It is used to update the player's score based on their performance in the game, such as killing enemies or completing objectives.
        '''
        self.score += points

    def get_player_score(self):
        '''
            This method returns the current score of the player, which is stored in the `score` attribute of the Player class. This value represents the player's points based on their performance in the game.
        :return: The method returns the current score of the player, which is an integer value stored in the `score` attribute of the Player class. This value represents the player's points based on their performance in the game.
        '''
        return self.score

    def get_player_kill_count(self):
        '''
            This method returns the current kill count of the player, which is stored in the `enemies_killed` attribute of the Player class. This value represents the number of enemies the player has killed in the game.
        :return: The method returns the current kill count of the player, which is an integer value stored in the `enemies_killed` attribute of the Player class. This value represents the number of enemies the player has killed in the game.
        '''
        return self.enemies_killed

    def increase_kill_count(self):
        '''
            This method increments the player's kill count by 1 each time it is called. It is used to keep track of the number of enemies the player has killed in the game.
        '''
        self.enemies_killed += 1

    def get_player_health(self):
        '''
            This method returns the current health of the player.
        :return: The method returns the current health of the player, which is stored in the `health` attribute of the Player class. This value represents the player's remaining health points in the game.
        '''
        return self.health


    def get_player_ammo(self):
        '''
            This method returns the current ammo count of the player.
        :return: The method returns the current ammo count of the player, which is stored in the `ammo` attribute of the Player class. This value represents the number of ammunition rounds the player has available for firing their weapon in the game.
        '''
        return self.ammo


    def player_gets_damage(self, damage):
        '''
            This method applies damage to the player by reducing the player's health by the specified damage amount.
        :param damage: This parameter represents the amount of damage that the player will take. It is subtracted from the player's current health to reflect the damage taken by the player.
        :return: None
        '''
        self.health -= damage
        # Call the player_damage_show_blood_screen method of the game's object renderer to display the damage effect on the screen.
        self.game.render_engine.player_damage_show_blood_screen()
        # Play the player pain sound effect using the game's sound manager to provide audio feedback for taking damage.
        self.game.sound_manager.play_player_pain()


    def movement(self):
        '''
            This method calculates the player's movement based on keyboard input and updates the player's position accordingly.
        '''
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_s]:
            dx += -speed_cos
            dy += -speed_sin
        if keys[pg.K_a]:
            dx += speed_sin
            dy += -speed_cos
        if keys[pg.K_d]:
            dx += -speed_sin
            dy += speed_cos

        self.check_wall_collision(dx, dy)
        self.angle %= math.tau


    def check_wall(self, x, y):
        '''
            This method checks if the player is colliding with a wall at the given coordinates (x, y).
            :param x: This parameter represents the x-coordinate of the player's position that we want to check for collision with a wall.
            :param y: This parameter represents the y-coordinate of the player's position that we want to check for collision with a wall.
            :return: The method returns a boolean value indicating whether the player is colliding with a wall at the given coordinates (x, y).
            It checks if the coordinates (x, y) are not present in the world map of the game, which contains the positions of all the walls. If (x, y) is not in the world map, it means there is no wall at that position, and the method returns True (indicating no collision).
            If (x, y) is in the world map, it means there is a wall at that position, and the method returns False (indicating a collision).
        '''
        return (x, y) not in self.game.map.get_world_map()


    def check_wall_collision(self, dx, dy):
        '''
            This method checks for wall collisions based on the player's movement in the x and y directions (dx and dy).
            It uses the check_wall method to determine if the player can move to the new position without colliding with a wall.
            If there is no collision, it updates the player's position accordingly.
        :param dx: This parameter represents the change in the player's x-coordinate based on their movement. It is calculated from the player's speed and angle of movement.
        :param dy: This parameter represents the change in the player's y-coordinate based on their movement. It is calculated from the player's speed and angle of movement.
        '''
        scale = PLAYER_SIZE_SCALE / self.game.delta_time
        if self.check_wall(int(self.x + dx * scale), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy * scale)):
            self.y += dy


    def mouse_control(self):
        '''
            This method handles the mouse control for looking around in the game. It checks the position of the mouse and updates the player's angle based on the relative movement of the mouse.
        '''
        # Get the current position of the mouse
        mx, my = pg.mouse.get_pos()
        # If the mouse is outside the defined borders, reset its position to the center of the screen
        if mx < MOUSE_BORDER_LEFT or mx > MOUSE_BORDER_RIGHT:
            pg.mouse.set_pos([HALF_WIDTH, HALF_HEIGHT])

        # Get the relative movement of the mouse in the x direction
        self.rel = pg.mouse.get_rel()[0]
        self.rel = max(-MOUSE_MAX_REL, min(MOUSE_MAX_REL, self.rel))
        # Update the player's angle based on the relative movement of the mouse, scaled by the mouse sensitivity and the game's delta time
        self.angle += self.rel * MOUSE_SENSITIVITY * self.game.delta_time


    def update(self):
        '''
            This method updates the player's position and angle based on keyboard and mouse input.
        '''
        self.movement()
        self.mouse_control()


    @property
    def pos(self):
        '''
            This property returns the current position of the player as a tuple (x, y).
        '''
        return self.x, self.y


    @property
    def map_pos(self):
        '''
            This property returns the current position of the player on the map as a tuple (x, y).
        '''
        return int(self.x), int(self.y)


    def weapon_fire_event(self, event):
        '''
            This method handles the event of firing the weapon when the left mouse button is pressed.
            It checks if the player has not already fired a shot and if the weapon is not currently reloading before allowing the player to fire.
            When the left mouse button is pressed, it plays the shotgun sound effect, sets the shot state to True, and sets the weapon's reloading state to True to trigger the shooting animation.
            :param event: This parameter represents the event object that is passed to the method when a mouse button is pressed. It contains information about the type of event and the specific button that was pressed.
        '''
        # Check if the event is a mouse button down event
        if event.type == pg.MOUSEBUTTONDOWN:
            # Check if the left mouse button (button 1) is pressed, and if the player has not already fired a shot and the weapon is not currently reloading
            if event.button == 1 and not self.weapon_shot and not self.game.weapon.is_reloading():
                # Play the shotgun sound effect using the game's sound manager
                self.game.sound_manager.play_shotgun()
                # Set the player's shot state to True to indicate that the player has fired a shot
                self.weapon_shot = True
                # Reduce the player's ammo count by 1 to reflect the shot that was fired.
                self.ammo -= 1
                # Set the weapon's reloading state to True to trigger the shooting animation and prevent the player from firing again until the animation is complete.
                self.game.weapon.set_reloading(True)
