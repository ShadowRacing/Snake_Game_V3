#****************************************************
# Initializing the Config.ini file
#****************************************************

"""
Module for initializing the config.ini file for the Shadows Snake game.
"""

import configparser
import traceback

class ConfigIni:
    """
    Class for initializing the config.ini file for the Shadows Snake game.
    """
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        self.set_config()

    def set_config(self):
        """
        Set the config.ini file with the initial values.
        """
        self.set_settings_initials()
        self.set_default_settings_initials()
        self.set_classic_snake_values()
        self.set_classic_snake_settings()
        self.set_endless_snake_values()
        self.set_endless_snake_settings()
        self.set_leveling_snake_values()
        self.set_leveling_snake_settings()
        self.set_food_time_attack_values()
        self.set_food_time_attack_settings()

    def set_settings_initials(self):
        """
        Set the Settings section in the config.ini file.
        """
        try:
            settings = {
                'initial_theme' : 'Default',
                'theme' : 'Default',
                'contrast' : 'Default',
                'language' : 'English',
                'snake_color' : 'Default',
                'screen_size' : 'Default',
                'label_needed_theme' : 'False',
                'button_press_time_limit' : '0.5',
                'label_needed_high_score' : 'Default',
                'label_needed_game_size' : 'False',
                'game_mode' : 'classic_snake',
                'snake_speed' : '50',
                'initial_game_size' : '600x600',
                'game_size' : '600x600',
                'home_button_state' : 'normal',
                'classic_reset_high_score_button_state' : 'normal',
                'classic_reset_high_score_time_button_state' : 'normal',
                'classic_reset_high_score_snake_length_button_state' : 'normal',
                'endless_reset_high_score_button_state' : 'normal',
                'endless_reset_high_score_time_button_state' : 'normal',
                'endless_reset_high_score_snake_length_button_state' : 'normal',
                'endless_reset_high_score_special_button_state' : 'normal',
                'endless_reset_high_score_shorten_button_state' : 'normal',
                'leveling_reset_high_score_button_state' : 'normal',
                'leveling_reset_high_score_time_button_state' : 'normal',
                'leveling_reset_high_score_special_button_state' : 'normal',
                'leveling_reset_high_score_shorten_button_state' : 'normal',
                'leveling_reset_high_score_xp_button_state' : 'normal',
                'leveling_reset_high_score_level_button_state' : 'normal',
            }

            if not self.config.has_section('Settings'):
                self.config.add_section('Settings')

            for option, value in settings.items():
                if not self.config.has_option('Settings', option):
                    self.config.set('Settings', option, value)
                    self.write_changes_to_configini()
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def set_default_settings_initials(self):
        """
        Set the Settings section in the config.ini file.
        """
        try:
            default_settings = {
                'initial_theme' : 'Default',
                'theme' : 'Default',
                'contrast' : 'Default',
                'language' : 'English',
                'snake_color' : 'Default',
                'screen_size' : 'Default',
                'label_needed_theme' : 'False',
                'button_press_time_limit' : '0.5',
                'label_needed_high_score' : 'Default',
                'label_needed_game_size' : 'False',
                'game_mode' : 'classic_snake',
                'snake_speed' : '50',
                'initial_game_size' : '600x600',
                'game_size' : '600x600',
                'home_button_state' : 'normal',
                'classic_reset_high_score_button_state' : 'normal',
                'classic_reset_high_score_time_button_state' : 'normal',
                'classic_reset_high_score_snake_length_button_state' : 'normal',
                'endless_reset_high_score_button_state' : 'normal',
                'endless_reset_high_score_time_button_state' : 'normal',
                'endless_reset_high_score_snake_length_button_state' : 'normal',
                'endless_reset_high_score_special_button_state' : 'normal',
                'endless_reset_high_score_shorten_button_state' : 'normal',
                'leveling_reset_high_score_button_state' : 'normal',
                'leveling_reset_high_score_time_button_state' : 'normal',
                'leveling_reset_high_score_special_button_state' : 'normal',
                'leveling_reset_high_score_shorten_button_state' : 'normal',
                'leveling_reset_high_score_xp_button_state' : 'normal',
                'leveling_reset_high_score_level_button_state' : 'normal',
            }

            if not self.config.has_section('DefaultSettings'):
                self.config.add_section('DefaultSettings')

            for option, value in default_settings.items():
                if not self.config.has_option('DefaultSettings', option):
                    self.config.set('DefaultSettings', option, value)
                    self.write_changes_to_configini()
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def set_classic_snake_values(self):
        """
        Set the Classic_Snake_Values section in the config.ini file.
        """
        try:
            classic_snake_values = {
                'score' : '0',
                'high_score' : '0',
                'snake_length' : '0',
                'snake_length_high_score' : '0',
                'time_score' : '0',
                'high_score_time' : '0',
            }
            if not self.config.has_section('Classic_Snake_Values'):
                self.config.add_section('Classic_Snake_Values')

            for option, value in classic_snake_values.items():
                if not self.config.has_option('Classic_Snake_Values', option):
                    self.config.set('Classic_Snake_Values', option, value)
                    self.write_changes_to_configini()
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def set_classic_snake_settings(self):
        """
        Set the Classic_Snake_Settings section in the config.ini file.
        """
        try:
            classic_snake_settings = {
                'state' : 'start_game',
            }

            if not self.config.has_section('Classic_Snake_Settings'):
                self.config.add_section('Classic_Snake_Settings')

            for option, value in classic_snake_settings.items():
                if not self.config.has_option('Classic_Snake_Settings', option):
                    self.config.set('Classic_Snake_Settings', option, value)
                    self.write_changes_to_configini()

        except FileNotFoundError as e:
            traceback.print_exc(e)

    def set_endless_snake_values(self):
        """
        Set the Endless_Snake_Values section in the config.ini file.
        """
        try:
            endles_snake_values = {
                'score' : '0',
                'high_score' : '0',
                'special_score' : '0',
                'special_score_high_score' : '0',
                'snake_length' : '0',
                'snake_length_high_score' : '0',
                'time_score' : '0',
                'high_score_time' : '0',
                'shorten_score' : '0',
                'shorten_snake_high_score' : '0',
                'next_special_food_score' : '50',
                'next_shorten_food_score' : '100',
            }
            if not self.config.has_section('Endless_Snake_Values'):
                self.config.add_section('Endless_Snake_Values')

            for option, value in endles_snake_values.items():
                if not self.config.has_option('Endless_Snake_Values', option):
                    self.config.set('Endless_Snake_Values', option, value)
                    self.write_changes_to_configini()

        except FileNotFoundError as e:
            traceback.print_exc(e)

    def set_endless_snake_settings(self):
        """
        Set the Endless_Snake_Settings section in the config.ini file.
        """
        try:
            endless_snake_settings = {
                'state' : 'start_game',
            }

            if not self.config.has_section('Endless_Snake_Settings'):
                self.config.add_section('Endless_Snake_Settings')

            for option, value in endless_snake_settings.items():
                if not self.config.has_option('Endless_Snake_Settings', option):
                    self.config.set('Endless_Snake_Settings', option, value)
                    self.write_changes_to_configini()

        except FileNotFoundError as e:
            traceback.print_exc(e)

    def set_leveling_snake_values(self):
        """
        Set the Leveling_Snake_Values section in the config.ini file.
        """
        try:
            leveling_snake_values = {
                'score' : '0',
                'high_score' : '0',
                'special_score' : '0',
                'special_score_high_score' : '0',
                'snake_length' : '0',
                'snake_length_high_score' : '0',
                'time_score' : '0',
                'high_score_time' : '0',
                'shorten_score' : '0',
                'shorten_snake_high_score' : '0',
                'next_special_food_score' : '50',
                'next_shorten_food_score' : '100',
                'level' : '1',
                'level_high_score' : '1',
                'xp' : '0',
                'xp_high_score' : '0',
                'initial_xp_needed' : '100',
                'levels_to_increase_xp' : '10',
                'xp_increase_amount' : '50',
            }

            if not self.config.has_section('Leveling_Snake_Values'):
                self.config.add_section('Leveling_Snake_Values')

            for option, value in leveling_snake_values.items():
                if not self.config.has_option('Leveling_Snake_Values', option):
                    self.config.set('Leveling_Snake_Values', option, value)
                    self.write_changes_to_configini()

        except FileNotFoundError as e:
            traceback.print_exc(e)

    def set_leveling_snake_settings(self):
        """
        Set the Leveling_Snake_Settings section in the config.ini file.
        """
        try:
            leveling_snake_settings = {
                'state' : 'start_game',
            }

            if not self.config.has_section('Leveling_Snake_Settings'):
                self.config.add_section('Leveling_Snake_Settings')

            for option, value in leveling_snake_settings.items():
                if not self.config.has_option('Leveling_Snake_Settings', option):
                    self.config.set('Leveling_Snake_Settings', option, value)
                    self.write_changes_to_configini()

        except FileNotFoundError as e:
            traceback.print_exc(e)

    def set_food_time_attack_values(self):
        """
        Set the food_time_attack_Values section in the config.ini file.
        """
        try:
            food_time_attack_values = {
                'score' : '0',
                'high_score' : '0',
                'special_score' : '0',
                'special_score_high_score' : '0',
                'snake_length' : '0',
                'snake_length_high_score' : '0',
                'time_score' : '0',
                'high_score_time' : '0',
                'shorten_score' : '0',
                'shorten_snake_high_score' : '0',
                'next_special_food_score' : '50',
                'next_shorten_food_score' : '100',
                'level' : '1',
                'level_high_score' : '1',
                'xp' : '0',
                'xp_high_score' : '0',
                'initial_xp_needed' : '100',
                'levels_to_increase_xp' : '10',
                'xp_increase_amount' : '50',
            }

            if not self.config.has_section('food_time_attack_Values'):
                self.config.add_section('food_time_attack_Values')

            for option, value in food_time_attack_values.items():
                if not self.config.has_option('food_time_attack_Values', option):
                    self.config.set('food_time_attack_Values', option, value)
                    self.write_changes_to_configini()

        except FileNotFoundError as e:
            traceback.print_exc(e)

    def set_food_time_attack_settings(self):
        """
        Set the food_time_attack_Settings section in the config.ini file.
        """
        try:
            food_time_attack_settings = {
                'state' : 'start_game',
            }

            if not self.config.has_section('food_time_attack_Settings'):
                self.config.add_section('food_time_attack_Settings')

            for option, value in food_time_attack_settings.items():
                if not self.config.has_option('food_time_attack_Settings', option):
                    self.config.set('food_time_attack_Settings', option, value)
                    self.write_changes_to_configini()

        except FileNotFoundError as e:
            traceback.print_exc(e)

    def set_keybindings(self):
        """
        Set the keybindings section in the config.ini file.
        """
        try:
            keybindings = {
                'up' : 'Up',
                'down' : 'Down',
                'left' : 'Left',
                'right' : 'Right',
                'start_game' : 'space',
                'pausegame' : 'Escape',
                'reset_game' : 'r',
            }

            if not self.config.has_section('Keybindings'):
                self.config.add_section('Keybindings')

            for option, value in keybindings.items():
                if not self.config.has_option('Keybindings', option):
                    self.config.set('Keybindings', option, value)
                    self.write_changes_to_configini()

        except FileNotFoundError as e:
            traceback.print_exc(e)

    def set_default_keybindings(self):
        """
        Set the default keybindings section in the config.ini file.
        """
        try:
            keybindings = {
                'up' : 'Up',
                'down' : 'Down',
                'left' : 'Left',
                'right' : 'Right',
                'start_game' : 'space',
                'pausegame' : 'Escape',
                'reset_game' : 'r',
            }

            if not self.config.has_section('Keybindings'):
                self.config.add_section('Keybindings')

            for option, value in keybindings.items():
                if not self.config.has_option('Keybindings', option):
                    self.config.set('Keybindings', option, value)
                    self.write_changes_to_configini()

        except FileNotFoundError as e:
            traceback.print_exc(e)

    def write_changes_to_configini(self):
        """
        Write the changes to the config.ini file.
        """
        with open('config.ini', 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)

## add keybindings settings and default values


#****************************************************
# Initializing the Config.ini file
#****************************************************
