# *****************************************
# Shadows Snake Game Config File
# *****************************************

"""
Module for the game configuration of the Shadows Snake game.
"""

import configparser
import traceback
from os import path

from Logic.config_ini_initials import ConfigIni

class GameConfig:
    """
    Class for the game configuration of the Shadows Snake game.
    """
    def __init__(self, game_logger, game_mode):
        # Initializing variables
        self.config_ini = ConfigIni()
        self.config_ini.set_config()
        self.game_logger = game_logger
        self.TIME_PLAYED = 0 # pylint: disable=invalid-name
        self.config_dir = path.dirname(__file__)
        self.config_path = path.join(self.config_dir, '..','config.ini')
        self.config = configparser.ConfigParser()
        try:
            self.config.read(self.config_path)
        except FileNotFoundError as e:
            traceback.print_exc(e)

        try:
            if not self.config.has_option('Settings', 'snake_color'):
                self.config.set('Settings','snake_color', 'Default')
                with open('config.ini', 'w', encoding='utf-8') as configfile:
                    self.config.write(configfile)
        except FileNotFoundError as e:
            traceback.print_exc(e)

        try:
            self.snake_speed = self.config.get('Settings', 'snake_speed', fallback='20')
            if self.snake_speed in ['10', '20', '30', '40', '50', '60', '70', '80', '90', '100']:
                if self.snake_speed == '10':
                    self.SPEED = 10 # pylint: disable=invalid-name
                elif self.snake_speed == '20':
                    self.SPEED = 20 # pylint: disable=invalid-name
                elif self.snake_speed == '30':
                    self.SPEED = 30 # pylint: disable=invalid-name
                elif self.snake_speed == '40':
                    self.SPEED = 40 # pylint: disable=invalid-name
                elif self.snake_speed == '50':
                    self.SPEED = 50 # pylint: disable=invalid-name
                elif self.snake_speed == '60':
                    self.SPEED = 60 # pylint: disable=invalid-name
                elif self.snake_speed == '70':
                    self.SPEED = 70 # pylint: disable=invalid-name
                elif self.snake_speed == '80':
                    self.SPEED = 80 # pylint: disable=invalid-name
                elif self.snake_speed == '90':
                    self.SPEED = 90 # pylint: disable=invalid-name
                elif self.snake_speed == '100':
                    self.SPEED = 100 # pylint: disable=invalid-name
        except ValueError as e:
            traceback.print_exc(e)

        self.config.read(self.config_path)

        try:
            self.game_size = self.config.get('Settings', 'game_size', fallback='500x500')
            if self.game_size in ["600x600", "700x700", "800x800", "900x900", "1000x1000", # pylint: disable=line-too-long
                                       "1100x1100", "1200x1200", "1300x1300","1400x1400", "1500x1500"]: # pylint: disable=line-too-long
                if self.game_size == "600x600":
                    self.game_width = 600
                    self.game_height = 600
                elif self.game_size == "700x700":
                    self.game_width = 700
                    self.game_height = 700
                elif self.game_size == "800x800":
                    self.game_width = 800
                    self.game_height = 800
                elif self.game_size == "900x900":
                    self.game_width = 900
                    self.game_height = 900
                elif self.game_size == "1000x1000":
                    self.game_width = 1000
                    self.game_height = 1000
                elif self.game_size == "1100x1100":
                    self.game_width = 1100
                    self.game_height = 1100
                elif self.game_size == "1200x1200":
                    self.game_width = 1200
                    self.game_height = 1200
                elif self.game_size == "1300x1300":
                    self.game_width = 1300
                    self.game_height = 1300
                elif self.game_size == "1400x1400":
                    self.game_width = 1400
                    self.game_height = 1400
                elif self.game_size == "1500x1500":
                    self.game_width = 1500
                    self.game_height = 1500
        except ValueError as e:
            traceback.print_exc(e)

        # Set the snake color from the configuration file
        try:
            self.snake_color = self.config.get('Settings', 'snake_color', fallback='Green')
            if self.snake_color in ['Default','Red', 'Blue', 'Green', 'Yellow',
                                    'Black', 'White', 'Grey', 'Olive', 'Purple',
                                    'Orange', 'Silver', 'Gold', 'OrangeRed', 'MidnightPurple']:
                if self.snake_color == 'Default':
                    self.SNAKE_OUTLINE = "#000000" # pylint: disable=invalid-name
                    self.snake_color = "#00FF00"
                elif self.snake_color == 'Red':
                    self.SNAKE_OUTLINE = "#FFFFFF" # pylint: disable=invalid-name
                    self.snake_color = "#FF0000"
                elif self.snake_color == 'Blue':
                    self.SNAKE_OUTLINE = "#FFFFFF" # pylint: disable=invalid-name
                    self.snake_color = "#0000FF"
                elif self.snake_color == 'Green':
                    self.SNAKE_OUTLINE = "#000000" # pylint: disable=invalid-name
                    self.snake_color = "#00FF00"
                elif self.snake_color == 'Yellow':
                    self.SNAKE_OUTLINE = "#000000" # pylint: disable=invalid-name
                    self.snake_color = "#FFFF00"
                elif self.snake_color == 'White':
                    self.SNAKE_OUTLINE = "#000000" # pylint: disable=invalid-name
                    self.snake_color = "#FF0000"
                elif self.snake_color == 'Black':
                    self.SNAKE_OUTLINE = "#FFFFFF" # pylint: disable=invalid-name
                    self.snake_color = "#000000"
                elif self.snake_color == 'Grey':
                    self.SNAKE_OUTLINE = "#000000" # pylint: disable=invalid-name
                    self.snake_color = "#808080"
                elif self.snake_color == 'Olive':
                    self.SNAKE_OUTLINE = "#000000" # pylint: disable=invalid-name
                    self.snake_color = "#808000"
                elif self.snake_color == 'Purple':
                    self.SNAKE_OUTLINE = "#FFFFFF" # pylint: disable=invalid-name
                    self.snake_color = "#800080"
                elif self.snake_color == 'Orange':
                    self.SNAKE_OUTLINE = "#000000" # pylint: disable=invalid-name
                    self.snake_color = "#FFA500"
                elif self.snake_color == 'Silver':
                    self.SNAKE_OUTLINE = "#000000" # pylint: disable=invalid-name
                    self.snake_color = "#C0C0C0"
                elif self.snake_color == 'Gold':
                    self.SNAKE_OUTLINE = "#000000" # pylint: disable=invalid-name
                    self.snake_color = "#FFD700"
                elif self.snake_color == 'OrangeRed':
                    self.SNAKE_OUTLINE = "#000000" # pylint: disable=invalid-name
                    self.snake_color = "#FF4500"
                elif self.snake_color == 'MidnightPurple':
                    self.SNAKE_OUTLINE = "#000000" # pylint: disable=invalid-name
                    self.snake_color = "#210F28"
        except ValueError as e:
            traceback.print_exc(e)

        # Set the game configuration
        try:
            self.set_configuration(game_mode)
        except ValueError as e:
            traceback.print_exc(e)

    # Method to set the game configuration
    def set_configuration(self, game_mode):
        """
        Set the game configuration based on the game mode.
        """
        try:
            if game_mode == "initial_config":
                self.GAME_WIDTH = 300 # pylint: disable=invalid-name
                self.GAME_HEIGHT = 300 # pylint: disable=invalid-name
                self.SPEED = self.snake_speed # pylint: disable=invalid-name
                self.CELL_SIZE = 20 # pylint: disable=invalid-name
                self.SNAKE_LENGTH = 3 # pylint: disable=invalid-name
                self.SNAKE_COLOR = self.snake_color # pylint: disable=invalid-name
                self.SNAKE_OUTLINE = 'Black' # pylint: disable=invalid-name
                self.FOOD_COLOR = 'Red' # pylint: disable=invalid-name
                self.SPECIAL_FOOD_COLOR = 'Blue' # pylint: disable=invalid-name
                self.BACKGROUND_COLOR = 'Blue' # pylint: disable=invalid-name
                self.HIGHLIGHTTHICKNESS = 5 # pylint: disable=invalid-name
                self.HIGHLIGHTBACKGROUND = 'Black' # pylint: disable=invalid-name
                self.DIRECTIONOFFSNAKE = "down" # pylint: disable=invalid-name
                self.game_logger.log_game_event("Game mode: initial config")

            elif game_mode == "classic_snake":
                self.GAME_WIDTH = self.game_width # pylint: disable=invalid-name
                self.GAME_HEIGHT = self.game_height # pylint: disable=invalid-name
                self.SPEED = self.snake_speed # pylint: disable=invalid-name
                self.CELL_SIZE = 20 # pylint: disable=invalid-name
                self.SNAKE_LENGTH = 5 # pylint: disable=invalid-name
                self.SNAKE_COLOR = self.snake_color # pylint: disable=invalid-name
                self.SNAKE_OUTLINE = 'White' # pylint: disable=invalid-name
                self.FOOD_COLOR = 'Red' # pylint: disable=invalid-name
                self.SPECIAL_FOOD_COLOR = 'Purple' # pylint: disable=invalid-name
                self.BACKGROUND_COLOR = 'Black' # pylint: disable=invalid-name
                self.HIGHLIGHTTHICKNESS = 5 # pylint: disable=invalid-name
                self.HIGHLIGHTBACKGROUND = 'Black' # pylint: disable=invalid-name
                self.DIRECTIONOFFSNAKE = "down" # pylint: disable=invalid-name
                self.game_logger.log_game_event("Game mode: classic_snake")

            elif game_mode == "snake_endless":
                self.GAME_WIDTH = self.game_width # pylint: disable=invalid-name
                self.GAME_HEIGHT = self.game_height # pylint: disable=invalid-name
                self.SPEED = self.snake_speed # pylint: disable=invalid-name
                self.CELL_SIZE = 20 # pylint: disable=invalid-name
                self.SNAKE_LENGTH = 5 # pylint: disable=invalid-name
                self.SNAKE_COLOR = self.snake_color # pylint: disable=invalid-name
                self.SNAKE_OUTLINE = 'White' # pylint: disable=invalid-name
                self.FOOD_COLOR = 'Red' # pylint: disable=invalid-name
                self.SPECIAL_FOOD_COLOR = 'Purple' # pylint: disable=invalid-name
                self.SHORTEN_FOOD_COLOR = 'yellow' # pylint: disable=invalid-name
                self.BACKGROUND_COLOR = 'Black' # pylint: disable=invalid-name
                self.HIGHLIGHTTHICKNESS = 5 # pylint: disable=invalid-name
                self.HIGHLIGHTBACKGROUND = 'Black' # pylint: disable=invalid-name
                self.DIRECTIONOFFSNAKE = "down" # pylint: disable=invalid-name
                self.game_logger.log_game_event("Game mode: snake_endless")

            elif game_mode == "snake_leveling":
                self.GAME_WIDTH = 400 # pylint: disable=invalid-name
                self.GAME_HEIGHT = 400 # pylint: disable=invalid-name
                self.SPEED = self.snake_speed # pylint: disable=invalid-name
                self.CELL_SIZE = 20 # pylint: disable=invalid-name
                self.SNAKE_LENGTH = 5 # pylint: disable=invalid-name
                self.SNAKE_COLOR = self.snake_color # pylint: disable=invalid-name
                self.SNAKE_OUTLINE = 'White' # pylint: disable=invalid-name
                self.FOOD_COLOR = 'Red' # pylint: disable=invalid-name
                self.SPECIAL_FOOD_COLOR = 'Purple' # pylint: disable=invalid-name
                self.BACKGROUND_COLOR = 'Black' # pylint: disable=invalid-name
                self.HIGHLIGHTTHICKNESS = 5 # pylint: disable=invalid-name
                self.HIGHLIGHTBACKGROUND = 'Black' # pylint: disable=invalid-name
                self.DIRECTIONOFFSNAKE = "down" # pylint: disable=invalid-name
                self.game_logger.log_game_event("Game mode: snake_leveling")

            elif game_mode == "food_time_attack":
                self.GAME_WIDTH = self.game_width # pylint: disable=invalid-name
                self.GAME_HEIGHT = self.game_height # pylint: disable=invalid-name
                self.SPEED = self.snake_speed # pylint: disable=invalid-name
                self.CELL_SIZE = 20 # pylint: disable=invalid-name
                self.SNAKE_LENGTH = 5 # pylint: disable=invalid-name
                self.SNAKE_COLOR = self.snake_color # pylint: disable=invalid-name
                self.SNAKE_OUTLINE = 'White' # pylint: disable=invalid-name
                self.FOOD_COLOR = 'Red' # pylint: disable=invalid-name
                self.SPECIAL_FOOD_COLOR = 'Purple' # pylint: disable=invalid-name
                self.BACKGROUND_COLOR = 'Black' # pylint: disable=invalid-name
                self.HIGHLIGHTTHICKNESS = 5 # pylint: disable=invalid-name
                self.HIGHLIGHTBACKGROUND = 'Black' # pylint: disable=invalid-name
                self.DIRECTIONOFFSNAKE = "down" # pylint: disable=invalid-name
                self.game_logger.log_game_event("Game mode: food_time_attack")

        except ValueError as e:
            traceback.print_exc(e)


# *****************************************
# Shadows Snake Game Config File
# *****************************************
