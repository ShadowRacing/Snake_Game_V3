#****************************************************
# Initializing the Config.ini file
#****************************************************

import configparser, traceback

class ConfigIni:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        self.set_config()
    
    def set_config(self):
        self.set_settings_initials()
        self.set_classic_snake_values()
        self.set_classic_snake_settings()
        self.set_endless_snake_values()
        self.set_endless_snake_settings()
    
    def set_settings_initials(self):
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
            if not self.config.has_option('Settings', 'label_needed'):
                self.config.set('Settings', 'label_needed', 'False')
            if not self.config.has_option('Settings', 'button_press_time_limit'):
                self.config.set('Settings', 'button_press_time_limit', '0.5')
            if not self.config.has_option('Settings', 'label_needed'):
                self.config.set('Settings', 'label_needed', 'True')
            if not self.config.has_option('Settings', 'label_needed_high_score'):
                self.config.set('Settings', 'label_needed_high_score', 'Default')
            if not self.config.has_option('Settings', 'game_mode'):
                self.config.set('Settings', 'game_mode', 'classic_snake')
            with open('config.ini', 'w') as configfile:
                self.config.write(configfile)
        except:
            traceback.print_exc()

    def set_classic_snake_values(self):
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
            with open('config.ini', 'w') as configfile:
                self.config.write(configfile)
        except:
            traceback.print_exc()

    def set_classic_snake_settings(self):
        try:
            if not self.config.has_section('Classic_Snake_Settings'):
                self.config.add_section('Classic_Snake_Settings')
            if not self.config.has_option('Classic_Snake_Settings', 'state'):
                self.config.set('Classic_Snake_Settings', 'state', 'start_game')
            with open('config.ini', 'w') as configfile:
                self.config.write(configfile)
        except:
            traceback.print_exc()

    def set_endless_snake_values(self):
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

            with open('config.ini', 'w') as configfile:
                self.config.write(configfile)
        except:
            traceback.print_exc()

    def set_endless_snake_settings(self):
        try:
            if not self.config.has_section('Endless_Snake_Settings'):
                self.config.add_section('Endless_Snake_Settings')
            if not self.config.has_option('Endless_Snake_Settings', 'state'):
                self.config.set('Endless_Snake_Settings', 'state', 'start_game')
            with open('config.ini', 'w') as configfile:
                self.config.write(configfile)
        except:
            traceback.print_exc()

#****************************************************
# Initializing the Config.ini file
#****************************************************