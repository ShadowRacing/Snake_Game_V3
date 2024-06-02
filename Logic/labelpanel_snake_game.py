"""
This module contains the classes that create the labels for the game
"""

import configparser
import traceback
from os import path
import customtkinter as ctk
from Configuration.constants_snake_game import FONT_LIST, GameConstants

class NameOffFrameLabelPanel:
    """
    Class for creating the labels for the game.
    """
    def __init__(self, parent, game_logger, info_callback, settings_callback, game_config):
        self.parent = parent
        self.game_logger = game_logger

        self.game_config = game_config
        self.create_label_canvas_flag = False
        self.info_callback = info_callback
        self.settings_callback = settings_callback
        self.label_canvas = None
        self.restart_game_game_size_label = None
        self.restart_game_theme_label = None
        self.label_texts = {
            "main_menu": "Main Menu",
            "classic_snake": "Classic Snake",
            "endless_snake": "Endless Snake",
            "leveling_snake": "Leveling Snake",
            "challange_choices": "Challange Choices",
            "challange_settings": "Challange Settings",
            "food_time_attack": "Challange Snake",
            "info": "Game Information",
            "info_general": "General Information",
            "info_classic": "Classic Information",
            "info_endless": "Endless Information",
            "info_leveling": "Leveling Information",
            "info_challange": "Challange Information",
            "settings": "Settings",
            "settings_reset": "Reset Settings",
            "settings_values": "Settings Values"
        }

    def create_label_with_border(self, text):
        """
        Create a label with a border.
        """
        try:
            label_border = ctk.CTkFrame(self.label_canvas, border_color='Grey10', border_width=5)
            label = ctk.CTkLabel(label_border, text=text, font=FONT_LIST[20])
            label.pack(fill="both", expand=True, padx=1, pady=1)
            label_border.pack(side="bottom", padx=10, pady=10, fill="x")
            label_border_width = label_border.winfo_width()
            self.game_logger.log_game_event(f"Label border width: {label_border_width}")
            label_border_height = label_border.winfo_height()
            self.game_logger.log_game_event(f"label_border_height: {label_border_height}")
            return label
        except AttributeError as e:
            traceback.print_exc(e)

    def create_label_canvas(self, label_type):
        """
        Create a label canvas.
        """
        if self.create_label_canvas_flag:
            self.label_canvas = ctk.CTkCanvas(self.parent, bg='Grey10', highlightthickness=5, highlightbackground='Black') # pylint: disable=line-too-long
            self.label_canvas.pack(side='bottom', fill='both')
            self.create_label_canvas_flag = False

        if label_type in self.label_texts:
            self.create_label_with_border(self.label_texts[label_type])

    def create_main_menu_label(self):
        """
        Create the main menu label.
        """
        self.create_label_canvas("main_menu")

    def create_classic_snake_label(self):
        """
        Create the classic snake label.
        """
        self.create_label_canvas("classic_snake")

    def create_endless_snake_label(self):
        """
        Create the endless snake label.
        """
        self.create_label_canvas("endless_snake")

    def create_leveling_snake_label(self):
        """
        Create the leveling snake label.
        """
        self.create_label_canvas("leveling_snake")

    def create_challange_choices_label(self):
        """
        Create the challange choices label.
        """
        self.create_label_canvas("challange_choices")

    def create_challange_settings_label(self):
        """
        Create the challange settings label.
        """
        self.create_label_canvas("challange_settings")

    def create_food_time_attack_label(self):
        """
        Create the food time attack label.
        """
        self.create_label_canvas("food_time_attack")

    def create_info_label(self):
        """
        Create the game information label.
        """
        self.create_label_canvas("info")

    def create_info_general_label(self):
        """
        Create the general information label.
        """
        self.create_label_canvas("info_general")

    def create_info_classic_label(self):
        """
        Create the classic snake information label.
        """
        self.create_label_canvas("info_classic")

    def create_info_endless_label(self):
        """
        Create the endless snake information label.
        """
        self.create_label_canvas("info_endless")

    def create_info_leveling_label(self):
        """
        Create the leveling snake information label.
        """
        self.create_label_canvas("info_leveling")

    def create_info_challange_label(self):
        """
        Create the challange snake information label.
        """
        self.create_label_canvas("info_challange")

    def create_settings_label(self):
        """
        Create the settings label.
        """
        self.create_label_canvas("settings")

    def create_settings_reset_label(self):
        """
        Create the settings reset label.
        """
        self.create_label_canvas("settings_reset")

    def create_settings_values_label(self):
        """
        Create the settings values label.
        """
        self.create_label_canvas("settings_values")

    def set_create_label_canvas_flag(self, value=True):
        """
        Set the create label canvas flag.
        """
        self.create_label_canvas_flag = value

class SettingsOptionButtonLabels:
    """
    Class for creating the labels for the settings options.
    """
    def __init__(self, game_logger, settings_canvas):
        self.game_logger = game_logger
        self.settings_canvas = settings_canvas
        self.restart_game_theme_label = None
        self.restart_game_game_size_label = None
        self.screen_label = None
        self.theme_label = None
        self.contrast_label = None
        self.snake_color_label = None
        self.high_score_label = None
        self.high_score_default_label = None
        self.snake_speed_label = None
        self.game_size_default_label = None
        self.snake_default_speed_label = None
        self.game_size_label = None
        self.keybindings_up_label = None
        self.keybindings_down_label = None
        self.keybindings_left_label = None
        self.keybindings_right_label = None
        self.keybindings_default_value_up_label = None
        self.keybindings_default_value_down_label = None
        self.keybindings_default_value_left_label = None
        self.keybindings_default_value_right_label = None
        self.start_game_label = None
        self.start_game_default_label = None
        self.pause_game_label = None
        self.pause_game_default_label = None
        self.restart_game_label = None
        self.restart_game_default_label = None
        self.reset_keybindings_label = None
        self.reset_all_settings_label = None
        self.keybinding_allready_used_label = None

        self.create_label_canvas_flag = False

        self.label_width = GameConstants.SETTINGS_LABEL_WIDTH
        self.label_height = GameConstants.SETTINGS_LABEL_HEIGHT
        self.corner_radius = GameConstants.SETTINGS_LABEL_CORNER_RADIUS
        self.anchor = GameConstants.ANCHOR

    def create_settings_labels(self):
        """
        Create the settings labels.
        """
        self.create_screen_options_label()
        self.create_theme_options_label()
        self.create_contrast_options_label()
        self.snake_color_options_label()
        self.create_high_score_label()
        self.snake_speed_options_label()
        self.game_size_options_label()
        self.create_keybinding_up_label()
        self.create_keybinding_down_label()
        self.create_keybinding_left_label()
        self.create_keybinding_right_label()
        self.create_start_game_label()
        self.create_pause_game_label()
        self.create_restart_game_label()
        self.snake_default_name_speed_label()
        self.game_size_default_name_label()
        self.create_keybinding_default_name_up_label()
        self.create_keybinding_default_name_down_label()
        self.create_keybinding_default_name_left_label()
        self.create_keybinding_default_name_right_label()
        self.create_game_default_name_label()
        self.create_pause_game_default_name_label()
        self.create_restart_game_default_name_label()

    def create_settings_reset_labels(self):
        """
        Create the settings labels.
        """
        self.create_screen_options_label()
        self.create_theme_options_label()
        self.create_contrast_options_label()
        self.snake_color_options_label()
        self.create_high_score_label()
        self.snake_speed_options_label()
        self.game_size_options_label()
        self.create_keybinding_up_label()
        self.create_keybinding_down_label()
        self.create_keybinding_left_label()
        self.create_keybinding_right_label()
        self.create_start_game_label()
        self.create_pause_game_label()
        self.create_restart_game_label()
        self.create_reset_keybindings_label()
        self.create_reset_all_settings_label()

    def create_screen_options_label(self):
        """
        Create the screen options label.
        """
        self.screen_label = ctk.CTkLabel(self.settings_canvas,
                                        width=self.label_width,
                                        height=self.label_height,
                                        corner_radius=self.corner_radius,
                                        text="Screen size",
                                        font=FONT_LIST[11],
                                        anchor=self.anchor)
        self.screen_label.place(x=200, y=10)

    def create_theme_options_label(self):
        """
        Create the theme options label.
        """
        self.theme_label = ctk.CTkLabel(self.settings_canvas,
                                        width=self.label_width,
                                        height=self.label_height,
                                        corner_radius=self.corner_radius,
                                        text="Theme",
                                        font=FONT_LIST[11],
                                        anchor=self.anchor)
        self.theme_label.place(x=400, y=10)

    def create_contrast_options_label(self):
        """
        Create the contrast options label.
        """
        self.contrast_label = ctk.CTkLabel(self.settings_canvas,
                                        width=self.label_width,
                                        height=self.label_height,
                                        corner_radius=self.corner_radius,
                                        text="Contrast",
                                        font=FONT_LIST[11],
                                        anchor=self.anchor)
        self.contrast_label.place(x=600, y=10)

    def snake_color_options_label(self):
        """
        Create the snake color options label.
        """
        self.snake_color_label = ctk.CTkLabel(self.settings_canvas,
                                        width=self.label_width,
                                        height=self.label_height,
                                        corner_radius=self.corner_radius,
                                        text="Snake Color",
                                        font=FONT_LIST[11],
                                        anchor=self.anchor)
        self.snake_color_label.place(x=800, y=10)

    def create_high_score_label(self):
        """
        Create the high score label.
        """
        self.high_score_label = ctk.CTkLabel(self.settings_canvas,
                                        width=self.label_width,
                                        height=self.label_height,
                                        corner_radius=self.corner_radius,
                                        text="High Score",
                                        font=FONT_LIST[11],
                                        anchor=self.anchor)
        self.high_score_label.place(x=600, y=160)

    def create_high_score_default_name_label(self):
        """
        Create the default high score label.
        """
        self.high_score_default_label = ctk.CTkLabel(self.settings_canvas,
                                        width=self.label_width,
                                        height=self.label_height,
                                        corner_radius=self.corner_radius,
                                        text="Default: Default",
                                        font=FONT_LIST[11],
                                        anchor=self.anchor)
        self.high_score_default_label.place(x=600, y=250)

    def snake_speed_options_label(self):
        """
        Create the snake speed options label.
        """
        self.snake_speed_label = ctk.CTkLabel(self.settings_canvas,
                                        width=self.label_width,
                                        height=self.label_height,
                                        corner_radius=self.corner_radius,
                                        text="Snake Speed",
                                        font=FONT_LIST[11],
                                        anchor=self.anchor)
        self.snake_speed_label.place(x=200, y=160)

    def snake_default_name_speed_label(self):
        """
        Create the default snake speed label.
        """
        self.snake_default_speed_label = ctk.CTkLabel(self.settings_canvas,
                                        width=self.label_width,
                                        height=self.label_height,
                                        corner_radius=self.corner_radius,
                                        text="Default: 50",
                                        font=FONT_LIST[11],
                                        anchor=self.anchor)
        self.snake_default_speed_label.place(x=200, y=250)

    def game_size_options_label(self):
        """
        Create the game size options label.
        """
        self.game_size_label = ctk.CTkLabel(self.settings_canvas,
                                        width=self.label_width,
                                        height=self.label_height,
                                        corner_radius=self.corner_radius,
                                        text="Game Size",
                                        font=FONT_LIST[11],
                                        anchor=self.anchor)
        self.game_size_label.place(x=400, y=160)

    def game_size_default_name_label(self):
        """
        Create the default game size label.
        """
        self.game_size_default_label = ctk.CTkLabel(self.settings_canvas,
                                        width=self.label_width,
                                        height=self.label_height,
                                        corner_radius=self.corner_radius,
                                        text="Default:600x600",
                                        font=FONT_LIST[11],
                                        anchor=self.anchor)
        self.game_size_default_label.place(x=400, y=250)

    def create_keybinding_up_label(self):
        """
        Create the keybinding up label.
        """
        self.keybindings_up_label = ctk.CTkLabel(self.settings_canvas,
                                        width=self.label_width,
                                        height=self.label_height,
                                        corner_radius=self.corner_radius,
                                        text="Move Up",
                                        font=FONT_LIST[11],
                                        anchor=self.anchor)
        self.keybindings_up_label.place(x=200, y=310)

    def create_keybinding_default_name_up_label(self):
        """
        Create the default keybinding up label.
        """
        self.keybindings_default_value_up_label = ctk.CTkLabel(self.settings_canvas,
                                        width=self.label_width,
                                        height=self.label_height,
                                        corner_radius=self.corner_radius,
                                        text="Default: W",
                                        font=FONT_LIST[11],
                                        anchor=self.anchor)
        self.keybindings_default_value_up_label.place(x=200, y=400)

    def create_keybinding_down_label(self):
        """
        Create the keybinding down label.
        """
        self.keybindings_down_label = ctk.CTkLabel(self.settings_canvas,
                                        width=self.label_width,
                                        height=self.label_height,
                                        corner_radius=self.corner_radius,
                                        text="Move Down",
                                        font=FONT_LIST[11],
                                        anchor=self.anchor)
        self.keybindings_down_label.place(x=600, y=310)

    def create_keybinding_default_name_down_label(self):
        """
        Create the default keybinding down label.
        """
        self.keybindings_default_value_down_label = ctk.CTkLabel(self.settings_canvas,
                                        width=self.label_width,
                                        height=self.label_height,
                                        corner_radius=self.corner_radius,
                                        text="Default: S",
                                        font=FONT_LIST[11],
                                        anchor=self.anchor)
        self.keybindings_default_value_down_label.place(x=600, y=400)

    def create_keybinding_left_label(self):
        """
        Create the keybinding left label.
        """
        self.keybindings_left_label = ctk.CTkLabel(self.settings_canvas,
                                        width=self.label_width,
                                        height=self.label_height,
                                        corner_radius=self.corner_radius,
                                        text="Move Left",
                                        font=FONT_LIST[11],
                                        anchor=self.anchor)
        self.keybindings_left_label.place(x=400, y=310)

    def create_keybinding_default_name_left_label(self):
        """
        Create the default keybinding left label.
        """
        self.keybindings_default_value_left_label = ctk.CTkLabel(self.settings_canvas,
                                        width=self.label_width,
                                        height=self.label_height,
                                        corner_radius=self.corner_radius,
                                        text="Default: A",
                                        font=FONT_LIST[11],
                                        anchor=self.anchor)
        self.keybindings_default_value_left_label.place(x=400, y=400)

    def create_keybinding_right_label(self):
        """
        Create the keybinding right label.
        """
        self.keybindings_right_label = ctk.CTkLabel(self.settings_canvas,
                                        width=self.label_width,
                                        height=self.label_height,
                                        corner_radius=self.corner_radius,
                                        text="Move Right",
                                        font=FONT_LIST[11],
                                        anchor=self.anchor)
        self.keybindings_right_label.place(x=800, y=310)

    def create_keybinding_default_name_right_label(self):
        """
        Create the default keybinding right label.
        """
        self.keybindings_default_value_right_label = ctk.CTkLabel(self.settings_canvas,
                                        width=self.label_width,
                                        height=self.label_height,
                                        corner_radius=self.corner_radius,
                                        text="Default: D",
                                        font=FONT_LIST[11],
                                        anchor=self.anchor)
        self.keybindings_default_value_right_label.place(x=800, y=400)

    def create_start_game_label(self):
        """
        Create the start game label.
        """
        self.start_game_label = ctk.CTkLabel(self.settings_canvas,
                                        width=self.label_width,
                                        height=self.label_height,
                                        corner_radius=self.corner_radius,
                                        text="Start Game",
                                        font=FONT_LIST[11],
                                        anchor=self.anchor)
        self.start_game_label.place(x=200, y=460)

    def create_game_default_name_label(self):
        """
        Create the default game label.
        """
        self.start_game_default_label = ctk.CTkLabel(self.settings_canvas,
                                        width=self.label_width,
                                        height=self.label_height,
                                        corner_radius=self.corner_radius,
                                        text="Default: Space",
                                        font=FONT_LIST[11],
                                        anchor=self.anchor)
        self.start_game_default_label.place(x=200, y=550)

    def create_pause_game_label(self):
        """
        Create the pause game label.
        """
        self.pause_game_label = ctk.CTkLabel(self.settings_canvas,
                                        width=self.label_width,
                                        height=self.label_height,
                                        corner_radius=self.corner_radius,
                                        text="Pause Game",
                                        font=FONT_LIST[11],
                                        anchor=self.anchor)
        self.pause_game_label.place(x=400, y=460)

    def create_pause_game_default_name_label(self):
        """
        Create the default pause game label.
        """
        self.pause_game_default_label = ctk.CTkLabel(self.settings_canvas,
                                        width=self.label_width,
                                        height=self.label_height,
                                        corner_radius=self.corner_radius,
                                        text="Default: Escape",
                                        font=FONT_LIST[11],
                                        anchor=self.anchor)
        self.pause_game_default_label.place(x=400, y=550)

    def create_restart_game_label(self):
        """
        Create the restart game label.
        """
        self.restart_game_label = ctk.CTkLabel(self.settings_canvas,
                                        width=self.label_width,
                                        height=self.label_height,
                                        corner_radius=self.corner_radius,
                                        text="Restart Game",
                                        font=FONT_LIST[11],
                                        anchor=self.anchor)
        self.restart_game_label.place(x=600, y=460)

    def create_restart_game_default_name_label(self):
        """
        Create the default restart game label.
        """
        self.restart_game_default_label = ctk.CTkLabel(self.settings_canvas,
                                        width=self.label_width,
                                        height=self.label_height,
                                        corner_radius=self.corner_radius,
                                        text="Default: R",
                                        font=FONT_LIST[11],
                                        anchor=self.anchor)
        self.restart_game_default_label.place(x=600, y=550)

    def create_reset_keybindings_label(self):
        """
        Create the reset Keybindings label.
        """
        self.reset_keybindings_label = ctk.CTkLabel(self.settings_canvas,
                                        width=self.label_width,
                                        height=self.label_height,
                                        corner_radius=self.corner_radius,
                                        text="Keybindings",
                                        font=FONT_LIST[11],
                                        anchor=self.anchor)
        self.reset_keybindings_label.place(x=800, y=460)

    def create_reset_all_settings_label(self):
        """
        Create the reset all keybindings label.
        """
        self.reset_all_settings_label = ctk.CTkLabel(self.settings_canvas,
                                        width=self.label_width,
                                        height=self.label_height,
                                        corner_radius=self.corner_radius,
                                        text="All Settings",
                                        font=FONT_LIST[11],
                                        anchor=self.anchor)
        self.reset_all_settings_label.place(x=800, y=160)

    def create_keybindings_allready_used_label(self):
        """
        Create the keybindings allready used label.
        """
        if not hasattr(self, 'keybinding_allready_used_label') or self.keybinding_allready_used_label is None: # pylint: disable=line-too-long
            self.keybinding_allready_used_label = ctk.CTkLabel(self.settings_canvas, # pylint: disable=line-too-long
                                                width=400,
                                                height=30,
                                                corner_radius=6,
                                                text="Keybinding already used, the keybinding will be reset.\n Please reopen this page to have the current keybindings", # pylint: disable=line-too-long
                                                font=FONT_LIST[11],
                                                anchor='w')
            self.keybinding_allready_used_label.place(x=200, y=650)

    def destroy_keybindings_allready_used_label(self):
        """
        Destroy the keybindings allready used label.
        """
        if hasattr(self, 'keybinding_allready_used_label') and self.keybinding_allready_used_label is not None: # pylint: disable=line-too-long
            self.keybinding_allready_used_label.destroy()

    def create_theme_label(self):
        """
        Create the theme label.
        """
        try:
            config_dir = path.dirname(__file__)
            config_path = path.join(config_dir, '..','config.ini')
            config = configparser.ConfigParser()
            config.read(config_path)

            current_theme = config.get('Settings', 'theme')
            initial_theme = config.get('Settings', 'initial_theme')
        except FileNotFoundError as e:
            traceback.print_exc(e)

        # Check if the 'label_needed' option exists, if not, add it
        try:
            if not config.has_option('Settings', 'label_needed_theme'):
                config.set('Settings', 'label_needed_theme', 'False')
        except FileNotFoundError as e:
            traceback.print_exc(e)

        try:
            if hasattr(self, 'restart_game_theme_label') and self.restart_game_theme_label is not None: # pylint: disable=line-too-long
                self.restart_game_theme_label.destroy()
            if current_theme != initial_theme:
                self.restart_game_theme_label = ctk.CTkLabel(self.settings_canvas,
                                                        width=160,
                                                        height=30,
                                                        corner_radius=6,
                                                        text="You need to restart to apply the theme", # pylint: disable=line-too-long
                                                        font=FONT_LIST[11],
                                                        anchor='w')
                self.restart_game_theme_label.place(x=400, y=100)
                config.set('Settings', 'label_needed_theme', 'True')
                with open('config.ini', 'w', encoding='utf-8') as configfile:
                    config.write(configfile)
            else:
                if hasattr(self, 'restart_game_theme_label') and self.restart_game_theme_label is not None: # pylint: disable=line-too-long
                    self.restart_game_theme_label.destroy()
                    del self.restart_game_theme_label
                config.set('Settings', 'label_needed_theme', 'False')
                with open('config.ini', 'w', encoding='utf-8') as configfile:
                    config.write(configfile)
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def update_initial_game_size(self):
        """
        Update the initial game size.
        """
        config_dir = path.dirname(__file__)
        config_path = path.join(config_dir, '..','config.ini')
        config = configparser.ConfigParser()
        config.read(config_path)
        # Check if the 'Settings' section exists in the config file
        if not config.has_option('Settings', 'game_size'):
            config.set('Settings', 'game_size', '500x500')

        # Set the 'initial_game_size' option to the current theme
        current_game_size = config.get('Settings', 'game_size', fallback='Default')
        config.set('Settings', 'initial_game_size', current_game_size)
        self.game_logger.log_game_event(f"Set initial game size to: {current_game_size}")

        # Write the changes to the config file
        with open('config.ini', 'w', encoding='utf-8') as configfile:
            config.write(configfile)

        self.game_logger.log_game_event(f"Updated initial_game_size in config.ini to: {current_game_size}") # pylint: disable=line-too-long
        self.game_logger.log_game_event(f"Current initial_game_size in config.ini to: {config.get('Settings', 'initial_game_size')}") # pylint: disable=line-too-long
        # The load_theme method loads a theme from a JSON file. If the file is not found, it logs an error and uses the default theme. # pylint: disable=line-too-long

    def create_game_size_label(self):
        """
        Create the game size label.
        """
        try:
            config_dir = path.dirname(__file__)
            config_path = path.join(config_dir, '..','config.ini')
            config = configparser.ConfigParser()
            config.read(config_path)

            current_game_size = config.get('Settings', 'game_size')
            initial_game_size = config.get('Settings', 'initial_game_size')
        except FileNotFoundError as e:
            traceback.print_exc(e)

        # Check if the 'label_needed' option exists, if not, add it
        try:
            if not config.has_option('Settings', 'label_needed_game_size'):
                config.set('Settings', 'label_needed_game_size', 'False')
                self.game_logger.log_game_event("Updated label_needed_game_size in config.ini to: False")
        except FileNotFoundError as e:
            traceback.print_exc(e)

        try:
            if current_game_size != initial_game_size:
                if hasattr(self, 'restart_game_game_size_label')  and self.restart_game_game_size_label is not None:
                    self.restart_game_game_size_label.destroy()
                self.restart_game_game_size_label = ctk.CTkLabel(self.settings_canvas,
                                                        width=160,
                                                        height=30,
                                                        corner_radius=6,
                                                        text="You need to restart to apply the game_size", # pylint: disable=line-too-long
                                                        font=FONT_LIST[11],
                                                        anchor='w')
                self.restart_game_game_size_label.place(x=400, y=250)
                config.set('Settings', 'label_needed_game_size', 'True')
                self.game_logger.log_game_event("Updated label_needed_game_size in config.ini to: True")
                with open('config.ini', 'w', encoding='utf-8') as configfile:
                    config.write(configfile)

            else:
                if current_game_size == initial_game_size:
                    if hasattr(self, 'restart_game_game_size_label') and self.restart_game_game_size_label is not None:
                        self.restart_game_game_size_label.destroy()
                        del self.restart_game_game_size_label
                config.set('Settings', 'label_needed_game_size', 'False')
                self.game_logger.log_game_event("Updated label_needed_game_size in config.ini to: False")
                with open('config.ini', 'w', encoding='utf-8') as configfile:
                    config.write(configfile)
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def set_create_label_canvas_flag(self, value=True):
        """
        Set the create label canvas flag.
        """
        self.create_label_canvas_flag = value


# pylint: disable=too-many-lines
