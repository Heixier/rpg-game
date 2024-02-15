import random

import gui2.screen as scr

from classes.units.reaper import Reaper
from classes.units.knight import Knight
from classes.units.bandit import Bandit
from classes.units.tank import Tank

import classes.unit as ut


def create_unit(name, unit_class, team, game):
    """Creates a new unit object and adds it to the sprite groups

    Args:
        name (str): Name of the unit
        unit_class (str): Class of the unit
        team (str, optional): Which team this unit is on. Defaults to "enemy".

    Returns:
        obj: returns the newly-created unit object
    """
    
    # If the given unit class is invalid, select a random one
    if unit_class not in ut.unit_list:
        print(f"[{unit_class}] is not a valid class")
        unit_class = random.choice(ut.unit_list)
        print(f"[{unit_class}] has been selected instead")
    
    # Create the unit object
    match unit_class:
        
        case "Reaper":
            unit = Reaper(name, team, game.current_id)
        
        case "Knight":
            unit = Knight(name, team, game.current_id)
            
        case "Bandit":
            unit = Bandit(name, team, game.current_id)
            
        case "Tank":
            unit = Tank(name, team, game.current_id)
        
        case _:
            raise Exception(f"An error has occured while creating Unit objects. (Class [{unit_class}] does not exist)")
        
    # Increment the current game id by 1
    game.current_id += 1
    
    # Add the unit to the correct sprite group
    match team:
        case "player":
            game.players.add(unit)
        
        case "enemy":
            game.enemies.add(unit)
            
    # Add all of the units to the main units sprite group as well
    game.all_units.add(unit)
    
    # Optional
    return unit


def create_team(unit_list: list, team: str, game):
    """Creates units based on an input list and team name
    
    unit_list = list of tuples (name, char_class)"""
    for unit in unit_list:
        create_unit(unit[0], unit[1], team, game)
        
def set_positions(position_list, sprite_group):
    for unit in sprite_group:
        
        # Assigns a coordinate position to the unit
        try:
            coordinates = position_list.pop(0)
            
            # assign the coordinates to the unit
            unit.rect.center = coordinates
        
        # If there are no available positions left, we leave the unit's coordinates at default
        except IndexError:
            unit.rect.center = random.randint(0, scr.SCREEN_WIDTH), random.randint(0, scr.SCREEN_HEIGHT)
            print(f"No available positions left! Randomising to {unit.rect.center}!")