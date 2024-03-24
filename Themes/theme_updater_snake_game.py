# *****************************************
# Wims Snake Theme Updater File
# *****************************************


import configparser, json
from os import path

# The ThemeUpdater class is responsible for loading and updating the theme of the game.
class ThemeUpdater:
    # The constructor initializes the logger, the configuration parser, reads the configuration file, and loads all the themes.
    def __init__(self, logfile):
        self.logfile = logfile
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
        self.config.read("config.ini")
        # Check if the 'Settings' section exists in the config file
        if not self.config.has_section('Settings'):
            self.config.add_section('Settings')
        if not self.config.has_option('Settings', 'theme'):
            self.config.add_section('Settings', 'theme') 

        # Set the 'initial_theme' option to the current theme
        current_theme = self.config.get('Settings', 'theme', fallback='Default')
        self.logfile.log_game_event(current_theme)
        self.config.set('Settings', 'initial_theme', current_theme)

        # Write the changes to the config file
        with open('config.ini', 'w') as configfile:
            self.config.write(configfile)

        self.logfile.log_game_event(f"Updated initial_theme in config.ini to {current_theme}")
        self.logfile.log_game_event(f"Current initial_theme in config.ini: {self.config.get('Settings', 'initial_theme')}")
        # The load_theme method loads a theme from a JSON file. If the file is not found, it logs an error and uses the default theme.

    def load_theme(self, theme_name):
        theme_dir = path.dirname(__file__)
        try:
            #with open(f"{theme_dir}/{theme_name}.json", "r") as theme_file:
                #theme = json.load(theme_file)
            with open(path.join(theme_dir, f"{theme_name}.json"), "r") as theme_file:
                theme = json.load(theme_file)
        except FileNotFoundError:
            self.logfile.log_game_event(f"Theme file {theme_name}.json not found in {theme_dir}. Using default theme.")
            theme = self.themes["Default"]
        return theme

    # The update_config_theme method updates the theme in the configuration file and writes the changes to the file.
    def update_config_theme(self, selected_value):
        if not self.config.has_section('Settings'):
            self.config.add_section('Settings')
        if not self.config.has_option('Settings', 'theme'):
            self.config.add_section('theme') 
        self.config.set('Settings', 'theme', selected_value)
        with open('config.ini', 'w') as configfile:
            self.config.write(configfile)
        self.logfile.log_game_event(f"Updated the config.ini of theme")

# *****************************************
# Wims Snake Theme Updater File
# *****************************************