#***********************************************************
# Reset Config Values File
#***********************************************************

"""
File for resetting the configuration values of the game.
"""


import configparser
import traceback
import time


class ResetConfigValues:
    """
    Class for resetting the configuration values of the game.
    """
    def __init__(self, game_logger, classic_snake_canvas, endless_snake_canvas, leveling_snake_canvas):
        self.config = configparser.ConfigParser()
        self.config_path = 'config.ini'
        self.game_logger = game_logger
        self.classic_snake_canvas = classic_snake_canvas
        self.endless_snake_canvas = endless_snake_canvas
        self.leveling_snake_canvas = leveling_snake_canvas
        self.classic_button_press_variable_high_score = 0
        self.classic_button_press_variable_high_score_time = 0
        self.endless_button_press_variable_high_score = 0
        self.endless_button_press_variable_high_score_time = 0
        self.leveling_button_press_variable_high_score = 0
        self.leveling_button_press_variable_high_score_time = 0
        self.button_press_time_limit = 2
        self.first_button_press_time = None
        self.button_press_variable = 0

    def reset_screen_size(self):
        """
        Reset the screen size to the default value.
        """
        self.config.read(self.config_path)
        self.config.set('Settings', 'screen_size', 'Default')
        with open('config.ini', 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)
        self.game_logger.log_game_event("Screen size reset to Default")

    def reset_theme(self):
        """
        Reset the theme to the default value.
        """
        self.config.read(self.config_path)
        self.config.set('Settings', 'theme', 'Default')
        with open('config.ini', 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)
        self.game_logger.log_game_event("Theme reset to Default")

    def reset_contrast(self):
        """
        Reset the contrast to the default value.
        """
        self.config.read(self.config_path)
        self.config.set('Settings', 'contrast', 'Default')
        with open('config.ini', 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)
        self.game_logger.log_game_event("Contrast reset to Default")

    def reset_high_score_showing(self):
        """
        Reset the high score label showing to the default value.
        """
        self.config.read(self.config_path)
        self.config.set('Settings', 'high_score_label_showing', 'Default')
        with open('config.ini', 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)
        self.game_logger.log_game_event("High score label showing reset to True")

    def reset_snake_speed(self):
        """
        Reset the snake speed to the default value.
        """
        self.config.read(self.config_path)
        self.config.set('Settings', 'snake_speed', '50')
        with open('config.ini', 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)
        self.game_logger.log_game_event("Snake speed reset to 5")

    def reset_game_size(self):
        """
        Reset the game size to the default value.
        """
        self.config.read(self.config_path)
        self.config.set('Settings', 'game_size', '600x600')
        with open('config.ini', 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)
        self.game_logger.log_game_event("Game size reset to 600x600")

    def reset_snake_color(self):
        """
        Reset the snake color to the default value.
        """
        self.config.read(self.config_path)
        self.config.set('Settings', 'snake_color', 'Default')
        with open('config.ini', 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)
        self.game_logger.log_game_event("Snake color reset to Default")

    def reset_move_up(self):
        """
        Reset the move up key to the default value.
        """
        self.config.read(self.config_path)
        self.config.set('KeyBindings', 'move_up', 'w')
        with open('config.ini', 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)
        self.game_logger.log_game_event("Move up key reset to w")

    def reset_move_down(self):
        """
        Reset the move down key to the default value.
        """
        self.config.read(self.config_path)
        self.config.set('KeyBindings', 'move_down', 's')
        with open('config.ini', 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)
        self.game_logger.log_game_event("Move down key reset to s")

    def reset_move_left(self):
        """
        Reset the move left key to the default value.
        """
        self.config.read(self.config_path)
        self.config.set('KeyBindings', 'move_left', 'a')
        with open('config.ini', 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)
        self.game_logger.log_game_event("Move left key reset to a")

    def reset_move_right(self):
        """
        Reset the move right key to the default value.
        """
        self.config.read(self.config_path)
        self.config.set('KeyBindings', 'move_right', 'd')
        with open('config.ini', 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)
        self.game_logger.log_game_event("Move right key reset to d")

    def reset_pause(self):
        """
        Reset the pause key to the default value.
        """
        self.config.read(self.config_path)
        self.config.set('KeyBindings', 'pausegame', 'Escape')
        with open('config.ini', 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)
        self.game_logger.log_game_event("Pause key reset to Escape")

    def reset_start_game(self):
        """
        Reset the start game key to the default value.
        """
        self.config.read(self.config_path)
        self.config.set('KeyBindings', 'startgame', 'space')
        with open('config.ini', 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)
        self.game_logger.log_game_event("Start game key reset to space")

    def reset_restart(self):
        """
        Reset the restart key to the default value.
        """
        self.config.read(self.config_path)
        self.config.set('KeyBindings', 'restartgame', 'r')
        with open('config.ini', 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)
        self.game_logger.log_game_event("Restart key reset to r")

    def reset_all_settings(self):
        """
        Reset all the settings to the default values.
        """
        self.config.read(self.config_path)
        print('Before resetting:')  # Print settings before resetting
        print(dict(self.config['Settings']))
        self.config.set('Settings', 'screen_size', 'Default')
        self.config.set('Settings', 'theme', 'Default')
        self.config.set('Settings', 'contrast', 'Default')
        self.config.set('Settings', 'label_needed_high_score', 'Default')
        self.config.set('Settings', 'snake_speed', '50')
        self.config.set('Settings', 'game_size', '600x600')
        self.config.set('Settings', 'snake_color', 'Default')
        with open('config.ini', 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)
        print('After resetting:')  # Print settings after resetting
        print(print(dict(self.config['Settings'])))
        self.config.set('KeyBindings', 'move_up', 'w')
        self.config.set('KeyBindings', 'move_down', 's')
        self.config.set('KeyBindings', 'move_left', 'a')
        self.config.set('KeyBindings', 'move_right', 'd')
        self.config.set('KeyBindings', 'pausegame', 'Escape')
        self.config.set('KeyBindings', 'startgame', 'space')
        self.config.set('KeyBindings', 'restartgame', 'r')
        with open('config.ini', 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)
        self.game_logger.log_game_event("All settings reset to default")

    def reset_all_movements(self):
        """
        Reset all the movements to the default values.
        """
        self.config.read(self.config_path)
        self.config.set('KeyBindings', 'move_up', 'w')
        self.config.set('KeyBindings', 'move_down', 's')
        self.config.set('KeyBindings', 'move_left', 'a')
        self.config.set('KeyBindings', 'move_right', 'd')
        self.config.set('KeyBindings', 'pausegame', 'Escape')
        self.config.set('KeyBindings', 'startgame', 'space')
        self.config.set('KeyBindings', 'restartgame', 'r')
        with open('config.ini', 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)
        self.game_logger.log_game_event("All movements reset to default")

    def classic_reset_high_score(self):
        """
        Reset the high score for the classic snake game.
        """
        if self.classic_button_press_variable_high_score == 0:
            self.first_button_press_time = time.time()
            self.classic_button_press_variable_high_score += 1
        elif self.classic_button_press_variable_high_score == 1 and time.time() - self.first_button_press_time <= self.button_press_time_limit: # pylint: disable=line-too-long
            try:
                self.config.read(self.config_path)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                self.config.set('Classic_Snake_Values', 'high_score', '0')
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                with open('config.ini', 'w', encoding='utf-8') as configfile:
                    self.config.write(configfile)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                self.config.read(self.config_path)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            self.game_logger.log_game_event("Highscore reset to 0")
            self.classic_button_press_variable_high_score = 0
            self.first_button_press_time = None

    def classic_reset_high_score_time(self):
        """
        Reset the high score time for the classic snake game.
        """
        if self.classic_button_press_variable_high_score_time == 0:
            self.first_button_press_time = time.time()
            self.classic_button_press_variable_high_score_time += 1
        elif self.classic_button_press_variable_high_score_time == 1 and time.time() - self.first_button_press_time <= self.button_press_time_limit: # pylint: disable=line-too-long
            try:
                self.config.read(self.config_path)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                self.config.set('Classic_Snake_Values', 'high_score_time', '0')
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                with open('config.ini', 'w', encoding='utf-8') as configfile:
                    self.config.write(configfile)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                self.config.read(self.config_path)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            self.game_logger.log_game_event("Highscore time reset to 0")
            self.classic_button_press_variable_high_score_time = 0
            self.first_button_press_time = None

    def classic_reset_snake_length(self):
        """
        Reset the high score snake length for the classic snake game.
        """
        if self.classic_button_press_variable_high_score_time == 0:
            self.first_button_press_time = time.time()
            self.classic_button_press_variable_high_score_time += 1
        elif self.classic_button_press_variable_high_score_time == 1 and time.time() - self.first_button_press_time <= self.button_press_time_limit: # pylint: disable=line-too-long
            try:
                self.config.read(self.config_path)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                self.config.set('Classic_Snake_Values', 'snake_length_high_score', '0')
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                with open('config.ini', 'w', encoding='utf-8') as configfile:
                    self.config.write(configfile)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                self.config.read(self.config_path)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            self.game_logger.log_game_event("Highscore time reset to 0")
            self.classic_button_press_variable_high_score_time = 0
            self.first_button_press_time = None

    def classic_reset_button_press_variable(self):
        """
        Reset the button press variable for the classic snake game.
        """
        self.classic_button_press_variable_high_score = 0
        self.classic_button_press_variable_high_score_time = 0

    def endless_reset_high_score(self):
        """
        Reset the high score for the endless snake game.
        """
        if self.endless_button_press_variable_high_score == 0:
            self.first_button_press_time = time.time()
            self.endless_button_press_variable_high_score += 1
        elif self.endless_button_press_variable_high_score == 1 and time.time() - self.first_button_press_time <= self.button_press_time_limit: # pylint: disable=line-too-long
            try:
                self.config.read(self.config_path)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                self.config.set('Endless_Snake_Values', 'high_score', '0')
                with open('config.ini', 'w', encoding='utf-8') as configfile:
                    self.config.write(configfile)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                self.config.read(self.config_path)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            self.game_logger.log_game_event("Highscore reset to 0")
            self.endless_button_press_variable_high_score = 0
            self.first_button_press_time = None

    def endless_reset_high_score_time(self):
        """
        Reset the high score time for the endless snake game.
        """
        if self.endless_button_press_variable_high_score_time == 0:
            self.first_button_press_time = time.time()
            self.endless_button_press_variable_high_score_time += 1
        elif self.endless_button_press_variable_high_score_time == 1 and time.time() - self.first_button_press_time <= self.button_press_time_limit: # pylint: disable=line-too-long
            try:
                self.config.read(self.config_path)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                self.config.set('Endless_Snake_Values', 'high_score_time', '0')
                with open('config.ini', 'w', encoding='utf-8') as configfile:
                    self.config.write(configfile)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                self.config.read(self.config_path)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            self.game_logger.log_game_event("Highscore time reset to 0")
            self.endless_button_press_variable_high_score_time = 0
            self.first_button_press_time = None

    def endless_reset_high_score_snake_length(self):
        """
        Reset the high score snake length for the endless snake game.
        """
        if self.endless_button_press_variable_high_score_time == 0:
            self.first_button_press_time = time.time()
            self.endless_button_press_variable_high_score_time += 1
        elif self.endless_button_press_variable_high_score_time == 1 and time.time() - self.first_button_press_time <= self.button_press_time_limit: # pylint: disable=line-too-long
            try:
                self.config.read(self.config_path)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                self.config.set('Endless_Snake_Values', 'snake_length_high_score', '0')
                with open('config.ini', 'w', encoding='utf-8') as configfile:
                    self.config.write(configfile)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                self.config.read(self.config_path)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            self.game_logger.log_game_event("Highscore time reset to 0")
            self.endless_button_press_variable_high_score_time = 0
            self.first_button_press_time = None

    def endless_reset_high_score_special_score(self):
        """
        Reset the high score special score for the endless snake game.
        """
        if self.endless_button_press_variable_high_score_time == 0:
            self.first_button_press_time = time.time()
            self.endless_button_press_variable_high_score_time += 1
        elif self.endless_button_press_variable_high_score_time == 1 and time.time() - self.first_button_press_time <= self.button_press_time_limit: # pylint: disable=line-too-long
            try:
                self.config.read(self.config_path)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                self.config.set('Endless_Snake_Values', 'special_score_high_score', '0')
                with open('config.ini', 'w', encoding='utf-8') as configfile:
                    self.config.write(configfile)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                self.config.read(self.config_path)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            self.game_logger.log_game_event("Highscore special reset to 0")
            self.endless_button_press_variable_high_score_time = 0
            self.first_button_press_time = None

    def endless_reset_high_score_shorten_snake(self):
        """
        Reset the high score shorten snake for the endless snake game.
        """
        if self.endless_button_press_variable_high_score_time == 0:
            self.first_button_press_time = time.time()
            self.endless_button_press_variable_high_score_time += 1
        elif self.endless_button_press_variable_high_score_time == 1 and time.time() - self.first_button_press_time <= self.button_press_time_limit: # pylint: disable=line-too-long
            try:
                self.config.read(self.config_path)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                self.config.set('Endless_Snake_Values', 'shorten_snake_high_score', '0')
                with open('config.ini', 'w', encoding='utf-8') as configfile:
                    self.config.write(configfile)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                self.config.read(self.config_path)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            self.game_logger.log_game_event("Highscore shorten snake reset to 0")
            self.endless_button_press_variable_high_score_time = 0
            self.first_button_press_time = None

    def endless_reset_button_press_variable(self):
        """
        Reset the button press variable for the endless snake game.
        """
        self.endless_button_press_variable_high_score = 0
        self.endless_button_press_variable_high_score_time = 0

    def leveling_reset_high_score(self):
        """
        Reset the high score for the leveling snake game.
        """
        if self.leveling_button_press_variable_high_score == 0:
            self.first_button_press_time = time.time()
            self.leveling_button_press_variable_high_score += 1
        elif self.leveling_button_press_variable_high_score == 1 and time.time() - self.first_button_press_time <= self.button_press_time_limit: # pylint: disable=line-too-long
            try:
                self.config.read(self.config_path)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                self.config.set('Leveling_Snake_Values', 'high_score', '0')
                with open('config.ini', 'w', encoding='utf-8') as configfile:
                    self.config.write(configfile)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                self.config.read(self.config_path)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            self.game_logger.log_game_event("Highscore reset to 0")
            self.leveling_button_press_variable_high_score = 0
            self.first_button_press_time = None

    def leveling_reset_high_score_time(self):
        """
        Reset the high score time for the leveling snake game.
        """
        if self.leveling_button_press_variable_high_score_time == 0:
            self.first_button_press_time = time.time()
            self.leveling_button_press_variable_high_score_time += 1
        elif self.leveling_button_press_variable_high_score_time == 1 and time.time() - self.first_button_press_time <= self.button_press_time_limit: # pylint: disable=line-too-long
            try:
                self.config.read(self.config_path)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                self.config.set('Leveling_Snake_Values', 'high_score_time', '0')
                with open('config.ini', 'w', encoding='utf-8') as configfile:
                    self.config.write(configfile)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                self.config.read(self.config_path)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            self.game_logger.log_game_event("Highscore time reset to 0")
            self.leveling_button_press_variable_high_score_time = 0
            self.first_button_press_time = None

    def leveling_reset_high_score_snake_length(self):
        """
        Reset the high score snake length for the leveling snake game.
        """
        if self.leveling_button_press_variable_high_score_time == 0:
            self.first_button_press_time = time.time()
            self.leveling_button_press_variable_high_score_time += 1
        elif self.leveling_button_press_variable_high_score_time == 1 and time.time() - self.first_button_press_time <= self.button_press_time_limit: # pylint: disable=line-too-long
            try:
                self.config.read(self.config_path)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                self.config.set('Leveling_Snake_Values', 'snake_length_high_score', '0')
                with open('config.ini', 'w', encoding='utf-8') as configfile:
                    self.config.write(configfile)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                self.config.read(self.config_path)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            self.game_logger.log_game_event("Highscore time reset to 0")
            self.leveling_button_press_variable_high_score_time = 0
            self.first_button_press_time = None

    def leveling_reset_high_score_special_score(self):
        """
        Reset the high score special score for the leveling snake game.
        """
        if self.leveling_button_press_variable_high_score_time == 0:
            self.first_button_press_time = time.time()
            self.leveling_button_press_variable_high_score_time += 1
        elif self.leveling_button_press_variable_high_score_time == 1 and time.time() - self.first_button_press_time <= self.button_press_time_limit: # pylint: disable=line-too-long
            try:
                self.config.read(self.config_path)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                self.config.set('Leveling_Snake_Values', 'special_score_high_score', '0')
                with open('config.ini', 'w', encoding='utf-8') as configfile:
                    self.config.write(configfile)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                self.config.read(self.config_path)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            self.game_logger.log_game_event("Highscore special reset to 0")
            self.leveling_button_press_variable_high_score_time = 0
            self.first_button_press_time = None

    def leveling_reset_high_score_shorten_snake(self):
        """
        Reset the high score shorten snake for the leveling snake game.
        """
        if self.leveling_button_press_variable_high_score_time == 0:
            self.first_button_press_time = time.time()
            self.leveling_button_press_variable_high_score_time += 1
        elif self.leveling_button_press_variable_high_score_time == 1 and time.time() - self.first_button_press_time <= self.button_press_time_limit: # pylint: disable=line-too-long
            try:
                self.config.read(self.config_path)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                self.config.set('Leveling_Snake_Values', 'shorten_snake_high_score', '0')
                with open('config.ini', 'w', encoding='utf-8') as configfile:
                    self.config.write(configfile)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                self.config.read(self.config_path)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            self.game_logger.log_game_event("Highscore shorten snake reset to 0")
            self.leveling_button_press_variable_high_score_time = 0
            self.first_button_press_time = None

    def leveling_reset_high_scores_xp(self):
        """
        Reset the high score xp for the leveling snake game.
        """
        if self.leveling_button_press_variable_high_score_time == 0:
            self.first_button_press_time = time.time()
            self.leveling_button_press_variable_high_score_time += 1
        elif self.leveling_button_press_variable_high_score_time == 1 and time.time() - self.first_button_press_time <= self.button_press_time_limit: # pylint: disable=line-too-long
            try:
                self.config.read(self.config_path)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                self.config.set('Leveling_Snake_Values', 'xp_high_score', '0')
                with open('config.ini', 'w', encoding='utf-8') as configfile:
                    self.config.write(configfile)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                self.config.read(self.config_path)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            self.game_logger.log_game_event("Highscore xp reset to 0")
            self.leveling_button_press_variable_high_score_time = 0
            self.first_button_press_time = None

    def leveling_reset_high_score_level(self):
        """
        Reset the high score level for the leveling snake game.
        """
        if self.leveling_button_press_variable_high_score_time == 0:
            self.first_button_press_time = time.time()
            self.leveling_button_press_variable_high_score_time += 1
        elif self.leveling_button_press_variable_high_score_time == 1 and time.time() - self.first_button_press_time <= self.button_press_time_limit: # pylint: disable=line-too-long
            try:
                self.config.read(self.config_path)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                self.config.set('Leveling_Snake_Values', 'level_high_score', '0')
                with open('config.ini', 'w', encoding='utf-8') as configfile:
                    self.config.write(configfile)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                self.config.read(self.config_path)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            self.game_logger.log_game_event("Highscore level reset to 0")
            self.leveling_button_press_variable_high_score_time = 0
            self.first_button_press_time = None

    def leveling_reset_button_press_variable(self):
        """
        Reset the button press variable for the leveling snake game.
        """
        self.leveling_button_press_variable_high_score = 0
        self.leveling_button_press_variable_high_score_time = 0

    def general_reset_button_press_variable(self):
        """
        Reset the button press variable for the game.
        """
        self.button_press_variable = 0

#***********************************************************
# Reset Config Values File
#***********************************************************
