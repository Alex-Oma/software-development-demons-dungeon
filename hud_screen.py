import pygame as pg
from global_settings import *

class HudScreen:
    def __init__(self, game):
        self.game = game
        self.font = pg.font.Font(FONT, 50)

    def draw(self, score, level, ammo, enemies_killed, player_health):
        # Here, this method is used to draw the player's image on the level.
        self.score(score)
        self.show_level(level)
        self.show_ammo(ammo)
        self.show_enemies_killed(enemies_killed)
        self.show_player_health(player_health)


    # Here, this function displays the variable score on the screen of the game and keeps count of the player's score and sets the font and size of the text.
    def score(self, count):
        # This method is used to display the player's score on the screen.
        # It takes a parameter count, which represents the player's current score.
        # The method uses the font attribute to render the text "Score: " followed by the value of count in yellow color.
        # Finally, it blits the rendered text onto the game screen at the position (10, 0).
        text = self.font.render("Score: " + str(count), True, RED)
        self.game.screen.blit(text, [10, 0])


    def show_level(self, level):
        # This method is used to display the current level of the game on the screen.
        # It takes a parameter level, which represents the current level of the game.
        # The method uses the font attribute to render the text "Level: " followed by the value of level in yellow color.
        # Finally, it blits the rendered text onto the game screen at the position (240, 0).
        text = self.font.render("Level: " + str(level), True, RED)
        self.game.screen.blit(text, [240, 0])


    def show_ammo(self, ammo):
        # This method is used to display the player's current ammunition on the screen.
        # It takes a parameter ammo, which represents the player's current ammunition count.
        # The method uses the font attribute to render the text "Ammo: " followed by the value of ammo in yellow color.
        # Finally, it blits the rendered text onto the game screen at the position (470, 0).
        text = self.font.render("Ammo: " + str(ammo), True, RED)
        self.game.screen.blit(text, [470, 0])


    def show_enemies_killed(self, enemies_killed):
        # This method is used to display the number of enemies killed by the player on the screen.
        # It takes a parameter enemies_killed, which represents the number of enemies the player has killed.
        # The method uses the font attribute to render the text "Enemies Killed: " followed by the value of enemies_killed in yellow color.
        # Finally, it blits the rendered text onto the game screen at the position (730, 0).
        text = self.font.render("Enemies Killed: " + str(enemies_killed), True, RED)
        self.game.screen.blit(text, [730, 0])

    def show_player_health(self, player_health):
        # This method is used to display the player's health on the screen.
        # It takes a parameter player_health, which represents the player's current health.
        # The method uses the font attribute to render the text "Player Health: " followed by the value of player_health in yellow color.
        # Finally, it blits the rendered text onto the game screen at the position (1100, 0).
        text = self.font.render("Player Health: " + str(player_health), True, RED)
        self.game.screen.blit(text, [1100, 0])

