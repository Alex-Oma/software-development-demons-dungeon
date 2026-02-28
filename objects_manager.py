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


        # self.add_enemy_to_the_game(BloodGhostEnemy(game, pos=(13.0, 5.0)))
        # self.add_enemy_to_the_game(BloodGhostEnemy(game, pos=(13.0, 5.0)))


        # self.add_enemy_to_the_game(BloodDemonEnemy(game, pos=(11.0, 19.0)))
        # self.add_enemy_to_the_game(AbaddonEnemy(game, pos=(11.0, 19.0)))
        # self.add_enemy_to_the_game(AfritEnemy(game, pos=(11.0, 19.0)))

    def get_enemies_positions(self):
        # return a set of positions of all alive enemies
        return self.enemies_positions

    def update(self):
        self.enemies_positions = {enemy.map_pos for enemy in self.enemies_list if enemy.enemy_alive}
        [enemy.update() for enemy in self.enemies_list]

    def add_enemy_to_the_game(self, enemy):
        self.enemies_list.append(enemy)

