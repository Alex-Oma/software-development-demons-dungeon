import pygame as pg
from global_settings import *
import os
from collections import deque
from sprite import Sprite

class AnimatedSprite(Sprite):
    '''
        This class is responsible for creating and rendering animated sprites in the game.
        It extends the Sprite class and adds functionality for loading multiple images from a specified directory to create an animation effect.
        The class manages the timing of the animation and updates the sprite's image based on the elapsed time, allowing for smooth animations in the game.
        The images are loaded into a deque to facilitate easy rotation for animation, and the class checks the animation time to determine when to update the sprite's image to the next frame in the animation sequence.
    '''
    def __init__(self, game, path='assets/sprites/animated/green_light/0.png',
                 pos=(11.5, 3.5), scale=0.8, shift=0.16, animation_time=120):
        # Initialize the animated sprite by calling the parent class constructor and setting up the animation parameters.
        super().__init__(game, path, pos, scale, shift)
        # Set the animation time, which determines how long each frame of the animation should be displayed before switching to the next frame.
        self.animation_time = animation_time
        # Extract the directory path from the provided image path to load all images in that directory for the animation.
        self.path = path.rsplit('/', 1)[0]
        # Load the images for the animation from the specified directory and store them in a deque for easy rotation during animation.
        self.images = self.get_images(self.path)
        # Initialize the previous animation time to the current time to manage the timing of the animation frames.
        self.animation_time_prev = pg.time.get_ticks()
        # Initialize the animation trigger to False, which will be set to True when it's time to switch to the next frame in the animation.
        self.animation_trigger = False

    def update(self):
        '''
           This method updates the animated sprite by first calling the parent class's update method to handle the sprite's position and rendering,
           then checking if it's time to switch to the next frame in the animation using the check_animation_time method,
           and finally calling the animate method to update the sprite's image if the animation trigger is set.
        '''
        super().update()
        self.check_animation_time()
        self.animate(self.images)

    def animate(self, images):
        '''
            This method handles the animation by rotating the deque of images to switch to the next frame in the animation sequence when the animation trigger is set to True.
        '''
        if self.animation_trigger:
            images.rotate(-1)
            self.image = images[0]

    def check_animation_time(self):
        '''
            This method checks if the specified animation time has elapsed since the last frame change.
            If it has, it updates the previous animation time and sets the animation trigger to True,
            indicating that it's time to switch to the next frame in the animation.
        '''
        self.animation_trigger = False
        # Get the current time in milliseconds using Pygame's time module.
        time_now = pg.time.get_ticks()
        # Check if the time elapsed since the last animation frame change exceeds the specified animation time.
        if time_now - self.animation_time_prev > self.animation_time:
            self.animation_time_prev = time_now
            self.animation_trigger = True

    def get_images(self, path):
        '''
            This method loads all images from the specified directory path and returns them as a deque.
            It iterates through the files in the directory, checks if they are files (not directories), and loads them as Pygame images with alpha transparency support.
            The loaded images are appended to a deque, which allows for easy rotation during animation.
        '''
        # Initialize an empty deque to store the loaded images for the animation.
        images = deque()
        # Iterate through the files in the specified directory path.
        for file_name in os.listdir(path):
            # Check if the current item is a file (not a directory) before attempting to load it as an image.
            if os.path.isfile(os.path.join(path, file_name)):
                # Load the image using Pygame's image loading function, converting it to include alpha transparency for proper rendering in the game.
                img = pg.image.load(path + '/' + file_name).convert_alpha()
                # Append the loaded image to the deque of images for the animation.
                images.append(img)
        return images
