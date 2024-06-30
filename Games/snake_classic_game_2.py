# *****************************************
# Shadows Snake Game Snake Classic Game File
# *****************************************

"""
This module is responsible for the classic snake game mode of the Shadows Snake game.
"""

import time
import configparser
import traceback
from os import path
import customtkinter as ctk

# Importing thhe necessary modules from other folders
from Configuration.constants_snake_game import FONT_LIST
from Configuration.gameconfig_snake_game import GameConfig
from Logic.food_logic_snake_game import ClassicFood
from Logic.snake_logic_snake_game import Snake
from Logic.game_labelpanel import GameLabelsPanel
from Logic.buttonpanel_snake_game import ClickButtonPanel

class SnakeClassicGame(ctk.CTkCanvas):
    """
    Class for the classic snake game mode of the Shadows Snake game.
    """
    def __init__(self, parent, game_config, game_logger, functions, create_button_panel):
        # Create the game logger
        self.game_logger = game_logger
        self.game_config = game_config
        self.functions = functions
        self.create_button_panel = create_button_panel

        self.config_dir = path.dirname(__file__)
        self.config_path = path.join(self.config_dir, '..','config.ini')
        self.config = configparser.ConfigParser()
        self.config.read(self.config_path)
        self.game_logger.log_game_event("Config file read.")

        # Game configuration
        self.width = game_config.GAME_WIDTH
        self.height = game_config.GAME_HEIGHT
        self.highlightthickness = game_config.HIGHLIGHTTHICKNESS
        self.highlightbackground = game_config.HIGHLIGHTBACKGROUND
        self.direction = self.game_config.DIRECTIONOFFSNAKE

        self.game_logger.log_game_event(f"Game width: {self.width}")
        self.game_logger.log_game_event(f"Game height: {self.height}")
        self.game_logger.log_game_event(f"Highlight thickness: {self.highlightthickness}")
        self.game_logger.log_game_event(f"Highlight background: {self.highlightbackground}")
        self.game_logger.log_game_event(f"Initial direction of snake: {self.direction}")

        # Game state
        self.score = 0
        self.game_over_flag = False
        self.paused = False
        self.has_changed_direction = False

        self.game_logger.log_game_event(f"Initial score: {self.score}")
        self.game_logger.log_game_event(f"Game over flag: {self.game_over_flag}")
        self.game_logger.log_game_event(f"Game paused: {self.paused}")
        self.game_logger.log_game_event(f"Has changed direction: {self.has_changed_direction}")

        # Time-related variables
        self.start_time = None
        self.paused_time = None
        self.total_paused_time = 0
        self.total_time_played = 0
        self.total_time_paused = 0
        self.last_direction_change_time = 0
        self.pause_duration = 0
        self.high_score_time = 0
        self.current_time = 0
        self.get_time_score = 0
        self.get_snake_length = 0

        self.game_logger.log_game_event("Time-related variables initialized.")

        # High scores
        self.high_score = 0
        self.snake_length_high_score = 0

        self.game_logger.log_game_event("High scores initialized")

        super().__init__(parent, bg='Grey20', width=self.width, height=self.height, highlightthickness=self.highlightthickness, # pylint: disable=line-too-long
                                            highlightbackground=self.highlightbackground)

        self.snake_canvas = ctk.CTkCanvas(self, bg="black", width= self.width, height= self.height,  highlightthickness=self.highlightthickness, # pylint: disable=line-too-long
                                             highlightbackground=self.highlightbackground)
        self.snake_canvas.place(x=800, y=50)

        # Create the snake and the food
        self.snake = Snake(self.game_logger, self.snake_canvas, game_config)
        self.food = ClassicFood(self.game_logger, self.snake_canvas, game_config)
        self.game_labels_panel = GameLabelsPanel(parent, self.game_logger,  self.game_config)
        self.game_config = GameConfig(self.game_logger, 'classic_snake')
        self.create_button_panel = ClickButtonPanel(parent, self.game_logger, self.functions) # pylint: disable=line-too-long

        self.game_labels_panel.classic_create_game_labels()

        self.state = 'start_game'
        self.config.set('Classic_Snake_Settings', 'state', self.state)
        self.write_changes_to_configini()

    

    def write_changes_to_configini(self):
        """
        Write the changes to the config.ini file.
        """
        with open('config.ini', 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)