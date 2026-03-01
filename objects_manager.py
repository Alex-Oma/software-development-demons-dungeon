from sprite import *
from animated_sprite import *
from enemy import *


class ObjectsManager:
    def __init__(self, game):
        self.game = game
        self.enemies_positions = {}
        self.enemies_list = []

        # spawn npc
        self.enemies_count = 1  # npc count
        self.npc_types = [BloodGhostEnemy, BloodDemonEnemy, AbaddonEnemy, AfritEnemy, AnnihilatorEnemy]

        # enemies spawn
        # Final boss demon at the end of the map
        self.add_enemy_to_the_game(AnnihilatorEnemy(game, pos=(60.0, 29.0)))

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
        [enemy.update() for enemy in self.enemies_list]

    def add_enemy_to_the_game(self, enemy):
        self.enemies_list.append(enemy)

