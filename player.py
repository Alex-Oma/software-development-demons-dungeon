from global_settings import *
import pygame as pg
import math
from weapon import Weapon


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
        # Initialize the health recovery mode to False, which will be used to determine whether the player is currently in a state where they can recover health over time.
        self.health_recover_mode = False
        self.health_recovery_delay = 700

        self.time_prev = pg.time.get_ticks()

        self.has_armor = False
        self.armor_start_time = 0
        self.armor_duration = ARMOR_ACTIVE_TIME * 1000  # 60 seconds in ms
        self.armor_remaining_time = 0

        # Initialize weapon inventory and switching system
        self.weapons = {
            'shotgun': None,  # Will be initialized after game.weapon is created
            'an94': None,
            'minigun': None,
        }
        self.current_weapon_id = 'shotgun'
        self.weapon_switch_blocked_time = 0  # Track when blocked-switch warning was last shown

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

    def get_armor_remaining_time(self):
        '''
            This method returns the remaining time of the player's armor in seconds.
        :return: The method returns the remaining time of the player's armor in seconds.
        '''
        return self.armor_remaining_time

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

    def top_up_health(self, amount):
        '''
            This method increases the player's health by the specified amount, up to the maximum health limit defined in the settings.
        :param amount: This parameter represents the number of health points to be added to the player's current health. It is used to replenish the player's health when they pick up health pickups in the game.
        '''
        self.health = min(self.health + amount, PLAYER_MAX_HEALTH)

    def get_player_ammo(self):
        '''
            This method returns the current ammo count of the player.
        :return: The method returns the current ammo count of the player, which is stored in the `ammo` attribute of the Player class. This value represents the number of ammunition rounds the player has available for firing their weapon in the game.
        '''
        return self.ammo

    def top_up_ammo(self, amount):
        '''
            This method increases the player's ammo count by the specified amount, up to the maximum ammo limit defined in the settings.
        :param amount: This parameter represents the number of ammunition rounds to be added to the player's current ammo count. It is used to replenish the player's ammo when they pick up ammo pickups in the game.
        '''
        self.ammo = min(self.ammo + amount, PLAYER_MAX_AMMO)

    def player_gets_damage(self, damage):
        '''
            This method applies damage to the player by reducing the player's health by the specified damage amount.
        :param damage: This parameter represents the amount of damage that the player will take. It is subtracted from the player's current health to reflect the damage taken by the player.
        :return: None
        '''
        if self.has_armor:
            damage = int(damage * 0.5)

        # Reduce the player's health by the specified damage amount to reflect the damage taken by the player.
        self.health -= damage
        # Call the player_damage_show_blood_screen method of the game's object renderer to display the damage effect on the screen.
        self.game.render_engine.player_damage_show_blood_screen()
        # Play the player pain sound effect using the game's sound manager to provide audio feedback for taking damage.
        self.game.sound_manager.play_player_pain()
        # After applying the damage and showing the damage effect, it checks if the player's health has dropped below 1.
        # If the player's health is less than 1, it calls the is_game_over method to handle the game over state,
        # which involves displaying a game over screen.
        self.is_game_over()


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
        # Update the player's movement based on keyboard input
        self.movement()
        # Update the player's angle based on mouse input for looking around
        self.mouse_control()

        # Check if the player has armor and is in health recovery mode then we recover player's health
        if self.has_armor:
            self.recover_player_health()

        if self.get_player_ammo() > 0:
            # Update auto-fire for weapons that support hold-to-fire
            self.update_auto_fire()

        # Check and update armor duration
        if self.has_armor:
            if pg.time.get_ticks() - self.armor_start_time > self.armor_duration:
                self.has_armor = False
            else:
                self.armor_remaining_time = (self.armor_duration - (pg.time.get_ticks() - self.armor_start_time)) / 1000.0

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


    def get_current_weapon(self):
        '''
            This method returns the currently active weapon instance.
        '''
        return self.game.weapon

    def switch_weapon(self, weapon_id):
        '''
            This method switches to the specified weapon if not currently reloading/animating.
            :param weapon_id: The weapon id to switch to ('shotgun', 'an94', 'minigun')
        '''
        # Check if a switch is blocked due to current weapon reloading
        if self.game.weapon.is_reloading():
            # Trigger blocked-switch warning event
            self.weapon_switch_blocked_time = pg.time.get_ticks()
            return False

        # Switch weapon if different from current
        if weapon_id != self.current_weapon_id:
            self.current_weapon_id = weapon_id
            # Create new weapon instance with the selected weapon id
            self.game.weapon = Weapon(self.game, weapon_id=weapon_id)
            self.game.weapon.reset_fire_cooldown()
            return True
        return False

    def try_switch_weapon(self, weapon_id):
        '''
            This method attempts to switch weapons and returns True if successful, False if blocked.
        '''
        return self.switch_weapon(weapon_id)

    def is_weapon_switch_blocked_warning_active(self):
        '''
            This method checks if the blocked-switch warning should be displayed (within 0.8s and not rate-limited).
        '''
        if self.weapon_switch_blocked_time == 0:
            return False
        elapsed = (pg.time.get_ticks() - self.weapon_switch_blocked_time) / 1000.0
        return elapsed < WEAPON_SWITCH_BLOCK_MSG_DURATION

    def weapon_fire_event(self, event):
        '''
            This method handles weapon firing events (single-shot for shotgun, auto-fire tracking for an94/minigun).
            It also handles weapon switching via 1/2/3 keys and manages blocking during reload.
            :param event: The pygame event object
        '''
        current_weapon = self.get_current_weapon()

        # Handle weapon switching via 1/2/3 keys
        if event.type == pg.KEYDOWN:
            if event.key in WEAPON_SLOT_KEYS:
                weapon_id = WEAPON_SLOT_KEYS[event.key]
                self.try_switch_weapon(weapon_id)

        if self.get_player_ammo() > 0:
            # Handle firing
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    # For single-shot weapons (shotgun)
                    if not current_weapon.is_auto_fire():
                        if not self.weapon_shot and not current_weapon.is_reloading():
                            # Play weapon-specific sound
                            self.game.sound_manager.play_weapon_sound(current_weapon.get_weapon_sound_id())
                            # Set the shot state to True
                            self.weapon_shot = True
                            # Reduce ammo
                            self.ammo -= 1
                            # Trigger reload/animation
                            current_weapon.set_reloading(True)
                    else:
                        # For auto-fire weapons, just mark button as pressed (tracking continues in update loop)
                        pass

            # Handle mouse button release for auto-fire weapons
            elif event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    # Auto-fire tracking stops here, will be handled in update() based on key press
                    pass


    def update_auto_fire(self):
        '''
            This method handles continuous fire for auto-fire weapons (an94, minigun) when mouse button is held.
        '''
        current_weapon = self.get_current_weapon()

        # Only process auto-fire if weapon supports it
        if not current_weapon.is_auto_fire():
            return

        # Check if left mouse button is currently pressed
        mouse_buttons = pg.mouse.get_pressed()
        if mouse_buttons[0]:  # Left mouse button is pressed
            # Fire if weapon cooldown allows and not currently animating
            if current_weapon.can_fire() and not current_weapon.is_reloading():
                # Play weapon-specific sound
                self.game.sound_manager.play_weapon_sound(current_weapon.get_weapon_sound_id())
                # Set weapon_shot to True so enemies can detect the hit
                self.weapon_shot = True
                # Reduce ammo
                self.ammo -= 1
                # Trigger animation
                current_weapon.set_reloading(True)
        else:
            # Reset weapon_shot when mouse button is released
            self.weapon_shot = False


    def check_health_recovery_mode(self):
        # This method checks if the player is in health recovery mode by comparing the current time with the previous time the player took damage.
        self.health_recover_mode = False
        time_now = pg.time.get_ticks()
        # If the time elapsed since the last time the player took damage exceeds the defined health recovery delay, it sets the health recovery mode to True, allowing the player to start recovering health over time.
        if time_now - self.time_prev > self.health_recovery_delay:
            self.time_prev = time_now
            self.health_recover_mode = True


    def recover_player_health(self):
        # This method checks if the player is in health recovery mode and if their health is below the maximum health.
        # If both conditions are true, it increases the player's health by 1 point.
        self.check_health_recovery_mode()
        if self.health_recover_mode and self.health < PLAYER_MAX_HEALTH:
            # Increase the player's health by 1 point to allow for gradual health recovery over time.
            self.health += 2


    def is_game_over(self):
        if self.health < 1:
            # self.game.sound_manager.play_game_over()
            self.game.render_engine.show_game_over()
            pg.display.flip()
            pg.time.delay(4000)
            from menu import Menu
            menu = Menu(self.game.get_game_result())
            menu.run()