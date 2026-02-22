from sprite import *
from animated_sprite import *
from enemy import *


class ObjectsManager:
    def __init__(self, game):
        self.game = game
        self.enemies_list = []

        # spawn npc
        self.enemies_count = 1  # npc count
        self.npc_types = [BloodGhostEnemy]

        # enemies map
        self.add_enemy_to_the_game(BloodGhostEnemy(game, pos=(11.0, 19.0)))
        # add_npc(SoldierNPC(game, pos=(11.5, 4.5)))
        # add_npc(SoldierNPC(game, pos=(13.5, 6.5)))
        # add_npc(SoldierNPC(game, pos=(2.0, 20.0)))
        # add_npc(SoldierNPC(game, pos=(4.0, 29.0)))
        # add_npc(CacoDemonNPC(game, pos=(5.5, 14.5)))
        # add_npc(CacoDemonNPC(game, pos=(5.5, 16.5)))
        # add_npc(CyberDemonNPC(game, pos=(14.5, 25.5)))


    def update(self):
        [enemy.update() for enemy in self.enemies_list]

    def add_enemy_to_the_game(self, enemy):
        self.enemies_list.append(enemy)

