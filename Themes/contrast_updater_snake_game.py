# *****************************************
# Shadows Snake Contrast Updating File
# *****************************************
"""
Module for updating the contrast setting of the Shadows Snake game.

This module contains the UpdateContrast class which is responsible for applying and updating
the contrast setting of the game.
"""

import configparser
import customtkinter as ctk

class UpdateContrast:
    """
    Class for updating the contrast setting of the Shadows Snake game.

    This class provides methods to apply a contrast setting and update the contrast setting
    in the config.ini file.
    """
    def __init__(self, game_logger):
        #Initializing variables
        self.game_logger = game_logger
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')

    def apply_contrast(self,  selected_value=None):
        """
        Apply the selected contrast mode to the game.

        If no value is provided, the method will read the contrast setting from the config.ini file.
        The contrast mode can be 'Dark', 'Light', or 'System'. If an unrecognized value is provided,
        the method defaults to 'Dark'.

        Args:
        selected_value (str, optional): The selected contrast mode. Defaults to None.
        """
        if selected_value is None:
            config = configparser.ConfigParser()
            config.read('config.ini')
            selected_value = config.get('Settings', 'contrast', fallback='Dark')

        self.update_config_contrast(selected_value)
        if selected_value == 'Dark':
            ctk.set_appearance_mode('dark')
            self.game_logger.log_game_event("Contrast mode set to dark")
        elif selected_value == 'Light':
            ctk.set_appearance_mode('light')
            self.game_logger.log_game_event("Contrast mode set to light")
        elif selected_value == 'System':
            ctk.set_appearance_mode('system')
            self.game_logger.log_game_event("Contrast mode set to system")
        else:
            ctk.set_appearance_mode('dark')
            self.game_logger.log_game_event("Contrast mode set to dark")

    def update_config_contrast(self, selected_value):
        """
        Update the 'contrast' setting in the config.ini file.

        Args:
        selected_value (str): The selected contrast value to be set in the config file.
        """
        self.config.set('Settings', 'contrast', selected_value)
        with open('config.ini', 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)

# *****************************************
# Shadows Snake Contrast Updating File
# *****************************************
