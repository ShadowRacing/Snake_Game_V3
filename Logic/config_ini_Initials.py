#****************************************************
# Initializing the Config.ini file
#****************************************************

import configparser


class ConfigIni:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        self.set_settings_initials()
        self.set_classic_snake_values()
        self.set_classic_snake_settings()
        self.set_classic_snake_values()
        self.set_classic_snake_settings()
    
    def set_settings_initials(self):
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
        with open('config.ini', 'w') as configfile:
            self.config.write(configfile)

    def set_classic_snake_values(self):
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

    def set_classic_snake_settings(self):
        if not self.config.has_option('Classic_Snake_Settings', 'state'):
            self.config.set('Classic_Snake_Values', 'state', 'start_game')

    def set_endless_snake_values(self):
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

    def set_endless_snake_settings(self):
        if not self.config.has_option('Endless_Snake_Settings', 'state'):
            self.config.set('Endless_Snake_Values', 'state', 'start_game')

#****************************************************
# Initializing the Config.ini file
#****************************************************