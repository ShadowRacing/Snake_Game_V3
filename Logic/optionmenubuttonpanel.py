"""
This module is responsible for creating the option button panel of the Shadows Snake game. # pylint: disable=line-too-long
"""


# Importing necessary modules
import configparser
import traceback
from os import path
import customtkinter as ctk

# Importing necessary modules from other folders
from Themes.contrast_updater_snake_game import UpdateContrast
from Themes.theme_updater_snake_game import ThemeUpdater
from Configuration.constants_snake_game import GameConstants, FONT_LIST, COLORS_DICT
from Logic.screen_size_changer_snake_game import ScreenSize
from Logic.labelpanel_snake_game import SettingsOptionButtonLabels

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
        try:
            self.config.set('Settings', 'screen_size', selected_value)
            self.updating_config_ini()
            self.screen_size_changer.change_screen_size(selected_value)
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def theme_callback(self, selected_value):
        """
        Function for the theme callback.
        """
        try:
            self.config.set('Settings', 'theme', selected_value)
            self.updating_config_ini()
            self.label_panel.create_theme_label()
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def contrast_callback(self, selected_value):
        """
        Function for the contrast callback.
        """
        try:
            self.config.set('Settings', 'contrast', selected_value)
            self.updating_config_ini()
            self.contrast_updater.apply_contrast()
        except FileNotFoundError as e:
            traceback.print_exc(e)

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
                self.label_panel.create_keybindings_allready_used_label()
                return True
            self.label_panel.destroy_keybindings_allready_used_label()

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
                                          command=command,
                                          state='normal')
        option_button.place(x=x, y=y)
        try:
            option_button.set(config)
        except ValueError as e:
            traceback.print_exc(e)

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
                                        ['Default','Black', 'Blue', 'Dark-Blue', 'Green',
                                        'Grey', 'Orange', 'Pink', 'Purple', 'Red',
                                        'White', 'Yellow', 'Gold', 'OrangeRed', 'MidnightPurple'],
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

            self.keybindings_config_up = self.config.get('KeyBindings', 'move_up', fallback='Default') # pylint: disable=line-too-long
            self.create_option_button(self.keybindings_callback_up,
                                    ["Default", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", # pylint: disable=line-too-long
                                    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "KP_0", "KP_1", "KP_2", "KP_3", "KP_4", "KP_5", "KP_6", "KP_7", "KP_8", "KP_9", "Escape", "space"], # pylint: disable=line-too-long,
                                    self.keybindings_config_up, 200, 350)

            self.keybindings_config_down = self.config.get('KeyBindings', 'move_down', fallback='Default') # pylint: disable=line-too-long
            self.create_option_button(self.keybindings_callback_down,
                                    ["Default", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", # pylint: disable=line-too-long
                                    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "KP_0", "KP_1", "KP_2", "KP_3", "KP_4", "KP_5", "KP_6", "KP_7", "KP_8", "KP_9", "Escape", "space"], # pylint: disable=line-too-long,
                                    self.keybindings_config_down, 600, 350)

            self.keybindings_config_left = self.config.get('KeyBindings', 'move_left', fallback='Default') # pylint: disable=line-too-long
            self.create_option_button(self.keybindings_callback_left,
                                    ["Default", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", # pylint: disable=line-too-long
                                    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "KP_0", "KP_1", "KP_2", "KP_3", "KP_4", "KP_5", "KP_6", "KP_7", "KP_8", "KP_9", "Escape", "space"], # pylint: disable=line-too-long,
                                    self.keybindings_config_left, 400, 350)

            self.keybindings_config_right = self.config.get('KeyBindings', 'move_right', fallback='Default') # pylint: disable=line-too-long
            self.create_option_button(self.keybindings_callback_right,
                                    ["Default", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", # pylint: disable=line-too-long
                                    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "KP_0", "KP_1", "KP_2", "KP_3", "KP_4", "KP_5", "KP_6", "KP_7", "KP_8", "KP_9", "Escape", "space"], # pylint: disable=line-too-long,
                                    self.keybindings_config_right, 800, 350)

            self.keybindings_config_startgame = self.config.get('KeyBindings', 'startgame', fallback='Default') # pylint: disable=line-too-long
            self.create_option_button(self.keybindings_callback_startgame,
                                    ["Default", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", # pylint: disable=line-too-long
                                    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "KP_0", "KP_1", "KP_2", "KP_3", "KP_4", "KP_5", "KP_6", "KP_7", "KP_8", "KP_9", "Escape", "space"], # pylint: disable=line-too-long,
                                    self.keybindings_config_startgame, 200, 500)

            self.keybindings_config_pausegame = self.config.get('KeyBindings', 'pausegame', fallback='Default') # pylint: disable=line-too-long
            self.create_option_button(self.keybindings_callback_pausegame,
                                    ["Default", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", # pylint: disable=line-too-long
                                    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "KP_0", "KP_1", "KP_2", "KP_3", "KP_4", "KP_5", "KP_6", "KP_7", "KP_8", "KP_9", "Escape", "space"], # pylint: disable=line-too-long,
                                    self.keybindings_config_pausegame, 400, 500)

            self.keybindings_config_restartgame = self.config.get('KeyBindings', 'restartgame', fallback='Default') # pylint: disable=line-too-long
            self.create_option_button(self.keybindings_callback_restartgame,
                                    ["Default", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", # pylint: disable=line-too-long
                                    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "KP_0", "KP_1", "KP_2", "KP_3", "KP_4", "KP_5", "KP_6", "KP_7", "KP_8", "KP_9", "Escape", "Spacebar"], # pylint: disable=line-too-long,
                                    self.keybindings_config_restartgame, 600, 500)

        # Handle exceptions appropriately
        except ValueError as e:
            traceback.print_exc(e)
