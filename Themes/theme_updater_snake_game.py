# *****************************************
# Shadows Snake Theme Updater File
# *****************************************

"""
This module is responsible for updating the theme of the Shadows Snake game.
"""
import json
import configparser
from os import path

class ThemeUpdater:
    """
    Class for updating the theme of the Shadows Snake game.
    """
    def __init__(self, game_logger):
        self.game_logger = game_logger
        self.config = configparser.ConfigParser()
        self.config.read("config.ini")
        self.themes = {
            "Default": self.load_theme("default"),
            "Black": self.load_theme("black"),
            "Blue": self.load_theme("blue"),
            "Dark_blue": self.load_theme("dark-blue"),
            "Green": self.load_theme("green"),
            "Grey": self.load_theme("grey"),
            "Orange": self.load_theme("orange"),
            "Pink": self.load_theme("pink"),
            "Purple": self.load_theme("purple"),
            "Red": self.load_theme("red"),
            "White": self.load_theme("white"),
            "Yellow": self.load_theme("yellow")
        }

    def set_initial_theme(self):
        """
        Set the initial theme of the game.
        """
        self.config.read("config.ini")
        # Check if the 'Settings' section exists in the config file
        if not self.config.has_option('Settings', 'theme'):
            self.config.set('Settings', 'theme', 'Default')

        # Set the 'initial_theme' option to the current theme
        current_theme = self.config.get('Settings', 'theme', fallback='Default')
        self.game_logger.log_game_event(f"Current Theme: {current_theme}")
        self.config.set('Settings', 'initial_theme', current_theme)
        self.game_logger.log_game_event(f"Set initial theme to: {current_theme}")

        # Write the changes to the config file
        with open('config.ini', 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)

        self.game_logger.log_game_event(f"Updated initial_theme in config.ini to: {current_theme}")
        self.game_logger.log_game_event(f"Current initial_theme in config.ini to: {self.config.get('Settings', 'initial_theme')}") # pylint: disable=line-too-long

    def load_theme(self, theme_name):
        """
        Load a theme from a JSON file.
        """
        theme_dir = path.dirname(__file__)
        try:
            with open(path.join(theme_dir, f"{theme_name}.json"), "r", encoding="utf-8") as theme_file: # pylint: disable=line-too-long`
                theme = json.load(theme_file)
        except FileNotFoundError:
            self.game_logger.log_game_event(f"Theme file {theme_name}.json not found in {theme_dir}. Using default theme.") # pylint: disable=line-too-long
            theme = self.themes["Default"]
        return theme

    def reset_theme(self):
        """
        Reset the theme to the initial theme.
        """
        # Set the theme to its initial state
        initial_theme = self.config.get('Settings', 'initial_theme', fallback='Default')
        self.update_config_theme(initial_theme)
        # Reset the theme label
        
        self.config.set('Settings', 'theme', initial_theme)
        with open('config.ini', 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)
        self.game_logger.log_game_event("Reset theme label")


    def update_config_theme(self, selected_value):
        """
        Update the theme in the configuration file and write the changes to the file.
        """
        self.config.set('Settings', 'theme', selected_value)
        with open('config.ini', 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)
        self.game_logger.log_game_event("Updated the config.ini of theme")

# *****************************************
# Shadows Snake Theme Updater File
# *****************************************
