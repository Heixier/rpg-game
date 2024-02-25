import pygame, random

from classes.unit import Unit

import resources2.audio as audio

# Range of values
STRENGTH = (10, 25)
INTELLIGENCE = (1, 10)
DEFENCE = (1, 5)
MAGIC_RESIST = (1, 5)


class Reaper(Unit):
    def __init__(self, name, team, id_no=0, game=None):
        super().__init__(name, team, id_no)
        self.game = game

        self.unit_class = "Reaper"
        self.attack_audio = audio.reaper_basic

        self.name = name
        self.team = team
        self.id = id_no

        self.strength = random.randint(*STRENGTH)
        self.intelligence = random.randint(*INTELLIGENCE)
        self.defence = random.randint(*DEFENCE)
        self.magic_resist = random.randint(*MAGIC_RESIST)

        self.size_scale = 2

        if self.team == "enemy":
            self.direction = "left"

        self.load_animations()

        self.image = self.animations["idle"][0]
        self.rect = self.image.get_rect()
        self.rect.center = self.position

        self.moves["Sacrifice (100)"] = self.sacrifice

    def sacrifice(self, target, target_team):
        mana_cost = 100
        if self.mana >= mana_cost:
            self.mana -= mana_cost
            damage = 999

            self.melee(target)
            self.update_stats(target, damage, "atk", 2)
            self.health -= damage
            self.change_state("hurt")

            if self.game.sound:
                pygame.mixer.Sound.play(self.attack_audio)

            print(f"{self.name} sacrificed itself to kill {target.name}")

            return True

        # Return False is optional because the default is -> None and -> None is already False
        else:
            return False
