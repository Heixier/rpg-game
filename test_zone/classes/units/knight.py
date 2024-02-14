import random

from classes.unit import Unit

# Range of values
STRENGTH = (5, 20)
INTELLIGENCE = (3, 15)
DEFENCE = (1, 10)
MAGIC_RESIST = (1, 5)

class Knight(Unit):
    def __init__(self, name, team, id_no = 0):
        super().__init__(name, team, id_no)
        self.unit_class = "Knight"
        
        self.name = name
        self.team = team
        self.id = id_no
        
        self.strength = random.randint(*STRENGTH)
        self.intelligence = random.randint(*INTELLIGENCE)
        self.defence = random.randint(*DEFENCE)
        self.magic_resist = random.randint(*MAGIC_RESIST)
        