# *****************************************
# Shadows Snake Theme Updater File
# *****************************************

"""
This module is responsible for updating the theme of the Shadows Snake game.
"""
import json
from os import path


class ThemeUpdater:
    """
    Class for updating the theme of the Shadows Snake game.
    """
    def __init__(self, game_logger, config, config_path, config_handler):
        self.game_logger = game_logger
        self.config = config
        self.config_path = config_path
        self.config_handler = config_handler
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
        if 'Settings' not in self.config:
            self.config['Settings'] = {}
        if 'theme' not in self.config['Settings']:
            self.config['Settings']['theme'] = 'Default'

        current_theme = self.config['Settings'].get('theme', 'Default')
        self.game_logger.log_game_event(f"Current Theme: {current_theme}")
        self.config['Settings']['initial_theme'] = current_theme
        self.game_logger.log_game_event(f"Set initial theme to: {current_theme}")

        self.save_config()

        self.game_logger.log_game_event(f"Updated initial_theme in config to: {current_theme}")
        self.game_logger.log_game_event(f"Current initial_theme in config: {self.config['Settings'].get('initial_theme')}")

    def load_theme(self, theme_name):
        """
        Load a theme from a JSON file.
        """
        theme_dir = path.dirname(__file__)
        try:
            with open(path.join(theme_dir, f"{theme_name}.json"), "r", encoding="utf-8") as theme_file:
                theme = json.load(theme_file)
        except FileNotFoundError:
            self.game_logger.log_game_event(f"Theme file {theme_name}.json not found in {theme_dir}. Using default theme.")
            theme = self.themes["Default"]
        return theme

    def reset_theme(self):
        """
        Reset the theme to the initial theme.
        """
        initial_theme = self.config['Settings'].get('initial_theme', 'Default')
        self.update_config_theme(initial_theme)
        self.game_logger.log_game_event("Reset theme")

    def update_config_theme(self, selected_value):
        """
        Update the theme in the configuration file and write the changes to the file.
        """
        self.config['Settings']['theme'] = selected_value
        self.save_config()
        self.game_logger.log_game_event("Updated the config of theme")

    def save_config(self):
        """
        Save the configuration to the file.
        """
        self.config_handler.save_config(self.config, self.config_path)

# *****************************************
# Shadows Snake Theme Updater File
# *****************************************
