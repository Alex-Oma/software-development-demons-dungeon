import pygame as pg


class SoundManager:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = 'assets/sound/'
        self.main_theme = pg.mixer.music.load(self.path + 'doom_theme.mp3')
        pg.mixer.music.set_volume(0.3)