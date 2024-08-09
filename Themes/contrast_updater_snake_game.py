# *****************************************
# Shadows Snake Contrast Updating File
# *****************************************
"""
Module for updating the contrast setting of the Shadows Snake game.

This module contains the UpdateContrast class which is responsible for applying and updating
the contrast setting of the game.
"""

import json
import customtkinter as ctk

class UpdateContrast:
    """
    Class for updating the contrast setting of the Shadows Snake game.

    This class provides methods to apply a contrast setting and update the contrast setting
    in the config file.
    """
    def __init__(self, game_logger, config, config_path):
        #Initializing variables
        self.game_logger = game_logger
        self.config = config
        self.config_path = config_path

    def apply_contrast(self, selected_value=None):
        """
        Apply the selected contrast mode to the game.

        If no value is provided, the method will read the contrast setting from the config file.
        The contrast mode can be 'Dark', 'Light', or 'System'. If an unrecognized value is provided,
        the method defaults to 'Dark'.

        Args:
        selected_value (str, optional): The selected contrast mode. Defaults to None.
        """
        if selected_value is None:
            selected_value = self.config.get('Settings', {}).get('contrast', 'Dark')

        self.update_config_contrast(selected_value)
        if selected_value == 'Dark':
            ctk.set_appearance_mode('dark')
            self.game_logger.log_game_event("Contrast mode set to: dark")
        elif selected_value == 'Light':
            ctk.set_appearance_mode('light')
            self.game_logger.log_game_event("Contrast mode set to: light")
        elif selected_value == 'System':
            ctk.set_appearance_mode('system')
            self.game_logger.log_game_event("Contrast mode set to: system")
        elif selected_value == 'Default':
            ctk.set_appearance_mode('dark')
            self.game_logger.log_game_event("Contrast mode set to: default")
        else:
            ctk.set_appearance_mode('dark')
            self.game_logger.log_game_event("Contrast mode set to: dark")

    def update_config_contrast(self, selected_value):
        """
        Update the 'contrast' setting in the config file.

        Args:
        selected_value (str): The selected contrast value to be set in the config file.
        """
        if 'Settings' not in self.config:
            self.config['Settings'] = {}
        self.config['Settings']['contrast'] = selected_value
        self.game_logger.log_game_event(f"Updated contrast in config to: {selected_value}")
        self.save_config()

    def save_config(self):
        """
        Save the configuration to the file.
        """
        with open(self.config_path, 'w', encoding='utf-8') as configfile:
            json.dump(self.config, configfile, indent=4)

# *****************************************
# Shadows Snake Contrast Updating File
# *****************************************
