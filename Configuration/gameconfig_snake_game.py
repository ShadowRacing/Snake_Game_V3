# *****************************************
# Wims Snake Game Config File
# *****************************************
import configparser, traceback
from os import path

from Logic.config_ini_Initials import ConfigIni

# Class for the game configuration
class GameConfig:
    def __init__(self, logfile, game_mode):
        # Initializing variables
        self.config_ini = ConfigIni()
        self.config_ini.set_config()
        self.logfile = logfile
        self.TIME_PLAYED = 0
        self.config_dir = path.dirname(__file__)
        self.config_path = path.join(self.config_dir, '..','config.ini')
        self.config = configparser.ConfigParser()
        try:
            self.config.read(self.config_path)
        except:
            traceback.print_exc()

        try:
            if not self.config.has_option('Settings', 'snake_color'):
                self.config.set('Settings','snake_color', 'Default')
                with open('config.ini', 'w') as configfile:
                    self.config.write(configfile)
        except:
            traceback.print_exc()
        
        # Set the snake color from the configuration file
        try:
            self.snake_color = self.config.get('Settings', 'snake_color', fallback='Green')
            if self.snake_color in ['Default','Red', 'Blue', 'Green', 'Yellow', 'Black', 'White', 'Grey', 'Olive', 'Purple', 'Orange', 'Silver', 'Gold', 'OrangeRed', 'MidnightPurple']:
                if self.snake_color == 'Default':
                    self.SNAKE_OUTLINE = "#000000"
                    self.snake_color = "#00FF00"
                elif self.snake_color == 'Red':
                    self.SNAKE_OUTLINE = "#FFFFFF"
                    self.snake_color = "#FF0000"
                elif self.snake_color == 'Blue':
                    self.SNAKE_OUTLINE = "#FFFFFF"
                    self.snake_color = "#0000FF"
                elif self.snake_color == 'Green':
                    self.SNAKE_OUTLINE = "#000000"
                    self.snake_color = "#00FF00"
                elif self.snake_color == 'Yellow':
                    self.SNAKE_OUTLINE = "#000000"
                    self.snake_color = "#FFFF00"
                elif self.snake_color == 'White':
                    self.SNAKE_OUTLINE = "#000000"
                    self.snake_color = "#FF0000"
                elif self.snake_color == 'Black':
                    self.SNAKE_OUTLINE = "#FFFFFF"
                    self.snake_color = "#000000"
                elif self.snake_color == 'Grey':
                    self.SNAKE_OUTLINE = "#000000"
                    self.snake_color = "#808080"
                elif self.snake_color == 'Olive':
                    self.SNAKE_OUTLINE = "#000000"
                    self.snake_color = "#808000"
                elif self.snake_color == 'Purple':
                    self.SNAKE_OUTLINE = "#FFFFFF"
                    self.snake_color = "#800080"
                elif self.snake_color == 'Orange':
                    self.SNAKE_OUTLINE = "#000000"
                    self.snake_color = "#FFA500"
                elif self.snake_color == 'Silver':
                    self.SNAKE_OUTLINE = "#000000"
                    self.snake_color = "#C0C0C0"
                elif self.snake_color == 'Gold':
                    self.SNAKE_OUTLINE = "#000000"
                    self.snake_color = "#FFD700"
                elif self.snake_color == 'OrangeRed':
                    self.SNAKE_OUTLINE = "#000000"
                    self.snake_color = "#FF4500"
                elif self.snake_color == 'MidnightPurple':
                    self.SNAKE_OUTLINE = "#000000"
                    self.snake_color = "#210F28"
        except:
            traceback.print_exc()

        # Set the game configuration
        try:
            self.set_configuration(game_mode)
        except:
            traceback.print_exc()

    # Method to set the game configuration
    def set_configuration(self, game_mode):
        try:
            if game_mode == "initial_config":
                self.GAME_WIDTH = 300
                self.GAME_HEIGHT = 300
                self.SPEED = 10
                self.CELL_SIZE = 20
                self.SNAKE_LENGTH = 3
                self.SNAKE_COLOR = self.snake_color
                self.SNAKE_OUTLINE = 'Black'
                self.FOOD_COLOR = 'Red'
                self.SPECIAL_FOOD_COLOR = 'Blue'
                self.BACKGROUND_COLOR = 'Blue'
                self.HIGHLIGHTTHICKNESS = 5
                self.HIGHLIGHTBACKGROUND = 'Black'
                self.DIRECTIONOFFSNAKE = "down"
                self.logfile.log_game_event("Game mode: initial config")

            elif game_mode == "classic_snake":
                self.GAME_WIDTH = 500
                self.GAME_HEIGHT = 500
                self.SPEED = 10
                self.CELL_SIZE = 20
                self.SNAKE_LENGTH = 5
                self.SNAKE_COLOR = self.snake_color
                self.SNAKE_OUTLINE = 'White'
                self.FOOD_COLOR = 'Red'
                self.SPECIAL_FOOD_COLOR = 'Purple'
                self.BACKGROUND_COLOR = 'Black'
                self.HIGHLIGHTTHICKNESS = 5
                self.HIGHLIGHTBACKGROUND = 'Black'
                self.DIRECTIONOFFSNAKE = "down"
                self.logfile.log_game_event("Game mode: classic_snake")

            elif game_mode == "snake_endless":
                self.GAME_WIDTH = 400
                self.GAME_HEIGHT = 400
                self.SPEED = 20
                self.CELL_SIZE = 20
                self.SNAKE_LENGTH = 5
                self.SNAKE_COLOR = self.snake_color
                self.SNAKE_OUTLINE = 'White'
                self.FOOD_COLOR = 'Red'
                self.SPECIAL_FOOD_COLOR = 'Purple'
                self.BACKGROUND_COLOR = 'Black'
                self.HIGHLIGHTTHICKNESS = 5
                self.HIGHLIGHTBACKGROUND = 'Black'
                self.DIRECTIONOFFSNAKE = "down"
                self.logfile.log_game_event("Game mode: snake_endless")

            elif game_mode == "snake_special":
                self.GAME_WIDTH = 400
                self.GAME_HEIGHT = 400
                self.SPEED = 40
                self.CELL_SIZE = 10
                self.SNAKE_LENGTH = 2
                self.SNAKE_COLOR = self.snake_color
                self.SNAKE_OUTLINE = 'White'
                self.FOOD_COLOR = 'Green'
                self.SPECIAL_FOOD_COLOR = 'Purple'
                self.BACKGROUND_COLOR = 'Black'
                self.HIGHLIGHTTHICKNESS = 5
                self.HIGHLIGHTBACKGROUND = 'Black'
                self.DIRECTIONOFFSNAKE = "down"
                self.logfile.log_game_event("Game mode: snake_special")
        except:
            traceback.print_exc()
# *****************************************
# Wims Snake Game Config File
# *****************************************