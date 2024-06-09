"""
This module is responsible for creating the button panel of the Shadows Snake game. # pylint: disable=line-too-long
"""

# Importing necessary modules
import time
import customtkinter as ctk

# Importing necessary modules from other folders
from Themes.theme_updater_snake_game import ThemeUpdater
from Configuration.constants_snake_game import GameConstants, FONT_LIST

class ButtonCommands:
    """
    Class for assigning functions to button commands.
    """
    def __init__(self, game_logger, functions):
        self.functions = functions
        self.game_logger = game_logger
        self.theme_updater = ThemeUpdater(self.game_logger)

    def home_command(self):
        """
        Function for the home button command.
        """
        if 'return_home' in self.functions:
            self.functions['return_home']()
            self.theme_updater.reset_theme()
        else:
            self.game_logger.log_game_event("No function assigned to 'home'")

    def quit_command(self):
        """
        Function for the quit button command.
        """
        if 'confirm_quit' in self.functions:
            self.functions['confirm_quit']()
        else:
            self.game_logger.log_game_event("No function assigned to 'confirm_quit'")

    def settings_command(self):
        """
        Function for the settings button command.
        """
        if 'open_settings' in self.functions:
            self.functions['open_settings']()
        else:
            self.game_logger.log_game_event("No function assigned to 'open_settings'")

    def info_home_command(self):
        """
        Function for the home button command.
        """
        if 'return_info_home' in self.functions:
            self.functions['return_info_home']()
        else:
            self.game_logger.log_game_event("No function assigned to 'home'")

    def info_command(self):
        """
        Function for the information button command.
        """
        if 'open_info' in self.functions:
            self.functions['open_info']()
        else:
            self.game_logger.log_game_event("No function assigned to 'info'")

    def info_general_command(self):
        """
        Function for the general info button command.
        """
        if 'info_general' in self.functions:
            self.functions['info_general']()
        else:
            self.game_logger.log_game_event("No function assigned to 'info_general'")

    def info_classic_game_mode_command(self):
        """
        Function for the classic game mode info button command.
        """
        if 'info_classic_game_mode' in self.functions:
            self.functions['info_classic_game_mode']()
        else:
            self.game_logger.log_game_event("No function assigned to 'info_classic_game_mode'")

    def info_endless_game_mode_command(self):
        """
        Function for the endless game mode info button command.
        """
        if 'info_endless_game_mode' in self.functions:
            self.functions['info_endless_game_mode']()
        else:
            self.game_logger.log_game_event("No function assigned to 'info_endless_game_mode'")

    def info_leveling_game_mode_command(self):
        """
        Function for the leveling game mode info button command.
        """
        if 'info_leveling_game_mode' in self.functions:
            self.functions['info_leveling_game_mode']()
        else:
            self.game_logger.log_game_event("No function assigned to 'info_leveling_game_mode'")

    def info_challange_game_mode_command(self):
        """
        Function for the challange game mode info button command.
        """
        if 'info_challange_game_mode' in self.functions:
            self.functions['info_challange_game_mode']()
        else:
            self.game_logger.log_game_event("No function assigned to 'info_challange_game_mode'")

    def patchnotes_command(self):
        """
        Function for the patchnotes button command.
        """
        if 'patchnotes' in self.functions:
            self.functions['patchnotes']()
        else:
            self.game_logger.log_game_event("No function assigned to 'patchnotes'")

    def reset_settings_command(self):
        """
        Function for the reset settings button command.
        """
        if 'reset_settings' in self.functions:
            self.functions['reset_settings']()
        else:
            self.game_logger.log_game_event("No function assigned to 'reset_settings'")

    def settings_values_command(self):
        """
        Function for the settings values button command.
        """
        if 'settings_values' in self.functions:
            self.functions['settings_values']()
        else:
            self.game_logger.log_game_event("No function assigned to 'settings_values'")

    def classic_snake_command(self):
        """
        Function for the classic snake button command.
        """
        if 'classic_snake' in self.functions:
            self.functions['classic_snake']()
        else:
            self.game_logger.log_game_event("No function assigned to 'classic_snake'")

    def snake_endless_command(self):
        """
        Function for the endless snake button command.
        """
        if 'snake_endless' in self.functions:
            self.functions['snake_endless']()
        else:
            self.game_logger.log_game_event("No function assigned to 'snake_endless'")

    def snake_leveling_command(self):
        """
        Function for the leveling snake button command.
        """
        if 'snake_leveling' in self.functions:
            self.functions['snake_leveling']()
        else:
            self.game_logger.log_game_event("No function assigned to 'snake_leveling'")

    def challange_choices_command(self):
        """
        Function for the challange choices button command.
        """
        if 'challange_choices' in self.functions:
            self.functions['challange_choices']()
        else:
            self.game_logger.log_game_event("No function assigned to 'challange_choice'")

    def challange_settings_command(self):
        """
        Function for the challange settings button command.
        """
        if 'challange_settings' in self.functions:
            self.functions['challange_settings']()
        else:
            self.game_logger.log_game_event("No function assigned to 'challange_settings'")

    def time_attack_command(self):
        """
        Function for the time attack button command.
        """
        if 'time_attack' in self.functions:
            self.functions['time_attack']()
        else:
            self.game_logger.log_game_event("No function assigned to 'time_attack'")

    def food_time_attack_command(self):
        """
        Function for the Food Time Attack button command.
        """
        if 'food_time_attack' in self.functions:
            self.functions['food_time_attack']()
        else:
            self.game_logger.log_game_event("No function assigned to 'food_time_attack'")

    def snake_color_command(self):
        """
        Function for the snake color button command.
        """
        if 'snake_color' in self.functions:
            self.functions['snake_color']()
        else:
            self.game_logger.log_game_event("No function assigned to 'snake_color'")

    def snake_outline_command(self):
        """
        Function for the snake outline button command.
        """
        if 'snake_outline' in self.functions:
            self.functions['snake_outline']()
        else:
            self.game_logger.log_game_event("No function assigned to 'snake_outline'")

    def snake_length_command(self):
        """
        Function for the snake length button command.
        """
        if 'snake_length' in self.functions:
            self.functions['snake_length']()
        else:
            self.game_logger.log_game_event("No function assigned to 'snake_length'")

    def classic_reset_high_score_command(self):
        """
        Function for the reset high score button command.
        """
        if 'classic_reset_high_score' in self.functions:
            self.functions['classic_reset_high_score']()
        else:
            self.game_logger.log_game_event("No function assigned to 'reset_high_score'")

    def classic_reset_high_score_time_command(self):
        """
        Function for the reset high score time button command.
        """
        if 'classic_reset_high_score_time' in self.functions:
            self.functions['classic_reset_high_score_time']()
        else:
            self.game_logger.log_game_event("No function assigned to 'reset_high_score_time'")

    def classic_reset_high_score_snake_length_command(self):
        """
        Function for the reset high score snake length button command.
        """
        if 'classic_reset_high_score_snake_length' in self.functions:
            self.functions['classic_reset_high_score_snake_length']()
        else:
            self.game_logger.log_game_event("No function assigned to 'reset_high_score_snake_length'") # pylint: disable=line-too-long

    def endless_reset_high_score_command(self):
        """
        Function for the reset high score button command.
        """
        if 'endless_reset_high_score' in self.functions:
            self.functions['endless_reset_high_score']()
        else:
            self.game_logger.log_game_event("No function assigned to 'endless_reset_high_score'")

    def endless_reset_high_score_time_command(self):
        """
        Function for the reset high score time button command.
        """
        if 'endless_reset_high_score_time' in self.functions:
            self.functions['endless_reset_high_score_time']()
        else:
            self.game_logger.log_game_event("No function assigned to 'reset_high_score_time'")

    def endless_reset_high_score_snake_length_command(self):
        """
        Function for the reset high score snake length button command.
        """
        if 'endless_reset_high_score_snake_length' in self.functions:
            self.functions['endless_reset_high_score_snake_length']()
        else:
            self.game_logger.log_game_event("No function assigned to 'reset_high_score_snake_length'") # pylint: disable=line-too-long

    def endless_reset_high_special_score_command(self):
        """
        Function for the reset high special score button command.
        """
        if 'endless_reset_high_score_special_score' in self.functions:
            self.functions['endless_reset_high_score_special_score']()
        else:
            self.game_logger.log_game_event("No function assigned to 'reset_high_special_score'")

    def endless_reset_high_score_shorten_snake_command(self):
        """
        Function for the reset high score shorten snake button command.
        """
        if 'endless_reset_high_score_shorten_snake' in self.functions:
            self.functions['endless_reset_high_score_shorten_snake']()
        else:
            self.game_logger.log_game_event("No function assigned to 'reset_high_score_shorten_snake'") # pylint: disable=line-too-long

    def leveling_reset_high_score_command(self):
        """
        Function for the reset high score button command.
        """
        if 'leveling_reset_high_score' in self.functions:
            self.functions['leveling_reset_high_score']()
        else:
            self.game_logger.log_game_event("No function assigned to 'reset_high_score'")

    def leveling_reset_high_score_time_command(self):
        """
        Function for the reset high score time button command.
        """
        if 'leveling_reset_high_score_time' in self.functions:
            self.functions['leveling_reset_high_score_time']()
        else:
            self.game_logger.log_game_event("No function assigned to 'reset_high_score_time'")

    def leveling_reset_high_score_snake_length_command(self):
        """
        Function for the reset high score snake length button command.
        """
        if 'leveling_reset_high_score_snake_length' in self.functions:
            self.functions['leveling_reset_high_score_snake_length']()
        else:
            self.game_logger.log_game_event("No function assigned to 'reset_high_score_snake_length'") # pylint: disable=line-too-long

    def leveling_reset_high_score_special_score_command(self):
        """
        Function for the reset high score special score button command.
        """
        if 'leveling_reset_high_score_special_score' in self.functions:
            self.functions['leveling_reset_high_score_special_score']()
        else:
            self.game_logger.log_game_event("No function assigned to 'reset_high_special_score'")

    def leveling_reset_high_score_shorten_snake_command(self):
        """
        Function for the reset high score shorten snake button command.
        """
        if 'leveling_reset_high_score_shorten_snake' in self.functions:
            self.functions['leveling_reset_high_score_shorten_snake']()
        else:
            self.game_logger.log_game_event("No function assigned to 'reset_high_score_shorten_snake'") # pylint: disable=line-too-long

    def leveling_reset_high_scores_xp_command(self):
        """
        Function for the reset high scores xp button command.
        """
        if 'leveling_reset_high_scores_xp' in self.functions:
            self.functions['leveling_reset_high_scores_xp']()
        else:
            self.game_logger.log_game_event("No function assigned to 'reset_high_scores_xp'")

    def leveling_reset_high_score_level_command(self):
        """
        Function for the reset high score level button command.
        """
        if 'leveling_reset_high_score_level' in self.functions:
            self.functions['leveling_reset_high_score_level']()
        else:
            self.game_logger.log_game_event("No function assigned to 'reset_high_score_level'")

    def game_size_command(self):
        """
        Function for the game size button command.
        """
        if 'game_size' in self.functions:
            self.functions['game_size']()
        else:
            self.game_logger.log_game_event("No function assigned to 'game_size'")

    def snake_speed_command(self):
        """
        Function for the snake speed button command.
        """
        if 'snake_speed' in self.functions:
            self.functions['snake_speed']()
        else:
            self.game_logger.log_game_event("No function assigned to 'snake_speed'")

    def destroy_canvas(self):
        """
        Function for the destroy canvas button command.
        """
        if 'destroy_canvas' in self.functions:
            self.functions['destroy_canvas']()
        else:
            self.game_logger.log_game_event("No function assigned to 'destroy_canvas'")

# Class for creating the button panel
class ClickButtonPanel:
    """
    Class for creating the button panel of the Shadows Snake game.
    """
    def __init__(self, parent, game_logger, functions, home_button=None):
        # Initializing variables
        self.parent = parent
        self.game_logger = game_logger
        self.functions = functions
        self.home_button = home_button
        self.theme_updater = ThemeUpdater(self.game_logger)

        # Managing the buttons height and width
        self.button_width = GameConstants.CLICK_BUTTON_WIDTH
        self.button_height = GameConstants.CLICK_BUTTON_HEIGHT
        self.corner_radius = GameConstants.CLICK_BUTTON_CORNER_RADIUS

        self.button_commands = ButtonCommands(self.game_logger, self.functions)

        # Creating a separate canvas for the buttons
        self.button_canvas = ctk.CTkCanvas(self.parent, bg='Grey10', highlightbackground='Black', highlightthickness=5) # pylint: disable=line-too-long
        self.button_canvas.pack(side='left', fill='both')

        # Creating counter for home button clicks
        self.home_button_clicks = 0
        self.first_click_time = 0

    # Methods to create specific buttons
    # Each method calls the create_click_button method with specific parameters
    def create_home_button(self):
        """
        Function for creating the home button.
        """
        self.home_button = ctk.CTkButton(self.button_canvas, text="Main Menu", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, corner_radius=self.corner_radius ,state="normal", # pylint: disable=line-too-long
                                command=self.home_button_command)
        self.home_button.grid(in_=self.button_canvas, row=0, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def home_button_command(self):
        """
        Function for the home button command.
        """
        # If it's the first click, record the current time
        if self.home_button_clicks == 0:
            self.first_click_time = time.time()
        # If it's the second click, check if it's within the time limit
        elif self.home_button_clicks == 1:
            if time.time() - self.first_click_time > 2:  # 2 seconds
                # If it's not within the time limit, reset the counter
                self.home_button_clicks = 0
                return
        self.home_button_clicks += 1
        if self.home_button_clicks >= 2:
            self.button_commands.home_command()

    def quit_button(self):
        """
        Function for creating the quit button.
        """
        quit_button = ctk.CTkButton(self.button_canvas, text="Quit", font=FONT_LIST[11],
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.button_commands.quit_command)
        quit_button.grid(in_=self.button_canvas, row=100, column=0, padx=10, pady=10, sticky="w")

    def settings_button(self):
        """
        Function for creating the settings button.
        """
        settings_button = ctk.CTkButton(self.button_canvas, text="Settings", font=FONT_LIST[11],
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.button_commands.settings_command)
        settings_button.grid(in_=self.button_canvas, row=9, column=0, padx=10, pady=10, sticky="w")

    def settings_values_button(self):
        """
        Function for creating the settings values button.
        """
        settings_values_button = ctk.CTkButton(self.button_canvas, text="Values\nSettings", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.button_commands.settings_values_command)
        settings_values_button.grid(in_=self.button_canvas, row=2, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def info_home_button(self):
        """
        Function for creating the home button.
        """
        info_home_button = ctk.CTkButton(self.button_canvas, text="Home info", font=FONT_LIST[11],
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.button_commands.info_home_command)
        info_home_button.grid(in_=self.button_canvas, row=2, column=0, padx=10, pady=10, sticky="w")

    def info_button(self):
        """
        Function for creating the information button.
        """
        info_button = ctk.CTkButton(self.button_canvas, text="Information", font=FONT_LIST[11],
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.button_commands.info_command)
        info_button.grid(in_=self.button_canvas, row=6, column=0, padx=10, pady=10, sticky="w")

    def info_general_button(self):
        """
        Function for creating the general info button.
        """
        info_general_button = ctk.CTkButton(self.button_canvas, text="General", font=FONT_LIST[11],
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.button_commands.info_general_command)
        info_general_button.grid(in_=self.button_canvas, row=16, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def info_classic_game_mode_button(self):
        """
        Function for creating the classic game mode info button.
        """
        info_classic_game_mode_button = ctk.CTkButton(self.button_canvas, text="Classic", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.button_commands.info_classic_game_mode_command)
        info_classic_game_mode_button.grid(in_=self.button_canvas, row=17, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def info_endless_game_mode_button(self):
        """
        Function for creating the endless game mode info button.
        """
        info_endless_game_mode_button = ctk.CTkButton(self.button_canvas, text="Endless", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.button_commands.info_endless_game_mode_command)
        info_endless_game_mode_button.grid(in_=self.button_canvas, row=18, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def info_leveling_game_mode_button(self):
        """
        Function for creating the leveling game mode info button.
        """
        info_leveling_game_mode_button = ctk.CTkButton(self.button_canvas, text="Leveling", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.button_commands.info_leveling_game_mode_command)
        info_leveling_game_mode_button.grid(in_=self.button_canvas, row=19, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def info_challange_game_mode_button(self):
        """
        Function for creating the challange game mode info button.
        """
        info_challange_game_mode_button = ctk.CTkButton(self.button_canvas, text="Challange", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.button_commands.info_challange_game_mode_command)
        info_challange_game_mode_button.grid(in_=self.button_canvas, row=20, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def patchnotes_button(self):
        """
        Function for creating the patchnotes button.
        """
        patchnotes_button = ctk.CTkButton(self.button_canvas, text="Patchnotes", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal", #Should ne normal # pylint: disable=line-too-long
                                command=self.button_commands.patchnotes_command)
        patchnotes_button.grid(in_=self.button_canvas, row=14, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def reset_settings_button(self):
        """
        Function for creating the reset settings button.
        """
        reset_settings_button = ctk.CTkButton(self.button_canvas, text="Reset\nSettings", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal", # pylint: disable=line-too-long
                                command=self.button_commands.reset_settings_command)
        reset_settings_button.grid(in_=self.button_canvas, row=15, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def classic_snake_button(self):
        """
        Function for creating the classic snake button.
        """
        classic_snake_button = ctk.CTkButton(self.button_canvas, text="Classic", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal", # pylint: disable=line-too-long
                                command=self.button_commands.classic_snake_command)
        classic_snake_button.grid(in_=self.button_canvas, row=1, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def snake_endless_button(self):
        """
        Function for creating the endless snake button.
        """
        snake_endless_button = ctk.CTkButton(self.button_canvas, text="Endless", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal", # pylint: disable=line-too-long
                                command=self.button_commands.snake_endless_command)
        snake_endless_button.grid(in_=self.button_canvas, row=2, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def snake_leveling_button(self):
        """
        Function for creating the leveling snake button.
        """
        snake_leveling_button = ctk.CTkButton(self.button_canvas, text="Leveling", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal",  #Should ne normal # pylint: disable=line-too-long
                                command=self.button_commands.snake_leveling_command)
        snake_leveling_button.grid(in_=self.button_canvas, row=3, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def challange_choice_button(self):
        """
        Function for creating the challange choices button.
        """
        challange_choice_button = ctk.CTkButton(self.button_canvas, text="Challanges", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal", # pylint: disable=line-too-long
                                command=self.button_commands.challange_choices_command)
        challange_choice_button.grid(in_=self.button_canvas, row=4, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def challange_settings_button(self):
        """
        Function for creating the challange settings button.
        """
        challange_settings_button = ctk.CTkButton(self.button_canvas, text="Challange Settings", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal", # pylint: disable=line-too-long
                                command=self.button_commands.challange_settings_command)
        challange_settings_button.grid(in_=self.button_canvas, row=5, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def food_time_attack_button(self):
        """
        Function for creating the Food Time Attack button.
        """
        food_time_attack_button = ctk.CTkButton(self.button_canvas, text="Challange", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal", # pylint: disable=line-too-long
                                command=self.button_commands.food_time_attack_command)
        food_time_attack_button.grid(in_=self.button_canvas, row=5, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def snake_color_button(self):
        """
        Function for creating the snake color button.
        """
        snake_color_button = ctk.CTkButton(self.button_canvas, text="Snake Color", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal", # pylint: disable=line-too-long
                                command=self.button_commands.snake_color_command)
        snake_color_button.grid(in_=self.button_canvas, row=6, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def snake_outline_button(self):
        """
        Function for creating the snake outline button.
        """
        snake_outline_button = ctk.CTkButton(self.button_canvas, text="Snake Outline", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal", # pylint: disable=line-too-long
                                command=self.button_commands.snake_outline_command)
        snake_outline_button.grid(in_=self.button_canvas, row=7, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def classic_snake_length_button(self):
        """
        Function for creating the snake length button.
        """
        classic_snake_length_button = ctk.CTkButton(self.button_canvas, text="Snake Length", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal", # pylint: disable=line-too-long
                                command=self.button_commands.snake_length_command)
        classic_snake_length_button.grid(in_=self.button_canvas, row=8, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def classic_reset_high_score_button(self):
        """
        Function for creating the reset high score button.
        """
        classic_reset_high_score_button = ctk.CTkButton(self.button_canvas, text="Reset Score\n Highscore", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal", # pylint: disable=line-too-long
                                command=self.button_commands.classic_reset_high_score_command) # pylint: disable=line-too-long
        classic_reset_high_score_button.grid(in_=self.button_canvas, row=10, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def classic_reset_high_score_time_button(self):
        """
        Function for creating the reset high score time button.
        """
        classic_reset_high_score_button = ctk.CTkButton(self.button_canvas, text="Reset Time\n Highscore", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal", # pylint: disable=line-too-long
                                command=self.button_commands.classic_reset_high_score_time_command) # pylint: disable=line-too-long
        classic_reset_high_score_button.grid(in_=self.button_canvas, row=11, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def classic_reset_high_score_snake_length(self):
        """
        Function for creating the reset high score snake length button.
        """
        classic_reset_high_score_snake_length_button = ctk.CTkButton(self.button_canvas, text="Reset length\n Highscore", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal", # pylint: disable=line-too-long
                                command=self.button_commands.classic_reset_high_score_snake_length_command) # pylint: disable=line-too-long
        classic_reset_high_score_snake_length_button.grid(in_=self.button_canvas, row=12, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def endless_snake_length_button(self):
        """
        Function for creating the snake length button.
        """
        endless_snake_length_button = ctk.CTkButton(self.button_canvas, text="Snake Length", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal", # pylint: disable=line-too-long
                                command=self.button_commands.snake_length_command) # pylint: disable=line-too-long
        endless_snake_length_button.grid(in_=self.button_canvas, row=8, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def endless_reset_high_score_button(self):
        """
        Function for creating the reset high score button.
        """
        endless_reset_high_score_button = ctk.CTkButton(self.button_canvas, text="Reset Score\n Highscore", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal", # pylint: disable=line-too-long
                                command=self.button_commands.endless_reset_high_score_command) # pylint: disable=line-too-long
        endless_reset_high_score_button.grid(in_=self.button_canvas, row=10, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def endless_reset_high_score_time_button(self):
        """
        Function for creating the reset high score time button.
        """
        endless_reset_high_score_button = ctk.CTkButton(self.button_canvas, text="Reset Time\n Highscore", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal", # pylint: disable=line-too-long
                                command=self.button_commands.endless_reset_high_score_time_command) # pylint: disable=line-too-long
        endless_reset_high_score_button.grid(in_=self.button_canvas, row=11, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def endless_reset_high_score_snake_length(self):
        """
        Function for creating the reset high score snake length button.
        """
        endless_reset_high_score_snake_length_button = ctk.CTkButton(self.button_canvas, text="Reset length\n Highscore", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal", # pylint: disable=line-too-long
                                command=self.button_commands.endless_reset_high_score_snake_length_command) # pylint: disable=line-too-long
        endless_reset_high_score_snake_length_button.grid(in_=self.button_canvas, row=12, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def endless_reset_high_score_special_score_button(self):
        """
        Function for creating the reset high score special score button.
        """
        endless_reset_high_score_special_score_button = ctk.CTkButton(self.button_canvas, text="Reset Special\n Highscore", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.button_commands.endless_reset_high_special_score_command) # pylint: disable=line-too-long
        endless_reset_high_score_special_score_button.grid(in_=self.button_canvas, row=13, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def endless_reset_high_score_shorten_snake_button(self):
        """
        Function for creating the reset high score shorten snake button.
        """
        endless_reset_high_score_shorten_snake_button = ctk.CTkButton(self.button_canvas, text="Reset Shorten\n Highscore", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.button_commands.endless_reset_high_score_shorten_snake_command) # pylint: disable=line-too-long
        endless_reset_high_score_shorten_snake_button.grid(in_=self.button_canvas, row=14, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def leveling_reset_high_score_button(self):
        """
        Function for creating the reset high score button.
        """
        leveling_reset_high_score_button = ctk.CTkButton(self.button_canvas, text="Reset Score\n Highscore", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.button_commands.leveling_reset_high_score_command)
        leveling_reset_high_score_button.grid(in_=self.button_canvas, row=10, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def leveling_reset_high_score_time_button(self):
        """
        Function for creating the reset high score time button.
        """
        leveling_reset_high_score_button = ctk.CTkButton(self.button_canvas, text="Reset Time\n Highscore", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.button_commands.leveling_reset_high_score_time_command)
        leveling_reset_high_score_button.grid(in_=self.button_canvas, row=11, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def leveling_reset_high_score_snake_length_button(self):
        """
        Function for creating the reset high score snake length button.
        """
        leveling_reset_high_score_snake_length_button = ctk.CTkButton(self.button_canvas, text="Reset length\n Highscore", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.button_commands.leveling_reset_high_score_snake_length_command) # pylint: disable=line-too-long
        leveling_reset_high_score_snake_length_button.grid(in_=self.button_canvas, row=12, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def leveling_reset_high_score_special_score_button(self):
        """
        Function for creating the reset high score special score button.
        """
        leveling_reset_high_score_special_score_button = ctk.CTkButton(self.button_canvas, text="Reset Special\n Highscore", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.button_commands.leveling_reset_high_score_special_score_command) # pylint: disable=line-too-long
        leveling_reset_high_score_special_score_button.grid(in_=self.button_canvas, row=13, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def leveling_reset_high_score_shorten_snake_button(self):
        """
        Function for creating the reset high score shorten snake button.
        """
        leveling_reset_high_score_shorten_snake_button = ctk.CTkButton(self.button_canvas, text="Reset Shorten\n Highscore", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.button_commands.leveling_reset_high_score_shorten_snake_command) # pylint: disable=line-too-long
        leveling_reset_high_score_shorten_snake_button.grid(in_=self.button_canvas, row=14, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def leveling_reset_high_scores_xp_button(self):
        """
        Function for creating the reset high scores xp button.
        """
        leveling_reset_high_scores_xp_button = ctk.CTkButton(self.button_canvas, text="Reset XP\n Highscore", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.button_commands.leveling_reset_high_scores_xp_command)
        leveling_reset_high_scores_xp_button.grid(in_=self.button_canvas, row=15, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def leveling_reset_high_score_level_button(self):
        """
        Function for creating the reset high score level button.
        """
        leveling_reset_high_score_level_button = ctk.CTkButton(self.button_canvas, text="Reset Level\n Highscore", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.button_commands.leveling_reset_high_score_level_command) # pylint: disable=line-too-long
        leveling_reset_high_score_level_button.grid(in_=self.button_canvas, row=16, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    # only in the special game mode
    def game_size_button(self):
        """
        Function for creating the game size button.
        """
        game_size_button = ctk.CTkButton(self.button_canvas, text="Game Size", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.button_commands.game_size_command)
        game_size_button.grid(in_=self.button_canvas, row=15, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    # only in the special game mode
    def snake_speed_button(self):
        """
        Function for creating the snake speed button.
        """
        snake_speed_button = ctk.CTkButton(self.button_canvas, text="Snake Speed", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.button_commands.snake_speed_command)
        snake_speed_button.grid(in_=self.button_canvas, row=9, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long


# pylint: disable=too-many-lines
