#******************************************************************
# LabelPanel file for the Snake Game
#******************************************************************

"""
This module contains the classes that create the labels for the game
"""

import configparser
import traceback
from os import path
import customtkinter as ctk
from Configuration.constants_snake_game import FONT_LIST
from Logic.leveling_system import LevelingSystem


class NameOffFrameLabelPanel:
    """
    Class for creating the labels for the game.
    """
    def __init__(self, parent, logfile, info_callback, settings_callback, game_config):
        self.parent = parent
        self.logfile = logfile

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
            "settings": "Settings"
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
            print(label_border_width)
            label_border_height = label_border.winfo_height()
            print(label_border_height)
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

    def create_settings_label(self):
        """
        Create the settings label.
        """
        self.create_label_canvas("settings")

    def set_create_label_canvas_flag(self, value=True):
        """
        Set the create label canvas flag.
        """
        self.create_label_canvas_flag = value

class SettingsOptionButtonLabels:
    """
    Class for creating the labels for the settings options.
    """
    def __init__(self, logfile, settings_canvas):
        self.logfile = logfile
        self.settings_canvas = settings_canvas
        self.restart_game_theme_label = None
        self.restart_game_game_size_label = None
        self.screen_label = None
        self.theme_label = None
        self.contrast_label = None
        self.snake_color_label = None
        self.high_score_label = None
        self.snake_speed_label = None
        self.game_size_default_label = None
        self.snake_default_speed_label = None
        self.game_size_label = None
        self.create_label_canvas_flag = False

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

    def create_screen_options_label(self):
        """
        Create the screen options label.
        """
        self.screen_label = ctk.CTkLabel(self.settings_canvas,
                                        width=160,
                                        height=30,
                                        corner_radius=6,
                                        text="Screen size",
                                        font=FONT_LIST[11],
                                        anchor='w')
        self.screen_label.place(x=200, y=10)

    def create_theme_options_label(self):
        """
        Create the theme options label.
        """
        self.theme_label = ctk.CTkLabel(self.settings_canvas,
                                        width=160,
                                        height=30,
                                        corner_radius=6,
                                        text="Theme options",
                                        font=FONT_LIST[11],
                                        anchor='w')
        self.theme_label.place(x=400, y=10)

    def create_contrast_options_label(self):
        """
        Create the contrast options label.
        """
        self.contrast_label = ctk.CTkLabel(self.settings_canvas,
                                           width=160,
                                           height=30,
                                           corner_radius=6,
                                           text="Dark or Light",
                                           font=FONT_LIST[11],
                                           anchor='w'
                                           )
        self.contrast_label.place(x=600, y=10)

    def snake_color_options_label(self):
        """
        Create the snake color options label.
        """
        self.snake_color_label = ctk.CTkLabel(self.settings_canvas,
                                              width=160,
                                              height=30,
                                              corner_radius=6,
                                              text="Snake Color",
                                              font=FONT_LIST[11],
                                              anchor='w'
                                              )
        self.snake_color_label.place(x=800, y=10)

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
            if current_theme != initial_theme:
                if hasattr(self, 'restart_game_theme_label'):
                    self.restart_game_theme_label.destroy()
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
                if hasattr(self, 'restart_game_theme_label'):
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
        self.logfile.log_game_event(current_game_size)
        config.set('Settings', 'initial_game_size', current_game_size)

        # Write the changes to the config file
        with open('config.ini', 'w', encoding='utf-8') as configfile:
            config.write(configfile)

        self.logfile.log_game_event(f"Updated initial_game_size in config.ini to {current_game_size}") # pylint: disable=line-too-long
        self.logfile.log_game_event(f"Current initial_game_size in config.ini: {config.get('Settings', 'initial_game_size')}") # pylint: disable=line-too-long
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
        except FileNotFoundError as e:
            traceback.print_exc(e)

        try:
            if current_game_size != initial_game_size:
                if hasattr(self, 'restart_game_game_size_label'):
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
                with open('config.ini', 'w', encoding='utf-8') as configfile:
                    config.write(configfile)

            else:
                if current_game_size == initial_game_size:
                    if hasattr(self, 'restart_game_game_size_label'):
                        self.restart_game_game_size_label.destroy()
                        del self.restart_game_game_size_label
                config.set('Settings', 'label_needed_game_size', 'False')
                with open('config.ini', 'w', encoding='utf-8') as configfile:
                    config.write(configfile)
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def create_high_score_label(self):
        """
        Create the high score label.
        """
        self.high_score_label = ctk.CTkLabel(self.settings_canvas,
                                             width=160,
                                             height=30,
                                             corner_radius=6,
                                             text="High Score",
                                             font=FONT_LIST[11],
                                             anchor='w'
                                             )
        self.high_score_label.place(x=1000, y=10)

    def snake_speed_options_label(self):
        """
        Create the snake speed options label.
        """
        self.snake_speed_label = ctk.CTkLabel(self.settings_canvas,
                                              width=160,
                                              height=30,
                                              corner_radius=6,
                                              text="Snake Speed",
                                              font=FONT_LIST[11],
                                              anchor='w'
                                              )
        self.snake_speed_label.place(x=200, y=160)

        self.snake_default_speed_label = ctk.CTkLabel(self.settings_canvas,
                                                         width=160,
                                                         height=30,
                                                         corner_radius=6,
                                                         text="Default: 50",
                                                         font=FONT_LIST[11],
                                                         anchor='w'
                                                         )
        self.snake_default_speed_label.place(x=200, y=250)

    def game_size_options_label(self):
        """
        Create the game size options label.
        """
        self.game_size_label = ctk.CTkLabel(self.settings_canvas,
                                            width=160,
                                            height=30,
                                            corner_radius=6,
                                            text="Game Size",
                                            font=FONT_LIST[11],
                                            anchor='w'
                                            )
        self.game_size_label.place(x=400, y=160)

        self.game_size_default_label = ctk.CTkLabel(self.settings_canvas,
                                                         width=160,
                                                         height=30,
                                                         corner_radius=6,
                                                         text="Default:600x600",
                                                         font=FONT_LIST[11],
                                                         anchor='w'
                                                         )
        self.game_size_default_label.place(x=400, y=250)

    def set_create_label_canvas_flag(self, value=True):
        """
        Set the create label canvas flag.
        """
        self.create_label_canvas_flag = value

class GameLabelsPanel:
    """
    Class for creating the labels for the game.
    """
    def __init__(self, snake_canvas, logfile, game_config):
        self.snake_canvas = snake_canvas
        self.logfile = logfile
        self.game_config = game_config
        self.width = game_config.GAME_WIDTH
        self.height = game_config.GAME_HEIGHT

        self.high_score_label_needed = None
        self.score_label_needed = None

        self.classic_score_label = None
        self.classic_high_score_label = None
        self.classic_time_label = None
        self.classic_high_score_time_label = None
        self.classic_high_scores_label = None
        self.classic_snake_length_label = None
        self.classic_high_score_snake_length_label = None

        self.endless_score_label = None
        self.endless_high_score_label = None
        self.endless_time_label = None
        self.endless_high_score_time_label = None
        self.endless_high_scores_label = None
        self.endless_snake_length_label = None
        self.endless_high_score_snake_length_label = None
        self.endless_special_score_label = None
        self.endless_special_high_score_label = None
        self.endless_shorten_score_label = None
        self.endless_shorten_high_score_label = None

        self.leveling_score_label = None
        self.leveling_high_score_label = None
        self.leveling_time_label = None
        self.leveling_high_score_time_label = None
        self.leveling_high_scores_label = None
        self.leveling_snake_length_label = None
        self.leveling_high_score_snake_length_label = None
        self.leveling_xp_score_label = None
        self.leveling_xp_high_score_label = None
        self.leveling_level_score_label = None
        self.leveling_level_high_score_label = None

        self.challange_score_label = None
        self.challange_high_score_label = None

        self.classic_score_label_ = None
        self.classic_high_score_label_ = None
        self.classic_time_label_ = None
        self.classic_high_score_time_label_ = None
        self.classic_high_scores_label_ = None
        self.classic_snake_length_label_ = None
        self.classic_high_score_snake_length_label_ = None

        self.endless_score_label_ = None
        self.endless_high_score_label_ = None
        self.endless_time_label_ = None
        self.endless_high_score_time_label_ = None
        self.endless_high_scores_label_ = None
        self.endless_snake_length_label_ = None
        self.endless_high_score_snake_length_label_ = None
        self.endless_special_score_label_ = None
        self.endless_special_high_score_label_ = None
        self.endless_shorten_score_label_ = None
        self.endless_shorten_high_score_label_ = None

        self.leveling_score_label_ = None
        self.leveling_high_score_label_ = None
        self.leveling_time_label_ = None
        self.leveling_high_score_time_label_ = None
        self.leveling_high_scores_label_ = None
        self.leveling_snake_length_label_ = None
        self.leveling_high_score_snake_length_label_ = None
        self.leveling_xp_score_label_ = None
        self.leveling_xp_high_score_label_ = None
        self.leveling_level_score_label_ = None
        self.leveling_level_high_score_label_ = None

        self.challange_score_label_ = None
        self.challange_high_score_label_ = None

        self.classic_score_label_flag = False
        self.classic_time_label_flag = False
        self.classic_high_score_label_flag = False
        self.classic_high_score_time_label_flag = False

        self.endless_score_label_flag = False
        self.endless_time_label_flag = False
        self.endless_high_score_label_flag = False
        self.endless_high_score_time_label_flag = False
        self.endless_special_score_label_flag = False
        self.endless_shorten_score_label_flag = False

        self.leveling_score_label_flag = False
        self.leveling_time_label_flag = False
        self.leveling_high_score_label_flag = False
        self.leveling_high_score_time_label_flag = False

        self.challange_score_label_flag = False
        self.challange_high_score_label_flag = False

        self.leveling_system = LevelingSystem()

        try:
            self.config_dir = path.dirname(__file__)
            self.config_path = path.join(self.config_dir, '..', 'config.ini')
            self.config = configparser.RawConfigParser()
            self.config.read(self.config_path)
        except FileNotFoundError as e:
            traceback.print_exc(e)

        #Get the score from the config file
        try:
            self.classic_score_label_ = 0
            self.config.set('Classic_Snake_Values', 'score', '0')
            self.classic_time_label_ = 0
            self.config.set('Classic_Snake_Values', 'time_score', '0')
            self.classic_snake_length_label_ = 0
            self.config.set('Classic_Snake_Values', 'snake_length', '0')
            self.endless_score_label_ = 0
            self.config.set('Endless_Snake_Values', 'score', '0')
            self.endless_time_label_ = 0
            self.config.set('Endless_Snake_Values', 'time_score', '0')
            self.endless_snake_length_label_ = 0
            self.config.set('Endless_Snake_Values', 'snake_length', '0')
            self.endless_special_score_label_ = 0
            self.config.set('Endless_Snake_Values', 'special_score', '0')
            self.endless_shorten_score_label_ = 0
            self.config.set('Endless_Snake_Values', 'shorten_score', '0')
            self.leveling_score_label_ = 0
            self.config.set('Leveling_Snake_Values', 'score', '0')
            self.leveling_time_label_ = 0
            self.config.set('Leveling_Snake_Values', 'time_score', '0')
            self.leveling_snake_length_label_ = 0
            self.config.set('Leveling_Snake_Values', 'snake_length', '0')
            self.challange_score_label_ = 0
            self.config.set('food_time_attack_Values', 'score', '0')
            with open('config.ini', 'w', encoding='utf-8') as configfile:
                self.config.write(configfile)
        except FileNotFoundError as e:
            traceback.print_exc(e)


    def classic_create_game_labels(self):
        """
        Create the game labels for the classic snake game.
        """
        self.config.read(self.config_path)
        self.high_score_label_needed = self.config.get('Settings', 'label_needed_high_score', fallback='Default') # pylint: disable=line-too-long

        self.classic_create_score_label()
        self.classic_create_time_label()
        self.classic_create_snake_length_label()
        if self.high_score_label_needed == 'True' or self.high_score_label_needed == 'Default':
            self.classic_create_high_score_label()
            self.classic_create_high_score_time_label()
            self.classic_create_high_scores_label()
            self.classic_create_high_score_snake_length_label()

    def classic_update_high_score_labels(self):
        """
        Update the high score labels for the classic snake game.
        """
        self.config.read(self.config_path)
        self.high_score_label_needed = self.config.get('Settings', 'label_needed_high_score', fallback='Default') # pylint: disable=line-too-long

        if self.high_score_label_needed == 'True' or self.high_score_label_needed == 'Default':
            self.classic_update_high_score_label()
            self.classic_update_high_score_time_label()
            self.classic_update_high_score_snake_length_label()

    def classic_update_game_labels(self):
        """
        Update the game labels for the classic snake game.
        """
        self.classic_update_score_label()
        self.classic_update_time_label()
        self.classic_update_snake_length_label()

    def classic_create_score_label(self):
        """
        Create the score label for the classic snake game.
        """
        self.classic_score_label = ctk.CTkLabel(self.snake_canvas,
                                            height=30,
                                            width=275,
                                            corner_radius=10,
                                            text=f"Score:{self.classic_score_label_} ",
                                            font=FONT_LIST[11],
                                            bg_color='grey20',
                                            anchor='w'
                                            )
        self.classic_score_label.place(x=200, y=50)

    def classic_update_score_label(self):
        """
        Update the score label for the classic snake game.
        """
        try:
            self.config_dir = path.dirname(__file__)
            self.config_path = path.join(self.config_dir, '..', 'config.ini')
            self.config = configparser.RawConfigParser()
            self.config.read(self.config_path)
            self.classic_score_label_ = self.config.get('Classic_Snake_Values', 'score', fallback='0') # pylint: disable=line-too-long
            #update the score label on the screen
            self.classic_score_label.configure(text=f"Score: {self.classic_score_label_} ") # pylint: disable=line-too-long
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def classic_create_high_score_label(self):
        """
        Create the high score label for the classic snake game.
        """
        self.classic_high_score_label = ctk.CTkLabel(self.snake_canvas,
                                             height=30,
                                             width=275,
                                             corner_radius=10,
                                             text=f"Score: {self.classic_score_label_} ",
                                             font=FONT_LIST[11],
                                             bg_color='grey20',
                                             anchor='w'
                                             )
        self.classic_high_score_label.place(x=200, y=550)

    def classic_update_high_score_label(self):
        """
        Update the high score label for the classic snake game.
        """
        try:
            self.config_dir = path.dirname(__file__)
            self.config_path = path.join(self.config_dir, '..', 'config.ini')
            self.config = configparser.RawConfigParser()
            self.config.read(self.config_path)
            self.classic_high_score_label_ = self.config.get('Classic_Snake_Values', 'high_score', fallback='0') # pylint: disable=line-too-long
            #update the high score label on the screen
            self.classic_high_score_label.configure(text=f"Score: {self.classic_high_score_label_} ") # pylint: disable=line-too-long
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def classic_create_time_label(self):
        """
        Create the time label for the classic snake game.
        """
        self.classic_time_label = ctk.CTkLabel(self.snake_canvas,
                                        height=30,
                                        width=275,
                                        corner_radius=10,
                                        text=f"Time: {self.classic_score_label_} Seconds",
                                        font=FONT_LIST[11],
                                        bg_color='grey20',
                                        anchor='w'
                                        )
        self.classic_time_label.place(x=200, y=100)

    def classic_update_time_label(self):
        """
        Update the time label for the classic snake game.
        """
        try:
            self.config_dir = path.dirname(__file__)
            self.config_path = path.join(self.config_dir, '..', 'config.ini')
            self.config = configparser.RawConfigParser()
            self.config.read(self.config_path)
            self.classic_time_label_ = self.config.get('Classic_Snake_Values', 'time_score', fallback='0') # pylint: disable=line-too-long
            #update the time label on the screen
            self.classic_time_label.configure(text=f"Time: {self.classic_time_label_} Seconds")
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def classic_create_high_score_time_label(self):
        """
        Create the high score time label for the classic snake game.
        """
        self.classic_high_score_time_label = ctk.CTkLabel(self.snake_canvas,
                                                    height=30,
                                                    width=275,
                                                    corner_radius=10,
                                                    text=f"Score Time: {self.classic_score_label_} Seconds", # pylint: disable=line-too-long
                                                    font=FONT_LIST[11],
                                                    bg_color='grey20',
                                                    anchor='w'
                                                    )
        self.classic_high_score_time_label.place(x=200, y=600)

    def classic_update_high_score_time_label(self):
        """
        Update the high score time label for the classic snake game.
        """
        try:
            self.config_dir = path.dirname(__file__)
            self.config_path = path.join(self.config_dir, '..', 'config.ini')
            self.config = configparser.RawConfigParser()
            self.config.read(self.config_path)
            self.classic_high_score_time_label_ = self.config.get('Classic_Snake_Values', 'high_score_time', fallback='0') # pylint: disable=line-too-long
            #update the high score time label on the screen
            self.classic_high_score_time_label.configure(text=f"Score Time: {self.classic_high_score_time_label_} Seconds") # pylint: disable=line-too-long
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def classic_create_snake_length_label(self):
        """
        Create the snake length label for the classic snake game.
        """
        self.classic_snake_length_label = ctk.CTkLabel(self.snake_canvas,
                                                height=30,
                                                width=275,
                                                corner_radius=10,
                                                text="Snake Length:",
                                                font=FONT_LIST[11],
                                                bg_color='grey20',
                                                anchor='w'
                                                )
        self.classic_snake_length_label.place(x=200, y=150)

    def classic_update_snake_length_label(self):
        """
        Update the snake length label for the classic snake game.
        """
        try:
            self.config_dir = path.dirname(__file__)
            self.config_path = path.join(self.config_dir, '..', 'config.ini')
            self.config = configparser.RawConfigParser()
            self.config.read(self.config_path)
            self.classic_snake_length_label_ = self.config.get('Classic_Snake_Values', 'snake_length', fallback='0') # pylint: disable=line-too-long
            #update the high score time label on the screen
            self.classic_snake_length_label.configure(text=f"Snake Length: {self.classic_snake_length_label_}") # pylint: disable=line-too-long
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def classic_create_high_score_snake_length_label(self):
        """
        Create the high score snake length label for the classic snake game.
        """
        self.classic_high_score_snake_length_label = ctk.CTkLabel(self.snake_canvas,
                                                            height=30,
                                                            width=275,
                                                            corner_radius=10,
                                                            text="Snake Length:",
                                                            font=FONT_LIST[11],
                                                            bg_color='grey20',
                                                            anchor='w'
                                                            )
        self.classic_high_score_snake_length_label.place(x=200, y=650)

    def classic_update_high_score_snake_length_label(self):
        """
        Update the high score snake length label for the classic snake game.
        """
        try:
            self.config_dir = path.dirname(__file__)
            self.config_path = path.join(self.config_dir, '..', 'config.ini')
            self.config = configparser.RawConfigParser()
            self.config.read(self.config_path)
            self.classic_high_score_snake_length_label_ = self.config.get('Classic_Snake_Values', 'snake_length_high_score', fallback='0') # pylint: disable=line-too-long
            #update the high score time label on the screen
            self.classic_high_score_snake_length_label.configure(text=f"Snake Length: {self.classic_high_score_snake_length_label_}") # pylint: disable=line-too-long
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def classic_create_high_scores_label(self):
        """
        Create the high scores label for the classic snake game.
        """
        self.classic_high_scores_label = ctk.CTkLabel(self.snake_canvas,
                                                height=30,
                                                width=275,
                                                corner_radius=10,
                                                text="High Scores:",
                                                font=FONT_LIST[11],
                                                bg_color='grey20',
                                                anchor='w'
                                                )
        self.classic_high_scores_label.place(x=200, y=500)

    def classic_reset_labels(self):
        """
        Reset the labels for the classic snake game.
        """
        self.classic_score_label.configure(text='0')
        self.classic_time_label.configure(text='0')

    def classic_delete_labels(self):
        """
        Delete the labels for the classic snake game.
        """
        try:
            if self.classic_score_label is not None:
                self.classic_score_label.destroy()
            if self.classic_time_label is not None:
                self.classic_time_label.destroy()
            if self.classic_high_score_label is not None:
                self.classic_high_score_label.destroy()
            if self.classic_high_score_time_label is not None:
                self.classic_high_score_time_label.destroy()
            if self.classic_high_scores_label is not None:
                self.classic_high_scores_label.destroy()
            if self.classic_snake_length_label is not None:
                self.classic_snake_length_label.destroy()
            if self.classic_high_score_snake_length_label is not None:
                self.classic_high_score_snake_length_label.destroy()
        except ValueError as e:
            traceback.print_exc(e)


    def endless_create_game_labels(self):
        """
        Create the game labels for the endless snake game.
        """
        self.config.read(self.config_path)
        self.high_score_label_needed = self.config.get('Settings', 'label_needed_high_score', fallback='Default') # pylint: disable=line-too-long
        self.endless_create_score_label()
        self.endless_create_time_label()
        self.endless_create_snake_length_label()
        self.endless_create_special_score_label()
        self.endless_create_shorten_score_label()

        if self.high_score_label_needed == 'True' or self.high_score_label_needed == 'Default':
            self.endless_create_high_score_label()
            self.endless_create_high_score_time_label()
            self.endless_create_high_scores_label()
            self.endless_create_high_score_snake_length_label()
            self.endless_create_special_high_score_label()
            self.endless_create_shorten_high_score_label()

    def endless_update_high_score_labels(self):
        """
        Update the high score labels for the endless snake game.
        """

        self.config.read(self.config_path)
        self.high_score_label_needed = self.config.get('Settings', 'label_needed_high_score', fallback='Default') # pylint: disable=line-too-long
        if self.high_score_label_needed == 'True' or self.high_score_label_needed == 'Default': # pylint: disable=line-too-long
            self.endless_update_high_score_label()
            self.endless_update_high_score_time_label()
            self.endless_update_high_score_snake_length_label()
            self.endless_update_special_high_score_label()
            self.endless_update_shorten_high_score_label()

    def endless_update_game_labels(self):
        """
        Update the game labels for the endless snake game.
        """
        self.endless_update_score_label()
        self.endless_update_time_label()
        self.endless_update_snake_length_label()
        self.endless_update_special_score_label()
        self.endless_update_shorten_score_label()

    def endless_create_high_scores_label(self):
        """
        Create the high scores label for the endless snake game.
        """
        self.endless_high_scores_label = ctk.CTkLabel(self.snake_canvas,
                                                height=30,
                                                width=275,
                                                corner_radius=10,
                                                text="High Scores:",
                                                font=FONT_LIST[11],
                                                bg_color='grey20',
                                                anchor='w'
                                                )
        self.endless_high_scores_label.place(x=200, y=400)

    def endless_create_score_label(self):
        """
        Create the score label for the endless snake game.
        """
        self.endless_score_label = ctk.CTkLabel(self.snake_canvas,
                                            height=30,
                                            width=275,
                                            corner_radius=10,
                                            text=f"Score:{self.endless_score_label_}",
                                            font=FONT_LIST[11],
                                            bg_color='grey20',
                                            anchor='w'
                                            )
        self.endless_score_label.place(x=200, y=50)

    def endless_update_score_label(self):
        """
        Update the score label for the endless snake game.
        """
        try:
            self.config_dir = path.dirname(__file__)
            self.config_path = path.join(self.config_dir, '..', 'config.ini')
            self.config = configparser.RawConfigParser()
            self.config.read(self.config_path)
            self.endless_score_label_ = self.config.get('Endless_Snake_Values', 'score', fallback='0') # pylint: disable=line-too-long
            #update the score label on the screen
            self.endless_score_label.configure(text=f"Score: {self.endless_score_label_} ")
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def endless_create_high_score_label(self):
        """
        Create the high score label for the endless snake game.
        """
        self.endless_high_score_label = ctk.CTkLabel(self.snake_canvas,
                                             height=30,
                                             width=275,
                                             corner_radius=10,
                                             text=f"Score: {self.endless_score_label_} ",
                                             font=FONT_LIST[11],
                                             bg_color='grey20',
                                             anchor='w'
                                             )
        self.endless_high_score_label.place(x=200, y=450)

    def endless_update_high_score_label(self):
        """
        Update the high score label for the endless snake game.
        """
        try:
            self.config_dir = path.dirname(__file__)
            self.config_path = path.join(self.config_dir, '..', 'config.ini')
            self.config = configparser.RawConfigParser()
            self.config.read(self.config_path)
            self.endless_high_score_label_ = self.config.get('Endless_Snake_Values', 'high_score', fallback='0') # pylint: disable=line-too-long
            #update the high score label on the screen
            self.endless_high_score_label.configure(text=f"Score: {self.endless_high_score_label_} ") # pylint: disable=line-too-long
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def endless_create_time_label(self):
        """
        Create the time label for the endless snake game.
        """
        self.endless_time_label = ctk.CTkLabel(self.snake_canvas,
                                        height=30,
                                        width=275,
                                        corner_radius=10,
                                        text=f"Time: {self.endless_time_label_} Seconds",
                                        font=FONT_LIST[11],
                                        bg_color='grey20',
                                        anchor='w'
                                        )
        self.endless_time_label.place(x=200, y=100)

    def endless_update_time_label(self):
        """
        Update the time label for the endless snake game.
        """
        try:
            self.config_dir = path.dirname(__file__)
            self.config_path = path.join(self.config_dir, '..', 'config.ini')
            self.config = configparser.RawConfigParser()
            self.config.read(self.config_path)
            self.endless_time_label_ = self.config.get('Endless_Snake_Values', 'time_score', fallback='0') # pylint: disable=line-too-long
            #update the time label on the screen
            self.endless_time_label.configure(text=f"Time: {self.endless_time_label_} Seconds")
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def endless_create_high_score_time_label(self):
        """
        Create the high score time label for the endless snake game.
        """
        self.endless_high_score_time_label = ctk.CTkLabel(self.snake_canvas,
                                                    height=30,
                                                    width=275,
                                                    corner_radius=10,
                                                    text=f"Score Time: {self.endless_time_label_} Seconds", # pylint: disable=line-too-long
                                                    font=FONT_LIST[11],
                                                    bg_color='grey20',
                                                    anchor='w'
                                                    )
        self.endless_high_score_time_label.place(x=200, y=500)

    def endless_update_high_score_time_label(self):
        """
        Update the high score time label for the endless snake game.
        """
        try:
            self.config_dir = path.dirname(__file__)
            self.config_path = path.join(self.config_dir, '..', 'config.ini')
            self.config = configparser.RawConfigParser()
            self.config.read(self.config_path)
            self.endless_high_score_time_label_ = self.config.get('Endless_Snake_Values', 'high_score_time', fallback='0') # pylint: disable=line-too-long
            #update the high score time label on the screen
            self.endless_high_score_time_label.configure(text=f"Score Time: {self.endless_high_score_time_label_} Seconds") # pylint: disable=line-too-long
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def endless_create_snake_length_label(self):
        """
        Create the snake length label for the endless snake game.
        """
        self.endless_snake_length_label = ctk.CTkLabel(self.snake_canvas,
                                                height=30,
                                                width=275,
                                                corner_radius=10,
                                                text="Snake Length:",
                                                font=FONT_LIST[11],
                                                bg_color='grey20',
                                                anchor='w'
                                                )
        self.endless_snake_length_label.place(x=200, y=150)

    def endless_update_snake_length_label(self):
        """
        Update the snake length label for the endless snake game.
        """
        try:
            self.config_dir = path.dirname(__file__)
            self.config_path = path.join(self.config_dir, '..', 'config.ini')
            self.config = configparser.RawConfigParser()
            self.config.read(self.config_path)
            self.endless_snake_length_label_ = self.config.get('Endless_Snake_Values', 'snake_length', fallback='0') # pylint: disable=line-too-long
            #update the high score time label on the screen
            self.endless_snake_length_label.configure(text=f"Snake Length: {self.endless_snake_length_label_}") # pylint: disable=line-too-long
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def endless_create_high_score_snake_length_label(self):
        """
        Create the high score snake length label for the endless snake game.
        """
        self.endless_high_score_snake_length_label = ctk.CTkLabel(self.snake_canvas,
                                                            height=30,
                                                            width=275,
                                                            corner_radius=10,
                                                            text="Snake Length:",
                                                            font=FONT_LIST[11],
                                                            bg_color='grey20',
                                                            anchor='w'
                                                            )
        self.endless_high_score_snake_length_label.place(x=200, y=550)

    def endless_update_high_score_snake_length_label(self):
        """
        Update the high score snake length label for the endless snake game.
        """
        try:
            self.config_dir = path.dirname(__file__)
            self.config_path = path.join(self.config_dir, '..', 'config.ini')
            self.config = configparser.RawConfigParser()
            self.config.read(self.config_path)
            self.endless_high_score_snake_length_label_ = self.config.get('Endless_Snake_Values', 'snake_length_high_score', fallback='0') # pylint: disable=line-too-long
            #update the high score time label on the screen
            self.endless_high_score_snake_length_label.configure(text=f"Snake Length: {self.endless_high_score_snake_length_label_}") # pylint: disable=line-too-long
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def endless_create_special_score_label(self):
        """
        Create the special score label for the endless snake game.
        """
        self.endless_special_score_label = ctk.CTkLabel(self.snake_canvas,
                                            height=30,
                                            width=275,
                                            corner_radius=10,
                                            text=f"Special Score:{self.endless_special_score_label} ", # pylint: disable=line-too-long
                                            font=FONT_LIST[11],
                                            bg_color='grey20',
                                            anchor='w'
                                            )
        self.endless_special_score_label.place(x=200, y=200)

    def endless_update_special_score_label(self):
        """
        Update the special score label for the endless snake game.
        """
        try:
            self.config_dir = path.dirname(__file__)
            self.config_path = path.join(self.config_dir, '..', 'config.ini')
            self.config = configparser.RawConfigParser()
            self.config.read(self.config_path)
            self.endless_special_score_label_ = self.config.get('Endless_Snake_Values', 'special_score', fallback='0') # pylint: disable=line-too-long
            #update the score label on the screen
            self.endless_special_score_label.configure(text=f"Special Score: {self.endless_special_score_label_} ") # pylint: disable=line-too-long
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def endless_create_special_high_score_label(self):
        """
        Create the special high score label for the endless snake game.
        """
        self.endless_special_high_score_label = ctk.CTkLabel(self.snake_canvas,
                                             height=30,
                                             width=275,
                                             corner_radius=10,
                                             text=f"Special Score: {self.endless_special_high_score_label} ", # pylint: disable=line-too-long
                                             font=FONT_LIST[11],
                                             bg_color='grey20',
                                             anchor='w'
                                             )
        self.endless_special_high_score_label.place(x=200, y=600)

    def endless_update_special_high_score_label(self):
        """
        Update the special high score label for the endless snake game.
        """
        try:
            self.config_dir = path.dirname(__file__)
            self.config_path = path.join(self.config_dir, '..', 'config.ini')
            self.config = configparser.RawConfigParser()
            self.config.read(self.config_path)
            self.endless_special_high_score_label_ = self.config.get('Endless_Snake_Values', 'special_score_high_score', fallback='0') # pylint: disable=line-too-long
            #update the high score label on the screen
            self.endless_special_high_score_label.configure(text=f"Special Score: {self.endless_special_high_score_label_} ") # pylint: disable=line-too-long
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def endless_create_shorten_score_label(self):
        """
        Create the shorten score label for the endless snake game.
        """
        self.endless_shorten_score_label = ctk.CTkLabel(self.snake_canvas,
                                                  height=30,
                                                  width=275,
                                                    corner_radius=10,
                                                    text=f"Shorten Score: {self.endless_shorten_score_label} ", # pylint: disable=line-too-long
                                                    font=FONT_LIST[11],
                                                    bg_color='grey20',
                                                    anchor='w'
                                                    )
        self.endless_shorten_score_label.place(x=200, y=250)

    def endless_update_shorten_score_label(self):
        """
        Update the shorten score label for the endless snake game.
        """
        try:
            self.config_dir = path.dirname(__file__)
            self.config_path = path.join(self.config_dir, '..', 'config.ini')
            self.config = configparser.RawConfigParser()
            self.config.read(self.config_path)
            self.endless_shorten_score_label_ = self.config.get('Endless_Snake_Values', 'shorten_score', fallback='0') # pylint: disable=line-too-long
            #update the high score label on the screen
            self.endless_shorten_score_label.configure(text=f"Shorten Score: {self.endless_shorten_score_label_} ") # pylint: disable=line-too-long
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def endless_create_shorten_high_score_label(self):
        """
        Create the shorten high score label for the endless snake game.
        """
        self.endless_shorten_high_score_label = ctk.CTkLabel(self.snake_canvas,
                                                  height=30,
                                                  width=275,
                                                    corner_radius=10,
                                                    text=f"Shorten Score: {self.endless_shorten_high_score_label} ", # pylint: disable=line-too-long
                                                    font=FONT_LIST[11],
                                                    bg_color='grey20',
                                                    anchor='w'
                                                    )
        self.endless_shorten_high_score_label.place(x=200, y=650)

    def endless_update_shorten_high_score_label(self):
        """
        Update the shorten high score label for the endless snake game.
        """
        try:
            self.config_dir = path.dirname(__file__)
            self.config_path = path.join(self.config_dir, '..', 'config.ini')
            self.config = configparser.RawConfigParser()
            self.config.read(self.config_path)
            self.endless_shorten_high_score_label_ = self.config.get('Endless_Snake_Values', 'shorten_snake_high_score', fallback='0') # pylint: disable=line-too-long
            #update the high score label on the screen
            self.endless_shorten_high_score_label.configure(text=f"Shorten Score: {self.endless_shorten_high_score_label_} ") # pylint: disable=line-too-long
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def endless_reset_labels(self):
        """
        Reset the labels for the endless snake game.
        """
        self.endless_score_label.configure(text='0')
        self.endless_time_label.configure(text='0')

    def endless_delete_labels(self):
        """
        Delete the labels for the endless snake game.
        """
        try:
            if self.endless_score_label is not None:
                self.endless_score_label.destroy()
            if self.endless_time_label is not None:
                self.endless_time_label.destroy()
            if self.endless_high_score_label is not None:
                self.endless_high_score_label.destroy()
            if self.endless_high_score_time_label is not None:
                self.endless_high_score_time_label.destroy()
            if self.endless_high_scores_label is not None:
                self.endless_high_scores_label.destroy()
            if self.endless_snake_length_label is not None:
                self.endless_snake_length_label.destroy()
            if self.endless_high_score_snake_length_label is not None:
                self.endless_high_score_snake_length_label.destroy()
            if self.endless_special_score_label is not None:
                self.endless_special_score_label.destroy()
            if self.endless_special_high_score_label is not None:
                self.endless_special_high_score_label.destroy()
            if self.endless_shorten_score_label is not None:
                self.endless_shorten_score_label.destroy()
            if self.endless_shorten_high_score_label is not None:
                self.endless_shorten_high_score_label.destroy()
        except ValueError as e:
            traceback.print_exc(e)


    def leveling_create_game_labels(self):
        """
        Create the game labels for the leveling snake game.
        """
        self.config.read(self.config_path)
        self.high_score_label_needed = self.config.get('Settings', 'label_needed_high_score', fallback='Default') # pylint: disable=line-too-long

        self.leveling_create_score_label()
        self.leveling_create_time_label()
        self.leveling_create_snake_length_label()
        self.leveling_create_xp_label()
        self.leveling_create_level_label()

        if self.high_score_label_needed == 'True' or self.high_score_label_needed == 'Default':
            self.leveling_create_high_score_label()
            self.leveling_create_high_score_time_label()
            self.leveling_create_high_scores_label()
            self.leveling_create_high_score_snake_length_label()
            self.leveling_create_xp_high_score_label()
            self.leveling_create_level_high_score_label()

    def leveling_update_high_score_labels(self):
        """
        Update the high score labels for the leveling snake game.
        """
        self.config.read(self.config_path)
        self.high_score_label_needed = self.config.get('Settings', 'label_needed_high_score', fallback='Default') # pylint: disable=line-too-long

        if self.high_score_label_needed == 'True' or self.high_score_label_needed == 'Default':
            self.leveling_update_high_score_label()
            self.leveling_update_high_score_time_label()
            self.leveling_update_high_score_snake_length_label()
            self.leveling_update_xp_high_score_label()
            self.leveling_update_level_high_score_label()

    def leveling_create_high_scores_label(self):
        """
        Create the high scores label for the leveling snake game.
        """
        self.leveling_high_scores_label = ctk.CTkLabel(self.snake_canvas,
                                                height=30,
                                                width=275,
                                                corner_radius=10,
                                                text="High Scores:",
                                                font=FONT_LIST[11],
                                                bg_color='grey20',
                                                anchor='w'
                                                )
        self.leveling_high_scores_label.place(x=200, y=300)

    def leveling_update_game_labels(self):
        """
        Update the game labels for the leveling snake game.
        """
        self.leveling_update_score_label()
        self.leveling_update_time_label()
        self.leveling_update_snake_length_label()
        self.leveling_update_xp_label()
        self.leveling_update_level_label()

    def leveling_create_score_label(self):
        """
        Create the score label for the leveling snake game.
        """
        self.leveling_score_label = ctk.CTkLabel(self.snake_canvas,
                                            height=30,
                                            width=275,
                                            corner_radius=10,
                                            text=f"Score:{self.leveling_score_label_} ",
                                            font=FONT_LIST[11],
                                            bg_color='grey20',
                                            anchor='w'
                                            )
        self.leveling_score_label.place(x=200, y=50)

    def leveling_update_score_label(self):
        """
        Update the score label for the leveling snake game.
        """
        try:
            self.config_dir = path.dirname(__file__)
            self.config_path = path.join(self.config_dir, '..', 'config.ini')
            self.config = configparser.RawConfigParser()
            self.config.read(self.config_path)
            self.leveling_score_label_ = self.config.get('Leveling_Snake_Values', 'score', fallback='0') # pylint: disable=line-too-long
            #update the score label on the screen
            self.leveling_score_label.configure(text=f"Score: {self.leveling_score_label_} ") # pylint: disable=line-too-long
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def leveling_create_high_score_label(self):
        """
        Create the high score label for the leveling snake game.
        """
        self.leveling_high_score_label = ctk.CTkLabel(self.snake_canvas,
                                             height=30,
                                             width=275,
                                             corner_radius=10,
                                             text=f"Score: {self.leveling_score_label_} ", # pylint: disable=line-too-long
                                             font=FONT_LIST[11],
                                             bg_color='grey20',
                                             anchor='w'
                                             )
        self.leveling_high_score_label.place(x=200, y=350)

    def leveling_update_high_score_label(self):
        """
        Update the high score label for the leveling snake game.
        """
        try:
            self.config_dir = path.dirname(__file__)
            self.config_path = path.join(self.config_dir, '..', 'config.ini')
            self.config = configparser.RawConfigParser()
            self.config.read(self.config_path)
            self.leveling_high_score_label_ = self.config.get('Leveling_Snake_Values', 'high_score', fallback='0') # pylint: disable=line-too-long
            #update the high score label on the screen
            self.leveling_high_score_label.configure(text=f"Score: {self.leveling_high_score_label_} ") # pylint: disable=line-too-long
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def leveling_create_time_label(self):
        """
        Create the time label for the leveling snake game.
        """
        self.leveling_time_label = ctk.CTkLabel(self.snake_canvas,
                                        height=30,
                                        width=275,
                                        corner_radius=10,
                                        text=f"Time: {self.leveling_score_label_} Seconds",
                                        font=FONT_LIST[11],
                                        bg_color='grey20',
                                        anchor='w'
                                        )
        self.leveling_time_label.place(x=200, y=100)

    def leveling_update_time_label(self):
        """
        Update the time label for the leveling snake game.
        """
        try:
            self.config_dir = path.dirname(__file__)
            self.config_path = path.join(self.config_dir, '..', 'config.ini')
            self.config = configparser.RawConfigParser()
            self.config.read(self.config_path)
            self.leveling_time_label_ = self.config.get('Leveling_Snake_Values', 'time_score', fallback='0') # pylint: disable=line-too-long
            #update the time label on the screen
            self.leveling_time_label.configure(text=f"Time: {self.leveling_time_label_} Seconds") # pylint: disable=line-too-long
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def leveling_create_high_score_time_label(self):
        """
        Create the high score time label for the leveling snake game.
        """
        self.leveling_high_score_time_label = ctk.CTkLabel(self.snake_canvas,
                                                    height=30,
                                                    width=275,
                                                    corner_radius=10,
                                                    text=f"Score Time: {self.leveling_score_label_} Seconds", # pylint: disable=line-too-long
                                                    font=FONT_LIST[11],
                                                    bg_color='grey20',
                                                    anchor='w'
                                                    )
        self.leveling_high_score_time_label.place(x=200, y=400)

    def leveling_update_high_score_time_label(self):
        """
        Update the high score time label for the leveling snake game.
        """
        try:
            self.config_dir = path.dirname(__file__)
            self.config_path = path.join(self.config_dir, '..', 'config.ini')
            self.config = configparser.RawConfigParser()
            self.config.read(self.config_path)
            self.leveling_high_score_time_label_ = self.config.get('Leveling_Snake_Values', 'high_score_time', fallback='0') # pylint: disable=line-too-long
            #update the high score time label on the screen
            self.leveling_high_score_time_label.configure(text=f"Score Time: {self.leveling_high_score_time_label_} Seconds") # pylint: disable=line-too-long
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def leveling_create_snake_length_label(self):
        """
        Create the snake length label for the leveling snake game.
        """
        self.leveling_snake_length_label = ctk.CTkLabel(self.snake_canvas,
                                                height=30,
                                                width=275,
                                                corner_radius=10,
                                                text="Snake Length:",
                                                font=FONT_LIST[11],
                                                bg_color='grey20',
                                                anchor='w'
                                                )
        self.leveling_snake_length_label.place(x=200, y=150)

    def leveling_update_snake_length_label(self):
        """
        Update the snake length label for the leveling snake game.
        """
        try:
            self.config_dir = path.dirname(__file__)
            self.config_path = path.join(self.config_dir, '..', 'config.ini')
            self.config = configparser.RawConfigParser()
            self.config.read(self.config_path)
            self.leveling_snake_length_label_ = self.config.get('Leveling_Snake_Values', 'snake_length', fallback='0') # pylint: disable=line-too-long
            #update the high score time label on the screen
            self.leveling_snake_length_label.configure(text=f"Snake Length: {self.leveling_snake_length_label_}") # pylint: disable=line-too-long
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def leveling_create_high_score_snake_length_label(self):
        """
        Create the high score snake length label for the leveling snake game.
        """
        self.leveling_high_score_snake_length_label = ctk.CTkLabel(self.snake_canvas,
                                                            height=30,
                                                            width=275,
                                                            corner_radius=10,
                                                            text="Snake Length:",
                                                            font=FONT_LIST[11],
                                                            bg_color='grey20',
                                                            anchor='w'
                                                            )
        self.leveling_high_score_snake_length_label.place(x=200, y=450)

    def leveling_update_high_score_snake_length_label(self):
        """
        Update the high score snake length label for the leveling snake game.
        """
        try:
            self.config_dir = path.dirname(__file__)
            self.config_path = path.join(self.config_dir, '..', 'config.ini')
            self.config = configparser.RawConfigParser()
            self.config.read(self.config_path)
            self.leveling_high_score_snake_length_label_ = self.config.get('Leveling_Snake_Values', 'snake_length_high_score', fallback='0') # pylint: disable=line-too-long
            #update the high score time label on the screen
            self.leveling_high_score_snake_length_label.configure(text=f"Snake Length: {self.leveling_high_score_snake_length_label_}") # pylint: disable=line-too-long
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def leveling_create_xp_label(self):
        """
        Create the xp label for the leveling snake game.
        """
        self.leveling_xp_score_label = ctk.CTkLabel(self.snake_canvas,
                                                height=30,
                                                width=275,
                                                corner_radius=10,
                                                text="XP hello:",
                                                font=FONT_LIST[11],
                                                bg_color='grey20',
                                                anchor='w'
                                                )
        self.leveling_xp_score_label.place(x=500, y=10)

    def leveling_update_xp_label(self):
        """
        Update the xp label for the leveling snake game.
        """
        try:
            self.config_dir = path.dirname(__file__)
            self.config_path = path.join(self.config_dir, '..', 'config.ini')
            self.config = configparser.RawConfigParser()
            self.config.read(self.config_path)
            self.leveling_xp_score_label_ = self.config.get('Leveling_Snake_Values', 'xp', fallback='0') # pylint: disable=line-too-long
            #update the high score time label on the screen
            self.leveling_xp_score_label.configure(text=f"XP Hello: {self.leveling_xp_score_label_}") # pylint: disable=line-too-long
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def leveling_create_xp_high_score_label(self):
        """
        Create the xp high score label for the leveling snake game.
        """
        self.leveling_xp_high_score_label = ctk.CTkLabel(self.snake_canvas,
                                                    height=30,
                                                    width=275,
                                                    corner_radius=10,
                                                    text="XP:",
                                                    font=FONT_LIST[11],
                                                    bg_color='grey20',
                                                    anchor='w'
                                                    )
        self.leveling_xp_high_score_label.place(x=200, y=500)

    def leveling_update_xp_high_score_label(self):
        """
        Update the xp high score label for the leveling snake game.
        """
        try:
            self.config_dir = path.dirname(__file__)
            self.config_path = path.join(self.config_dir, '..', 'config.ini')
            self.config = configparser.RawConfigParser()
            self.config.read(self.config_path)
            self.leveling_xp_high_score_label_ = self.config.get('Leveling_Snake_Values', 'xp_high_score', fallback='0') # pylint: disable=line-too-long
            #update the high score time label on the screen
            self.leveling_xp_high_score_label.configure(text=f"XP: {self.leveling_xp_high_score_label_}") # pylint: disable=line-too-long
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def leveling_create_level_label(self):
        """
        Create the level label for the leveling snake game.
        """
        self.leveling_level_score_label = ctk.CTkLabel(self.snake_canvas,
                                                    height=30,
                                                    width=275,
                                                    corner_radius=10,
                                                    text="Level:",
                                                    font=FONT_LIST[11],
                                                    bg_color='grey20',
                                                    anchor='w'
                                                    )
        self.leveling_level_score_label.place(x=800, y=10)

    def leveling_update_level_label(self):
        """
        Update the level label for the leveling snake game.
        """
        try:
            self.config_dir = path.dirname(__file__)
            self.config_path = path.join(self.config_dir, '..', 'config.ini')
            self.config = configparser.RawConfigParser()
            self.config.read(self.config_path)
            self.leveling_level_score_label_ = self.config.get('Leveling_Snake_Values', 'level', fallback='0') # pylint: disable=line-too-long
            #update the high score time label on the screen
            self.leveling_level_score_label.configure(text=f"Level: {self.leveling_level_score_label_}") # pylint: disable=line-too-long
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def leveling_create_level_high_score_label(self):
        """
        Create the level high score label for the leveling snake game.
        """
        self.leveling_level_high_score_label = ctk.CTkLabel(self.snake_canvas,
                                                    height=30,
                                                    width=275,
                                                    corner_radius=10,
                                                    text="Level:",
                                                    font=FONT_LIST[11],
                                                    bg_color='grey20',
                                                    anchor='w'
                                                    )
        self.leveling_level_high_score_label.place(x=200, y=550)

    def leveling_update_level_high_score_label(self):
        """
        Update the level high score label for the leveling snake game.
        """
        try:
            self.config_dir = path.dirname(__file__)
            self.config_path = path.join(self.config_dir, '..', 'config.ini')
            self.config = configparser.RawConfigParser()
            self.config.read(self.config_path)
            self.leveling_level_high_score_label_ = self.config.get('Leveling_Snake_Values', 'level_high_score', fallback='0') # pylint: disable=line-too-long
            #update the high score time label on the screen
            self.leveling_level_high_score_label.configure(text=f"level: {self.leveling_level_high_score_label_}") # pylint: disable=line-too-long
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def leveling_reset_labels(self):
        """
        Reset the labels for the leveling snake game.
        """
        self.leveling_score_label.configure(text='0')
        self.leveling_time_label.configure(text='0')

    def leveling_delete_labels(self):
        """
        Delete the labels for the leveling snake game.
        """
        try:
            if self.leveling_score_label is not None:
                self.leveling_score_label.destroy()
            if self.leveling_time_label is not None:
                self.leveling_time_label.destroy()
            if self.leveling_high_score_label is not None:
                self.leveling_high_score_label.destroy()
            if self.leveling_high_score_time_label is not None:
                self.leveling_high_score_time_label.destroy()
            if self.leveling_high_scores_label is not None:
                self.leveling_high_scores_label.destroy()
            if self.leveling_snake_length_label is not None:
                self.leveling_snake_length_label.destroy()
            if self.leveling_high_score_snake_length_label is not None:
                self.leveling_high_score_snake_length_label.destroy()
            if self.leveling_xp_score_label is not None:
                self.leveling_xp_score_label.destroy()
            if self.leveling_xp_high_score_label is not None:
                self.leveling_xp_high_score_label.destroy()
            if self.leveling_level_score_label is not None:
                self.leveling_level_score_label.destroy()
            if self.leveling_level_high_score_label is not None:
                self.leveling_level_high_score_label.destroy()
        except ValueError as e:
            traceback.print_exc(e)

    def challange_create_game_labels(self):
        """
        Create the game labels for the challange snake game.
        """
        self.config.read(self.config_path)
        self.score_label_needed = self.config.get('Settings', 'label_needed_score', fallback='Default') # pylint: disable=line-too-long
        self.challange_create_score_label()

        if self.score_label_needed == 'True' or self.score_label_needed == 'Default':
            self.challange_create_high_score_label()

    def challange_update_game_labels(self):
        """
        Update the game labels for the challange snake game.
        """
        self.challange_update_score_label()

    def challange_update_high_score_labels(self):
        """
        Update the high score labels for the challange snake game.
        """
        self.config.read(self.config_path)
        self.score_label_needed = self.config.get('Settings', 'label_needed_score', fallback='Default') # pylint: disable=line-too-long

        if self.score_label_needed == 'True' or self.score_label_needed == 'Default':
            self.challange_update_high_score_label()

    def challange_create_score_label(self):
        """
        Create the score label for the challange snake game.
        """
        self.challange_score_label = ctk.CTkLabel(self.snake_canvas,
                                                height=30,
                                                width=275,
                                                corner_radius=10,
                                                text=f"Score:{self.challange_score_label_} ",
                                                font=FONT_LIST[11],
                                                bg_color='grey20',
                                                anchor='w'
                                                )
        self.challange_score_label.place(x=200, y=500)  # adjust the position as needed

    def challange_update_score_label(self):
        """
        Update the score label for the challange snake game.
        """
        try:
            self.config_dir = path.dirname(__file__)
            self.config_path = path.join(self.config_dir, '..', 'config.ini')
            self.config = configparser.RawConfigParser()
            self.config.read(self.config_path)
            self.challange_score_label_ = self.config.get('food_time_attack_Values', 'score', fallback='0') # pylint: disable=line-too-long
            #update the high score time label on the screen
            self.challange_score_label.configure(text=f"Score: {self.challange_score_label_}")
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def challange_create_high_score_label(self):
        """
        Create the high score label for the challange snake game.
        """
        self.challange_high_score_label = ctk.CTkLabel(self.snake_canvas,
                                                    height=30,
                                                    width=275,
                                                    corner_radius=10,
                                                    text=f"Score:{self.challange_score_label_} ",
                                                    font=FONT_LIST[11],
                                                    bg_color='grey20',
                                                    anchor='w'
                                                    )
        self.challange_high_score_label.place(x=200, y=550)

    def challange_update_high_score_label(self):
        """
        Update the high score label for the challange snake game.
        """
        try:
            self.config_dir = path.dirname(__file__)
            self.config_path = path.join(self.config_dir, '..', 'config.ini')
            self.config = configparser.RawConfigParser()
            self.config.read(self.config_path)
            self.challange_high_score_label_ = self.config.get('food_time_attack_Values', 'high_score', fallback='0') # pylint: disable=line-too-long
            #update the high score time label on the screen
            self.challange_high_score_label.configure(text=f"level: {self.challange_score_label_}")
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def challange_reset_labels(self):
        """
        Reset the labels for the challange snake game.
        """
        self.challange_score_label.configure(text='0')

    def challange_delete_labels__(self):
        """
        Delete the labels for the challange snake game.
        """
        try:
            if self.challange_score_label is not None:
                self.challange_score_label.destroy()
                print('Deleted score challange')
            if self.challange_high_score_label is not None:
                self.challange_high_score_label.destroy()
                print('Deleted high score challange')
            print('Deleted Labels challange')
        except ValueError as e:
            traceback.print_exc(e)

# pylint: disable=too-many-lines
