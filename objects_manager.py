from sprite import *
from animated_sprite import *
from enemy import *


class ObjectsManager:
    def __init__(self, game):
        self.game = game
        self.enemies_positions = {}
        self.enemies_list = []
        self.ambient_objects_list = []
        self.ambient_sprites_path = 'assets/sprites/animated/ambient_objects/'

        self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'improved_torches/blue_torches/TBLUA0.png', pos=(1.2, 1.5)))
        self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'improved_torches/blue_torches/TBLUA0.png', pos=(1.2, 5.5)))
        self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'improved_torches/blue_torches/TBLUA0.png', pos=(1.2, 10.5)))
        self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'improved_torches/blue_torches/TBLUA0.png', pos=(10.5, 1.2)))
        self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'improved_torches/blue_torches/TBLUA0.png', pos=(13.5, 1.2)))
        self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'improved_torches/blue_torches/TBLUA0.png', pos=(7.5, 1.2)))
        self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'improved_torches/blue_torches/TBLUA0.png', pos=(4.5, 1.2)))
        self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'improved_torches/blue_torches/TBLUA0.png', pos=(16.5, 1.2)))
        self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'improved_torches/blue_torches/TBLUA0.png', pos=(19.5, 1.2)))
        self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'improved_torches/green_torches/TGRNA0.png', pos=(7.8, 7.8)))
        self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'improved_torches/green_torches/TGRNA0.png', pos=(6.3, 4.3)))
        self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'improved_torches/green_torches/TGRNA0.png', pos=(16.8, 4.2)))
        self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'improved_torches/green_torches/TGRNA0.png', pos=(16.8, 5.8)))
        self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'stone_torch/blue/STFBA0.png', pos=(10.6, 10.8)))
        self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'stone_torch/blue/STFBA0.png', pos=(9.3, 7.3)))
        self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'black_torch/BTORA0.png', pos=(6.2, 9.2)))
        self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'fire_blu_torches/TFBTA0.png', pos=(19.7, 8.8)))
        self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'stone_torch/blue/STFBA0.png', pos=(21.2, 1.2)))
        self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'improved_torches/green_torches/TGRNA0.png', pos=(29.7, 1.2)))
        self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'improved_torches/green_torches/TGRNA0.png', pos=(29.7, 2.8)))
        self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'improved_torches/blue_torches/TBLUA0.png', pos=(24.2, 4.2)))
        self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'improved_torches/blue_torches/TBLUA0.png', pos=(24.2, 9)))
        self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'improved_torches/blue_torches/TBLUA0.png', pos=(24.2, 13)))
        self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'more_hexen_candles/SCANA0.png', pos=(22.8, 13.8)))
        self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'more_hexen_candles/SCANA0.png', pos=(15.2, 13.8)))
        self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'stone_torch/blue/STFBA0.png', pos=(17.2, 10.2)))
        self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'stone_torch/blue/STFBA0.png', pos=(12.2, 10.2)))
        self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'stone_torch/blue/STFBA0.png', pos=(13.8, 13.8)))
        self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'stone_torch/blue/STFBA0.png', pos=(6, 12.2)))
        self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'more_hexen_candles/SCANA0.png', pos=(31.2, 1.2)))
        self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'more_hexen_candles/SCANA0.png', pos=(31.2, 2.8)))
        self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'more_hexen_candles/SCANA0.png', pos=(39.8, 1.2)))
        self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'more_hexen_candles/SCANA0.png', pos=(39.8, 2.8)))
        self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'improved_torches/red_torches/TREDA0.png', pos=(42.8, 8.8)))
        self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'improved_torches/red_torches/TREDA0.png', pos=(41.2, 1.2)))
        self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'improved_torches/red_torches/TREDA0.png', pos=(53, 1.2)))
        self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'improved_torches/red_torches/TREDA0.png', pos=(62, 1.2)))
        self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'improved_torches/red_torches/TREDA0.png', pos=(53.8, 8.8)))
        self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'improved_torches/red_torches/TREDA0.png', pos=(58.2, 4.8)))
        self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'improved_torches/red_torches/TREDA0.png', pos=(46.2, 5.8)))
        self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'improved_torches/red_torches/TREDA0.png', pos=(46.2, 4.2)))
        self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'stone_torch/blue/STFBA0.png', pos=(62.8, 4)))
        self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'stone_torch/blue/STFBA0.png', pos=(62.8, 9)))
        self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'stone_torch/blue/STFBA0.png', pos=(62.8, 15)))
        self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'stone_torch/blue/STFBA0.png', pos=(62.8, 21.8)))
        self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'more_hexen_candles/SCANA0.png', pos=(58.8, 6.2)))
        self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'more_hexen_candles/SCANA0.png', pos=(55.2, 8.8)))
        self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'more_hexen_candles/SCANA0.png', pos=(59.8, 13.8)))
        self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'more_hexen_candles/SCANA0.png', pos=(55.2, 10.2)))
        self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'more_hexen_candles/SCANA0.png', pos=(44.2, 8.9)))
        self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'black_torch/BTORA0.png', pos=(62.8, 24.2)))
        self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'black_torch/BTORA0.png', pos=(62.8, 27)))
        self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'black_torch/BTORA0.png', pos=(59, 30.8)))
        self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'black_torch/BTORA0.png', pos=(56.2, 30.8)))



        # self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'black_torch/BTORA0.png', pos=(20.5, 4.5)))
        #
        # self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'fire_blu_torches/TFBTA0.png', pos=(21.5, 1.5)))
        # self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'fire_bowl/FBWLA0.png', pos=(6.5, 15.5)))
        # self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'more_hexen_candles/SCANA0.png', pos=(8.5, 18.5)))



        # self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'black_torch/BTORA0.png', pos=(20.5, 6.5)))
        #
        # self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'fire_blu_torches/TFBTA0.png', pos=(25.5, 1.5)))
        #
        #
        #
        # self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'improved_torches/green_torches/TGRNA0.png', pos=(3.5, 7.5)))
        #
        # self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'improved_torches/red_torches/TREDA0.png', pos=(13.5, 12.5)))
        #
        # self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'fire_bowl/FBWLA0.png', pos=(9.5, 15.5)))
        #
        # self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'more_hexen_candles/SCANA0.png', pos=(8.5, 21.5)))
        #
        # self.add_ambient_object(AnimatedSprite(game, path=self.ambient_sprites_path + 'stone_torch/blue/STFBA0.png', pos=(10.5, 28.5)))






        # enemies spawn
        # Final boss demon at the end of the map
        self.add_enemy_to_the_game(AnnihilatorEnemy(game, pos=(60.0, 29.0)))
        # Other enemies scattered around the map
        self.add_enemy_to_the_game(BloodGhostEnemy(game, pos=(13.0, 5.0)))
        self.add_enemy_to_the_game(BloodGhostEnemy(game, pos=(28.0, 3.0)))
        self.add_enemy_to_the_game(BloodGhostEnemy(game, pos=(9.0, 10.0)))
        self.add_enemy_to_the_game(BloodGhostEnemy(game, pos=(7.0, 10.5)))
        self.add_enemy_to_the_game(BloodGhostEnemy(game, pos=(44.0, 4.0)))
        self.add_enemy_to_the_game(AfritEnemy(game, pos=(61.0, 5.0)))
        self.add_enemy_to_the_game(AfritEnemy(game, pos=(7.0, 26.0)))
        self.add_enemy_to_the_game(BloodDemonEnemy(game, pos=(6.0, 25.0)))
        self.add_enemy_to_the_game(BloodDemonEnemy(game, pos=(13.0, 22.0)))
        self.add_enemy_to_the_game(AbaddonEnemy(game, pos=(18.0, 21.0)))
        self.add_enemy_to_the_game(AbaddonEnemy(game, pos=(18.0, 16.0)))
        self.add_enemy_to_the_game(AbaddonEnemy(game, pos=(25.0, 26.0)))
        self.add_enemy_to_the_game(AbaddonEnemy(game, pos=(27.5, 25.0)))
        self.add_enemy_to_the_game(BloodGhostEnemy(game, pos=(31.0, 29.0)))
        self.add_enemy_to_the_game(BloodDemonEnemy(game, pos=(33.0, 24.0)))
        self.add_enemy_to_the_game(BloodDemonEnemy(game, pos=(37.0, 24.0)))
        self.add_enemy_to_the_game(BloodGhostEnemy(game, pos=(42.5, 24.0)))
        self.add_enemy_to_the_game(AfritEnemy(game, pos=(46.0, 19.0)))
        self.add_enemy_to_the_game(AfritEnemy(game, pos=(40.0, 21.0)))
        self.add_enemy_to_the_game(AbaddonEnemy(game, pos=(38.0, 30.0)))
        self.add_enemy_to_the_game(AbaddonEnemy(game, pos=(41.0, 27.5)))
        self.add_enemy_to_the_game(AbaddonEnemy(game, pos=(46.0, 27.0)))
        self.add_enemy_to_the_game(AbaddonEnemy(game, pos=(49.0, 19.0)))
        self.add_enemy_to_the_game(AbaddonEnemy(game, pos=(50.0, 21.0)))
        self.add_enemy_to_the_game(AbaddonEnemy(game, pos=(47.0, 30.0)))
        self.add_enemy_to_the_game(AbaddonEnemy(game, pos=(54.0, 27.0)))
        self.add_enemy_to_the_game(AbaddonEnemy(game, pos=(59.0, 24.0)))
        self.add_enemy_to_the_game(BloodDemonEnemy(game, pos=(62.0, 16.0)))
        self.add_enemy_to_the_game(BloodGhostEnemy(game, pos=(62.5, 8.5)))
        self.add_enemy_to_the_game(AbaddonEnemy(game, pos=(62.0, 12.5)))
        self.add_enemy_to_the_game(BloodDemonEnemy(game, pos=(50.0, 8.5)))
        self.add_enemy_to_the_game(BloodGhostEnemy(game, pos=(18.0, 29.5)))
        self.add_enemy_to_the_game(BloodDemonEnemy(game, pos=(24.0, 30.5)))
        self.add_enemy_to_the_game(AbaddonEnemy(game, pos=(28.0, 20.0)))
        self.add_enemy_to_the_game(BloodGhostEnemy(game, pos=(39.0, 15.5)))
        self.add_enemy_to_the_game(BloodGhostEnemy(game, pos=(34.0, 15.5)))
        self.add_enemy_to_the_game(BloodDemonEnemy(game, pos=(24.0, 7)))
        self.add_enemy_to_the_game(BloodDemonEnemy(game, pos=(36.0, 7)))
        self.add_enemy_to_the_game(BloodGhostEnemy(game, pos=(31.0, 1.0)))
        self.add_enemy_to_the_game(BloodGhostEnemy(game, pos=(38.0, 2.5)))
        self.add_enemy_to_the_game(AbaddonEnemy(game, pos=(47.0, 5.0)))


    def get_enemies_positions(self):
        # return a set of positions of all alive enemies
        return self.enemies_positions

    def update(self):
        self.enemies_positions = {enemy.map_pos for enemy in self.enemies_list if enemy.enemy_alive}
        [sprite.update() for sprite in self.ambient_objects_list]
        [enemy.update() for enemy in self.enemies_list]
        self.is_game_won()

    def add_enemy_to_the_game(self, enemy):
        self.enemies_list.append(enemy)

    def add_ambient_object(self, sprite):
        self.ambient_objects_list.append(sprite)

    def is_game_won(self):
        if self.game.player.map_pos == (62, 30) and self.enemies_list[0].enemy_alive == False:
            self.game.render_engine.render_game_won_screen()
            pg.display.flip()
            pg.time.delay(4000)
            from menu import Menu
            menu = Menu(self.game.get_game_result())
            menu.run()