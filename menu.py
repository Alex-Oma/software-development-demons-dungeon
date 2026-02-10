from global_settings import *
import pygame as pg
import sys
import json

class Menu:
    def __init__(self, game_result):
        pg.init()
        pg.mouse.set_visible(True)  # When True mouse pointer is visible otherwise it is hidden
        self.screen = pg.display.set_mode(RES)
        pg.display.set_caption(GAME_TITLE_PREFIX.upper() + GAME_TITLE.upper() + " // MAIN MENU")
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.current_menu_option = 1  # this way we track which menu option to highlight
        self.max_menu_options = 5
        self.show_menu_options = True  # when it is true then main menu options are being shown to player
        self.show_leaderboard = False
        self.show_game_credits = False
        self.show_player_name = False
        self.leaderboard = self.load_leaderboard()
        self.game_result = game_result  # Here we store the result of the previous game played by the player in order we could update leaderboard
        self.player_name = "Player1"  # this variable will hold player's name
        self.menu_image = pg.image.load(MENU_BACKGROUND_IMAGE).convert_alpha()
        self.menu_image = pg.transform.scale(self.menu_image, (WIDTH, HEIGHT))

    def load_leaderboard(self):
        with open(LEADERBOARD_FILE, "r") as leaderboard_file:
            return json.load(leaderboard_file)

    def save_leaderboard(self):
        with open(LEADERBOARD_FILE, "w") as leaderboard_file:
            return json.dump(self.leaderboard, leaderboard_file, sort_keys=False, indent=4)

    def update_leaderboard(self):
        # In this method we take the game result from the game played by a player and check if we need to update the leaderboard
        for entry in self.leaderboard["leaderboard"]:
            # If the game result is better than current entry in the list we squeeze the new entry at the index if the current entry in the loop
            if self.game_result["points_scored"] > entry["points_scored"]:
                index_of_current_entry = self.leaderboard["leaderboard"].index(entry)
                new_entry = {
                    "place": 0,
                    "player_name": self.player_name,
                    "points_scored": self.game_result["points_scored"],
                    "enemies_killed": self.game_result["enemies_killed"],
                    "levels_cleared": self.game_result["levels_cleared"],
                }
                self.leaderboard["leaderboard"].insert(index_of_current_entry, new_entry)
                break  # There is no point continuing the loop as we inserted new entry so we break the loop

        # Let's check if the leaderboard has been updated with new entry so we need to trim it back to top 10 entries only
        # therefore we remove the last 11th element in the list
        if len(self.leaderboard["leaderboard"]) > 10:
            self.leaderboard["leaderboard"].pop(len(self.leaderboard["leaderboard"]) - 1)
            # Now let's realign the places
            for x in range(0, len(self.leaderboard["leaderboard"])):
                self.leaderboard["leaderboard"][x]["place"] = x + 1


    # Here, we define the function check_events which checks whether the user has pressed quit
    def check_events(self):
        for event in pg.event.get():
            if self.show_menu_options:
                if (event.type == pg.KEYDOWN and event.key == pg.K_DOWN):
                    self.current_menu_option += 1
                    if self.current_menu_option > self.max_menu_options:
                        self.current_menu_option = self.max_menu_options
                elif event.type == pg.KEYDOWN and event.key == pg.K_UP:
                    self.current_menu_option -= 1
                    if self.current_menu_option == 0:
                        self.current_menu_option = 1
                elif event.type == pg.KEYDOWN and (event.key == pg.K_SPACE or event.key == pg.K_RETURN):
                    if self.current_menu_option == 5:
                        # User selected to quit the game
                        # Let's save leaderboard from memory into file
                        self.save_leaderboard()
                        # let's shutdown the pygame engine and then exit to the operating system
                        pg.quit()
                        sys.exit()
                    elif self.current_menu_option == 2:
                        # New game option is selected
                        pass
                    elif self.current_menu_option == 1:
                        # Now we need to show player name selection on the screen
                        self.show_menu_options = False
                        self.show_player_name = True
                    elif self.current_menu_option == 3:
                        # Now we need to show leaderboard on the screen
                        self.show_menu_options = False
                        self.show_leaderboard = True
                    elif self.current_menu_option == 4:
                        # Now we need to show game credits on the screen
                        self.show_menu_options = False
                        self.show_game_credits = True
            elif self.show_player_name == True:
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        # user pressed enter so we exit the player name screen and get back to the main menu
                        self.show_player_name = False
                        self.show_menu_options = True
                    elif event.key == pg.K_BACKSPACE:
                        # Let's remove last letter from the current player name as the user pressed backspace
                        self.player_name = self.player_name[0:-1]
                    elif event.key in PERMITTED_KEYS_FOR_PLAYER_NAME:
                        # user pressed one of the permitted keys which can be used in player name so we convert its integer value into ASCII character and add to the end of the player name
                        self.player_name = self.player_name + chr(event.key)
            else:
                if event.type == pg.KEYDOWN and (event.key == pg.K_SPACE or event.key == pg.K_RETURN):
                    self.show_game_credits = False
                    self.show_leaderboard = False
                    self.show_menu_options = True


    def draw_player_name(self):
        # This n function enables the player name screen to be drawn and shown to the user.
        font = pg.font.Font(FONT, 60)
        text = font.render("player name:", True, YELLOW)
        text_width = text.get_width()
        text_height = text.get_height()
        self.screen.blit(text, [WIDTH // 2 - text_width // 2, HEIGHT // 2 - 3 * (text_height // 2)])

        font = pg.font.Font(FONT, 40)

        text = font.render("please type player name below", True, YELLOW)
        text_width = text.get_width()
        text_height = text.get_height()
        self.screen.blit(text, [WIDTH // 2 - text_width // 2, HEIGHT // 2 - 2 * (text_height // 2)])

        text = font.render(self.player_name, True, YELLOW)
        text_width = text.get_width()
        text_height = text.get_height()
        self.screen.blit(text, [WIDTH // 2 - text_width // 2, HEIGHT // 2 + 1 * (text_height // 2)])
        # Let's draw yellow rectangle around the player name
        pg.draw.rect(self.screen, YELLOW, (WIDTH // 2 - text_width // 2 - 20, HEIGHT // 2 + 1 * (text_height // 2), text_width + 40, text_height), 4)

        text = font.render("please press enter to confirm", True, YELLOW)
        text_width = text.get_width()
        text_height = text.get_height()
        self.screen.blit(text, [WIDTH // 2 - text_width // 2, HEIGHT // 2 + 5 * (text_height // 2)])


    def draw_game_credits(self):
        # This function enables he game credits screen to be drawn and shown to the user.
        font = pg.font.Font(FONT, 60)
        text = font.render("game credits:", True, YELLOW)
        text_width = text.get_width()
        text_height = text.get_height()
        self.screen.blit(text, [WIDTH // 2 - text_width // 2, HEIGHT // 2 - 3 * (text_height // 2)])

        font = pg.font.Font(FONT, 40)
        text = font.render("game creator: Alex O", True, YELLOW)
        text_width = text.get_width()
        text_height = text.get_height()
        self.screen.blit(text, [WIDTH // 2 - text_width // 2, HEIGHT // 2 - 2 * (text_height // 2)])

        font = pg.font.Font(FONT, 40)
        text = font.render("software development module - Semester B", True, YELLOW)
        text_width = text.get_width()
        text_height = text.get_height()
        self.screen.blit(text, [WIDTH // 2 - text_width // 2, HEIGHT // 2 + 0 * (text_height // 2)])

        font = pg.font.Font(FONT, 40)
        text = font.render("Demons Dungeon is a retro-style FPS game", True, YELLOW)
        text_width = text.get_width()
        text_height = text.get_height()
        self.screen.blit(text, [WIDTH // 2 - text_width // 2, HEIGHT // 2 + 2 * (text_height // 2)])

        font = pg.font.Font(FONT, 40)
        text = font.render("please press spacebar or enter", True, YELLOW)
        text_width = text.get_width()
        text_height = text.get_height()
        self.screen.blit(text, [WIDTH // 2 - text_width // 2, HEIGHT // 2 + 5 * (text_height // 2)])


    def draw_leaderboard(self):
        # This function enables the leaderboard screen to be drawn and shown.
        font = pg.font.Font(FONT, 50)
        text = font.render("LEADERBOARD", True, YELLOW)
        text_width = text.get_width()
        text_height = text.get_height()
        self.screen.blit(text, [WIDTH // 2 - text_width // 2, HEIGHT // 2 - 5 * (text_height // 2)])
        pg.draw.rect(self.screen, YELLOW, (WIDTH // 2 - text_width // 2 - 20, HEIGHT // 2 - 3 * (text_height // 2), text_width + 40, 4), 4)

        font = pg.font.Font(FONT, 30)
        place = font.render("place", True, YELLOW)
        self.screen.blit(place, [50, HEIGHT // 2 - 2 * (text_height // 2)])
        player_name = font.render("player name", True, YELLOW)
        self.screen.blit(player_name, [270, HEIGHT // 2 - 2 * (text_height // 2)])
        points_scored = font.render("points scored", True, YELLOW)
        self.screen.blit(points_scored, [670, HEIGHT // 2 - 2 * (text_height // 2)])
        enemies_killed = font.render("enemies killed", True, YELLOW)
        self.screen.blit(enemies_killed, [970, HEIGHT // 2 - 2 * (text_height // 2)])
        levels_cleared = font.render("levels cleared", True, YELLOW)
        self.screen.blit(levels_cleared, [1270, HEIGHT // 2 - 2 * (text_height // 2)])

        offset = 1  # this variable will allow to shift each entry to be displayed lower and lower in the leaderboard
        for entry in self.leaderboard["leaderboard"]:
            place = font.render(str(entry["place"]), True, YELLOW)
            player_name = font.render(entry["player_name"].lower(), True, YELLOW)
            points_scored = font.render(str(entry["points_scored"]), True, YELLOW)
            enemies_killed = font.render(str(entry["enemies_killed"]), True, YELLOW)
            levels_cleared = font.render(str(entry["levels_cleared"]), True, YELLOW)
            self.screen.blit(place, [90, HEIGHT // 2 - offset * (text_height // 2)])
            self.screen.blit(player_name, [270, HEIGHT // 2 - offset * (text_height // 2)])
            self.screen.blit(points_scored, [760, HEIGHT // 2 - offset * (text_height // 2)])
            self.screen.blit(enemies_killed, [1070, HEIGHT // 2 - offset * (text_height // 2)])
            self.screen.blit(levels_cleared, [1390, HEIGHT // 2 - offset * (text_height // 2)])
            offset -= 1

        font = pg.font.Font(FONT, 40)
        text = font.render("please press spacebar or enter", True, YELLOW)
        text_width = text.get_width()
        text_height = text.get_height()
        self.screen.blit(text, [WIDTH // 2 - text_width // 2, HEIGHT // 2 + 12 * (text_height // 2)])

    def draw_game_title(self):
        # This function enables the title of the game to be drawn onto the game screen.
        font = pg.font.Font(FONT, 100)
        text = font.render(GAME_TITLE_PREFIX, True, YELLOW)
        text_width = text.get_width()
        text_height = text.get_height()
        self.screen.blit(text, [WIDTH // 2 - text_width // 2, HEIGHT // 2 - 6 * (text_height // 2)])
        text = font.render(GAME_TITLE, True, YELLOW)
        text_width = text.get_width()
        text_height = text.get_height()
        self.screen.blit(text, [WIDTH // 2 - text_width // 2, HEIGHT // 2 - 5 * (text_height // 2)])

    def draw_menu_options(self):
        # This function allows to draw the game menu screen and show it to the user.
        font = pg.font.Font(FONT, 60)

        text = font.render("PLAYER NAME", True, YELLOW)
        text_width = text.get_width()
        text_height = text.get_height()
        self.screen.blit(text, [WIDTH // 2 - text_width // 2, HEIGHT // 2 - 3 * (text_height // 2)])
        if self.current_menu_option == 1:
            pg.draw.rect(self.screen, RED, (WIDTH // 2 - text_width // 2 - 20, HEIGHT // 2 - 3 * (text_height // 2), text_width + 40, text_height), 4)


        text = font.render("NEW GAME", True, YELLOW)
        text_width = text.get_width()
        text_height = text.get_height()
        self.screen.blit(text, [WIDTH // 2 - text_width // 2, HEIGHT // 2 - 1 * (text_height // 2)])
        if self.current_menu_option == 2:
            pg.draw.rect(self.screen, RED, (WIDTH // 2 - text_width // 2 - 20, HEIGHT // 2 - 1 * (text_height // 2), text_width + 40, text_height), 4)

        text = font.render("LEADERBOARD", True, YELLOW)
        text_width = text.get_width()
        text_height = text.get_height()
        self.screen.blit(text, [WIDTH // 2 - text_width // 2, HEIGHT // 2 + 1 * (text_height // 2)])
        if self.current_menu_option == 3:
            pg.draw.rect(self.screen, RED, (WIDTH // 2 - text_width // 2 - 20, HEIGHT // 2 + 1 * (text_height // 2), text_width + 40, text_height), 4)

        text = font.render("GAME CREDITS", True, YELLOW)
        text_width = text.get_width()
        text_height = text.get_height()
        self.screen.blit(text, [WIDTH // 2 - text_width // 2, HEIGHT // 2 + 3 * (text_height // 2)])
        if self.current_menu_option == 4:
            pg.draw.rect(self.screen, RED, (WIDTH // 2 - text_width // 2 - 20, HEIGHT // 2 + 3 * (text_height // 2), text_width + 40, text_height), 4)

        text = font.render("QUIT GAME", True, YELLOW)
        text_width = text.get_width()
        text_height = text.get_height()
        self.screen.blit(text, [WIDTH // 2 - text_width // 2, HEIGHT // 2 + 5 * (text_height // 2)])
        if self.current_menu_option == 5:
            pg.draw.rect(self.screen, RED, (WIDTH // 2 - text_width // 2 - 20, HEIGHT // 2 + 5 * (text_height // 2), text_width + 40, text_height), 4)

    def draw(self):
        # This function enables all screens to be drawn for the game and displayed to the user.
        self.screen.fill('black')
        self.screen.blit(self.menu_image, (0, 0))
        # self.draw_game_title()
        if self.show_menu_options:
            self.draw_menu_options()
        elif self.show_leaderboard:
            self.draw_leaderboard()
        elif self.show_game_credits:
            self.draw_game_credits()
        elif self.show_player_name:
            self.draw_player_name()

    def update(self):
        # we flip the display to render all drawings onto the screen
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)

    # here, we define the function run which contains an infinite loop which draws and updates our sprites, levels and checks events
    def run(self):
        # Let's check if a game was already played and we need to update leaderboard
        if self.game_result is not None:
            self.update_leaderboard()

        while True:
            self.check_events()
            self.draw()
            self.update()
