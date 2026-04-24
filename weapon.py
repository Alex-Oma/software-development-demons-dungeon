from sprite import *
from animated_sprite import *
import time


class Weapon(AnimatedSprite):
    '''
    This class represents a weapon in the game and extends the AnimatedSprite class to provide functionality for animating the weapon's shooting action.
    The Weapon class now supports multiple weapon types (shotgun, an94, minigun) with configurable stats, fire modes, and animations.
    Each weapon instance is configured via the WEAPON_CONFIG in global_settings.

    Supports Doom WAD sprite organization:
    - idle_sprites: Weapon idle/base state (e.g., AN94A0.png)
    - fire_sprites: Muzzle flash animation frames (e.g., MZZLA0.png, MZZLB0.png, etc.)
    '''
    def __init__(self, game, weapon_id='shotgun'):
        # Load weapon configuration from global settings
        self.weapon_config = WEAPON_CONFIG.get(weapon_id, WEAPON_CONFIG['shotgun'])
        self.weapon_id = weapon_id

        # Extract weapon-specific settings
        path = self.weapon_config['path']
        scale = self.weapon_config['scale']
        animation_time = self.weapon_config['animation_time']

        # Initialize the parent AnimatedSprite with weapon configuration
        super().__init__(game=game, path=path, scale=scale, animation_time=animation_time)

        # Load idle and fire sprites from configuration
        self.idle_sprites = self.load_custom_sprites(self.weapon_config.get('idle_sprites', [path]))
        self.fire_sprites = self.load_custom_sprites(self.weapon_config.get('fire_sprites', self.idle_sprites))

        # Initialize with idle sprites
        self.images = self.idle_sprites.copy() if self.idle_sprites else self.images

        # Calculate the position of the weapon on the screen, centering it horizontally and placing it at the bottom
        self.weapon_pos = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT - self.images[0].get_height())

        # Initialize the reloading state to False, which will be set to True when the weapon is fired
        self.reloading = False

        # Store the number of images in the animation sequence for managing animation frames
        self.num_images = len(self.images)

        # Initialize a frame counter to keep track of the current frame in the shooting animation
        self.frame_counter = 0

        # Store weapon-specific stats from configuration
        self.damage = self.weapon_config['damage']
        self.fire_delay_ms = self.weapon_config['fire_delay_ms']
        self.auto_fire = self.weapon_config['auto_fire']
        self.sound_id = self.weapon_config['sound_id']

        # Initialize fire cooldown timer for auto-fire weapons
        self.last_fire_time = 0

    def load_custom_sprites(self, sprite_paths):
        '''
            Load sprites from a list of explicit file paths.
            Used for Doom WAD weapons with separated idle and fire animation frames.

            :param sprite_paths: List of sprite file paths to load
            :return: deque of loaded and scaled sprites
        '''
        images = deque()
        scale = self.weapon_config['scale']

        # Validate input - ensure sprite_paths is not empty
        if not sprite_paths:
            print(f"Warning: No sprite paths provided for {self.weapon_id}")
            return deque([self.image])

        # Special handling for minigun and AN94 which have multiple fire animation sequences
        if self.weapon_id == 'minigun':
            if sprite_paths and isinstance(sprite_paths[0], list):
                for sequence in sprite_paths:
                    if isinstance(sequence, list) and len(sequence) >= 2:
                        combined = self.combine_images_vertical(sequence[0], sequence[1], scale=scale, vertical_spacing=0, horizontal_spacing=0)
                        if combined:
                            images.append(combined)
            else:
                # Load individual sprites
                for sprite_path in sprite_paths:
                    try:
                        img = pg.image.load(sprite_path).convert_alpha()
                        # Scale the image
                        scaled_img = pg.transform.smoothscale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
                        images.append(scaled_img)
                    except Exception as e:
                        print(f"Warning: Failed to load sprite {sprite_path}: {e}")
        elif self.weapon_id == 'an94':
            if sprite_paths and isinstance(sprite_paths[0], list):
                for sequence in sprite_paths:
                    if isinstance(sequence, list) and len(sequence) >= 2:
                        combined = self.combine_images_vertical(sequence[0], sequence[1], scale=scale, vertical_spacing=40, horizontal_spacing=-10)
                        if combined:
                            images.append(combined)
            else:
                # Load individual sprites
                for sprite_path in sprite_paths:
                    try:
                        img = pg.image.load(sprite_path).convert_alpha()
                        # Scale the image
                        scaled_img = pg.transform.smoothscale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
                        images.append(scaled_img)
                    except Exception as e:
                        print(f"Warning: Failed to load sprite {sprite_path}: {e}")
        else:
            # Load individual sprites
            for sprite_path in sprite_paths:
                try:
                    img = pg.image.load(sprite_path).convert_alpha()
                    # Scale the image
                    scaled_img = pg.transform.smoothscale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
                    images.append(scaled_img)
                except Exception as e:
                    print(f"Warning: Failed to load sprite {sprite_path}: {e}")

        # Fallback if no images loaded
        if not images:
            print(f"Warning: No sprites loaded for {self.weapon_id}, using fallback")
            return deque([self.image])

        return images

    def combine_images_vertical(self, top_image_path, bottom_image_path, scale=1.0, vertical_spacing=0, horizontal_spacing=0):
        '''
            Combines two images vertically (stacked) into a single image.
            Useful for layering weapon sprites (e.g., weapon + muzzle flash overlay).

            :param top_image_path: Path to the top image file
            :param bottom_image_path: Path to the bottom image file
            :param scale: Scale factor to apply to both images
            :param vertical_spacing: Vertical spacing (pixels) between the two images
            :param horizontal_spacing: Horizontal spacing (pixels) between the two images
            :return: Combined pygame Surface with both images stacked, or None if failed

        '''
        try:
            # Load both images with alpha transparency
            top_img = pg.image.load(top_image_path).convert_alpha()
            bottom_img = pg.image.load(bottom_image_path).convert_alpha()

            # Scale both images
            top_scaled = pg.transform.smoothscale(
                top_img,
                (int(top_img.get_width() * scale), int(top_img.get_height() * scale))
            )
            bottom_scaled = pg.transform.smoothscale(
                bottom_img,
                (int(bottom_img.get_width() * scale), int(bottom_img.get_height() * scale))
            )

            # Calculate combined surface dimensions
            width = bottom_scaled.get_width()  # Use the width of the bottom image (weapon sprite) as the combined width
            # width = max(top_scaled.get_width(), bottom_scaled.get_width())
            height = top_scaled.get_height() + bottom_scaled.get_height() + vertical_spacing

            # Create a transparent surface to hold both images
            combined_surface = pg.Surface((width, height), pg.SRCALPHA)

            # Blit top image at the top
            top_x = (width - top_scaled.get_width()) // 2
            # combined_surface.blit(top_scaled, (top_x, 0))
            combined_surface.blit(top_scaled, (horizontal_spacing, top_scaled.get_height()))

            # Blit bottom image at the bottom
            bottom_x = (width - bottom_scaled.get_width()) // 2
            bottom_y = top_scaled.get_height() + vertical_spacing
            # combined_surface.blit(bottom_scaled, (bottom_x, bottom_y))
            combined_surface.blit(bottom_scaled, (0, bottom_y))

            return combined_surface

        except Exception as e:
            print(f"Error combining images {top_image_path} + {bottom_image_path}: {e}")
            return None

    def combine_images_horizontal(self, left_image_path, right_image_path, scale=1.0, spacing=0):
        '''
            Combines two images horizontally (side-by-side) into a single image.
            Useful for wide weapon sprites or dual-wielding effects.

            :param left_image_path: Path to the left image file
            :param right_image_path: Path to the right image file
            :param scale: Scale factor to apply to both images
            :param spacing: Horizontal spacing (pixels) between the two images
            :return: Combined pygame Surface with both images side-by-side, or None if failed

            Example:
                # Combine two weapon sprite variations side-by-side
                combined = weapon.combine_images_horizontal(
                    'assets/sprites/weapon/minigun/MNGFA0.png',
                    'assets/sprites/weapon/minigun/MNGGA0.png',
                    scale=0.4,
                    spacing=5
                )
        '''
        try:
            # Load both images with alpha transparency
            left_img = pg.image.load(left_image_path).convert_alpha()
            right_img = pg.image.load(right_image_path).convert_alpha()

            # Scale both images
            left_scaled = pg.transform.smoothscale(
                left_img,
                (int(left_img.get_width() * scale), int(left_img.get_height() * scale))
            )
            right_scaled = pg.transform.smoothscale(
                right_img,
                (int(right_img.get_width() * scale), int(right_img.get_height() * scale))
            )

            # Calculate combined surface dimensions
            width = left_scaled.get_width() + right_scaled.get_width() + spacing
            height = max(left_scaled.get_height(), right_scaled.get_height())

            # Create a transparent surface to hold both images
            combined_surface = pg.Surface((width, height), pg.SRCALPHA)

            # Blit left image on the left
            left_y = (height - left_scaled.get_height()) // 2
            combined_surface.blit(left_scaled, (0, left_y))

            # Blit right image on the right
            right_x = left_scaled.get_width() + spacing
            right_y = (height - right_scaled.get_height()) // 2
            combined_surface.blit(right_scaled, (right_x, right_y))

            return combined_surface

        except Exception as e:
            print(f"Error combining images {left_image_path} + {right_image_path}: {e}")
            return None


    def get_weapon_damage(self):
        '''
            This method returns the damage value of the current weapon.
        '''
        return self.damage

    def get_weapon_name(self):
        '''
            This method returns the friendly name of the current weapon.
        '''
        return self.weapon_config['name']

    def get_weapon_icon_path(self):
        '''
            This method returns the icon path for HUD display.
        '''
        return self.weapon_config['icon_path']

    def get_weapon_sound_id(self):
        '''
            This method returns the sound identifier for the current weapon.
        '''
        return self.sound_id

    def is_auto_fire(self):
        '''
            This method returns whether the current weapon supports auto-fire (hold-to-shoot).
        '''
        return self.auto_fire

    def can_fire(self):
        '''
            This method checks if the weapon can fire based on cooldown (for auto-fire weapons).
        '''
        current_time = time.time() * 1000  # Convert to milliseconds
        if current_time - self.last_fire_time >= self.fire_delay_ms:
            self.last_fire_time = current_time
            return True
        return False

    def reset_fire_cooldown(self):
        '''
            This method resets the fire cooldown timer.
        '''
        self.last_fire_time = 0

    def is_reloading(self):
        '''
            This method returns the current reloading state of the weapon, indicating whether the weapon is currently in the process of firing and animating the shooting action.
        '''
        return self.reloading

    def set_reloading(self, value):
        '''
            This method sets the reloading state of the weapon to the specified value, allowing other parts of the game logic to control when the weapon is in the shooting animation state.
        '''
        self.reloading = value

    def animate_shot(self):
        '''
            This method handles the animation of the weapon when it is fired.
            Supports Doom WAD animation pattern:
            1. Switch to fire_sprites (muzzle flash frames)
            2. Cycle through firing animation
            3. Return to idle_sprites when complete

            If the weapon is in the reloading state, it checks if the animation trigger is set to True,
            which indicates that it's time to switch to the next frame in the shooting animation.
            It rotates the deque of images to switch to the next frame and updates the current image being displayed.
            The frame counter is incremented, and if it reaches the total number of images in the animation sequence,
            it resets the reloading state and frame counter, indicating that the shooting animation has completed.
        '''
        if self.reloading:
            # When the weapon is reloading, set the player's shot state to False to prevent firing while the animation is in progress.
            self.game.player.weapon_shot = False

            # If just started reloading, switch to fire sprites on first frame
            if self.frame_counter == 0:
                self.images = self.fire_sprites.copy()
                self.num_images = len(self.images)

            # Check if the animation trigger is set to True, which indicates that it's time to switch to the next frame in the shooting animation.
            if self.animation_trigger:
                # Rotate the deque of images to switch to the next frame in the shooting animation and update the current image being displayed.
                self.images.rotate(-1)
                # Update the current image to the first image in the deque after rotation, which represents the next frame in the shooting animation.
                self.image = self.images[0]
                # Increment the frame counter to keep track of the current frame in the shooting animation sequence.
                self.frame_counter += 1
                # Check if the frame counter has reached the total number of images in the animation sequence, which indicates that the shooting animation has completed.
                if self.frame_counter >= self.num_images:
                    # Reset the reloading state to False and the frame counter to 0, indicating that the shooting animation has completed and the weapon is ready to be fired again.
                    self.reloading = False
                    # Reset the frame counter to 0 to start the animation sequence from the beginning the next time the weapon is fired.
                    self.frame_counter = 0
                    # Switch back to idle sprites
                    self.images = self.idle_sprites.copy()
                    self.num_images = len(self.images)
                    self.image = self.images[0]

    def draw(self):
        # Render the weapon on the game screen by blitting the current image (the first image in the deque) at the calculated weapon position.
        self.weapon_pos = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT - self.images[0].get_height())
        self.game.screen.blit(self.images[0], self.weapon_pos)

    def update(self):
        '''
            This method updates the weapon's state by first checking the animation time to determine if it's time to switch to the next frame in the shooting animation,
            and then calling the animate_shot method to handle the shooting animation if the weapon is currently in the reloading state.
        '''
        self.check_animation_time()
        self.animate_shot()