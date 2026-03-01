import pygame as pg


class SoundManager:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = 'assets/sound/'
        self.main_theme = pg.mixer.music.load(self.path + 'doom_theme.mp3')
        self.shotgun = pg.mixer.Sound(self.path + 'shotgun.wav')
        self.enemy_pain = pg.mixer.Sound(self.path + 'enemy_pain.wav')
        self.enemy_death = pg.mixer.Sound(self.path + 'enemy_death.wav')
        self.enemy_shot = pg.mixer.Sound(self.path + 'enemy_shot.wav')
        self.player_pain = pg.mixer.Sound(self.path + 'player_pain.wav')
        self.game_over = pg.mixer.Sound(self.path + 'game_over.wav')
        pg.mixer.music.set_volume(0.4)

    def play_game_over(self):
        # Play the game over music
        self.game_over.play()

    def play_shotgun(self):
        # Play the shotgun sound effect
        self.shotgun.play()

    def play_enemy_pain(self):
        # Play the enemy pain sound effect
        self.enemy_pain.play()

    def play_enemy_death(self):
        # Play the enemy death sound effect
        self.enemy_death.play()

    def play_enemy_shot(self):
        # Play the enemy shot sound effect
        self.enemy_shot.play()

    def play_player_pain(self):
        # Play the player pain sound effect
        self.player_pain.play()