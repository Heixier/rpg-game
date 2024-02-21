import pygame, random

from scenes.scene import Scene

from gui2 import ui_functions

import resources2.images as images


class EnemyTurn(Scene):
    def __init__(self, game: object):
        super().__init__(game)
        self.sprites = pygame.sprite.Group()
        self.effect_sprites = pygame.sprite.Group()

        self.alive_players = []
        self.alive_enemies = []

        # Number of times the enemy can attack
        self.attacks = 1

        # Delay before the enemy starts attacking
        self.wait = 1000
        self.start_time = pygame.time.get_ticks()
        self.current_time = pygame.time.get_ticks()

        for sprite in self.alive_enemies:
            print(sprite.health, sprite.alive)

    def update(self, actions):
        self.update_alive_dict()

        # If there are no alive enemies, go back to play screen
        if self.alive_enemy_dict:

            # Delay before attacking
            if self.current_time - self.start_time > self.wait and self.attacks:
                self.attacker = random.choice(list(self.alive_enemy_dict.values()))
                self.target = random.choice(list(self.alive_player_dict.values()))

                # If player character is not idle, wait until it is (where it will get deactivated on top)
                if self.target.state == "idle":
                    self.target.deactivate()  # Timing issue
                    self.attacker.basic_attack(self.target)
                    self.attacks -= 1
                    self.start_time = pygame.time.get_ticks()

            # Check if we still have to wait for everyone's animations to finish
            # And if the enemy still has moves left
            if self.attacks:
                self.waiting = True
            else:
                self.waiting = False
        else:
            self.waiting = False

        # Check if any sprites are still in their active animations
        for sprite in self.game.all_units.sprites():
            if not sprite.state == "idle" and not sprite.state == "death":
                self.waiting = True

            else:
                sprite.deactivate()

        if not self.waiting:
            for sprite in self.game.all_units.sprites():
                sprite.deactivate()

            while self.game.stack[-1] != self.anchor:
                self.exit_scene()

        self.current_time = pygame.time.get_ticks()
        self.sprites.update()
        self.game.all_units.update()

    def render(self, screen):
        self.anchor.render(screen)
        self.sprites.draw(screen)
