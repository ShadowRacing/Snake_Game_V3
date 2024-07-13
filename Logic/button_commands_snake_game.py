"""
This module contains the ButtonCommands class.
"""

# Importing necessary modules from other folders
from Themes.theme_updater_snake_game import ThemeUpdater

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

    def restart_app_command(self):
        """
        Function for the restart app button command.
        """
        if 'restart_app' in self.functions:
            self.functions['restart_app']()
        else:
            self.game_logger.log_game_event("No function assigned to 'restart_app'")

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
