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
            if not self.config.has_section('Settings'):
                self.config.add_section('Settings')
            if not self.config.has_option('Settings', 'initial_theme'):
                self.config.set('Settings', 'initial_theme', 'Default')
            if not self.config.has_option('Settings', 'theme'):
                self.config.set('Settings', 'theme', 'Default')
            if not self.config.has_option('Settings', 'contrast'):
                self.config.set('Settings', 'contrast', 'Default')
            if not self.config.has_option('Settings', 'language'):
                self.config.set('Settings', 'language', 'English')
            if not self.config.has_option('Settings', 'snake_color'):
                self.config.set('Settings', 'snake_color', 'Default')
            if not self.config.has_option('Settings', 'screen_size'):
                self.config.set('Settings', 'screen_size', 'Default')
            if not self.config.has_option('Settings', 'label_needed_theme'):
                self.config.set('Settings', 'label_needed_theme', 'False')
            if not self.config.has_option('Settings', 'button_press_time_limit'):
                self.config.set('Settings', 'button_press_time_limit', '0.5')
            if not self.config.has_option('Settings', 'label_needed_high_score'):
                self.config.set('Settings', 'label_needed_high_score', 'Default')
            if not self.config.has_option('Settings', 'label_needed_game_size'):
                self.config.set('Settings', 'label_needed_game_size', 'False')
            if not self.config.has_option('Settings', 'game_mode'):
                self.config.set('Settings', 'game_mode', 'classic_snake')
            if not self.config.has_option('Settings', 'snake_speed'):
                self.config.set('Settings', 'snake_speed', '50') # 50 is default
            if not self.config.has_option('Settings', 'initial_game_size'):
                self.config.set('Settings', 'initial_game_size', '500x500') # 500x500 is default
            if not self.config.has_option('Settings', 'game_size'):
                self.config.set('Settings', 'game_size', '500x500') # 500x500 is default
            if not self.config.has_option('Settings', 'button_state'):
                self.config.set('Settings', 'button_state', 'normal')
            if self.config.has_option('Settings', 'button_state'):
                self.config.set('Settings', 'button_state', 'normal')
            with open('config.ini', 'w', encoding='utf-8') as configfile:
                self.config.write(configfile)
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def set_classic_snake_values(self):
        """
        Set the Classic_Snake_Values section in the config.ini file.
        """
        try:
            if not self.config.has_section('Classic_Snake_Values'):
                self.config.add_section('Classic_Snake_Values')
            if not self.config.has_option('Classic_Snake_Values', 'score'):
                self.config.set('Classic_Snake_Values', 'score', '0')
            if not self.config.has_option('Classic_Snake_Values', 'high_score'):
                self.config.set('Classic_Snake_Values', 'high_score', '0')
            if not self.config.has_option('Classic_Snake_Values', 'snake_length'):
                self.config.set('Classic_Snake_Values', 'snake_length', '0')
            if not self.config.has_option('Classic_Snake_Values', 'snake_length_high_score'):
                self.config.set('Classic_Snake_Values', 'snake_length_high_score', '0')
            if not self.config.has_option('Classic_Snake_Values', 'time_scpre'):
                self.config.set('Classic_Snake_Values', 'time_score', '0')
            if not self.config.has_option('Classic_Snake_Values', 'high_score_time'):
                self.config.set('Classic_Snake_Values', 'high_score_time', '0')
            with open('config.ini', 'w', encoding='utf-8') as configfile:
                self.config.write(configfile)
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def set_classic_snake_settings(self):
        """
        Set the Classic_Snake_Settings section in the config.ini file.
        """
        try:
            if not self.config.has_section('Classic_Snake_Settings'):
                self.config.add_section('Classic_Snake_Settings')
            if not self.config.has_option('Classic_Snake_Settings', 'state'):
                self.config.set('Classic_Snake_Settings', 'state', 'start_game')
            with open('config.ini', 'w', encoding='utf-8') as configfile:
                self.config.write(configfile)
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def set_endless_snake_values(self):
        """
        Set the Endless_Snake_Values section in the config.ini file.
        """
        try:
            if not self.config.has_section('Endless_Snake_Values'):
                self.config.add_section('Endless_Snake_Values')
            if not self.config.has_option('Endless_Snake_Values', 'score'):
                self.config.set('Endless_Snake_Values', 'score', '0')
            if not self.config.has_option('Endless_Snake_Values', 'high_score'):
                self.config.set('Endless_Snake_Values', 'high_score', '0')
            if not self.config.has_option('Endless_Snake_Values', 'special_score'):
                self.config.set('Endless_Snake_Values', 'special_score', '0')
            if not self.config.has_option('Endless_Snake_Values', 'special_score_high_score'):
                self.config.set('Endless_Snake_Values', 'special_score_high_score', '0')
            if not self.config.has_option('Endless_Snake_Values', 'snake_length'):
                self.config.set('Endless_Snake_Values', 'snake_length', '0')
            if not self.config.has_option('Endless_Snake_Values', 'snake_length_high_score'):
                self.config.set('Endless_Snake_Values', 'snake_length_high_score', '0')
            if not self.config.has_option('Endless_Snake_Values', 'time_scpre'):
                self.config.set('Endless_Snake_Values', 'time_score', '0')
            if not self.config.has_option('Endless_Snake_Values', 'high_score_time'):
                self.config.set('Endless_Snake_Values', 'high_score_time', '0')
            if not self.config.has_option('Endless_Snake_Values', 'shorten_score'):
                self.config.set('Endless_Snake_Values', 'shorten_score', '0')
            if not self.config.has_option('Endless_Snake_Values', 'shorten_snake_high_score'):
                self.config.set('Endless_Snake_Values', 'shorten_snake_high_score', '0')
            if not self.config.has_option('Endless_Snake_Values', 'next_special_food_score'):
                self.config.set('Endless_Snake_Values', 'next_special_food_score', '50')
            if not self.config.has_option('Endless_Snake_Values', 'next_shorten_food_score'):
                self.config.set('Endless_Snake_Values', 'next_shorten_food_score', '100')

            with open('config.ini', 'w', encoding='utf-8') as configfile:
                self.config.write(configfile)
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def set_endless_snake_settings(self):
        """
        Set the Endless_Snake_Settings section in the config.ini file.
        """
        try:
            if not self.config.has_section('Endless_Snake_Settings'):
                self.config.add_section('Endless_Snake_Settings')
            if not self.config.has_option('Endless_Snake_Settings', 'state'):
                self.config.set('Endless_Snake_Settings', 'state', 'start_game')
            with open('config.ini', 'w', encoding='utf-8') as configfile:
                self.config.write(configfile)
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def set_leveling_snake_values(self):
        """
        Set the Leveling_Snake_Values section in the config.ini file.
        """
        try:
            if not self.config.has_section('Leveling_Snake_Values'):
                self.config.add_section('Leveling_Snake_Values')
            if not self.config.has_option('Leveling_Snake_Values', 'score'):
                self.config.set('Leveling_Snake_Values', 'score', '0')
            if not self.config.has_option('Leveling_Snake_Values', 'high_score'):
                self.config.set('Leveling_Snake_Values', 'high_score', '0')
            if not self.config.has_option('Leveling_Snake_Values', 'special_score'):
                self.config.set('Leveling_Snake_Values', 'special_score', '0')
            if not self.config.has_option('Leveling_Snake_Values', 'special_score_high_score'):
                self.config.set('Leveling_Snake_Values', 'special_score_high_score', '0')
            if not self.config.has_option('Leveling_Snake_Values', 'snake_length'):
                self.config.set('Leveling_Snake_Values', 'snake_length', '0')
            if not self.config.has_option('Leveling_Snake_Values', 'snake_length_high_score'):
                self.config.set('Leveling_Snake_Values', 'snake_length_high_score', '0')
            if not self.config.has_option('Leveling_Snake_Values', 'time_scpre'):
                self.config.set('Leveling_Snake_Values', 'time_score', '0')
            if not self.config.has_option('Leveling_Snake_Values', 'high_score_time'):
                self.config.set('Leveling_Snake_Values', 'high_score_time', '0')
            if not self.config.has_option('Leveling_Snake_Values', 'shorten_score'):
                self.config.set('Leveling_Snake_Values', 'shorten_score', '0')
            if not self.config.has_option('Leveling_Snake_Values', 'shorten_snake_high_score'):
                self.config.set('Leveling_Snake_Values', 'shorten_snake_high_score', '0')
            if not self.config.has_option('Leveling_Snake_Values', 'next_special_food_score'):
                self.config.set('Leveling_Snake_Values', 'next_special_food_score', '50')
            if not self.config.has_option('Leveling_Snake_Values', 'next_shorten_food_score'):
                self.config.set('Leveling_Snake_Values', 'next_shorten_food_score', '100')
            if not self.config.has_option('Leveling_Snake_Values', 'level'):
                self.config.set('Leveling_Snake_Values', 'level', '1')
            if not self.config.has_option('Leveling_Snake_Values', 'level_high_score'):
                self.config.set('Leveling_Snake_Values', 'level_high_score', '1')
            if not self.config.has_option('Leveling_Snake_Values', 'xp'):
                self.config.set('Leveling_Snake_Values', 'xp', '0')
            if not self.config.has_option('Leveling_Snake_Values', 'xp_high_score'):
                self.config.set('Leveling_Snake_Values', 'xp_high_score', '0')
            if not self.config.has_option('Leveling_Snake_Values', 'initial_xp_needed'):
                self.config.set('Leveling_Snake_Values', 'initial_xp_needed', '100')
            if not self.config.has_option('Leveling_Snake_Values', 'levels_to_increase_xp'):
                self.config.set('Leveling_Snake_Values', 'levels_to_increase_xp', '10')
            if not self.config.has_option('Leveling_Snake_Values', 'xp_increase_amount'):
                self.config.set('Leveling_Snake_Values', 'xp_increase_amount', '50')
            with open('config.ini', 'w', encoding='utf-8') as configfile:
                self.config.write(configfile)
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def set_leveling_snake_settings(self):
        """
        Set the Leveling_Snake_Settings section in the config.ini file.
        """
        try:
            if not self.config.has_section('Leveling_Snake_Settings'):
                self.config.add_section('Leveling_Snake_Settings')
            if not self.config.has_option('Leveling_Snake_Settings', 'state'):
                self.config.set('Leveling_Snake_Settings', 'state', 'start_game')
            with open('config.ini', 'w', encoding='utf-8') as configfile:
                self.config.write(configfile)
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def set_food_time_attack_values(self):
        """
        Set the food_time_attack_Values section in the config.ini file.
        """
        try:
            if not self.config.has_section('food_time_attack_Values'):
                self.config.add_section('food_time_attack_Values')
            if not self.config.has_option('food_time_attack_Values', 'score'):
                self.config.set('food_time_attack_Values', 'score', '0')
            if not self.config.has_option('food_time_attack_Values', 'high_score'):
                self.config.set('food_time_attack_Values', 'high_score', '0')
            if not self.config.has_option('food_time_attack_Values', 'special_score'):
                self.config.set('food_time_attack_Values', 'special_score', '0')
            if not self.config.has_option('food_time_attack_Values', 'special_score_high_score'):
                self.config.set('food_time_attack_Values', 'special_score_high_score', '0')
            if not self.config.has_option('food_time_attack_Values', 'snake_length'):
                self.config.set('food_time_attack_Values', 'snake_length', '0')
            if not self.config.has_option('food_time_attack_Values', 'snake_length_high_score'):
                self.config.set('food_time_attack_Values', 'snake_length_high_score', '0')
            if not self.config.has_option('food_time_attack_Values', 'time_scpre'):
                self.config.set('food_time_attack_Values', 'time_score', '0')
            if not self.config.has_option('food_time_attack_Values', 'high_score_time'):
                self.config.set('food_time_attack_Values', 'high_score_time', '0')
            if not self.config.has_option('food_time_attack_Values', 'shorten_score'):
                self.config.set('food_time_attack_Values', 'shorten_score', '0')
            if not self.config.has_option('food_time_attack_Values', 'shorten_snake_high_score'):
                self.config.set('food_time_attack_Values', 'shorten_snake_high_score', '0')
            if not self.config.has_option('food_time_attack_Values', 'next_special_food_score'):
                self.config.set('food_time_attack_Values', 'next_special_food_score', '50')
            if not self.config.has_option('food_time_attack_Values', 'next_shorten_food_score'):
                self.config.set('food_time_attack_Values', 'next_shorten_food_score', '100')
            if not self.config.has_option('food_time_attack_Values', 'level'):
                self.config.set('food_time_attack_Values', 'level', '1')
            if not self.config.has_option('food_time_attack_Values', 'level_high_score'):
                self.config.set('food_time_attack_Values', 'level_high_score', '1')
            if not self.config.has_option('food_time_attack_Values', 'xp'):
                self.config.set('food_time_attack_Values', 'xp', '0')
            if not self.config.has_option('food_time_attack_Values', 'xp_high_score'):
                self.config.set('food_time_attack_Values', 'xp_high_score', '0')
            if not self.config.has_option('food_time_attack_Values', 'initial_xp_needed'):
                self.config.set('food_time_attack_Values', 'initial_xp_needed', '100')
            if not self.config.has_option('food_time_attack_Values', 'levels_to_increase_xp'):
                self.config.set('food_time_attack_Values', 'levels_to_increase_xp', '10')
            if not self.config.has_option('food_time_attack_Values', 'xp_increase_amount'):
                self.config.set('food_time_attack_Values', 'xp_increase_amount', '50')
            with open('config.ini', 'w', encoding='utf-8') as configfile:
                self.config.write(configfile)
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def set_food_time_attack_settings(self):
        """
        Set the food_time_attack_Settings section in the config.ini file.
        """
        try:
            if not self.config.has_section('food_time_attack_Settings'):
                self.config.add_section('food_time_attack_Settings')
            if not self.config.has_option('food_time_attack_Settings', 'state'):
                self.config.set('food_time_attack_Settings', 'state', 'start_game')
            with open('config.ini', 'w', encoding='utf-8') as configfile:
                self.config.write(configfile)
        except FileNotFoundError as e:
            traceback.print_exc(e)


#****************************************************
# Initializing the Config.ini file
#****************************************************
