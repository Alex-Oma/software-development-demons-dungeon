from sprite import *
from animated_sprite import *


class Weapon(AnimatedSprite):
    '''
    This class represents a weapon in the game, specifically a shotgun, and extends the AnimatedSprite class to provide functionality for animating the weapon's shooting action.
    The Weapon class initializes the weapon's images, position, and animation parameters, and includes methods for animating the shooting action and drawing the weapon on the screen.
    The animate_shot method handles the animation of the weapon when it is fired, while the draw method is responsible for rendering the weapon on the game screen.
    The update method checks the animation time and triggers the shooting animation when necessary.
    '''
    def __init__(self, game, path='assets/sprites/weapon/shotgun/0.png', scale=0.4, animation_time=90):
        super().__init__(game=game, path=path, scale=scale, animation_time=animation_time)
        # Load the weapon images and scale them according to the specified scale factor, storing them in a deque for easy rotation during animation.
        self.images = deque([pg.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale)) for img in self.images])
        # Calculate the position of the weapon on the screen, centering it horizontally and placing it at the bottom of the screen based on the dimensions of the first image in the deque.
        self.weapon_pos = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT - self.images[0].get_height())
        # Initialize the reloading state to False, which will be set to True when the weapon is fired and the shooting animation is in progress.
        self.reloading = False
        # Store the number of images in the animation sequence for later use in managing the animation frames.
        self.num_images = len(self.images)
        # Initialize a frame counter to keep track of the current frame in the shooting animation, which will be incremented as the animation progresses.
        self.frame_counter = 0
        # Set the damage value for the weapon, which is used in the game logic to determine how much damage the weapon inflicts on targets when fired.
        self.damage = 50


    def get_weapon_damage(self):
        '''
            This method returns the damage value of the weapon, which is used in the game logic to determine how much damage the weapon inflicts on targets when fired.
        '''
        return self.damage

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
            If the weapon is in the reloading state, it checks if the animation trigger is set to True,
            which indicates that it's time to switch to the next frame in the shooting animation.
            It rotates the deque of images to switch to the next frame and updates the current image being displayed.
            The frame counter is incremented, and if it reaches the total number of images in the animation sequence,
            it resets the reloading state and frame counter, indicating that the shooting animation has completed.
        '''
        if self.reloading:
            # When the weapon is reloading, set the player's shot state to False to prevent firing while the animation is in progress.
            self.game.player.weapon_shot = False
            # Check if the animation trigger is set to True, which indicates that it's time to switch to the next frame in the shooting animation.
            if self.animation_trigger:
                # Rotate the deque of images to switch to the next frame in the shooting animation and update the current image being displayed.
                self.images.rotate(-1)
                # Update the current image to the first image in the deque after rotation, which represents the next frame in the shooting animation.
                self.image = self.images[0]
                # Increment the frame counter to keep track of the current frame in the shooting animation sequence.
                self.frame_counter += 1
                # Check if the frame counter has reached the total number of images in the animation sequence, which indicates that the shooting animation has completed.
                if self.frame_counter == self.num_images:
                    # Reset the reloading state to False and the frame counter to 0, indicating that the shooting animation has completed and the weapon is ready to be fired again.
                    self.reloading = False
                    # Reset the frame counter to 0 to start the animation sequence from the beginning the next time the weapon is fired.
                    self.frame_counter = 0

    def draw(self):
        # Render the weapon on the game screen by blitting the current image (the first image in the deque) at the calculated weapon position.
        self.game.screen.blit(self.images[0], self.weapon_pos)

    def update(self):
        '''
            This method updates the weapon's state by first checking the animation time to determine if it's time to switch to the next frame in the shooting animation,
            and then calling the animate_shot method to handle the shooting animation if the weapon is currently in the reloading state.
        '''
        self.check_animation_time()
        self.animate_shot()