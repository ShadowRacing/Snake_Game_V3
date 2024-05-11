#****************************************************
# This file contains the leveling system logic
#****************************************************

"""
This module contains the LevelingSystem class which is responsible for managing the leveling system in the game. # pylint: disable=line-too-long
"""

import configparser
from os import path


class LevelingSystem:
    """
    Class for managing the leveling system in the game.
    """
    def __init__(self):
        self.config_dir = path.dirname(__file__)
        self.config_path = path.join(self.config_dir, 'config.ini')
        self.config = configparser.ConfigParser()

        self.config.read(self.config_path)

        self.increase_amount = 50
        self.levels_to_increase_xp = 10

    def level_up(self, xp, level):
        """
        Increase the level of the player based on the experience points.
        """
        if xp >= self.increase_amount * level:
            return True
        return False
