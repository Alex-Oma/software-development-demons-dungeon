from sprite import *
from animated_sprite import *
from random import randint, random

class Enemy(AnimatedSprite):
    def __init__(self, game, path='assets/sprites/animated/enemies/blood_ghost/GHSTA1.png', pos=(10.5, 5.5),
                 scale=0.6, shift=0.38, animation_time=180, prefix='GHST'):
        super().__init__(game, path, pos, scale, shift, animation_time)
        # Let's load attack images, death images, idle images, pain images, walk images and gib images for the enemy using the get_event_images method.
        self.attack_images = self.get_event_images(self.path, ["E1.png", "F0.png", "G0.png"], prefix)
        self.death_images = self.get_event_images(self.path, [f"{c}0.png" for c in "IJKLMNOP"], prefix)
        self.idle_images = self.get_event_images(self.path, ["A1.png", "B1.png"], prefix)
        self.pain_images = self.get_event_images(self.path, ["H0.png"], prefix)
        self.walk_images = self.get_event_images(self.path, ["A1.png", "B1.png", "C1.png", "D1.png"], prefix)
        self.gib_images = self.get_event_images(self.path, [f"GB{c}0.png" for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"], prefix[:2])

        # Set the speed, size, health, attack damage, accuracy, alive status, pain status, ray cast value, frame counter, and player search trigger for the enemy.
        self.player_search_trigger = False
        self.ray_cast_value = False
        self.alive = True
        self.pain = False
        self.frame_counter = 0
        self.accuracy = 0.15
        # Set the movement speed for the enemy, which will determine how fast the enemy moves towards the player when it is in pursuit.
        self.speed = 0.03
        # Set the attack damage for the enemy to 10, which will be used to determine how much damage the enemy inflicts on the player when it successfully attacks.
        self.attack_damage = 10
        # Set the size of the enemy, which will be used for collision detection and movement calculations. The size can be adjusted based on the desired scale of the enemy in the game world.
        self.size = 20
        # Set the health of the enemy to 100, which will be reduced when the enemy takes damage from the player's attacks.
        self.health = 100
        # Set the score value for the enemy, which will be awarded to the player when the enemy is defeated.
        self.score_value = 100
        # Set the attack distance to a random value between 3 and 6, which will determine how close the enemy needs to be to the player in order to attack.
        self.attack_dist = randint(2, 7)

    def get_score_value(self):
        # This method returns the score value for the enemy, which can be used to determine how many points the player receives when they defeat this enemy.
        return self.score_value

    def set_score_value(self, value):
        # This method allows you to set the score value for the enemy, which can be used to determine how many points the player receives when they defeat this enemy.
        self.score_value = value

    def check_wall(self, x, y):
        # Check if the specified (x, y) position is a wall by checking if it is not in the game's world map, which contains the positions of all walls in the game.
        return (x, y) not in self.game.map.get_world_map()

    def check_wall_collision(self, dx, dy):
        # Check for wall collisions by checking if the enemy can move to the new position (x + dx * size, y) and (x, y + dy * size) without colliding with a wall.
        if self.check_wall(int(self.x + dx * self.size), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy * self.size)):
            self.y += dy

    def update(self):
        # Update the enemy's state by first checking the animation time to determine if it's time to switch to the next frame in the animation,
        # then getting the sprite's position and rendering it on the screen,
        # and finally running the enemy's logic to determine its behavior based on its current state and interactions with the player.
        self.check_animation_time()
        self.get_sprite()
        self.run_enemy_logic()

    def enemy_movement(self):
        # Get the next position for the enemy to move towards using the game's pathfinding system, which calculates the path from the enemy's current position to the player's position on the map.
        # next_pos = self.game.pathfinding.get_path(self.map_pos, self.game.player.map_pos)
        # next_x, next_y = next_pos
        #
        # # Let's check if the next position is not occupied by another NPC before moving towards it.
        # # If it's not occupied, we calculate the angle to the next position and move the enemy in that direction using the speed attribute.
        # if next_pos not in self.game.object_handler.npc_positions:
        #     # Let's calculate the angle to the next position using the atan2 function, which gives us the angle in radians between the enemy's current position and the next position.
        #     angle = math.atan2(next_y + 0.5 - self.y, next_x + 0.5 - self.x)
        #     dx = math.cos(angle) * self.speed
        #     dy = math.sin(angle) * self.speed
        #     # Finally, we check for wall collisions using the check_wall_collision method to ensure that the enemy does not move through walls while trying to reach the next position.
        #     self.check_wall_collision(dx, dy)
        pass

    def enemy_animate_pain(self):
        # If the enemy is in pain, we animate the pain images to show the enemy's reaction to being hit.
        self.animate(self.pain_images)
        # If the animation trigger is set, which indicates that it's time to switch to the next frame in the pain animation,
        # we set the pain status to False, allowing the enemy to return to its normal behavior after showing the pain animation.
        if self.animation_trigger:
            self.pain = False

    def enemy_check_health(self):
        # If the enemy's health drops below 1, we set the alive status to False to indicate that the enemy is dead and play the NPC death sound.
        if self.health < 1:
            self.alive = False
            self.game.player.increase_kill_count()
            self.game.player.increase_score(self.get_score_value())
            self.game.sound_manager.play_enemy_death()

    def check_enemy_is_hit(self):
        # If the ray cast value is True, which indicates that the player has a clear line of sight to the enemy, and the player has shot their weapon, we check if the enemy is hit by the player's shot.
        if self.ray_cast_value and self.game.player.weapon_shot:
            # We check if the enemy's horizontal position (screen_x) is within the range of the player's shot by comparing it to the half width of the screen and the half width of the enemy's sprite.
            if HALF_WIDTH - self.sprite_half_width < self.screen_x < HALF_WIDTH + self.sprite_half_width:
                # If the enemy is hit, we play the NPC pain sound, set the player's shot state to False to prevent multiple hits from a single shot,
                # set the pain status to True to trigger the pain animation, and reduce the enemy's health by the damage value of the player's weapon.
                # Finally, we call the check_health method to see if the enemy's health has dropped below zero and if it should be marked as dead.
                self.game.sound_manager.play_enemy_pain()
                self.game.player.weapon_shot = False
                self.pain = True
                self.health -= self.game.weapon.get_weapon_damage()
                self.enemy_check_health()


    def enemy_animate_death(self):
        # If the enemy is not alive, we check if the global trigger for animations is set and if the frame counter is less than the number of death images minus one.
        # If both conditions are true, we rotate the death images to switch to the next frame in the death animation and update the enemy's image to the current frame.
        # We also increment the frame counter to keep track of which frame of the death animation we are currently on.
        if not self.alive:
            if self.game.global_trigger and self.frame_counter < len(self.death_images) - 1:
                self.death_images.rotate(-1)
                self.image = self.death_images[0]
                self.frame_counter += 1


    def enemy_animate_death_through_gib(self):
        # If the enemy is not alive, we check if the global trigger for animations is set and if the frame counter is less than the number of death images minus one.
        # If both conditions are true, we rotate the death images to switch to the next frame in the death animation and update the enemy's image to the current frame.
        # We also increment the frame counter to keep track of which frame of the death animation we are currently on.
        if not self.alive:
            if self.game.global_trigger and self.frame_counter < len(self.gib_images) - 1:
                self.gib_images.rotate(-1)
                self.image = self.gib_images[0]
                self.frame_counter += 1


    def run_enemy_logic(self):
        # If the enemy is alive, we first check if the player is in line of sight using ray casting and then check if the enemy is hit by the player's shot.
        if self.alive:
            self.ray_cast_value = self.ray_cast_player_versus_enemy()
            self.check_enemy_is_hit()

            # If the enemy is in pain, we animate the pain images to show the enemy's reaction to being hit.
            if self.pain:
                self.enemy_animate_pain()
            elif self.ray_cast_value:
                # If the player is in line of sight, we set the player search trigger to True, which indicates that the enemy has detected the player and will start moving towards them.
                self.player_search_trigger = True

                # If the distance to the player is less than the attack distance, we animate the attack images and call the attack method to perform an attack on the player.
                if self.dist < self.attack_dist:
                    self.animate(self.attack_images)
                    self.enemy_attack()
                else:
                    # If the distance to the player is greater than or equal to the attack distance,
                    # we animate the walk images to show the enemy moving towards the player and call the movement method to update the enemy's position.
                    self.animate(self.walk_images)
                    self.enemy_movement()

            elif self.player_search_trigger:
                # If the player search trigger is True, which indicates that the enemy has detected the player but is not currently in line of sight,
                # we continue to animate the walk images and call the movement method to keep the enemy moving towards the player's last known position.
                self.animate(self.walk_images)
                self.enemy_movement()

            else:
                # If the player search trigger is False, which indicates that the enemy has not detected the player, we animate the idle images to show the enemy in a passive state.
                self.animate(self.idle_images)
        else:
            # If the enemy is not alive, we call the animate_death method to handle the death animation for the enemy.
            self.enemy_animate_death()
            # self.enemy_animate_death_through_gib()


    def enemy_attack(self):
        # If the animation trigger is set, which indicates that it's time to switch to the next frame in the attack animation,
        # we play the NPC shot sound and check if the attack hits the player based on the enemy's accuracy. If it hits, we call the get_damage method on the player to apply damage to them.
        if self.animation_trigger:
            self.game.sound_manager.play_enemy_shot()
            if random() < self.accuracy:
                self.game.player.player_gets_damage(self.attack_damage)


    @property
    def map_pos(self):
        return int(self.x), int(self.y)

    def ray_cast_player_versus_enemy(self):
        # This method performs ray casting to determine if the enemy has a clear line of sight to the player.
        # It calculates the distance to walls and the player in both vertical and horizontal directions,
        # and compares these distances to determine if the player is visible to the enemy.
        # If the player is within line of sight and not blocked by walls, it returns True; otherwise, it returns False.
        if self.game.player.map_pos == self.map_pos:
            return True

        wall_dist_v, wall_dist_h = 0, 0
        player_dist_v, player_dist_h = 0, 0

        # Get the player's position (ox, oy) and map position (x_map, y_map) to use in the ray casting calculations.
        ox, oy = self.game.player.pos
        x_map, y_map = self.game.player.map_pos

        # Calculate the angle of the ray from the enemy to the player using the enemy's current angle (theta) and the position of the player.
        ray_angle = self.theta

        sin_a = math.sin(ray_angle)
        cos_a = math.cos(ray_angle)

        # horizontals
        y_hor, dy = (y_map + 1, 1) if sin_a > 0 else (y_map - 1e-6, -1)

        # Calculate the depth to the horizontal intersection (y_hor) using the player's position and the angle of the ray.
        depth_hor = (y_hor - oy) / sin_a
        x_hor = ox + depth_hor * cos_a

        # Calculate the delta depth for horizontal intersections, which is the distance between horizontal grid lines in the ray's path, and the corresponding change in x (dx) for each step along the ray.
        delta_depth = dy / sin_a
        dx = delta_depth * cos_a

        # Perform ray casting for horizontal intersections by iterating up to a maximum depth (MAX_DEPTH) and checking if the current tile (tile_hor) is the player's map position or if it is a wall in the world map.
        for i in range(MAX_DEPTH):
            # Calculate the current tile position (tile_hor) based on the current horizontal intersection coordinates (x_hor, y_hor).
            tile_hor = int(x_hor), int(y_hor)
            # Check if the current tile (tile_hor) is the player's map position.
            # If it is, we set the player distance for horizontal intersections (player_dist_h) to the current depth (depth_hor) and break out of the loop, indicating that the player is visible in this direction.
            if tile_hor == self.map_pos:
                # If the current tile is the player's map position, we set the player distance for horizontal intersections (player_dist_h) to the current depth (depth_hor) and break out of the loop, indicating that the player is visible in this direction.
                player_dist_h = depth_hor
                break
            # If the current tile (tile_hor) is a wall in the world map, we set the wall distance for horizontal intersections (wall_dist_h) to the current depth (depth_hor) and break out of the loop, indicating that the line of sight is blocked by a wall in this direction.
            if tile_hor in self.game.map.get_world_map():
                # If the current tile is a wall in the world map, we set the wall distance for horizontal intersections (wall_dist_h) to the current depth (depth_hor) and break out of the loop, indicating that the line of sight is blocked by a wall in this direction.
                wall_dist_h = depth_hor
                break
            # If neither the player nor a wall is found at the current horizontal intersection, we move to the next horizontal intersection by adding the delta depth (delta_depth) to the current depth (depth_hor) and updating the horizontal coordinates (x_hor, y_hor) accordingly.
            x_hor += dx
            y_hor += dy
            depth_hor += delta_depth

        # verticals
        x_vert, dx = (x_map + 1, 1) if cos_a > 0 else (x_map - 1e-6, -1)

        # Calculate the depth to the vertical intersection (x_vert) using the player's position and the angle of the ray.
        depth_vert = (x_vert - ox) / cos_a
        y_vert = oy + depth_vert * sin_a

        # Calculate the delta depth for vertical intersections, which is the distance between vertical grid lines in the ray's path, and the corresponding change in y (dy) for each step along the ray.
        delta_depth = dx / cos_a
        dy = delta_depth * sin_a

        # Perform ray casting for vertical intersections by iterating up to a maximum depth (MAX_DEPTH) and checking if the current tile (tile_vert) is the player's map position or if it is a wall in the world map.
        for i in range(MAX_DEPTH):
            # Calculate the current tile position (tile_vert) based on the current vertical intersection coordinates (x_vert, y_vert).
            tile_vert = int(x_vert), int(y_vert)
            # Check if the current tile (tile_vert) is the player's map position.
            # If it is, we set the player distance for vertical intersections (player_dist_v) to the current depth (depth_vert) and break out of the loop, indicating that the player is visible in this direction.
            if tile_vert == self.map_pos:
                # If the current tile is the player's map position, we set the player distance for vertical intersections (player_dist_v) to the current depth (depth_vert) and break out of the loop, indicating that the player is visible in this direction.
                player_dist_v = depth_vert
                break
            # If the current tile (tile_vert) is a wall in the world map, we set the wall distance for vertical intersections (wall_dist_v) to the current depth (depth_vert) and break out of the loop, indicating that the line of sight is blocked by a wall in this direction.
            if tile_vert in self.game.map.world_map:
                # If the current tile is a wall in the world map, we set the wall distance for vertical intersections (wall_dist_v) to the current depth (depth_vert) and break out of the loop, indicating that the line of sight is blocked by a wall in this direction.
                wall_dist_v = depth_vert
                break
            # If neither the player nor a wall is found at the current vertical intersection, we move to the next vertical intersection by adding the delta depth (delta_depth) to the current depth (depth_vert) and updating the vertical coordinates (x_vert, y_vert) accordingly.
            x_vert += dx
            y_vert += dy
            depth_vert += delta_depth

        # After performing ray casting for both horizontal and vertical intersections, we calculate the maximum player distance (player_dist) and wall distance (wall_dist) by taking the maximum of the respective distances from both directions.
        player_dist = max(player_dist_v, player_dist_h)
        wall_dist = max(wall_dist_v, wall_dist_h)

        # Finally, we compare the player distance and wall distance to determine if the player is visible to the enemy. If the player distance is greater than zero and less than the wall distance, or if there is no wall distance (indicating that there are no walls blocking the line of sight), we return True to indicate that the player is visible; otherwise, we return False.
        if 0 < player_dist < wall_dist or not wall_dist:
            # If the player distance is greater than zero and less than the wall distance, or if there is no wall distance (indicating that there are no walls blocking the line of sight), we return True to indicate that the player is visible; otherwise, we return False.
            return True

        # If the player is not visible to the enemy based on the ray casting calculations, we return False to indicate that the player is not in line of sight.
        return False

class BloodGhostEnemy(Enemy):
    def __init__(self, game, path='assets/sprites/animated/enemies/blood_ghost/GHSTA1.png', pos=(10.5, 5.5),
                 scale=0.6, shift=0.38, animation_time=180, prefix='GHST'):
        super().__init__(game, path, pos, scale, shift, animation_time)
