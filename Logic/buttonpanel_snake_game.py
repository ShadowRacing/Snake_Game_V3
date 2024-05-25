# *****************************************
# Shadows Snake Button Panel File
# *****************************************

"""
This module is responsible for creating the button panel of the Shadows Snake game. # pylint: disable=line-too-long
"""


# Importing necessary modules
import configparser
import time
import traceback
from os import path
import customtkinter as ctk

# Importing necessary modules from other folders
from Themes.contrast_updater_snake_game import UpdateContrast
from Themes.theme_updater_snake_game import ThemeUpdater
from Configuration.constants_snake_game import GameConstants, FONT_LIST, COLORS_DICT
from Logic.screen_size_changer_snake_game import ScreenSize
from Logic.labelpanel_snake_game import SettingsOptionButtonLabels

class ButtonCommands:
    """
    Class for assigning functions to button commands.
    """
    def __init__(self, game_logger, functions):
        self.functions = functions
        self.game_logger = game_logger

    def home_command(self):
        """
        Function for the home button command.
        """
        if 'return_home' in self.functions:
            self.functions['return_home']()
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

    def info_command(self):
        """
        Function for the information button command.
        """
        if 'open_info' in self.functions:
            self.functions['open_info']()
        else:
            self.game_logger.log_game_event("No function assigned to 'info'")

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

class ResetSettingsPanel:
    """
    Class for creating the reset settings panel of the Shadows Snake game.
    """
    def __init__(self, settings_canvas_reset, game_logger, functions):
        # Initializing variables
        self.settings_canvas_reset = settings_canvas_reset
        self.game_logger = game_logger
        self.functions = functions
        self.buttons = []
        self.theme_updater = ThemeUpdater(self.game_logger)

        # Managing the buttons height and width
        self.button_width = GameConstants.SETTINGS_BUTTON_RESET_WIDTH
        self.button_height = GameConstants.SETTINGS_BUTTON_RESET_HEIGHT
        self.corner_radius = GameConstants.SETTINGS_BUTTON_RESET_CORNER_RADIUS
        self.text = GameConstants.SETTINGS_BUTTON_RESET_TEXT

    def show_all_reset_buttons(self):
        """
        Show all reset buttons.
        """
        self.reset_screen_size_button()
        self.reset_theme_button()
        self.reset_contrast_button()
        self.reset_high_score_label_showing_button()
        self.reset_snake_speed_button()
        self.reset_game_size_button()
        self.reset_snake_color_button()
        self.reset_move_up_button()
        self.reset_move_down_button()
        self.reset_move_left_button()
        self.reset_move_right_button()
        self.reset_start_game_button()
        self.reset_pause_game_button()
        self.reset_restart_game_button()
        self.reset_all_settings_button()
        self.reset_all_movements_button()

    def reset_screen_size_command(self):
        """
        Function for the reset screen size button command.
        """
        if 'reset_screen_size' in self.functions:
            self.functions['reset_screen_size']()
        else:
            self.game_logger.log_game_event("No function assigned to 'reset_screen_size'")

    def reset_theme_command(self):
        """
        Function for the reset theme button command.
        """
        if 'reset_theme' in self.functions:
            self.functions['reset_theme']()
        else:
            self.game_logger.log_game_event("No function assigned to 'reset_theme'")

    def reset_contrast_command(self):
        """
        Function for the reset contrast button command.
        """
        if 'reset_contrast' in self.functions:
            self.functions['reset_contrast']()
        else:
            self.game_logger.log_game_event("No function assigned to 'reset_contrast'")

    def reset_high_score_label_showing_command(self):
        """
        Function for the high score label showing button command.
        """
        if 'reset_high_score_label_showing' in self.functions:
            self.functions['reset_high_score_label_showing']()
        else:
            self.game_logger.log_game_event("No function assigned to 'reset_high_score_label_showing'") # pylint: disable=line-too-long

    def reset_snake_speed_command(self):
        """
        Function for the reset snake speed button command.
        """
        if 'reset_snake_speed' in self.functions:
            self.functions['reset_snake_speed']()
        else:
            self.game_logger.log_game_event("No function assigned to 'reset_snake_speed'")

    def reset_game_size_command(self):
        """
        Function for the reset game size button command.
        """
        if 'reset_game_size' in self.functions:
            self.functions['reset_game_size']()
        else:
            self.game_logger.log_game_event("No function assigned to 'reset_game_size'")

    def reset_snake_color_command(self):
        """
        Function for the reset snake color button command.
        """
        if 'reset_snake_color' in self.functions:
            self.functions['reset_snake_color']()
        else:
            self.game_logger.log_game_event("No function assigned to 'reset_snake_color'")

    def reset_move_up_command(self):
        """
        Function for the reset move up button command.
        """
        if 'reset_move_up' in self.functions:
            self.functions['reset_move_up']()
        else:
            self.game_logger.log_game_event("No function assigned to 'reset_move_up'")

    def reset_move_down_command(self):
        """
        Function for the reset move down button command.
        """
        if 'reset_move_down' in self.functions:
            self.functions['reset_move_down']()
        else:
            self.game_logger.log_game_event("No function assigned to 'reset_move_down'")

    def reset_move_left_command(self):
        """
        Function for the reset move left button command.
        """
        if 'reset_move_left' in self.functions:
            self.functions['reset_move_left']()
        else:
            self.game_logger.log_game_event("No function assigned to 'reset_move_left'")

    def reset_move_right_command(self):
        """
        Function for the reset move right button command.
        """
        if 'reset_move_right' in self.functions:
            self.functions['reset_move_right']()
        else:
            self.game_logger.log_game_event("No function assigned to 'reset_move_right'")

    def reset_start_game_command(self):
        """
        Function for the reset start button command.
        """
        if 'reset_start_game' in self.functions:
            self.functions['reset_start_game']()
        else:
            self.game_logger.log_game_event("No function assigned to 'reset_start_game'")

    def reset_pause_game_command(self):
        """
        Function for the reset pause button command.
        """
        if 'reset_pause' in self.functions:
            self.functions['reset_pause']()
        else:
            self.game_logger.log_game_event("No function assigned to 'reset_pause'")

    def reset_restart_game_command(self):
        """
        Function for the reset restart button command.
        """
        if 'reset_restart' in self.functions:
            self.functions['reset_restart']()
        else:
            self.game_logger.log_game_event("No function assigned to 'reset_restart'")

    def reset_all_settings_command(self):
        """
        Function for the reset all settings button command.
        """
        if 'reset_all_settings' in self.functions:
            self.functions['reset_all_settings']()
        else:
            self.game_logger.log_game_event("No function assigned to 'reset_all_settings'")

    def reset_all_movements_command(self):
        """
        Function for the reset all movements button command.
        """
        if 'reset_all_movements' in self.functions:
            self.functions['reset_all_movements']()
        else:
            self.game_logger.log_game_event("No function assigned to 'reset_all_movements'")

    def reset_screen_size_button(self):
        """
        Function for creating the reset screen size button.
        """
        reset_screen_size_button = ctk.CTkButton(self.settings_canvas_reset, text=self.text, font=FONT_LIST[11],
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.reset_screen_size_command)
        reset_screen_size_button.place(in_=self.settings_canvas_reset, x=200, y=50) # pylint: disable=line-too-long
        self.buttons.append(reset_screen_size_button)

    def reset_theme_button(self):
        """
        Function for creating the reset theme button.
        """
        reset_theme_button = ctk.CTkButton(self.settings_canvas_reset, text=self.text, font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.reset_theme_command)
        reset_theme_button.place(in_=self.settings_canvas_reset, x=400, y=50) # pylint: disable=line-too-long
        self.buttons.append(reset_theme_button)

    def reset_contrast_button(self):
        """
        Function for creating the reset contrast button.
        """
        reset_contrast_button = ctk.CTkButton(self.settings_canvas_reset, text=self.text, font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.reset_contrast_command)
        reset_contrast_button.place(in_=self.settings_canvas_reset, x=600, y=50) # pylint: disable=line-too-long
        self.buttons.append(reset_contrast_button)

    def reset_high_score_label_showing_button(self):
        """
        Function for creating the high score label showing button.
        """
        reset_high_score_label_showing_button = ctk.CTkButton(self.settings_canvas_reset, text=self.text, font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.reset_high_score_label_showing_command)
        reset_high_score_label_showing_button.place(in_=self.settings_canvas_reset, x=600, y=200) # pylint: disable=line-too-long
        self.buttons.append(reset_high_score_label_showing_button)

    def reset_snake_speed_button(self):
        """
        Function for creating the reset snake speed button.
        """
        reset_snake_speed_button = ctk.CTkButton(self.settings_canvas_reset, text=self.text, font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.reset_snake_speed_command)
        reset_snake_speed_button.place(in_=self.settings_canvas_reset, x=200, y=200) # pylint: disable=line-too-long
        self.buttons.append(reset_snake_speed_button)

    def reset_game_size_button(self):
        """
        Function for creating the reset game size button.
        """
        reset_game_size_button = ctk.CTkButton(self.settings_canvas_reset, text=self.text, font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.reset_game_size_command)
        reset_game_size_button.place(in_=self.settings_canvas_reset, x=400, y=200) # pylint: disable=line-too-long
        self.buttons.append(reset_game_size_button)

    def reset_snake_color_button(self):
        """
        Function for creating the reset snake color button.
        """
        reset_snake_color_button = ctk.CTkButton(self.settings_canvas_reset, text=self.text, font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.reset_snake_color_command)
        reset_snake_color_button.place(in_=self.settings_canvas_reset,x=800, y=50) # pylint: disable=line-too-long
        self.buttons.append(reset_snake_color_button)

    def reset_move_up_button(self):
        """
        Function for creating the reset move up button.
        """
        reset_move_up_button = ctk.CTkButton(self.settings_canvas_reset, text=self.text, font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.reset_move_up_command)
        reset_move_up_button.place(in_=self.settings_canvas_reset, x=200, y=350) # pylint: disable=line-too-long
        self.buttons.append(reset_move_up_button)

    def reset_move_down_button(self):
        """
        Function for creating the reset move down button.
        """
        reset_move_down_button = ctk.CTkButton(self.settings_canvas_reset, text=self.text, font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.reset_move_down_command)
        reset_move_down_button.place(in_=self.settings_canvas_reset, x=600, y=350) # pylint: disable=line-too-long
        self.buttons.append(reset_move_down_button)

    def reset_move_left_button(self):
        """
        Function for creating the reset move left button.
        """
        reset_move_left_button = ctk.CTkButton(self.settings_canvas_reset, text=self.text, font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.reset_move_left_command)
        reset_move_left_button.place(in_=self.settings_canvas_reset, x=400, y=350) # pylint: disable=line-too-long
        self.buttons.append(reset_move_left_button)

    def reset_move_right_button(self):
        """
        Function for creating the reset move right button.
        """
        reset_move_right_button = ctk.CTkButton(self.settings_canvas_reset, text=self.text, font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.reset_move_right_command)
        reset_move_right_button.place(in_=self.settings_canvas_reset, x=800, y=350) # pylint: disable=line-too-long
        self.buttons.append(reset_move_right_button)

    def reset_start_game_button(self):
        """
        Function for creating the reset start game button.
        """
        reset_start_game_button = ctk.CTkButton(self.settings_canvas_reset, text=self.text, font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.reset_start_game_command)
        reset_start_game_button.place(in_=self.settings_canvas_reset, x=200, y=500) # pylint: disable=line-too-long
        self.buttons.append(reset_start_game_button)

    def reset_pause_game_button(self):
        """
        Function for creating the reset pause game button.
        """
        reset_pause_game_button = ctk.CTkButton(self.settings_canvas_reset, text=self.text, font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.reset_pause_game_command)
        reset_pause_game_button.place(in_=self.settings_canvas_reset, x=400, y=500) # pylint: disable=line-too-long
        self.buttons.append(reset_pause_game_button)

    def reset_restart_game_button(self):
        """
        Function for creating the reset restart game button.
        """
        reset_restart_game_button = ctk.CTkButton(self.settings_canvas_reset, text=self.text, font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.reset_restart_game_command)
        reset_restart_game_button.place(in_=self.settings_canvas_reset, x=600, y=500) # pylint: disable=line-too-long
        self.buttons.append(reset_restart_game_button)

    def reset_all_settings_button(self):
        """
        Function for creating the reset all settings button.
        """
        reset_all_settings_button = ctk.CTkButton(self.settings_canvas_reset, text=self.text, font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.reset_all_settings_command)
        reset_all_settings_button.place(in_=self.settings_canvas_reset, x=800, y=200) # pylint: disable=line-too-long
        self.buttons.append(reset_all_settings_button)

    def reset_all_movements_button(self):
        """
        Function for creating the reset all movements button.
        """
        reset_all_movements_button = ctk.CTkButton(self.settings_canvas_reset, text=self.text, font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.reset_all_movements_command)
        reset_all_movements_button.place(in_=self.settings_canvas_reset, x=800, y=500) # pylint: disable=line-too-long
        self.buttons.append(reset_all_movements_button)

    def destroy_buttons(self):
        """
        Destroy all buttons.
        """
        for button in self.buttons:
            button.destroy()
        self.buttons.clear()


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
        self.home_button = ctk.CTkButton(self.button_canvas, text="Home", font=FONT_LIST[11], # pylint: disable=line-too-long
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
        quit_button.grid(in_=self.button_canvas, row=20, column=0, padx=10, pady=10, sticky="w")

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
        settings_values_button = ctk.CTkButton(self.button_canvas, text="Values\nSettings", font=FONT_LIST[11],
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.button_commands.settings_values_command)
        settings_values_button.grid(in_=self.button_canvas, row=10, column=0, padx=10, pady=10, sticky="w")

    def info_button(self):
        """
        Function for creating the information button.
        """
        info_button = ctk.CTkButton(self.button_canvas, text="Information", font=FONT_LIST[11],
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.button_commands.info_command)
        info_button.grid(in_=self.button_canvas, row=6, column=0, padx=10, pady=10, sticky="w")

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


# Class for creating the option button panel
class OptionButtonPanel:
    """
    Class for creating the option button panel of the Shadows Snake game.
    """
    def __init__(self, root, settings_canvas_values, game_logger):
        # Initializing variables
        self.settings_canvas_values = settings_canvas_values
        self.game_logger = game_logger
        self.label_panel = SettingsOptionButtonLabels(game_logger, self.settings_canvas_values)
        self.config_dir = path.dirname(__file__)
        self.config_path = path.join(self.config_dir, '..','config.ini')
        self.config = configparser.RawConfigParser()
        self.game_size_config = 0
        self.snake_speed_config = 0
        self.snake_color_config = 0
        self.keybindings_config_up = 0
        self.keybindings_config_down = 0
        self.keybindings_config_left = 0
        self.keybindings_config_right = 0
        self.keybindings_config_startgame = 0
        self.keybindings_config_pausegame = 0
        self.keybindings_config_restartgame = 0
        self.current_key = None
        self.combobox = None

        self.button_width = GameConstants.OPTION_BUTTON_WIDTH
        self.button_height = GameConstants.OPTION_BUTTON_HEIGHT
        self.corner_radius = GameConstants.OPTION_BUTTON_CORNER_RADIUS

        self.keys = [str(i) for i in range(10)] + [chr(i) for i in range(ord('a'), ord('z')+1)]

        try:
            self.config.read(self.config_path)
        except FileNotFoundError as e:
            traceback.print_exc(e)

        self.snake_color_rgb = COLORS_DICT.get('Green')

        # Setting up screen size changer
        try:
            self.screen_size_config = self.config.get('Settings', 'screen_size', fallback='Default')
            self.screen_size_var = ctk.StringVar()  # Variable to track the selected value
            self.screen_size_var.set(self.screen_size_config)  # Set the default value
            self.screen_size_changer = ScreenSize(root, self.game_logger, self.screen_size_var, self.config, self.screen_size_config) # pylint: disable=line-too-long
        except FileNotFoundError as e:
            traceback.print_exc(e)

        # Setting up theme changer
        try:
            self.theme_config = self.config.get('Settings', 'theme', fallback='Default')
            self.theme_var = ctk.StringVar()  # Variable to track the selected value
            self.theme_var.set(self.theme_config)
            self.theme_changer = ThemeUpdater(self.game_logger)
        except FileNotFoundError as e:
            traceback.print_exc(e)

        # Setting up contrast updater
        try:
            self.contrast_config = self.config.get('Settings', 'contrast', fallback='Default')
            self.contrast_mode = ctk.StringVar()
            self.contrast_mode.set(self.contrast_config)
            self.contrast_updater = UpdateContrast(self.game_logger)
        except FileNotFoundError as e:
            traceback.print_exc(e)

        try:
            self.high_score_label_showing_config = self.config.get('Settings', 'label_needed_high_score', fallback='Default') # pylint: disable=line-too-long
            self.high_score_var = ctk.StringVar()
            self.high_score_var.set(self.high_score_label_showing_config)
        except FileNotFoundError as e:
            traceback.print_exc(e)

    # Method to update the config.ini file
    def updating_config_ini(self):
        """
        Method to update the config.ini file with the new settings.
        """
        try:
            with open(self.config_path, 'w', encoding='utf 8') as configfile:
                self.config.write(configfile)
        except FileNotFoundError as e:
            traceback.print_exc(e)

    # Callback methods for handling changes in screen size, theme, and contrast
    def screen_size_callback(self, selected_value):
        """
        Function for the screen size callback.
        """
        self.updating_config_ini()
        self.screen_size_changer.change_screen_size(selected_value)

    def theme_callback(self, selected_value):
        """
        Function for the theme callback.
        """
        self.updating_config_ini()
        self.theme_changer.update_config_theme(selected_value)
        self.label_panel.create_theme_label()

    def contrast_callback(self, selected_value):
        """
        Function for the contrast callback.
        """
        self.updating_config_ini()
        self.contrast_updater.apply_contrast(selected_value)

    def snake_color_callback(self, selected_value):
        """
        Function for the snake color callback.
        """
        try:
            self.config.set('Settings', 'snake_color', selected_value)
        except FileNotFoundError as e:
            traceback.print_exc(e)
        self.updating_config_ini()
        self.snake_color_rgb = COLORS_DICT.get(selected_value)

    def is_key_binding_used(self, selected_value):
        """
        Check if a keybinding is already in use.
        """
        # Get all current keybindings
        current_keybindings = self.config.items('KeyBindings')
        print(current_keybindings)

        # Check if the selected keybinding is in the list of current keybindings
        for _, value in current_keybindings:
            if value == selected_value:
                return True

        return False

    def high_score_label_showing_callback(self, selected_value):
        """
        Function for the high score label showing callback.
        """
        if self.is_key_binding_used(selected_value):
            print("This keybinding is already in use.")
            return
        try:
            self.config.set('Settings', 'label_needed_high_score', selected_value)
        except FileNotFoundError as e:
            traceback.print_exc(e)
        self.updating_config_ini()

    def snake_speed_callback(self, selected_value):
        """
        Function for the snake speed callback.
        """
        if self.is_key_binding_used(selected_value):
            print("This keybinding is already in use.")
            return
        try:
            self.config.set('Settings', 'snake_speed', selected_value)
        except FileNotFoundError as e:
            traceback.print_exc(e)
        self.updating_config_ini()

    def game_size_callback(self, selected_value):
        """
        Function for the game size callback.
        """
        if self.is_key_binding_used(selected_value):
            print("This keybinding is already in use.")
            return
        try:
            self.config.set('Settings', 'game_size', selected_value)
            self.game_logger.log_game_event("Game size changed")
            with open(self.config_path, 'w', encoding='utf-8') as configfile:
                self.config.write(configfile)
            self.label_panel.create_game_size_label()
            self.game_logger.log_game_event("Game size changed2")
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def keybindings_callback_up(self, selected_value):
        """
        Function for the keybindings callback up.
        """
        if self.is_key_binding_used(selected_value):
            print("This keybinding is already in use.")
            return
        try:
            self.config.set('KeyBindings', 'move_up', selected_value)
        except FileNotFoundError as e:
            traceback.print_exc(e)
        self.updating_config_ini()

    def keybindings_callback_down(self, selected_value):
        """
        Function for the keybindings callback down.
        """
        if self.is_key_binding_used(selected_value):
            print("This keybinding is already in use.")
            return
        try:
            self.config.set('KeyBindings', 'move_down', selected_value)
        except FileNotFoundError as e:
            traceback.print_exc(e)
        self.updating_config_ini()

    def keybindings_callback_left(self, selected_value):
        """
        Function for the keybindings callback left.
        """
        if self.is_key_binding_used(selected_value):
            print("This keybinding is already in use.")
            return
        try:
            self.config.set('KeyBindings', 'move_left', selected_value)
        except FileNotFoundError as e:
            traceback.print_exc(e)
        self.updating_config_ini()

    def keybindings_callback_right(self, selected_value):
        """
        Function for the keybindings callback right.
        """
        if self.is_key_binding_used(selected_value):
            print("This keybinding is already in use.")
            return
        try:
            self.config.set('KeyBindings', 'move_right', selected_value)
        except FileNotFoundError as e:
            traceback.print_exc(e)
        self.updating_config_ini()

    def keybindings_callback_startgame(self, selected_value):
        """
        Function for the keybindings callback startgame.
        """
        if self.is_key_binding_used(selected_value):
            print("This keybinding is already in use.")
            return
        try:
            self.config.set('KeyBindings', 'startgame', selected_value)
        except FileNotFoundError as e:
            traceback.print_exc(e)
        self.updating_config_ini()

    def keybindings_callback_pausegame(self, selected_value):
        """
        Function for the keybindings callback pausegame.
        """
        if self.is_key_binding_used(selected_value):
            print("This keybinding is already in use.")
            return
        try:
            self.config.set('KeyBindings', 'pausegame', selected_value)
        except FileNotFoundError as e:
            traceback.print_exc(e)
        self.updating_config_ini()

    def keybindings_callback_restartgame(self, selected_value):
        """
        Function for the keybindings callback restartgame.
        """
        if self.is_key_binding_used(selected_value):
            print("This keybinding is already in use.")
            return
        try:
            self.config.set('KeyBindings', 'restartgame', selected_value)
        except FileNotFoundError as e:
            traceback.print_exc(e)
        self.updating_config_ini()

    # Method to create an option button
    def create_option_button(self, command, values, config, x, y):
        """
        Method to create an option button with the given parameters.
        """
        option_button = ctk.CTkOptionMenu(self.settings_canvas_values,
                                          width=self.button_width,
                                          height=self.button_height,
                                          font=FONT_LIST[11],
                                          corner_radius=self.corner_radius,
                                          values=values,
                                          command=command)
        option_button.place(x=x, y=y)
        try:
            option_button.set(config)
        except ValueError as e:
            traceback.print_exc(e)

    # def create_combobox(self, command, values_2, config, x, y, additional_value):
    #     """
    #     Method to create a combobox with the given parameters.
    #     """
    #     self.combobox = ctk.CTkComboBox(self.settings_canvas,
    #                                width=self.button_width,
    #                                height=self.button_height,
    #                                font=FONT_LIST[11],
    #                                corner_radius=self.corner_radius,
    #                                values=values_2,
    #                                command=lambda selected_value: command(selected_value, additional_value)) # pylint: disable=line-too-long
    #     self.combobox.place(x=x, y=y)
    #     self.combobox.bind("<KeyRelease>", lambda event: self.keybindings_key_release_callback(event, additional_value)) # pylint: disable=line-too-long
    #     try:
    #         self.combobox.set(config)
    #     except ValueError as e:
    #         traceback.print_exc(e)

    # def keybindings_key_release_callback(self, event, additional_value):
    #     """
    #     Function for handling key release events.
    #     """
    #     if event.keysym not in ("Delete", "BackSpace"):
    #         choice = self.combobox.get()
    #         print(choice)
    #         self.current_key = additional_value
    #         print(self.current_key)
    #         if choice in ["Default", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", # pylint: disable=line-too-long
    #                       "`","1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "KP_0", "KP_1", "KP_2", "KP_3", "KP_4", "KP_5", "KP_6", "KP_7", "KP_8", "KP_9"]: # pylint: disable=line-too-long
    #             self.update_config(self.current_key, choice)
    #         else:
    #             print("not working")

    # def keybindings_combobox_callback(self, selected_value, additional_value):
    #     """
    #     Function for handling combobox selection changes.
    #     """
    #     self.current_key = additional_value
    #     if selected_value in ["Default", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", # pylint: disable=line-too-long
    #                     "`","1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "KP_0", "KP_1", "KP_2", "KP_3", "KP_4", "KP_5", "KP_6", "KP_7", "KP_8", "KP_9"]: # pylint: disable=line-too-long
    #         self.update_config(self.current_key, selected_value)

    # def update_config(self, key, value):
    #     """
    #     Function to update the configuration.
    #     """
    #     try:
    #         current_config = self.get_current_config()
    #         if value in current_config.values():
    #             print("Value already in use")
    #         else:
    #             self.config['KeyBindings'][key] = value
    #             self.game_logger.log_game_event("Keybindings changed")
    #             self.config.set('KeyBindings', key, value)
    #             with open(self.config_path, 'w', encoding='utf-8') as configfile:
    #                 self.config.write(configfile)
    #             self.game_logger.log_game_event("Keybindings changed2")
    #     except ValueError as e:
    #         traceback.print_exc(e)

    # def get_current_config(self):
    #     """
    #     Function to get the current configuration.
    #     """
    #     return self.config['KeyBindings']

    # def keybindings_callback(self, selected_value, event):
    #     """
    #     Function for the keybindings callback.
    #     """
    #     if event.keysym not in ("Delete", "BackSpace"):
    #         choice = self.combobox.get()
    #         if choice in ["Default", "Black", "Blue", "Dark-Blue", "Green", "Grey", "Orange", # pylint: disable=line-too-long
    #                               "Pink", "Purple", "Red", "White", "Yellow"]: # pylint: disable=line-too-long
    #             self.config.set('KeyBindings', 'test', selected_value)
    #             self.game_logger.log_game_event("Keybindings changed")
    #             with open(self.config_path, 'w', encoding='utf-8') as configfile:
    #                 self.config.write(configfile)
    #             self.game_logger.log_game_event("Keybindings changed2")
    #     elif choice in ["Default", "Black", "Blue", "Dark-Blue", "Green", "Grey", "Orange", # pylint: disable=line-too-long
    #                               "Pink", "Purple", "Red", "White", "Yellow"]:
    #         self.config.set('KeyBindings', 'test', selected_value)
    #         self.game_logger.log_game_event("Keybindings changed")
    #         with open(self.config_path, 'w', encoding='utf-8') as configfile:
    #             self.config.write(configfile)
    #         self.game_logger.log_game_event("Keybindings changed2")

    # Method to show the options
    def show_options(self):
        """
        Method to show the options on the screen.
        """
        try:
            # Creating the option buttons for screen size, theme, and contrast
            # Screen Size Option
            self.screen_size_config = self.config.get('Settings', 'screen_size', fallback='Default')
            self.create_option_button(self.screen_size_callback,
                                      ["Fullscreen", "Default", "1600x900", "1800x1080",
                                       "1800x1200", "1920x1080", "1920x1200", "2560x1440"],
                                      self.screen_size_config, 200, 50)

            # Theme Option
            self.theme_config = self.config.get('Settings', 'theme', fallback='Default')
            self.create_option_button(self.theme_callback,
                                      ["Default", "Black", "Blue", "Dark-Blue", "Green", "Grey", "Orange", # pylint: disable=line-too-long
                                       "Pink", "Purple", "Red", "White", "Yellow"],
                                      self.theme_config, 400, 50)

            # Contrast Option
            self.contrast_config = self.config.get('Settings', 'contrast', fallback='Dark')
            self.create_option_button(self.contrast_callback, ["Default", "Dark", "Light", "System"], # pylint: disable=line-too-long
                                      self.contrast_config, 600, 50)

            # Creating the option buttons for snake color
            self.snake_color_config = self.config.get('Settings', 'snake_color', fallback='Green')
            self.create_option_button(self.snake_color_callback,
                                      ["Default", "Red", "Blue", "Green", "Yellow", "Black", "White", "Grey", "Olive", # pylint: disable=line-too-long
                                       "Purple", "Orange", "Silver", "Gold", "OrangeRed", "MidnightPurple"], # pylint: disable=line-too-long
                                      self.snake_color_config, 800, 50)

            self.high_score_label_showing_config = self.config.get('Settings', 'label_needed_high_score', fallback='False') # pylint: disable=line-too-long
            self.create_option_button(self.high_score_label_showing_callback, # pylint: disable=line-too-long
                                      ["Default", "True", "False"],
                                      self.high_score_label_showing_config, 600, 200)

            self.snake_speed_config = self.config.get('Settings', 'snake_speed', fallback='20')
            self.create_option_button(self.snake_speed_callback,
                                      ["2","4","6","8","10", "20", "30", "40", "50", "60", "70", "80", "90", "100"], # pylint: disable=line-too-long
                                      self.snake_speed_config, 200, 200)

            self.game_size_config = self.config.get('Settings', 'game_size', fallback='Default')
            self.create_option_button(self.game_size_callback,
                                      ["600x600", "700x700", "800x800", "900x900", "1000x1000",
                                       "1100x1100", "1200x1200", "1300x1300","1400x1400", "1500x1500"], # pylint: disable=line-too-long
                                      self.game_size_config, 400, 200)

            self.keybindings_config_up = self.config.get('KeyBindings', 'move_up', fallback='Default')
            self.create_option_button(self.keybindings_callback_up,
                                    ["Default", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", # pylint: disable=line-too-long
                                    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "KP_0", "KP_1", "KP_2", "KP_3", "KP_4", "KP_5", "KP_6", "KP_7", "KP_8", "KP_9", "Escape", "space"], # pylint: disable=line-too-long,
                                    self.keybindings_config_up, 200, 350)

            self.keybindings_config_down = self.config.get('KeyBindings', 'move_down', fallback='Default')
            self.create_option_button(self.keybindings_callback_down,
                                    ["Default", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", # pylint: disable=line-too-long
                                    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "KP_0", "KP_1", "KP_2", "KP_3", "KP_4", "KP_5", "KP_6", "KP_7", "KP_8", "KP_9", "Escape", "space"], # pylint: disable=line-too-long,
                                    self.keybindings_config_down, 600, 350)

            self.keybindings_config_left = self.config.get('KeyBindings', 'move_left', fallback='Default')
            self.create_option_button(self.keybindings_callback_left,
                                    ["Default", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", # pylint: disable=line-too-long
                                    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "KP_0", "KP_1", "KP_2", "KP_3", "KP_4", "KP_5", "KP_6", "KP_7", "KP_8", "KP_9", "Escape", "space"], # pylint: disable=line-too-long,
                                    self.keybindings_config_left, 400, 350)

            self.keybindings_config_right = self.config.get('KeyBindings', 'move_right', fallback='Default')
            self.create_option_button(self.keybindings_callback_right,
                                    ["Default", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", # pylint: disable=line-too-long
                                    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "KP_0", "KP_1", "KP_2", "KP_3", "KP_4", "KP_5", "KP_6", "KP_7", "KP_8", "KP_9", "Escape", "space"], # pylint: disable=line-too-long,
                                    self.keybindings_config_right, 800, 350)

            self.keybindings_config_startgame = self.config.get('KeyBindings', 'startgame', fallback='Default')
            self.create_option_button(self.keybindings_callback_startgame,
                                    ["Default", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", # pylint: disable=line-too-long
                                    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "KP_0", "KP_1", "KP_2", "KP_3", "KP_4", "KP_5", "KP_6", "KP_7", "KP_8", "KP_9", "Escape", "space"], # pylint: disable=line-too-long,
                                    self.keybindings_config_startgame, 200, 500)

            self.keybindings_config_pausegame = self.config.get('KeyBindings', 'pausegame', fallback='Default')
            self.create_option_button(self.keybindings_callback_pausegame,
                                    ["Default", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", # pylint: disable=line-too-long
                                    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "KP_0", "KP_1", "KP_2", "KP_3", "KP_4", "KP_5", "KP_6", "KP_7", "KP_8", "KP_9", "Escape", "space"], # pylint: disable=line-too-long,
                                    self.keybindings_config_pausegame, 400, 500)

            self.keybindings_config_restartgame = self.config.get('KeyBindings', 'restartgame', fallback='Default')
            self.create_option_button(self.keybindings_callback_restartgame,
                                    ["Default", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", # pylint: disable=line-too-long
                                    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "KP_0", "KP_1", "KP_2", "KP_3", "KP_4", "KP_5", "KP_6", "KP_7", "KP_8", "KP_9", "Escape", "Spacebar"], # pylint: disable=line-too-long,
                                    self.keybindings_config_restartgame, 600, 500)

        # Handle exceptions appropriately
        except ValueError as e:
            traceback.print_exc(e)


# *****************************************
# Shadows Snake Button Panel File
# *****************************************

# pylint: disable=too-many-lines
