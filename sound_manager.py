import pygame as pg


class SoundManager:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = 'assets/sound/'
        self.main_theme = pg.mixer.music.load(self.path + 'doom_theme.mp3')

        # Load weapon-specific shot sounds
        self.shotgun = pg.mixer.Sound(self.path + 'shotgun.wav')
        self.an94 = pg.mixer.Sound(self.path + 'AN94FIRE.wav')
        self.minigun = pg.mixer.Sound(self.path + 'minigun_sound.ogg')

        # Load other sounds
        self.enemy_pain = pg.mixer.Sound(self.path + 'enemy_pain.wav')
        self.enemy_death = pg.mixer.Sound(self.path + 'enemy_death.wav')
        self.enemy_shot = pg.mixer.Sound(self.path + 'enemy_shot.wav')
        self.player_pain = pg.mixer.Sound(self.path + 'player_pain.wav')
        self.game_over = pg.mixer.Sound(self.path + 'game_over.wav')
        pg.mixer.music.set_volume(0.4)

        # Map weapon sound ids to sound objects
        self.weapon_sounds = {
            'shotgun': self.shotgun,
            'an94': self.an94,
            'minigun': self.minigun,
        }

    def play_game_over(self):
        # Play the game over music
        self.game_over.play()

    def play_weapon_sound(self, sound_id):
        '''
            This method plays weapon-specific sound based on the weapon sound id.
            :param sound_id: The sound identifier for the weapon ('shotgun', 'an94', 'minigun')
        '''
        if sound_id in self.weapon_sounds:
            self.weapon_sounds[sound_id].play()

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